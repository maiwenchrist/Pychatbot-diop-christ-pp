# PARTIE 2
import string
from functions import counter
import math


def tokenize_question(question):
    # Convertir en minuscules
    question = question.lower()
    # Supprimer la ponctuation
    question = question.translate(str.maketrans('', '', string.punctuation))
    # Diviser en mots
    tokens = question.split()
    return tokens


def find_terms_in_corpus(question_tokens, idf_scores):
    return [token for token in question_tokens if token in idf_scores]


def calculate_question_tf_idf(question_tokens, unique_words, idf_scores):
    # Initialiser le vecteur TF-IDF de la question avec des zéros
    question_tf_idf = [0] * len(unique_words)

    # Calculer la fréquence des mots dans la question
    # convertir les tokens en une seule chaine
    word_freq = counter(" ".join(question_tokens))

    # Calculer le vecteur TF-IDF pour la question
    for i, word in enumerate(unique_words):
        if word in word_freq:
            # TF * IDF
            question_tf_idf[i] = word_freq[word] * idf_scores.get(word, 0)

    return question_tf_idf


# 4e fonction SIMILARITE DE COSINUS
# calcule le produit scalaire entre les deux vecteurs
def dot_product(vector_a, vector_b):
    return sum(a * b for a, b in zip(vector_a, vector_b))


# norme de chaque vecteur
def vecteur_norm(vector):
    return math.sqrt(sum(a * a for a in vector))


# division produit scalaire par le produit des deux normes
def cosinus_similarite(vector_a, vector_b):
    dot_prod = dot_product(vector_a, vector_b)
    norm_a = vecteur_norm(vector_a)
    norm_b = vecteur_norm(vector_b)

    if norm_a == 0 or norm_b == 0:
        return 0
    return dot_prod / (norm_a * norm_b)


def find_most_relevant_document(tfidf_matrix, question_vector):
    highest_similarity = 0
    most_relevant_doc_index = -1

    for index, doc_vector in enumerate(tfidf_matrix):
        similarity = cosinus_similarite(question_vector, doc_vector)
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_relevant_doc_index = index

    return most_relevant_doc_index


# 6e fonctions
def highest_tf_idf_word(question_tf_idf, unique_words):
    highest_score_index = question_tf_idf.index(max(question_tf_idf))
    return unique_words[highest_score_index]


def find_sentence_with_word(text, word):
    sentences = [sentence.strip() + '.' for sentence in text.split('.') if word in sentence]
    return sentences[0] if sentences else ""


# 7e fonctions
def refine_response(question, answer):
    # Liste de propositions non exhaustives
    question_starters = {
        "Comment": "Après analyse, ",
        "Pourquoi": "Car, ",
        "Peux-tu": "Oui, bien sûr! ",
    }
    # Trouver le début de la question et sélectionner la réponse appropriée
    for starter, response_starter in question_starters.items():
        if question.startswith(starter):
            return response_starter + answer[0].upper() + answer[1:]

    # Si aucune correspondance n'est trouvée, retourner la réponse originale
    return answer[0].upper() + answer[1:]
