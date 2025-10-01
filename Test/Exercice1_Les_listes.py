# 1. Imprimer toutes les valeurs de la liste une par une
print("Exercice 1:")
liste1 = [1, 2, 3, 4]
for valeur in liste1:
    print(valeur)

# 2. Imprimer toutes les valeurs de la liste multipliées par 20
print("\nExercice 2:")
liste2 = [1, 2, 3, 4]
for valeur in liste2:
    print(valeur * 20)

# 3. Renvoie une nouvelle liste avec seulement la première lettre de chaque nom
print("\nExercice 3:")
liste3 = ["Elie", "Tim", "Matt"]
premieres_lettres = [nom[0] for nom in liste3]
print(premieres_lettres)

# 4. Renvoie une nouvelle liste avec toutes les valeurs paires
print("\nExercice 4:")
liste4 = [1, 2, 3, 4, 5, 6]
valeurs_paires = [val for val in liste4 if val % 2 == 0]
print(valeurs_paires)

# 5. Renvoie une nouvelle liste qui ne contient que les valeurs présentes dans les deux listes
print("\nExercice 5:")
liste5a = [1, 2, 3, 4]
liste5b = [3, 4, 5, 6]
valeurs_communes = [val for val in liste5a if val in liste5b]
print(valeurs_communes)

# 6. Renvoie une nouvelle liste avec chaque mot inversé et en minuscules
print("\nExercice 6:")
liste6 = ["Elie", "Tim", "Matt"]
mots_inverses = [mot[::-1].lower() for mot in liste6]
print(mots_inverses)

# 7. Renvoie une nouvelle liste des lettres présentes dans les deux chaînes
print("\nExercice 7:")
chaine7a = "first"
chaine7b = "third"
lettres_communes = [lettre for lettre in chaine7a if lettre in chaine7b]
print(lettres_communes)

# 8. Renvoie une liste des nombres divisibles par 12 entre 1 et 100
print("\nExercice 8:")
divisibles_par_12 = [i for i in range(1, 101) if i % 12 == 0]
print(divisibles_par_12)

# 9. Renvoie une liste avec toutes les voyelles supprimées
print("\nExercice 9:")
chaine9 = "amazing"
voyelles = "aeiouy"
sans_voyelles = [lettre for lettre in chaine9 if lettre.lower() not in voyelles]
print(sans_voyelles)

# 10. Générez une liste avec la valeur suivante : [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
print("\nExercice 10:")
liste10 = [[0, 1, 2] for _ in range(3)]
print(liste10)

# 11. Générez une liste avec la structure suivante
print("\nExercice 11:")
liste11 = [[i for i in range(10)] for _ in range(10)]
for ligne in liste11:
    print(ligne)