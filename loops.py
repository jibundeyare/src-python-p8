import random
from timeit import default_timer as timer

# boucle == structure itérative

# boucle infinie
# i = 0
# while True:
#     print(i)
#     i += 1
#     if i > 99:
#         i = 0

# équivalent de la boucle for en C/C++, PHP ou JS
# condition d'initialisation
i = 0
# condition de continuation
while i < 10:
    # le corps de la boucle
    print(i)
    # le pas (incrémentation ou décrémentation du comteur) 
    i += 1

# boucle for classique en JS
# for (let i = 0; i < 10; i++) {
#     console.log(i);
# }

names = [
    'Alice',
    'Bob',
    'Charly',
    'Dave',
    'Elody',
    'Frank'
]

name = 'Toto'
i = 0
name_found = False
while True:
    if i >= len(names):
        break

    if names[i] == name:
        name_found = True
        break

    i += 1

if name_found:
    print("trouvé à l'index:", i)
else:
    print('non trouvé')

# remplace la boucle for classique des autres langages
for i in range(0, 100):
    print(i)

# ça marche mais pas recommandé
for i in range(0, len(names)):
    print(names[i])

# boucle foreach
for name in names:
    print(name)

for key, value in enumerate(names):
    print(key, value)

# équivalent de la boucle foreach en JS
# for (let key in values) {
#     console.log(values[key]);
# }

name = 'Toto'
name_found = False
for key, value in enumerate(names):
    print(key, value)

    if value == name:
        name_found = True
        break

if name_found:
    print("trouvé à l'index:", key)
else:
    print('non trouvé')

vowels = 0
for name in names:
    for letter in name:
        print(letter.lower())
        if letter.lower() == 'a' or \
            letter.lower() == 'e' or \
            letter.lower() == 'i' or \
            letter.lower() == 'o' or \
            letter.lower() == 'u' or \
            letter.lower() == 'y':

            vowels += 1

print('vowels:', vowels)

# exo converion degré celsius vers degré fahrenheit
# temperature_f = (temperature_c * 9/5) + 32
n = 10
temperatures_c = []
for i in range(0, n):
    temperatures_c.append(random.randint(-50, 300) / 10)

print('temperatures celsius:', temperatures_c)

temperatures_f = []

for temperature_c in temperatures_c:
    # conversion celsius -> fahrenheit
    temperatures_f.append((temperature_c * 9/5) + 32)

print('temperatures fahrenheit:', temperatures_f)


# start benchmark
start = timer()

for _ in range(0, 1000000):
    # exo recherche températires négatives
    negative_temperatures_c = []

    for temperature_c in temperatures_c:
        if temperature_c < 0:
            # nous avons une température négative
            negative_temperatures_c.append(temperature_c)

    # print('temperatures c:', temperatures_c)
    # print('negative temperatures c:', negative_temperatures_c)

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# start benchmark
start = timer()

negative_temperatures_c = [None] * len(temperatures_c)

for _ in range(0, 1000000):
    for i in range(0, len(temperatures_c)):
        if temperatures_c[i] < 0:
            # nous avons une température négative
            negative_temperatures_c[i] = temperatures_c[i]

    # print('temperatures c:', temperatures_c)
    # print('negative temperatures c:', negative_temperatures_c)

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)
