# list == array
# liste == tableau (index numériques)

# liste != variable scalaire

# liste vide
my_list = []
print(my_list)

# liste
my_list = [123, 3.14, 'foo', True]

my_list = [
    123,    # 0
    3.14,   # 1
    'foo',  # 2
    True    # 3
]
print(my_list)
print()

courses = [
    'bananes',
    'kiwi',
    'framboise',
    'mangue',
    'poire'
]

# lecture du premier élément
value_a = my_list[0]
print(my_list[0])

print('premier fruit:', courses[0])

# lecture des éléments suivants
value_b = my_list[1]
value_c = my_list[3]
print(my_list[1])
print(value_c)

print('fruit suivant:', courses[1])
print('fruit suivant:', courses[2])

# taille d'une liste
length = len(my_list)
print(len(my_list))
# print(length)

# nombre de type de fruit
print('nombre type fruit:', len(courses))

# dernier élément
dernier_index = len(my_list) - 1
value_d = my_list[dernier_index]

print('dernier fruit:', courses[len(courses) - 1])

# idem
value_d = my_list[len(my_list) - 1]

print(my_list[len(my_list) - 1])
print(value_d)

# remplacer
my_list[1] = None
print(my_list)

courses[0] = 'x ' + courses[0]
courses[1] = 'x ' + courses[1]
courses[3] = 'fraises'
print(courses)

# supprimer
del my_list[0]
print(my_list)

# supprime 'x banane'
del courses[0]
# supprime 'x kiwi'
del courses[0]
print(courses)

# ajouter à la fin de la liste
my_list.append('baz')

courses.append('chocolat')
print(courses)

# insérer au milieu
courses.insert(3, "huile d'olive")
print(courses)

# récupérer et supprimer de la liste
fruit = courses.pop(1)
print(fruit)
print(courses)

# pop le dernier élément de la liste
fruit2 = courses.pop()
print(fruit2)
print(courses)

# push == append
# pop() == inverse de append
# pop(index) == inverse de insert

# compter
my_list2 = [123, 123, 42, 0]
print(my_list2)

print(my_list2.count(123))
print(my_list2.count(3.14))

# retrouver l'index d'une valeur
print('index de 42:', my_list2.index(42))

index_123 = my_list2.index(123)
print('index de 123:', index_123)

# rechercher après l'index déjà trouvé
index_123 = my_list2.index(123, index_123 + 1)
print('index de 123:', index_123)

# rechercher encore après l'index déjà trouvé
# provoque l'erreur ValueError: 123 is not in list
# index_123 = my_list2.index(123, index_123 + 1)
# print('index de 123:', index_123)

# tester la présence d'une valeur
if 'poire' in courses:
    print('il y a des poires dans la liste de courses')
else:
    print("il n'y a pas de poires dans la liste de courses")

# concaténation
nouvelle_liste = my_list + courses + my_list2
print(nouvelle_liste)

# liste de liste, c-à-d une liste en 2D
morpion = [
    ['', '', ''],   # 0
    ['', '', ''],   # 1
    ['', '', '']    # 2
]

ligne = morpion[1]
ligne[1] = 'X'
print(ligne[1])

morpion[1][1] = 'X'
print(morpion[1][1])

morpion[2][2] = 'O'
print(morpion[2][2])

print(morpion)

# tri sur une copie
courses_copie = sorted(courses)
print(courses)
print(courses_copie)

# tri sur l'original
courses.append('Zimbabwe')
courses.append('étoile')
print(courses)
courses.sort()
print(courses)

courses_copie.sort(reverse=True)
print(courses_copie)

# un tri ne peut se faire qu'avec des données comparable (c-à-d du même type)
# provoque l'erreur TypeError: '<' not supported between instances of 'str' and 'NoneType'
# parce qu'on ne peut pas comparer une chaîne de caractères et un None
# ou tout couple de type différent
# my_list.sort()
