Projet  de python 


My first chat bot 




Oumy Diop et Maïwen Christ - L1 PLUS


https://github.com/maiwenchrist/Pychatbot-diop-christ-pp.git






































2023 - 2024
  

Sommaire : 


1. Introduction de la première partie du projet


2. Fonctionnalités principales de notre application


1. Prétraitement des données
2. Création de la matrice TF-IDF
3. Recherche des mots les moins pertinents et plus pertinents


3. Deuxième partie


4. difficultés


5. Conclusion








































  

1. Introduction :


 
     Dans cette première partie du projet, le programme présente l’analyse et le traitement de fichiers textes afin de comprendre la méthode utilisée dans la création d’un chat bot ou d’une intelligence artificielle (IA). L’objectif de cette 
première partie est de pouvoir développer des fonctions de base telles que la collecte et le prétraitement des données. La création de ces fonctions nous permettra de  collecter nos fichiers à partir d’un dossier donné nommé “speeches-20231109” , de nettoyer nos fichiers en supprimant la ponctuation, d’effectuer une conversion des textes en minuscules et la création d'une matrice TF-IDF nous permettra d’associer à chaque mot un score nommé “TF”. Ce score  permet de montrer l’importance des mots dans chaque document, cela nous apporte une meilleure compréhension du contenu de chaque fichier. De plus, un menu a pu être créé afin que l’utilisateur puisse interagir avec la première partie du programme.


Ces fonctions sont importantes pour la suite de notre projet car on pourra rendre notre chatbot capable de fournir des réponses pertinentes et adaptées aux questions posées par les utilisateurs.
















  











  
II.  Fonctionnalités principales de notre application
   Prétraitement des données


* Fonction : def convert_text(directory, cleaned_directory): 


* Description : La fonction permet de prendre l’ensemble des fichiers texte puis de les convertir en minuscules puis  supprime la ponctuation et sauvegarde les fichiers nettoyés dans un nouveau répertoire nommé “cleaned”


Création de la matrice TF-IDF


* Fonctions : def counter(text):; def calculate_idf(directory):;def calculate_tf_idf(directory):


* Description : Les fonctions counter, calculate_idf et calculate_tf_idf permettent de calculer ou analyser la fréquence des mots. Ces fonctions évaluent leur importance respective dans chaque document et créent une matrice TF-IDF. La matrice permet d’évaluer numériquement l’importance des mots dans chacun des textes du corpus. 


Recherche des mots les moins pertinents et plus pertinents


* Fonctions : def non_important_words(tfidf_matrix, unique_words):; def highest_tfidf_words(corpus_directory):; def get_words_from_indices(indices, unique_words):; def highest_words_bychirac(corpus_directory):;def words_nation(corpus_directory): et def words_environment(corpus_directory):


* Description : La fonction non_important_words permet d’identifier les mots qui ne sont pas importants dans un corpus grâce à la matrice. Elle vérifie que chaque mot est une valeur TF-IDF nulle dans tous les fichiers puis elle l’ajoute à la liste ‘non_important’.


La fonction highest_tfidf_words(corpus_directory):
 est l’inverse de la précédente. Le principe est le même mais avec le score TF-IDF le plus élevé, puis elle rassemble les indices vers une liste ‘max_tfidf_words.


La fonction get_words_from_indices(indices, unique_words):
 regroupe les deux listes (’indices et mots uniques) qui est renvoyée dans une nouvelle liste contenant les mots correspondant aux indices spécifiés dans la liste des mots uniques.


La fonction highest_words_bychirac(corpus_directory):
 se sert de la matrice TF-IDF pour connaître le mot le plus utilisé lors du discours de Jacques Chirac. Tout d’abord, elle calcule les indices non importants dans tous les fichiers correspondant à Chirac. Ensuite, la fonction identifie et additionne leur score TF-IDF, puis retourne l’indice du mot le plus fréquent.


La fonction words_nation(corpus_directory):
vise à identifier les présidents ayant dit le mot “Nation”. Le principe est le même que la fonction précédente, elle identifie les indices du mot “Nation” dans la liste des mots uniques et calcule la fréquence du mot dans chaque corpus. Puis elle retourne le nom du président qui l’a mentionné le plus de fois avec le nombre total d’appartions.


