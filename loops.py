# équivalent de la boucle for en C/C++, PHP ou JS
# condition d'initialisation
i = 0
# condition de continuation
while i < 10:
    # le corps de la boucle
    print(i)
    # le pas (incrémentation ou décrémentation du comteur) 
    i += 1

# boucle for en JS
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
    print('Trouvé:', names[i])
