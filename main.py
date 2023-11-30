from functions import *


print()
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


while True:
    print("\nMenu:")
    print("1. Afficher les mots non importants")
    print("0. Quitter")

    choice = input("Choisissez une fonctionnalité (1 ou 0 pour quitter): ")

    if choice == "1":
        display_non_important_words(tf_idf_matrix, )

    elif choice == "0":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez choisir une option valide.")
