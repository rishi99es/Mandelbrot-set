import numpy as np
from pylab import *

def mandelbrot_set(x_min, x_max, y_min, y_max, x_num, y_num, max_iteration):
    # np.linspace(start, stop, num_samples, dtype = type of output array) ............ linspace syntax
    X = np.linspace(x_min, x_max, x_num, dtype = np.float32)
    Y = np.linspace(y_min, y_max, y_num, dtype = np.float32)

    # cmath syntax to represent an array of complex numbers.
    C = X + Y[:, None] * 1j

    # create empty array to hold real values
    N = np.zeros(C.shape, dtype = int)
    # create empty array to hold imaginary values
    Z = np.zeros(C.shape, np.complex64)

    for n in range(max_iteration):
        I = np.less(abs(Z), 2)
        N[I] = n
        # implement Mandelbrot set definition: z = (z ** 2) + C
        Z[I] = Z[I] ** 2 + C[I]

    N[N == max_iteration - 1] = 0
    return Z, N


if __name__ == '__main__':

    x_min, x_max, x_num = -2, .5, 3000/2
    y_min, y_max, y_num = -1,  1, 2500/2

    max_iteration = 200

    Z, N = mandelbrot_set(x_min, x_max, y_min, y_max, x_num, y_num, max_iteration)

    with np.errstate(invalid = 'ignore'):
        M = np.nan_to_num(N + 1 - np.log(np.log(abs(Z))) / np.log(2))

    imshow(M, cmap = plt.cm.gray, interpolation = 'none', extent = (x_min, x_max, y_min, y_max))

    xlabel("Re(c)")
    ylabel("Im(c)")
    savefig("mandelbrot_python.png")
    show()
