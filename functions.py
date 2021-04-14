# définition (description) d'une fonction avec type hinting
def addition(a: float, b: float) -> float:
    return a + b

# définition d'une fonction sans type hinting
def addition_no_type_hinting(a, b):
    return a + b

# appel (utilisation / exécution) d'une fonction
result = addition(3.14, 2.71)
print('result:', result)

result = addition_no_type_hinting([123], [42])
print('result:', result)

def iteration(items: list) -> None:
    for item in items:
        print(item)

a = [123, 42, 3.14, 2.71]
iteration(a)

# def moyenne(items: list) -> float:
# len(items)