la fonction words_environment(corpus_directory):
 fonctionne comme la précédente.
  



















  
III. Deuxième Partie




* Fonction : def tokenize_question(question):;def find_terms_in_corpus(question_tokens, idf_scores):;def calculate_question_tf_idf(question_tokens, unique_words, idf_scores):


* Description : La fonction permet de convertir la question en minuscules, supprimer toute ponctuation et de diviser en mots distincts
* La fonction compare les tokens de la question avec ceux du corpus grâce aux scores IDF
* La fonction  calculate_question_tf_idf est chargée de calculer un vecteur TF-IDF pour une question donnée en fonction des mots présents dans cette question et des scores IDF des mots du corpus.


        Prétraitement des données


* Fonction : def dot_product(vector1, vector2):; def vector_norm(vector):; def cosinus_similarity(vector1, vector2):


* Description : La fonction dot_product calcule le produit scalaire entre deux vecteurs. 
* La fonction vector_norm calcule la norme d’un vecteur
* La fonction cosinus_similarity utilise les deux fonctions précédente pour calculer la similarité de cosinus entre deux vecteurs


        Prétraitement des données


* Fonction : def most_relevant_document(tfidf_matrix, question_vector):; def highest_tf_idf_word(question_tf_idf, unique_words):;def find_sentence_with_word(text, word):;def refine_response(question, answer):


* Description : La fonction most_relevant_document cherche le document le plus pertinent en comparant la similarité de cosinus entre le vecteur de la question et chaque vecteur de document dans la matrice TF-IDF.Elle initialise highest_similarity à 0 et most_relevant_doc_index à -1. Puis elle itère à travers chaque vecteur de document dans tfidf_matrix, calcule la similarité du cosinus entre le vecteur de la question et chaque vecteur de document. Si la similarité est supérieure à highest_similarity, elle met à jour highest_similarity avec cette nouvelle valeur et enregistre l'index du document correspondant dans most_relevant_doc_index. Puis, elle renvoie l'index du document ayant la plus grande similarité avec la question.


* La fonction highest_tf_idf_word identifie le mot ayant le score TF-IDF le plus élevé dans le vecteur de la question. Elle recherche l'index du score TF-IDF le plus élevé dans le vecteur question_tf_idf à l'aide de la fonction index. Ensuite, elle renvoie le mot correspondant à cet index dans la liste unique_words.


* La fonction find_sentence_with_word recherche la première phrase dans le texte qui contient un mot spécifique.Elle divise le texte en phrases en utilisant le délimiteur "." et recherche la première phrase contenant le mot spécifié.Si elle trouve une phrase avec ce mot, elle la retourne. Sinon, elle renvoie une chaîne vide


* La fonction refine_response peaufine la réponse en fonction du type de question posée.Elle utilise un dictionnaire question_starters contenant des préfixes courants de questions (comme "Comment", "Pourquoi", "Peux-tu") et associe à chaque préfixe une réponse appropriée.Si la question commence par l'un de ces préfixes, elle retourne une réponse avec le préfixe approprié. Sinon, elle renvoie simplement la réponse originale avec la première lettre en majuscule.


  

6. difficultés


La deuxième partie du projet, centrée sur des fonctions mathématiques, a été un défi pour nous, étant donné nos difficultés dans ce domaine. Par ailleurs, la mise en place du script principal présente également présenté des défis. L'absence de fonctionnalité de 'break' a nécessité l'apprentissage de nouvelles méthodes, telles que l'utilisation de 'import sys', pour gérer l'arrêt du programme. Au départ, nous avons rencontré des difficultés lors de la conversion des textes dans le dossier. Nous avons appris à contourner le problème des caractères spéciaux pour maintenir la lisibilité des textes en utilisant 'encoding=utf-8'. Cette approche nous a permis d'effectuer la conversion sans altérer les caractères spéciaux.


7. Conclusion


En somme, ce projet a été une expérience enrichissante. Malgré les défis rencontrés, nous avons appris de nouvelles compétences et surmonté des obstacles techniques. Cela nous a permis de mieux comprendre la complexité des problèmes abordés et d'améliorer nos capacités en programmation.
