from functions import *
from functions2 import *

print()
print("\t\tBienvenue dans le programme principal !")
while True:
    print()
    print("\t\t\t\t\t\tMenu ")
    print()
    print("\t\t1. Afficher les noms de fichiers")
    print("\t\t2. Extraire les noms de présidents")
    print("\t\t3. Nettoyer les fichiers")
    print("\t\t4. Afficher la fréquence des termes")
    print("\t\t5. Afficher la fréquence inverse du document")
    print("\t\t6. Afficher la matrice TF-IDF")
    print("\t\t7. Afficher les mots les moins importants")
    print("\t\t8. Afficher les mots avec le score TF-IDF le plus élevé")
    print("\t\t9. Afficher le(s) mot(s) le(s) plus répété(s) par Chirac")
    print("\t\t10. Afficher le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois ")
    print("\t\t11. Afficher le(s) nom(s) président(s) qui a (ont) parlé de la 'Nation'  et celui qui l'a répété le plus de fois ")
    print("\t\t12. ")
    print("\t\t0. Quitter")
    print()

    choix = input("Veuillez sélectionner une option (0-13) : ")
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

        # Affichage des scores IDF pour chaque mot (arrondis à l'entier le plus proche)
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
        tf_idf_matrix = calculate_tf_idf(corpus_directory)
        idf_scores = calculate_idf(corpus_directory)
        unique_words = list(calculate_idf(corpus_directory).keys())

        question_user = input("\nPosez votre question: ")
        tokens = tokenize_question(question_user)
        terms_in_corpus = find_terms_in_corpus(tokens, idf_scores)
        question_tf_idf = calculate_question_tf_idf(question_user, unique_words, idf_scores)
        most_relevant_doc_index = find_most_relevant_document(tf_idf_matrix, question_tf_idf)
        most_relevant_doc_name = filename[most_relevant_doc_index]
        with open(os.path.join(corpus_directory, most_relevant_doc_name), 'r', encoding='utf-8') as file:
            text = file.read()
        highest_tf_idf_word_in_question = highest_tf_idf_word(question_tf_idf, unique_words)
        question_starters = {
            "Comment": "Après analyse, ",
            "Pourquoi": "Car, ",
            "Peux-tu": "Oui, bien sûr! ",
        }
        relevant_sentence = find_sentence_with_word(text, highest_tf_idf_word_in_question)
        refined_answer = refine_response(question_user, relevant_sentence)
        print("Document pertinent:", most_relevant_doc_name)
        print()
        print("Mot le plus pertinent dans la question:", highest_tf_idf_word_in_question)
        print()
        print("Réponse générée:", relevant_sentence)
        print()
        print("Réponse raffinée:", refined_answer)

    elif choix == "0":
        print("Au revoir !")
        break

    else:
        print("Option invalide. Veuillez choisir une option valide.")
