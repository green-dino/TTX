from socket import *
import sys

def main():
    if len(sys.argv) <= 1:
        print('Usage : "python ProxyServer.py server_ip"\n[server_ip : IP Address Of Proxy Server]')
        sys.exit(2)

    # Create a server socket, bind it to a port, and start listening
    server_ip = "127.0.0.1" 
    server_port = 8888  # Choose a port for the proxy server
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)  # Listen for incoming connections

    print(f"Proxy server is ready to serve on {server_ip}:{server_port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f'Received a connection from: {addr}')

        message = client_socket.recv(4096).decode()

        # Extract the filename from the given message 
        filename = message.split()[1]
        filetouse = "/" + filename

        file_exist = "false"

        try:
            # Check if the file exists in the cache
            with open(filetouse[1:], "rb") as f:
                outputdata = f.read()
                file_exist = "true"
                client_socket.send("HTTP/1.0 200 OK\r\n")
                client_socket.send("Content-Type: text/html\r\n")
                client_socket.send("\r\n")
                client_socket.sendall(outputdata)
                print('Read from cache')

        except FileNotFoundError:
            if file_exist == "false":
                # Create a socket on the proxy server
                c = socket(AF_INET, SOCK_STREAM)
                hostn = filename.replace("www.", "", 1)

                try:
                    # Connect to the socket to port 80
                    c.connect((hostn, 80))

                    # Create a temporary file on this socket and ask port 80
                    # for the file requested by the client
                    fileobj = c.makefile('rb', 0)
                    fileobj.write(f"GET http://{filename} HTTP/1.0\r\n\r\n".encode())

                    # Read the response into a buffer
                    response = b""
                    while True:
                        data = fileobj.read(4096)
                        if not data:
                            break
                        response += data

                    # Create a new file in the cache for the requested file.
                    # Also send the response in the buffer to the client socket
                    # and the corresponding file in the cache.
                    with open(filetouse[1:], "wb") as tmp_file:
                        tmp_file.write(response)

                    client_socket.send("HTTP/1.0 200 OK\r\n")
                    client_socket.send("Content-Type: text/html\r\n")
                    client_socket.send("\r\n")
                    client_socket.sendall(response)

                except Exception as e:
                    print(f"Error: {e}")
                    client_socket.send("HTTP/1.0 404 Not Found\r\n")
                    client_socket.send("Content-Type: text/html\r\n")
                    client_socket.send("\r\n")
                    client_socket.send("<html><body>404 Not Found</body></html>")

                finally:
                    c.close()

        except Exception as e:
            print(f"Error: {e}")

        client_socket.close()

if __name__ == "__main__":
    main()
