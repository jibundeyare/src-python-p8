import math

# carré
square = 3 * 3

# puissance 2 == carré
square = 3 ** 2

i = 3
square = i * i

for i in range(1, 10):
    square = i * i
    print(i, square)

# math.ceil() : plafond
# math.floor() : plancher ; équivalent de int()

n_min = math.ceil(math.sqrt(10000000))
n_max = math.ceil(math.sqrt(99999999))

print(n_min, n_max)
print()

for i in range(n_min, n_max):
    square = i * i

    # méthode alphanumérique

    # 12345678 nombre de lettres
    # 01234567 indexes
    # abcdefgh lettres

    square_str = str(square)

    # 4 premiers caractères
    a = int(square_str[:4])
    # 4 derniers caractères
    b = int(square_str[4:])

    # méthode arithmétique

    # 4 premiers chiffres
    a = square // 10000
    # 4 derniers chiffres
    b = square % 10000

    # a b -> b - a = 1
    if b - a == 1:
        print(i, square)
