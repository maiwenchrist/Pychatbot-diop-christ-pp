from functions import *


"""print()
print("//*** Voici l'extraction des noms de présidents à partir des fichiers texte ***//")
print()

directory = "./speeches"
files_list = list_of_files(directory, ".txt")
print_list(files_list)
print()

presidents_list = extract_presidents(files_list)
print("//*** Noms de fichier ***//")
print()
print(presidents_list)
print()

# dictionnaire
names = {
    "Giscard dEstaing": 'Valéry',
    "Mitterand": 'François',
    "Chirac": 'Jacque',
    "Sarkozy": 'Nicolas',
    "Hollande": 'François',
    "Macron": 'Emmanuel'
}
print("//*** Prénoms associer au nom de presidents sans doublon ***//")
print()

# affiche des noms et prenoms des presidents
for cle, name_president in names.items():
    print(cle, ':', name_president)
print()

cleaned_directory = "./cleaned"
convert_text(directory, cleaned_directory)
print("//*** Fichier nettoyés succès ***//")
print()

print("//*** Frequence des termes ***//")
print()

cleaned_files_list = list_of_files(cleaned_directory, ".txt")

for filename in cleaned_files_list:
    with open(os.path.join(cleaned_directory, filename), 'r', encoding='utf-8') as file:
        text = file.read()
        word_counts = counter(text)

        # Affichage des occurrences de mots pour chaque fichier
        print(f"Occurrences de mots dans le fichier {filename}:")
        print()
        for word, count in word_counts.items():
            print(f"Le mot '{word}' apparaît {count} fois.")
        print()


print("//*** Fréquence Inverse du Document ***//")
print()

corpus_directory = "./cleaned"
idf_scores = calculate_idf(corpus_directory)

# Affichage des scores IDF pour chaque mot (arrondis à l'entier le plus proche)
for word, score in idf_scores.items():
    print(f"Mot: {word}, Score IDF: {score}")
print()

tf_idf_matrix = calculate_tf_idf(corpus_directory)

# Affichage de la matrice TF-IDF
print("Matrice TF-IDF:")
print()

for row in tf_idf_matrix:
    print(row)

"""

print("Bienvenue dans le programme principal !")
while True:
    print("\nMenu :")
    print("1. Afficher les noms de fichiers")
    print("2. Extraire les noms de présidents")
    print("3. Nettoyer les fichiers")
    print("4. Afficher la fréquence des termes")
    print("5. Afficher la fréquence inverse du document")
    print("6. Afficher la matrice TF-IDF")
    print("7. Afficher les mots les moins importants")
    print("8. Afficher les mots avec le score TF-IDF le plus élevé")
    print("0. Quitter")

    choix = input("Veuillez sélectionner une option (0-7) : ")

    if choix == "1":
        print("//*** Affichage des noms de fichiers ***//")
        files_list = list_of_files("./speeches", ".txt")
        print_list(files_list)

    elif choix == "2":
        print("//*** Extraction des noms de présidents ***//")
        files_list = list_of_files("./speeches", ".txt")

        presidents_list = extract_presidents(files_list)

        print("Noms des présidents :")
        print(presidents_list)

    elif choix == "3":
        names = {
            "Giscard dEstaing": 'Valéry',
            "Mitterand": 'François',
            "Chirac": 'Jacque',
            "Sarkozy": 'Nicolas',
            "Hollande": 'François',
            "Macron": 'Emmanuel'
        }
        print("//*** Prénoms associer au nom de presidents sans doublon ***//")
        print()

        # affiche des noms et prenoms des presidents
        for cle, name_president in names.items():
            print(cle, ':', name_president)
        print()

    elif choix == "4":
        print("//*** Nettoyage des fichiers ***//")
        print()
        convert_text("./speeches", "./cleaned")
        print("Fichiers nettoyés avec succès !")

    elif choix == "5":
        cleaned_directory = "./cleaned"
        print("//*** Fréquence des termes ***//")
        print()

        cleaned_files_list = list_of_files(cleaned_directory, ".txt")

        for filename in cleaned_files_list:
            with open(os.path.join(cleaned_directory, filename), 'r', encoding='utf-8') as file:
                text = file.read()
                word_counts = counter(text)

                # Affichage des occurrences de mots pour chaque fichier
                print(f"Occurrences de mots dans le fichier {filename}:")
                print()
                for word, count in word_counts.items():
                    print(f"Le mot '{word}' apparaît {count} fois.")
                print()

    elif choix == "6":
        print("//*** Fréquence Inverse du Document ***//")
        print()

        corpus_directory = "./cleaned"
        idf_scores = calculate_idf(corpus_directory)

        # Affichage des scores IDF pour chaque mot (arrondis à l'entier le plus proche)
        for word, score in idf_scores.items():
            print(f"Mot: {word}, Score IDF: {score}")
        print()

    elif choix == "7":
        corpus_directory = "./cleaned"
        tf_idf_matrix = calculate_tf_idf(corpus_directory)

        # Affichage de la matrice TF-IDF
        print("Matrice TF-IDF:")
        print()

        for row in tf_idf_matrix:
            print(row)

    elif choix == "0":
        print("Au revoir !")
        break

    else:
        print("Option invalide. Veuillez choisir une option valide.")
