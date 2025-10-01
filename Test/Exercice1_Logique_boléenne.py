# Exercice 1 : Logique Booléenne
# 1. Déclarez une variable appelée et attribuez-la à la valeur .first "Hello World"
et = "Hello World"
# This is a comment.

# 3. Consignez un message sur le terminal indiquant "I AM A COMPUTER!"
print("I AM A COMPUTER!")

# 4. Écrivez une instruction if qui vérifie si est inférieur à et si est supérieur à
# Si c'est le cas, affichez le message 1242 "Math is fun."
if 1 < 2 and 4 > 2:
    print("Math is fun.")

# 5. Attribuez une variable appelée à une absence de valeur (none)
nope = None

# 6. Utilisez l'opérateur booléen « and » de la langue pour combiner la valeur « true »
# de la langue avec sa valeur « false »
result_and = True and False

# 7. Calculer la longueur de la chaîne "What's my length?"
length = len("What's my length?")

# 8. Convertissez la chaîne en majuscules "i am shouting"
uppercase = "i am shouting".upper()

# 9. Convertissez la chaîne en nombre "1000"
number = int("1000")

# 10. Combinez le nombre avec la chaîne pour obtenir 4 "real" "4real"
combined = str(4) + "real"

# 11. Enregistrez le résultat de l'expression .3 * "cool"
repeated = 3 * "cool"

# 12. Enregistrez le résultat de l'expression .1 / 0
# Note: Ceci causera une erreur ZeroDivisionError
# division_result = 1 / 0  # Décommentez pour voir l'erreur

# 13. Déterminez le type de []
type_list = type([])

# 14. Demandez à l'utilisateur son nom et stockez-le dans une variable appelée .name
name = input("Quel est votre nom? ")

# 15. Demandez un numéro à l'utilisateur. Si le nombre est négatif, affichez un message
# indiquant Si le nombre est positif, affichez un message indiquant Sinon, affichez
# un message indiquant "That number is less than 0!" "That number is greater than 0!" "You picked 0!"
number_input = int(input("Entrez un numéro: "))
if number_input < 0:
    print("That number is less than 0!")
elif number_input > 0:
    print("That number is greater than 0!")
else:
    print("You picked 0!")

# 16. Trouvez l'indice de dans "l" "apple"
index = "apple".index("l")

# 17. Vérifiez si est dans "y" "xylophone"
is_in = "y" in "xylophone"

# 18. Vérifiez si une chaîne appelée est entièrement en minuscules (my_string)
my_string = "example"
is_lowercase = my_string.islower()

# Affichage des résultats pour vérification
print("\n--- Résultats ---")
print(f"1. et = {et}")
print(f"3. Message affiché ci-dessus")
print(f"4. Condition vérifiée ci-dessus")
print(f"5. nope = {nope}")
print(f"6. True and False = {result_and}")
print(f"7. Longueur = {length}")
print(f"8. Majuscules = {uppercase}")
print(f"9. Nombre = {number}")
print(f"10. Combiné = {combined}")
print(f"11. Répété = {repeated}")
print(f"13. Type de [] = {type_list}")
print(f"14. Nom saisi ci-dessus")
print(f"15. Condition vérifiée ci-dessus")
print(f"16. Index de 'l' dans 'apple' = {index}")
print(f"17. 'y' dans 'xylophone' = {is_in}")
print(f"18. my_string est en minuscules = {is_lowercase}")