text1 = 'lorem "foo" ipsum'
text2 = "lorem 'foo' ipsum"

text3 = '''lorem
ipsum
<p>sit</p>
dolores
'''
print(text3)

text4 = """lorem
ipsum
<p>sit</p>
dolores
"""
print(text4)

# le symbole backslash \ est le caractère d'échappement

text5 = 'lorem\n"foo"\nipsum'
print(text5)
text6 = "lorem\n'foo'\nipsum"
print(text6)

text7 = "lorem \\ \"foo\" \\ ipsum"
print(text7)
text8 = 'lorem \\ \'foo\' \\ ipsum'
print(text8)

# concaténation

firstname = 'Toto'
lastname = 'Pop'
text9 = 'Bonjour ' + firstname + ' ' + lastname
print(text9)

stock = 42
print('état du stock: ' + str(stock) + ' pièces')

diametre = 3.14
print('diamètre = ' + str(diametre) + 'cm')
print('diamètre = ' + str(round(diametre, 1)) + 'cm')

# interpolation avec une f-string

firstname = 'Toto'
lastname = 'Pop'
text10 = f'Bonjour {firstname} {lastname}'
print(text10)

stock = 42
print(f'état du stock: {stock} pièces')

diametre = 3.14
print(f'diamètre = {diametre}cm')
print(f'diamètre = {round(diametre, 1)}cm')

# pour afficher des accolades, il faut les doubler
# le caractère d'échappement d'une f-string est l'accolade
print(f'{{stock}} {{diametre}}')
print()

print(text1)
# longueur
print(len(text1))
# recherche
print('foo' in text1)
print(text1.find('foo')) # trouvé à la 7ème position
print('baz' in text1)
print(text1.find('baz')) # (par convention) position -1 == non trouvé
# remplacement
text1 = text1.replace('foo', 'baz')
print(text1)

text11 = 'foo foo foo'
# on ne remplace qu'une seule occurence
text11 = text11.replace('foo', 'baz', 1)
print(text11)

text12 = "lorem ipsum sit dolores"
# sélection d'un caractère par son index
print(text12[3])
# sélection d'une suite de caractères par leur index,
# du 6ème inclus au 11ème exclus
print(text12[6:11])
# remplacer ipsum par baz sans utiliser str.replace()
# sélection du début au 6ème caractère exclus
# + baz
# + sélection du 11ème caractère au dernier
print(text12[:6] + 'baz' + text12[11:])
