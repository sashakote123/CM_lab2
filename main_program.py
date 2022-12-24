import numpy as np
import matplotlib.pyplot as plt


def k1(x):
    return np.sqrt(2) * np.sin(x)


def k2(x):
    return (np.cos(x)) ** 2


def q1():
    return 1


def q2(x):
    return x ** 2


def f1(x):
    return np.sin(2 * x)


def f2(x):
    return np.cos(x)


# методом Симпсона
def fi_wave(x, h, Zeta):
    if (x + h / 2) <= Zeta:
        return 1 / 6 * (f1(x - h / 2) + 4 * f1(x) + f1(x + h / 2))
    elif (x - h / 2) > Zeta:
        return 1 / 6 * (f2(x - h / 2) + 4 * f2(x) + f2(x + h / 2))
    else:
        return 1 / h * ((Zeta - x + h / 2) / 6 * (f1(x - h / 2) + 4 * f1((Zeta + x - h / 2) / 2) + f1(Zeta)) + (
                x + h / 2 - Zeta) / 6 * (f2(Zeta) + 4 * f2((Zeta + x + h / 2) / 2) + f2(x + h / 2)))


# методом трапеций
def ffi_wave(x, h, Zeta):
    if (x + h / 2) <= Zeta:
        return (f1(x - h / 2) + f1(x + h / 2)) / 2
    elif (x - h / 2) > Zeta:
        return (f2(x - h / 2) + f2(x + h / 2)) / 2
    else:
        return 1 / h * ((f1(x - h / 2) + f1(Zeta)) * (Zeta - x + h / 2) / 2 + (f2(Zeta) + f2(x + h / 2)) * (
                x + h / 2 - Zeta) / 2)


# методом трапеций
def d_wave(x, h, Zeta):
    if (x + h / 2) <= Zeta:
        return q1()
    elif (x - h / 2) > Zeta:
        return 1 / 2 * (q2(x - h / 2) + q2(x + h / 2))
    else:
        return 1 / h * ((1 / 2 * (q2(x - h / 2) + q2(Zeta)) * (Zeta - x + h / 2)) + (
                1 / 2 * (q2(Zeta) + q2(x + h / 2)) * (x + h / 2 - Zeta)))


# методом Симпсона
def a_wave(x, h, Zeta):
    if x <= Zeta:
        return 1 / (1 / 6 * (k1(x - h) + 4 * k1((2 * x - h) / 2) + k1(x)))
    elif (x - h) > Zeta:
        return 1 / (1 / 6 * (k2(x - h) + 4 * k2((2 * x - h) / 2) + k2(x)))
    else:
        return 1 / (1 / h * (
                ((Zeta - x + h) / 6) * (k1(x - h) + 4 * k1((Zeta + x - h) / 2) + k1(Zeta)) + ((x - Zeta) / 6) * (
                k2(Zeta) + 4 * k2((x + Zeta) / 2) + k2(x))))


# методом трапеций
def aa_wave(x, h, Zeta):
    if x <= Zeta:
        return 2 * k1(x - h) * k1(x) / (k1(x - h) + k1(x))
    elif (x - h) > Zeta:
        return 2 * k2(x - h) * k2(x) / (k2(x - h) + k2(x))
    else:
        return 1 / (1 / h * (((1 / k1(x - h) + 1 / k1(Zeta)) * (Zeta - x + h) / 2) + (
                (1 / k2(Zeta) + 1 / k2(x)) * (x - Zeta) / 2)))


def A(x, h, zeta):
    return a_wave(x, h, zeta) / (h ** 2)


def C(x, h, zeta):
    return (a_wave(x, h, zeta) + a_wave(x + h, h, zeta)) / (h ** 2) + d_wave(x, h, zeta)


def B(x, h, zeta):
    return a_wave(x + h, h, zeta) / (h ** 2)


