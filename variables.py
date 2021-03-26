# integer
number_1 = 123
# float
number_2 = 3.14

# string
text_1 = 'foo bar baz'
text_2 = "lorem ipsum"

# boolean
is_morning = False
is_afternoon = True

# is_ et has_ sont des préfixes couramment utilisés pour distinguer les variables booléennes

# None / null / nil
favourite_song = None

foo, bar, baz = 123, 42, 3.14
print(foo, bar, baz)
print()

print('number_1:', number_1)
number_1 = 'abc'
print('number_1:', number_1)

print(is_morning)
print(favourite_song)

number_1 = 42
number_3 = 2.71

print(type(number_1))
print(type(number_2))
print(type(text_1))
print(type(text_2))
print(type(is_morning))
print(type(is_afternoon))
print(type(favourite_song))

data_type = type(favourite_song)
print(data_type)

result = number_2 + 123 + number_3
print(result)

print(type(number_1))
print(type(float(number_1)))

print(type(number_2))
print(type(int(number_2)))
print()

# ValueError: invalid literal for int() with base 10
# print(int(text_1))

text_3 = '123'
print(int(text_3))
print(float(text_3))

text_4 = '123.45'
# ValueError: invalid literal for int() with base 10: '123.45'
# print(int(text_4))
print(float(text_4))
print()

number_1 = 42
number_2 = 3.14

number_1 = float(number_1)
print(number_1)

number_2 = int(number_2)
print(number_2)

a = 123
b = 42

print(a) # 123
print(b) # 42

# interdit !
# a = 42
# b = 123

# algorithme de l'interversion
c = a # la variable c contient 123
a = b # la variable a contient 42
b = c # la variable b contient 123

print(a) # 42
print(b) # 123

# interversion des valeurs
# destructured assignment
a, b = b, a

print(a) # 123
print(b) # 42
