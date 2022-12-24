import numpy as np
import math
import matplotlib.pyplot as plt

global eps
eps = math.pi / 4


def analytic2(x):
    c1, c2, c3, c4 = get_const()
    if x < eps:
        v = c1 * math.exp(x) + c2 * math.exp(-x) + 1
    else:
        v = c3 * math.exp((math.pi * x / math.sqrt(2)) - math.pi * x / (2 * math.sqrt(2))) + c4 * math.exp(
            -math.pi * x / (2 * math.sqrt(2))) + 8 * math.sqrt(2) / math.pi ** 2
    return v


def get_const():
    A = np.array([[1, 1, 0, 0], [0, 0, math.exp((math.pi / math.sqrt(2)) - (math.pi / (2 * math.sqrt(2)))),
                                 math.exp(-math.pi / (2 * math.sqrt(2)))],
                  [math.exp(math.pi / 4), math.exp(-math.pi / 4),
                   -math.exp((math.pi ** 2 / (4 * math.sqrt(2))) - (math.pi ** 2 / (8 * math.sqrt(2)))),
                   -math.exp(- math.pi ** 2 / (8 * math.sqrt(2)))],
                  [math.exp(math.pi / 4), -math.exp(-math.pi / 4),
                   -(math.pi * 2 ** 0.5) / 4 * math.exp(math.pi ** 2 * 2 ** 0.5 / 16),
                   (math.pi * 2 ** 0.5) / 4 * math.exp(-math.pi ** 2 * 2 ** 0.5 / 16)]])
    B = np.array([0, -8 * math.sqrt(2) / math.pi ** 2, 8 * math.sqrt(2) / math.pi ** 2 - 1, 0])

    const = np.linalg.solve(A, B)
    return const



def func_a(i, h):
    x_i = i * h
    x_i_1 = (i - 1) * h
    if x_i <= eps:
        return h / (x_i - x_i_1)
    elif x_i_1 >= eps:
        return (h * 0.5 / (x_i - x_i_1))
    else:
        integr = (eps - x_i_1) + 2 * (x_i - eps)
        return h / integr


def func_d(i, h):
    x_i_p = (i + 0.5) * h
    x_i_m = (i - 0.5) * h
    if x_i_p <= eps:
        return (x_i_p - x_i_m) / h
    elif x_i_m >= eps:
        return ((math.pi ** 2 / 16) * (x_i_p - x_i_m)) / h
    else:
        return (eps - x_i_m) / h + (math.pi ** 2 / 16) * (x_i_p - eps) / h


def func_A(i, h):
    return func_a(i, h) / h ** 2


def func_C(i, h):
    return (func_a(i, h) + func_a(i + 1, h)) / h ** 2 + func_d(i, h)


def func_B(i, h):
    return func_a(i + 1, h) / h ** 2


def func_f(i, h):
    x_i_p = (i + 0.5) * h
    x_i_m = (i - 0.5) * h
    if x_i_p <= eps:
        return (1 / h) * (x_i_p - x_i_m)
    elif x_i_m >= eps:
        return (1 / h) * (math.sqrt(2) / 2 * (x_i_p - x_i_m))
    else:
        return (eps - x_i_m) / h + math.sqrt(2) / 2 * (x_i_p - eps) / h


def setMatrix(N, h):
    Matrix = [[0] * (N + 1) for i in range(N + 1)]

    # for i in range(N + 1):
    # for j in range(N):
    # Matrix[i][j] = 0
    Matrix[0][0] = 1
    Matrix[N][N] = 1
    i = 1
    j = 0
    x = 0
    while j < N - 1:
        '''''
        Matrix[i][j] = func_A(i, h)
        Matrix[i][j + 1] = -func_C(i, h)
        Matrix[i][j + 2] = func_B(i, h)
        i += 1
        j += 1
        '''''
        if x + 0.5 * h <= eps:
            Matrix[i][j] = 1
            Matrix[i][j + 1] = -2 - h ** 2
            Matrix[i][j + 2] = 1
            x = h * j
            i += 1
            j += 1

        elif x - 0.5 * h >= eps:
            Matrix[i][j] = 1 / 2
            Matrix[i][j + 1] = -1 - ((math.pi ** 2) / 16 * h ** 2)
            Matrix[i][j + 2] = 1 / 2
            x = h * j
            i += 1
            j += 1
        else:
            Matrix[i][j] = 3 / 2
            Matrix[i][j + 1] = -3 - (1 + math.pi ** 2 / 16) * h ** 2
            Matrix[i][j + 2] = 3 / 2
            x = h * j
            i += 1
            j += 1

    return Matrix


def setSolveVector(N, h):
    List = []
    List.append(1)
    x = 0
    for i in range(N):
        '''''
        List.append(-func_f(i, h) * h ** 2)
        '''''
        if x + 0.5 * h <= eps:
            List.append(-h ** 2)
            x = h * i
        elif x - 0.5 * h >= eps:
            List.append(-math.sqrt(2)/2 * h ** 2)

        else:
            List.append(-(1 + 2 ** 0.5) * h ** 2)
            x = h * i

    List.append(0)
    return List


def setMatrix2(N):
    h = 1 / N
    M = setMatrix(N, h)
    V = setSolveVector(N - 1, h)
    N += 1
    Matrix = [[0] * (N + 1) for i in range(N)]

    for i in range(N):
        for j in range(N):
            Matrix[i][j] = M[i][j]

    j = 0
    while j < N:
        Matrix[j][-1] = V[j]
        j += 1

    return Matrix


def progonka_forward(matrix, N):
    List_alpha = []
    List_beta = []
    y = matrix[0][0]
    List_alpha.append(-matrix[0][1] / y)
    List_beta.append(matrix[0][-1] / y)
    for i in range(1, N):
        y = matrix[i][i] + matrix[i][i - 1] * List_alpha[i - 1]
        List_alpha.append(-matrix[i][i + 1] / y)
        List_beta.append((matrix[i][-1] - matrix[i][i - 1] * List_beta[i - 1]) / y)

    return List_alpha, List_beta


def progonka_reverse(matrix, N):
    List_alpha = progonka_forward(matrix, N)[0]
    List_beta = progonka_forward(matrix, N)[1]
    List_v = []
    List_alpha.pop(-1)
    List_alpha.reverse()
    List_beta.reverse()
    List_v.append(List_beta[0])
    for i in range(N - 1):
        List_v.append(List_alpha[i] * List_v[i] + List_beta[i + 1])
    List_v.reverse()
    return List_v


def get_data1(N):
    matrix = setMatrix2(N)
    List_v = progonka_reverse(matrix, N + 1)
    List_x = []
    for i in range(N + 1):
        List_x.append(i * 1 / N)
    return List_x, List_v


def info(N):
    h = 1 / N
    List_v = get_data1(N)[1]
    List_a = get_analytic_data(N)[1]
    List_r = []
    List_x = []
    for i in range(N + 1):
        List_x.append(h * i)
    for i in range(N + 1):
        List_r.append(abs(List_v[i] - List_a[i]))

    return List_x, List_v, List_a, List_r


print(max(info(2000)[3]))
print(info(10))
plt.plot(get_analytic_data(10)[0], get_analytic_data(10)[1])
plt.plot(get_data1(10)[0], get_data1(10)[1], 'y')
# plt.plot(analytic(1000)[0], analytic(1000)[1])
# plt.show()