def progonka_forward_v(alpha1, beta1, h, N, zeta):
    list_alpha = [alpha1]
    list_beta = [beta1]
    list_a = []
    list_b = []
    list_c = []
    list_f = []

    for i in range(1, int(N)):
        list_a.append(A(i * h, h, zeta))
        list_b.append(B(i * h, h, zeta))
        list_c.append(C(i * h, h, zeta))
        list_f.append(fi_wave(i * h, h, zeta))

    for j in range(0, int(N - 1)):
        list_alpha.append(list_b[j] / (list_c[j] - list_alpha[j] * list_a[j]))
        list_beta.append((list_f[j] + list_a[j] * list_beta[j]) / (list_c[j] - list_alpha[j] * list_a[j]))

    return list_alpha, list_beta


def progonka_forward_v2(alpha1, beta1, h, N, zeta):
    list_alpha = [alpha1]
    list_beta = [beta1]
    list_a = []
    list_b = []
    list_c = []
    list_f = []

    for i in range(1, int(2 * N)):
        list_a.append(A(i * h / 2, h / 2, zeta))
        list_b.append(B(i * h / 2, h / 2, zeta))
        list_c.append(C(i * h / 2, h / 2, zeta))
        list_f.append(fi_wave(i * h / 2, h / 2, zeta))

    for j in range(0, int(2 * N - 1)):
        list_alpha.append(list_b[j] / (list_c[j] - list_alpha[j] * list_a[j]))
        list_beta.append((list_f[j] + list_a[j] * list_beta[j]) / (list_c[j] - list_alpha[j] * list_a[j]))

    return list_alpha, list_beta


def progonka_backwards_v(list_alpha, list_beta, hi2, mu2, N):
    list_v = [(mu2 + list_beta[-1] * hi2) / (1 - list_alpha[-1] * hi2)]
    for i in range(int(N - 1), -1, -1):
        list_v.insert(0, list_alpha[i] * list_v[0] + list_beta[i])
    return list_v


def progonka_backwards_v2(list_alpha, list_beta, hi2, mu2, N):
    list_v = [(mu2 + list_beta[-1] * hi2) / (1 - list_alpha[-1] * hi2)]
    for i in range(int(2 * N - 1), -1, -1):
        list_v.insert(0, list_alpha[i] * list_v[0] + list_beta[i])
    return list_v


def get_data2(N):
    Hi1 = 0
    Hi2 = 0
    Mu1 = 1
    Mu2 = 0
    Zeta = np.pi / 4
    x_max = 1
    x_min = 0
    h = (x_max - x_min) / N
    Eps = 0.5e-6
    eps2 = 0
    x_eps2 = 0

    list_Alpha, list_Beta = progonka_forward_v(Hi1, Mu1, h, N, Zeta)
    list_Alpha2, list_Beta2 = progonka_forward_v2(Hi1, Mu1, h, N, Zeta)
    list_V = progonka_backwards_v(list_Alpha, list_Beta, Hi2, Mu2, N)
    list_V2 = progonka_backwards_v2(list_Alpha2, list_Beta2, Hi2, Mu2, N)

    list_x = [x_min]
    while list_x[-1] < (x_max - 1e-12):
        list_x.append(list_x[-1] + h)

    list_x_2 = [x_min]
    while list_x_2[-1] < (x_max - 1e-12):
        list_x_2.append(list_x_2[-1] + h / 2)

    list_VSubV2 = []
    for i in range(0, int(2 * N + 1)):
        if i % 2 == 0:
            list_VSubV2.append(abs(list_V[i - int(i / 2)] - list_V2[i]))
            if eps2 < abs(list_V[i - int(i / 2)] - list_V2[i]):
                eps2 = abs(list_V[i - int(i / 2)] - list_V2[i])
                x_eps2 = i
        else:
            list_VSubV2.append(0)
    '''''
    print('Узел сетки с Epsilon 2:', x_eps2)
    if eps2 <= Eps:
        print('Epsilon 2 <= 0.5e-6')
    else:
        print('Не выполняется условие задачи')
    '''''
    return list_x, list_V, list_x_2, list_V2, list_VSubV2


