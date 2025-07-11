# chatbot-bas-sur-ChatGPT-et-Streamlit
### 🧠 Description
Ce projet montre comment construire une application chatbot en Python, avec une interface graphique via Streamlit et des réponses générées par l’API OpenAI (ChatGPT).

L'objectif est d'explorer les fonctionnalités des LLM (Large Language Models) à travers des versions évolutives de l’application, en suivant un processus professionnel avec Git (branches, workflow, fusion, etc.).

### 🚀 Fonctionnalités
-Affichage des échanges sous forme de messages (utilisateur & assistant)

-Sélection dynamique du modèle GPT via un selectbox

-Contrôle du nombre de jetons générés via un slider

-Utilisation de l’API OpenAI avec clé sécurisée via secrets.toml

### 🔧 Installation
# 1.Cloner le projet

git clone https://github.com/<ton-utilisateur>/streamlitbot.git
cd streamlitbot

# 2.Créer un environnement virtuel
python -m venv stenv
stenv\Scripts\activate 

# 3.Installer les dépendances
pip install -r requirements.txt
# 4.Ajouter votre clé API OpenAI Dans .streamlit/secrets.toml :
OPENAI_API_KEY = "votre_clé_api"

### 🧾 Fichier 
### 1.gitignore
Assurez-vous que les éléments suivants sont ignorés dans Git :

### 2.Environnement virtuel
stenv/

### 3.Dossier de configuration Streamlit
.streamlit/
.streamlit/secrets.toml

### 📌 Commandes Git utiles

1.Vérifier l’état du dépôt
git status

2.Ajouter tous les fichiers modifiés
git add .

3.Valider les modifications
git commit -m "Message du commit"

4. Pousser vers la branche distante
git push origin <nom-de-la-branche>

5. Créer une nouvelle branche
git checkout -b versionX

6. Fusionner avec la branche main
git checkout main
git merge versionX

### ▶️ Lancer l’application
streamlit run chatbotgpt.py


L’application s’ouvre dans le navigateur avec une interface de type ChatGPT où :

Tu écris ton message

Tu choisis un modèle GPT

Tu règles le nombre de jetons

Et l’assistant te répond en streaming !
