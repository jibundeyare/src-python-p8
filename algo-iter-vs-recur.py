# algorithmes itératifs vs algorithmes récursifs

# suite de fibonacci
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

# F0 = 1
# F1 = 1
# Fn = Fn-1 + Fn-2

# F2 = F2-1 + F2-2 = F1 + F0 = 1 + 1 = 2
# F3 = F3-1 + F3-2 = F2 + F1 = 2 + 1 = 3

def fibonacci_iter(n: int) -> int:
    """Calcul de la suite de Fibonacci avec une méthode itérative
    """

    if n == 0:
        return 1
    elif n == 1:
        return 1

    # la valeur d'il y a 2 tours en arrière
    fa = 1
    # la valeur d'il y a 1 tour en arrière
    fb = 1

    for i in range(2, n + 1):
        # la valeur du tour actuel
        fc = fa + fb
        # on remplace la valeur d'il y a 2 tours en arrière
        # par la valeur d'il y a 1 tour en arrière
        fb = fa
        # on remplace la valeur d'il y a 1 tour en arrière
        # par la valeur du tour actuel
        fa = fc

    return fc

def fibonacci_recur(n: int) -> int:
    """Calcul de la suite de Fibonacci avec une méthode récursive
    """

    if n == 0:
        return 1
    elif n == 1:
        return 1

    return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)

class Cache:
    # variable statique de classe
    data = {}

def fibonacci_recur_memo(n: int) -> int:
    """Calcul de la suite de Fibonacci avec une méthode récursive et de la mémoisation
    """

    if n == 0:
        return 1
    elif n == 1:
        return 1

    # si la valeur existe dans le cache, on la renvoit
    # sinon on la calcule
    if n in Cache.data:
        return Cache.data[n]

    result = fibonacci_recur(n - 1) + fibonacci_recur(n - 2)

    # après un calcul, on stock la valeur dans le cache
    Cache.data[n] = result

    return result

# test de algo
for i in range(0, 15):
    print(i, fibonacci_iter(i), fibonacci_recur(i), fibonacci_recur_memo(i))

# f(0) -> 1
# f(1) -> 1
# f(2) -> f(2 - 1) + f(2 - 2) -> f(1) + f(0) -> 1 + 1 -> 2
# f(3) -> f(3 - 1) + f(3 - 2) -> f(2) + f(1) -> f(2) + 1 -> 2 + 1 -> 3
# f(4) -> f(4 - 1) + f(4 - 2) -> f(3) + f(2) -> f(3 - 1) + f(3 - 2) + f(2 - 1) + f(2 - 2) -> f(2) + f(1) + f(1) + f(0) -> f(2 - 1) + f(2 - 2) + 1 + 1 + 1 -> f(1) + f(0) + 3 -> 1 + 1 + 3 -> 5
