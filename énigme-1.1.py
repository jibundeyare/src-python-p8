import math

start = math.ceil(math.sqrt(1000))
end = math.floor(math.sqrt(9999))

squares = []

for i in range(1, 10):
    squares.append(i * i)

for i in range(start, end + 1):
    square = i * i

    # méthode alphanumérique
    # square_str = str(square)
    # a = int(square_str[0:2])
    # b = int(square_str[2:])

    # méthode arithmétique
    a = square // 100
    b = square % 100

    if a in squares and b in squares:
        print(square, a, b)
