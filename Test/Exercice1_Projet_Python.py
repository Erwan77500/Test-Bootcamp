import random

def number_guessing_game():
  """
  Jeu de devinettes de nombres.  L'ordinateur choisit un nombre aléatoire entre 1 et 100,
  et le joueur a 7 tentatives pour le deviner.
  """

  # 1. Choisir un nombre aléatoire entre 1 et 100
  secret_number = random.randint(1, 100)

  # 2. Initialiser le nombre de tentatives
  attempts_left = 7

  # 3. Afficher un message de bienvenue
  print("Bienvenue au jeu de devinettes de nombres !")
  print("J'ai choisi un nombre secret entre 1 et 100.")
  print("Vous avez 7 tentatives pour le deviner.")

  # 4. Boucle principale du jeu
  while attempts_left > 0:
    try:
      # 4.1 Demander au joueur de deviner le nombre
      guess = int(input(f"Tentative #{7 - attempts_left + 1}: Veuillez entrer votre estimation : "))
    except ValueError:
      print("Erreur : Veuillez entrer un nombre entier.")
      continue  # Retour au début de la boucle

    # 4.2 Vérifier si la proposition du joueur est correcte
    if guess == secret_number:
      print(f"Félicitations ! Vous avez deviné le nombre {secret_number} en {7 - attempts_left + 1} tentatives.")
      return  # Fin du jeu (le joueur a gagné)

    # 4.3 Fournir un indice si la proposition est trop haute ou trop basse
    elif guess < secret_number:
      print("Trop bas. Essayez encore.")
    else:
      print("Trop haut. Essayez encore.")

    # 4.4 Décrémenter le nombre de tentatives restantes
    attempts_left -= 1

  # 5. Si le joueur n'a plus de tentatives
  print(f"Vous avez épuisé toutes vos tentatives. Le nombre secret était {secret_number}.")


# Lancer le jeu
if __name__ == "__main__":
  number_guessing_game()