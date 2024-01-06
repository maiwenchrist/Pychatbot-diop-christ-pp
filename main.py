from functions import *
import sys

print()
print("\t\tWelcome in the principal program !")
while True:
    print()
    print("\t\t\t\t\t\tMenu ")
    print()
    print("1. displays file names")
    print("2. Extract presidents' names")
    print("3. Cleans up files")
    print("4. Displays term frequency")
    print("5. Displays the inverse frequency of the document")
    print("6. Display TF-IDF matrix")
    print("7. Displays the least important words")
    print("8. Displays words with the highest TF-IDF score")
    print("9. Display of Chirac's most repeated word(s)")
    print("10. Displays the presidents who mentioned the 'Nation' and the one who mentioned it most frequently.")
    print("11. Displays the presidents who mentioned 'Nation' and the one who repeated it most often.")
    print("12. écologie")
    print("0. Leave")
    print()

    choix = input("Please select an option (0-13) :")
    print()

    if choix == "1":
        print("//*** Affichage des noms de fichiers ***//")
        files_list = list_of_files("./speeches", ".txt")
        print_list(files_list)

        print("//*** Extraction des noms de présidents ***//")
        files_list = list_of_files("./speeches", ".txt")

        presidents_list = extract_presidents(files_list)

        print("Noms des présidents :")
        print(presidents_list)

    elif choix == "2":
        print("//*** Prénoms associer au nom de presidents sans doublon ***//")
        print()

        nom_president = associate_president_names()
        for cle, name_president in nom_president.items():
            print(cle, ':', name_president)
        print()

    elif choix == "3":
        print("//*** Nettoyage des fichiers ***//")
        print()
        convert_text("./speeches", "./cleaned")
        print("Fichiers nettoyés avec succès !")

    elif choix == "4":
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

    elif choix == "5":
        print("//*** Fréquence Inverse du Document ***//")
        print()

        corpus_directory = "./cleaned"
        idf_scores = calculate_idf(corpus_directory)

        # Affichage des scores IDF pour chaque mot (arrondis a de chiffres après la virgule)
        for word, score in idf_scores.items():
            print(f"Mot: {word}, Score IDF: {score}")
        print()

    elif choix == "6":
        corpus_directory = "./cleaned"
        tf_idf_matrix = calculate_tf_idf(corpus_directory)

        # Affichage de la matrice TF-IDF
        print("//*** Matrice TF-IDF ***//")
        print()

        for row in tf_idf_matrix:
            print(row)

    elif choix == "7":
        print("//*** Liste des mots les moins important")
        print()

        corpus_directory = "./cleaned"
        tf_idf_matrix = calculate_tf_idf(corpus_directory)
        idf_scores = calculate_idf(corpus_directory)

        mots_non_importants = non_important_words(tf_idf_matrix, list(idf_scores.keys()))

        print(mots_non_importants)

    elif choix == "8":
        print("//*** Mots ayant un score TD-IDF le plus élevé")
        print()

        corpus_directory = "./cleaned"
        mots_importants_indices = highest_tfidf_words(corpus_directory)

        unique_words = list(calculate_idf(corpus_directory).keys())
        mots_importants = get_words_from_indices(mots_importants_indices, unique_words)

        if mots_importants:
            print("Mots avec le score TF-IDF le plus élevé :", mots_importants)
        else:
            print("Aucun mot trouvé avec un score TF-IDF élevé.")

    elif choix == '9':
        print("//*** Mots les plus répétés par Chirac ***//")
        print()

        corpus_directory = "./cleaned"  # Adapter le répertoire selon votre structure
        highest_words_by_chirac = highest_words_bychirac(corpus_directory)

        if highest_words_by_chirac is not None:
            unique_words = list(calculate_idf(corpus_directory).keys())
            chirac_word = get_words_from_indices([highest_words_by_chirac], unique_words)[0]
            print(f"Le mot le plus fréquent pour Chirac (hors mots non importants) est : {chirac_word}")
        else:
            print("Aucun mot le plus fréquent pour Chirac n'a été trouvé.")

    elif choix == '11':
        corpus_directory = "./cleaned"
        result = words_nation(corpus_directory)
        if result:
            most_repeated_president = result["Most Repeated President"].replace('.txt', '')

            print("Le(s) président(s) qui a(ont) parlé de la « Nation » :", list(result["Presidents"]))
            print("Le(s) président(s) qui a(ont) le plus répété le mot « Nation » :", most_repeated_president)
        else:
            print("Aucun président n'a parlé de la « Nation » ou le mot n'a pas été trouvé.")

    elif choix == '12':
        print("//*** Présidents parlant du climat et de l'écologie ***//")
        print()
        corpus_directory = "./cleaned"
        result = words_environment(corpus_directory)
        if result:
            print("Le(s) président(s) qui a(ont) parlé du climat et/ou de l’écologie :", list(result["Presidents"]))
        else:
            print("Aucun président n'a parlé du climat et/ou de l’écologie ou les mots-clés n'ont pas été trouvés.")

    elif choix == '13':
        corpus_directory = "./cleaned"
        idf_scores = calculate_idf(corpus_directory)

        question = input("Posez votre question: ")
        # first function part 2
        question_tokens = tokenize_question(question)
        """print("Tokens de la question: ", question_tokens)"""
        # second function part 2
        term_in_corpus = find_terms_in_corpus(question_tokens, idf_scores)
        """print("Termes de la question présents dans le corpus:", term_in_corpus)"""

        # Calculer le vecteur TF-IDF de la question
        unique_words = list(idf_scores.keys())  # Récupérer les mots uniques du corpus
        question_tf_idf = calculate_question_tf_idf(question_tokens, unique_words, idf_scores)

        tf_idf_matrix = calculate_tf_idf(corpus_directory)
        similarities = []
        for doc_vector in tf_idf_matrix:
            similarity = cosinus_similarity(question_tf_idf, doc_vector)
            similarities.append(similarity)

        # Trouver l'indice du document le plus similaire
        most_similar_index = similarities.index(max(similarities))
        """print(f"Le document le plus similaire à la question est le document numéro {most_similar_index + 1}.")
"""
        # Utilisation de la fonction pour obtenir le document le plus pertinent
        most_relevant = most_relevant_document(tf_idf_matrix, question_tf_idf)
        """print("Document le plus pertinent:", most_relevant)"""

        # Partie 6 - Génération de la réponse
        most_relevant_doc = list_of_files(corpus_directory, ".txt")[most_relevant]
        text_of_relevant_doc = ""
        with open(os.path.join(corpus_directory, most_relevant_doc), 'r', encoding='utf-8') as file:
            text_of_relevant_doc = file.read()

        word_with_highest_tfidf = highest_tf_idf_word(question_tf_idf, unique_words)
        response = find_sentence_with_word(text_of_relevant_doc, word_with_highest_tfidf)
        """print("Réponse générée:", response)"""

        # Partie 7 -
        # Affiner la réponse en fonction de la forme de la question posée
        refined_response = refine_response(question, response)

        print(f"Document pertinent retourné : {most_similar_index}")
        print(f"Mot ayant le TF-IDF le plus élevé : {word_with_highest_tfidf}")
        print(f"La réponse générée : {response}")
        print(f"Réponse affinée : {refined_response}")

    elif choix == "0":
        print("GOOD BYE !")
        sys.quit()

    else:
        print("Invalid option. Please choose a valid option.")
