import random

if True:
    print("ce texte s'affichera toujours")

if False:
    print("ce texte ne s'affichera jamais")

billet_train = True

if billet_train:
    print('le voyageur possède un billet')
else:
    print('le voyageur ne possède pas de billet')

if not billet_train:
    print('le voyageur ne possède pas de billet')
    print('le contrôleur doit mettre une amende')
else:
    print('le voyageur possède un billet')
    print('le contrôleur ne fait rien')

print()

is_water_off = False
is_gas_off = True

# sans vérification de ce qui n'a pas été coupé
if is_water_off and is_gas_off:
    print("l'eau et le gaz sont coupés")
    print('je peux partir en vacances')
else:
    print("l'eau et/ou le gaz ne sont pas coupés")
    print('je ne peux pas partir en vacances')

# avec vérification de ce qui n'a pas été coupé
if is_water_off and is_gas_off:
    print("l'eau et le gaz sont coupés")
    print('je peux partir en vacances')
else:
    print('je ne peux pas partir en vacances')

    if not is_water_off:
        print("l'eau n'est pas coupée")

    if not is_gas_off:
        print("le gaz n'est pas coupé")

has_bank_card = True
has_cash = False

# sans vérification du mode de paiement
if has_bank_card or has_cash:
    print("j'ai ma carte bancaire ou du cash")
    print('je peux faire du tourisme')
else:
    print("je n'ai ni ma carte bancaire ni du cash")
    print('je ne peux pas faire de tourisme')

# avec vérification du mode de paiement
if has_bank_card or has_cash:
    print('je peux faire du tourisme')

    if has_bank_card:
        print("j'ai ma carte bancaire")

    if has_cash:
        print("j'ai du cash")
else:
    print("je n'ai ni ma carte bancaire ni du cash")
    print('je ne peux pas faire de tourisme')

print()

stock = 10

if stock > 5:
    print('on est bon sur le stock')
elif stock <= 5 and stock > 0:
    print('il faut réapprovisionner le stock')
else:
    print('on est rupture de stock')

temperature = random.randint(0, 100) / -10
print(temperature)

if temperature < -5:
    print('la temperature est ok')
elif temperature >= -5 and temperature < -1:
    print("alerte : la temperature n'est pas assez froide")
else:
    print("erreur : la temperature est trop chaude")
