import os
import string
import math
from collections import defaultdict


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


# demander au prof
def convert_text(directory, cleaned_directory):
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

        with open(cleaned_filename, 'w', encoding='utf-8') as file:
            file.write(text)


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
        idf = round(math.log(num_docs / count))
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
                    tfidf_vector.append(int(tfidf))  # Convertir en entier ici

                tfidf_matrix.append(tfidf_vector)

    return tfidf_matrix


"""def non_important_words(tfidf_matrix, unique_words):
    non_important = []
    for i, word in enumerate(unique_words):
        word_tfidf = [doc[i] for doc in tfidf_matrix]
        if all(tfidf == 0 for tfidf in word_tfidf):
            non_important.append(word)
    return non_important


def highest_tfidf_words(corpus_directory):

    tf_idf_matrix = calculate_tf_idf(corpus_directory)

    mots_moins_importants = []
    for i, doc in enumerate(tf_idf_matrix):
        if all(score == 0 for score in doc):
            mots_moins_importants.append(i)

    return mots_moins_importants



def display_non_important_words(tfidf_matrix, unique_words):
    non_important = non_important_words(tfidf_matrix, unique_words)
    if non_important:
        print("Mots non importants (avec un score TF-IDF de 0 dans tous les fichiers):")
        print(", ".join(non_important))
    else:
        print("Aucun mot non important trouvé.")"""
