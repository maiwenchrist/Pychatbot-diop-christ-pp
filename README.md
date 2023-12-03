# Pychatbot-diop-christ-pp
Projet  de python : My first chat bot (partie 1)

Oumy Diop et Maïwen Christ - L1 PLUS

URL du git : https://github.com/maiwenchrist/Pychatbot-diop-christ-pp.git

Année : 2023 - 2024
  

Sommaire : 


1. Introduction de la première partie du projet


2. Fonctionnalités principales de notre application


   1. Prétraitement des données
   2. Création de la matrice TF-IDF
   3. Recherche des mots les moins pertinents


3. Instruction d'exécution de notre code

   1. Prérequis
   2. Instructions
   3. Exécution du programme
   4. Interaction avec le Programme
   5. Options du menu



1. Introduction :
 
Dans cette première partie du projet, le programme présente l’analyse et le traitement de fichiers textes afin de comprendre la méthode utilisée dans la création d’un chat bot ou d’une intelligence artificielle (IA). L’objectif de cette 
première partie est de pouvoir développer des fonctions de base telles que la collecte et le prétraitement des données. La création de ces fonctions nous permettra de  collecter nos fichiers à partir d’un dossier donné nommé “speeches-20231109” , de nettoyer nos fichiers en supprimant la ponctuation, d’effectuer une conversion des textes en minuscules et la création d'une matrice TF-IDF nous permettra d’associer à chaque mot un score nommé “TF”. Ce score  permet de montrer l’importance des mots dans chaque document, cela nous apporte une meilleure compréhension du contenu de chaque fichiers. De plus, un menu a pu être créé afin que l’utilisateur puisse interagir avec la première partie du programme.


Ces fonctions sont importantes pour la suite de notre projet car on pourra rendre notre chatbot capable de fournir des réponses pertinentes et adaptées aux questions posées par les utilisateurs.


II.  Fonctionnalités principales de notre application
   Prétraitement des données


   * Fonction : def convert_text(directory, cleaned_directory): 


   * Description : La fonction permet de prendre l’ensemble des fichiers texte puis de les convertir en minuscules puis  supprime la ponctuation et sauvegarde les fichiers nettoyés dans un nouveau répertoire nommé “cleaned”


Création de la matrice TF-IDF


   * Fonctions : def counter(text):; def calculate_idf(directory):;def calculate_tf_idf(directory):


   * Description : Les fonctions counter, calculate_idf et calculate_tf_idf permettent de calculer ou analyser la fréquence des mots. Ces fonctions évaluent leur importance respective dans chaque document et créent une matrice TF-IDF. La matrice permet d’évaluer numériquement l’importance des mots dans chacun des textes du corpus. 


Recherche des mots les moins pertinents


   * Fonctions : def non_important_words(tfidf_matrix, unique_words):; def highest_tfidf_words(corpus_directory):; def display_non_important_words(tfidf_matrix, unique_words):


   * Description : Les fonctions non_important words, highest_tfidf_words et display_non_important_words permettent d’identifier les mots ayant un score TF_IDF de zéro dans tous les documents, ce qui suggère leur faible importance dans le corpus. Cela peut aider à voir les mots les moins pertinents.


III. Instructions d’exécutions du programme
   
   Prérequis


      * Il est conseillé d’avoir la version 3.10.11 de Python ainsi que de disposé des bibliothèques suivante : “os”, “string”, “maths”, “collections”


   Instruction


      * Instruction : Vérifier que vous avez bien téléchargé le dossier “speeches-20231109” contenant les fichiers ‘speeches’ à analyser. Assurez-vous aussi que vôtre dossier ‘cleaned’ soit vidé pour stocker les fichiers nettoyés.

   Exécution du programme


      * Ouvrez votre IDE Python et vérifiez que votre répertoire de travail est bien le code source. Puis exécutez le fichier principal contenant le code (‘main.py’ et ‘functions.py’)


   Interaction avec le programme


      * Dès le “run” du programme, un menu interactif s’affichera. Vous pourrez ainsi choisir l’option en saisissant son numéro et de pouvoir visualiser son action.


   Options du menu


      * Affichage des noms de fichiers : Affiche les noms des fichiers dans le répertoire speeches.
      *   Extraction des noms de présidents : Récupérer les noms des présidents à partir des noms de fichiers.
      * Nettoyage des fichiers : Effectue le nettoyage des fichiers textuels.
      * Affichage de la fréquence des termes : Affiche la fréquence des mots dans les fichiers nettoyés.
      * Affichage de la fréquence inverse du document (IDF) : Affiche les scores IDF pour chaque mot.
      * Affichage de la matrice TF-IDF : Affiche la matrice TF-IDF calculée.
      * Quitter : Termine l'exécution du programme. Pour quitter le programme, il faudra sélectionner l’option ‘0’ dans le menu, le programme affichera “Au revoir !”.
