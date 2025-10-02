# Exercice 1: Dictionnaire à partir d'une liste de tuples
def tuple_to_dict(list_of_tuples):
  """Convertit une liste de tuples (clé, valeur) en dictionnaire."""
  return dict(list_of_tuples)

# Exemple d'utilisation:
my_list = [("name", "Elie"), ("job", "Instructor")]
my_dict = tuple_to_dict(my_list)
print(my_dict)  # Output: {'name': 'Elie', 'job': 'Instructor'}


# Exercice 2: Dictionnaire à partir de deux listes
def lists_to_dict(keys, values):
  """Crée un dictionnaire à partir de deux listes (clés et valeurs)."""
  return dict(zip(keys, values))

# Exemple d'utilisation:
keys = ["CA", "NJ", "RI"]
values = ["California", "New Jersey", "Rhode Island"]
my_dict = lists_to_dict(keys, values)
print(my_dict)  # Output: {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}


# Exercice 3: Dictionnaire avec voyelles comme clés et 0 comme valeur (sans fromkeys)
def vowels_dict():
  """Crée un dictionnaire avec les voyelles comme clés et 0 comme valeur."""
  vowels = ['a', 'e', 'i', 'o', 'u']
  my_dict = {}
  for vowel in vowels:
    my_dict[vowel] = 0
  return my_dict

# ou plus simplement, en utilisant une compréhension de dictionnaire
def vowels_dict_comprehension():
    vowels = ['a', 'e', 'i', 'o', 'u']
    return {vowel: 0 for vowel in vowels}



# Exemple d'utilisation:
my_dict = vowels_dict()
print(my_dict)  # Output: {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}


# Exercice 4: Dictionnaire avec position de la lettre comme clé et la lettre comme valeur
def alphabet_dict():
  """Crée un dictionnaire avec la position de la lettre comme clé et la lettre comme valeur."""
  import string  # Importe le module string pour accéder à l'alphabet
  alphabet = string.ascii_uppercase  # Obtient l'alphabet en majuscules
  my_dict = {}
  for i, letter in enumerate(alphabet):
    my_dict[i + 1] = letter  # i commence à 0, donc on ajoute 1 pour la position
  return my_dict

# ou, en utilisant une compréhension de dictionnaire:
def alphabet_dict_comprehension():
    import string
    alphabet = string.ascii_uppercase
    return {i + 1: letter for i, letter in enumerate(alphabet)}

# Exemple d'utilisation:
my_dict = alphabet_dict()
print(my_dict)
# Output:
# {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}


# Super bonus: Dictionnaire de comptage des voyelles dans une chaîne
def count_vowels(text):
  """Compte le nombre de chaque voyelle dans une chaîne."""
  vowels = ['a', 'e', 'i', 'o', 'u']
  my_dict = {vowel: 0 for vowel in vowels}  # Initialise le dictionnaire avec des comptes à 0
  text = text.lower()  # Convertit le texte en minuscules pour simplifier la comparaison

  for char in text:
    if char in vowels:
      my_dict[char] += 1  # Incrémente le compteur si le caractère est une voyelle

  return my_dict

# Exemple d'utilisation:
text = "awesome sauce"
my_dict = count_vowels(text)
print(my_dict)  # Output: {'a': 2, 'e': 3, 'i': 0, 'o': 1, 'u': 1}