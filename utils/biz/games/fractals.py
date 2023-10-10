import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(x_min, x_max, y_min, y_max, width, height, max_iter):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    img = np.zeros((width, height))

    for i in range(width):
        for j in range(height):
            c = x[i] + 1j * y[j]
            img[i, j] = mandelbrot(c, max_iter)

    return img

def julia(c, x_min, x_max, y_min, y_max, width, height, max_iter):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    img = np.zeros((width, height))

    for i in range(width):
        for j in range(height):
            z = x[i] + 1j * y[j]
            n = 0
            while abs(z) <= 2 and n < max_iter:
                z = z*z + c
                n += 1
            img[i, j] = n

    return img

def plot_fractal(fractal_type, x_min, x_max, y_min, y_max, width, height, max_iter):
    if fractal_type == 'Mandelbrot':
        fractal_img = mandelbrot_set(x_min, x_max, y_min, y_max, width, height, max_iter)
    elif fractal_type == 'Julia':
        c_real = float(input("Enter the real part of the constant (e.g., -0.7): "))
        c_imag = float(input("Enter the imaginary part of the constant (e.g., 0.27015): "))
        c = complex(c_real, c_imag)
        fractal_img = julia(c, x_min, x_max, y_min, y_max, width, height, max_iter)
    else:
        print("Invalid fractal type. Please choose 'Mandelbrot' or 'Julia'.")
        return

    plt.imshow(fractal_img.T, extent=(x_min, x_max, y_min, y_max), cmap='inferno', origin='lower')
    plt.colorbar(label='Iterations')
    plt.title(f'{fractal_type} Set')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.show()

if __name__ == "__main__":
    fractal_type = input("Choose a fractal type ('Mandelbrot' or 'Julia'): ")
    x_min, x_max = float(input("Enter x_min: ")), float(input("Enter x_max: "))
    y_min, y_max = float(input("Enter y_min: ")), float(input("Enter y_max: "))
    width, height = int(input("Enter width: ")), int(input("Enter height: "))
    max_iter = int(input("Enter max iterations: "))
    
    plot_fractal(fractal_type, x_min, x_max, y_min, y_max, width, height, max_iter)
