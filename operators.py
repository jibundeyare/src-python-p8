# opérateurs arithmétiques

a = -123
b = -42

c = a + b
c = a - b
c = a * b
c = a / b
c = 10 // 3 # division entière, la variable c contient 3 (et pas la partie .333...)
c = 2 ** 8 # puissances
c = 10 ** (1 / 2) # racine carré, c'est le 2 qui définit le niveau de la racine
c = 10 ** (1 / 3) # racine cubique, c'est le 3 qui définit le niveau de la racine

c = 10 % 3 # modulo, la variable c contient 1

# vérifier la parité d'un nombre
print(5 % 2) # affiche 1 si le nombre est impaire
print(8 % 2) # affiche 0 si le nombre est paire

# priorité des opérateurs
# 1. **
# 2. * / // %
# 3. + -

c = (52 + 2) * 2 # c contient 108
c = 52 + 2 * 2 # c contient 56

# opérateurs d'incrémentation et décrémentation

# l'opérateur ++ permet d'incrémenter de 1
# l'opérateur -- permet de décrémenter de 1
# mais ils n'existent pas en python

c = 42
c += 1 # calcul c + 1 et affecte le résultat à la variable c
# pareil que
c = c + 1 # la variable c passe de 43 à 44
print(c)

c -= 3 # calcul c - 3 et affecte le résultat à la vraiable c
# pareil que
c = c - 3
print(c)

price = 100
tva1 = 2.1
tva2 = 5.5
tva3 = 10
tva4 = 20

# prix tva incluse
price_tva1 = price + price * tva1 / 100 # méthode A
price_tva2 = price + price * tva2 / 100
price_tva3 = price * (1 + tva3 / 100) # méthode B équivalente
price_tva4 = price * (1 + tva4 / 100)

# arrondi à 2 chiffres après la virgule
price_tva3 = round(price_tva3, 2)

print(price_tva1)
print(price_tva2)
print(price_tva3)
print(price_tva4)

# opérateurs de comparaison

# égalité (à ne pas confondre avec le simple =, opérateur d'affectation)
print(123 == 123)
print('foo' == 'foo')
# différence
print(42 != 123)
print('foo' != 'bar')

# inférieur
print(42 < 123)
# inférieur ou égal
print(42 <= 123)
# supérieur
print(123 > 42)
# supérieur ou égal
print(123 >= 42)

# les opérateurs de comparaison renvoient des booléens
print(123 == 42)

# numériquement les deux valeurs sont égales
print(123.0 == 123) # renvoit True
print()

# si l'opérateur d'identité === existait en python
# print(123.0 === 123) # renvoit False

# opérateurs logiques

total = 123
point_fidelite = 13

# si le total est supérieur ou égal à 100 ET si le nombre
# de point de fidélité est supérieur ou égal à 10 le
# client a droit à une remise
print(total >= 100 and point_fidelite >= 10)
print()

# A     B       A and B
# False False   False
# True  False   False
# False True    False
# True  True    True

point_fidelite = 6
carte_gold = True

# si le nombre de point de fidélité est supérieur OU égal
# à 10 ou si le client possède une carte gold, il a droit
# à une remise 

print(point_fidelite >= 10 or carte_gold == True)

# A     B       A or B
# False False   False
# True  False   True
# False True    True
# True  True    True

# le voyageur a un billet de train
billet_train = True

# le contrôleur peut-il lui mettre une amende ?
print(not billet_train)

# profil d'un client qui ne consomme pas beaucoup
total = 42
point_fidelite = 4
# doit-on lui envoyer de la publicité ou lui proposer la carte gold ?
print(not (total >= 100 and point_fidelite >= 10))

# priorité des opérateurs de comparaison et des opérateurs logique
# 1. == != < > <= >=
# 2. and or not

# A     not A
# True  False
# False True

# A     B       A xor B
# False False   False
# False True    True
# True  False   True
# True  True    False

# 1000001 A (65)
# 1100001 a (97)
# 0100000 A xor a == espace (32)
# 1000001 SP xor a == A (65)

# opérateurs etc

# inclusion
my_text = 'toto et titi sont dans une barque'
print('titi' in my_text)
print('foo' in my_text)

# une liste
my_list = [123, True, 'foo', 2.71]
print(2.71 in my_list)
print(3.14 in my_list)

my_int = 123
my_float = 3.14
my_bool = False
my_none = None

# la variable my_text est-elle une chaîne de caractères ?
print(type(my_text) is str)
print(type(my_text) is float)
print(type(my_text) is int)
print(type(my_text) is bool)

# on peut comparer le type de None avec le type d'une autre variable
print(type(my_text) is type(None))
# mais autant vérifier tout de suite si la variable est égale à None
print(my_text == None)
