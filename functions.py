import os
import string
import math
from collections import defaultdict

# PARTIE 1
#  Les fonctions de base


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def print_list(file_list):
    for file_name in file_list:
        print(file_name)


def extract_presidents(files_names):
    presidents = set()

    for file_name in files_names:

        president_name = file_name.split("_")[1].capitalize()

        presidents.add(president_name)

    return list(presidents)


def associate_president_names():
    president_names = {
        "Giscard dEstaing": 'Valéry',
        "Mitterand": 'François',
        "Chirac": 'Jacque',
        "Sarkozy": 'Nicolas',
        "Hollande": 'François',
        "Macron": 'Emmanuel'
    }

    return president_names


# demander au prof
def convert_text(directory, cleaned_directory):
    # Vérification de la création du dossier cleaned
    os.makedirs(cleaned_directory, exist_ok=True)

    files_names = list_of_files(directory, "txt")

    for filename in files_names:
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            text = file.read()
            # Conversion en minuscules
            text = text.lower()
            # Suppression de la ponctuation
            text = text.translate(str.maketrans('', '', string.punctuation))
            # Écriture du texte nettoyé dans un nouveau fichier
            cleaned_filename = os.path.join(cleaned_directory, filename)

            with open(cleaned_filename, 'w', encoding='utf-8') as cleaned_file:
                cleaned_file.write(text)


# La methode TF-IDF
def counter(text):
    words = text.split()
    word_freq = defaultdict(int)

    for word in words:
        word_freq[word] += 1

    return word_freq


def calculate_idf(directory):
    num_docs = 0
    word_doc_count = defaultdict(int)

    # Compter le nombre de documents dans lesquels chaque mot apparaît
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            num_docs += 1
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                text = file.read().lower()
                words = set(text.split())
                for word in words:
                    word_doc_count[word] += 1

    idf_scores = {}
    for word, count in word_doc_count.items():
        idf = (math.log10(num_docs / count))
        idf_scores[word] = idf

    return idf_scores


def calculate_tf_idf(directory):
    word_idf = calculate_idf(directory)
    unique_words = list(word_idf.keys())

    tfidf_matrix = []

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                text = file.read().lower()
                word_freq = counter(text)
                tfidf_vector = []

                for word in unique_words:
                    tf = word_freq[word] if word in word_freq else 0
                    tfidf = tf * word_idf[word]
                    # Convertir en entier
                    tfidf_vector.append(float(round(tfidf, 2)))  # Convertir en réel ici

                tfidf_matrix.append(tfidf_vector)

    return tfidf_matrix


def non_important_words(tfidf_matrix, unique_words):
    non_important = []
    for i, word in enumerate(unique_words):
        word_tfidf = [doc[i] for doc in tfidf_matrix]
        if all(tfidf == 0 for tfidf in word_tfidf):
            non_important.append(word)
    return non_important


def highest_tfidf_words(corpus_directory):
    tf_idf_matrix = calculate_tf_idf(corpus_directory)
    max_tfidf_words = []

    for i, doc in enumerate(tf_idf_matrix):
        max_tfidf = max(doc)
        if max_tfidf > 0:
            max_tfidf_indices = [index for index, value in enumerate(doc) if value == max_tfidf]
            max_tfidf_words.extend(max_tfidf_indices)

    return max_tfidf_words


# Fonction pour obtenir les mots à partir des indices
def get_words_from_indices(indices, unique_words):
    return [unique_words[idx] for idx in indices]


def highest_words_bychirac(corpus_directory):
    tf_idf_matrix = calculate_tf_idf(corpus_directory)
    non_important = non_important_words(tf_idf_matrix, list(calculate_idf(corpus_directory).keys()))
    max_tdidf_chirac = defaultdict(float)

    for i, doc in enumerate(tf_idf_matrix):
        if "Chirac" in list_of_files(corpus_directory, ".txt")[i]:  # Vérifie si le fichier correspond à Chirac
            for index, value in enumerate(doc):
                if value > 0 and index not in non_important:
                    max_tdidf_chirac[index] += value

    # Obtenez l'indice du mot le plus répété pour Chirac
    if max_tdidf_chirac:
        max_index = max(max_tdidf_chirac, key=max_tdidf_chirac.get)
        return max_index
    else:
        return None


def words_nation(corpus_directory):
    tf_idf_matrix = calculate_tf_idf(corpus_directory)
    unique_words = list(calculate_idf(corpus_directory).keys())
    word_indices = [i for i, word in enumerate(unique_words) if word.lower() == 'nation']

    if word_indices:
        president_word_count = defaultdict(float)
        presidents_with_nation = set()  # Utilisation d'un ensemble pour éviter les doublons

        for i, doc in enumerate(tf_idf_matrix):
            filename = list_of_files(corpus_directory, ".txt")[i]
            president_name = filename.split("_")[1].capitalize()
            for index in word_indices:
                president_word_count[president_name] += doc[index]
                if doc[index] > 0:
                    presidents_with_nation.add(president_name)

        if president_word_count:
            max_repeated_president = max(president_word_count, key=president_word_count.get)

            return {
                "Presidents": list(presidents_with_nation),
                "Most Repeated President": max_repeated_president,
                "Word Count": president_word_count[max_repeated_president]
            }
    return None


def words_environment(corpus_directory):
    tf_idf_matrix = calculate_tf_idf(corpus_directory)
    unique_words = list(calculate_idf(corpus_directory).keys())

    # Chercher les mots liés à l'environnement, par exemple : climat, écologie, environnement, etc.
    environment_words = ['climat', 'écologie', 'environnement']  # Vous pouvez ajouter d'autres mots-clés

    word_indices = [i for i, word in enumerate(unique_words) if word.lower() in environment_words]

    if word_indices:
        president_word_count = defaultdict(float)
        presidents_about_environment = set()

        for i, doc in enumerate(tf_idf_matrix):
            filename = list_of_files(corpus_directory, ".txt")[i]
            president_name = filename.split("_")[1].capitalize()
            for index in word_indices:
                president_word_count[president_name] += doc[index]
                if doc[index] > 0:
                    presidents_about_environment.add(president_name)

        if president_word_count:
            return {
                "Presidents": list(presidents_about_environment),
                "Word Count": president_word_count
            }
    return None

# PARTIE 2 dans functions2
