import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def render_terminal(elements):
    clear_screen()
    print("╔════════════════════╗")
    print("║  16-Bit Terminal   ║")
    print("╠════════════════════╣")
    for element in elements:
        print(f"║  {element}")
    print("╠════════════════════╣")
    print("║  Type 'exit' to    ║")
    print("║  quit the terminal.║")
    print("╚════════════════════╝")

def main():
    elements = []
    
    while True:
        render_terminal(elements)
        command = input("\nEnter a command or element to add (type 'exit' to quit): ")
        if command.lower() == 'exit':
            break
        else:
            elements.append(command)

if __name__ == "__main__":
    main()
