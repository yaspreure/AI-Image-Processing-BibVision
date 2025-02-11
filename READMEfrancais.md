# 🚀 AI-Image-Processing-BibVision

**AI-Image-Processing-BibVision** est un outil de traitement d'images basé sur l'IA en Python qui extrait les numéros de dossard des coureurs à partir d'images en utilisant l'API OpenAI. Il traite automatiquement les images, extrait les numéros et enregistre les résultats aux formats JSON et CSV.

## 📌 Table des Matières
- [🔍 Présentation](#-présentation)
- [✨ Fonctionnalités](#-fonctionnalités)
- [⚙️ Installation](#-installation)
- [▶️ Utilisation](#-utilisation)
- [📂 Structure des fichiers](#-structure-des-fichiers)
- [🔑 Configuration de la clé API](#-configuration-de-la-clé-api)
- [🛠️ Personnalisation](#-personnalisation)
- [🤝 Contribution](#-contribution)
- [📜 Licence](#-licence)

## 🔍 Présentation
Ce projet utilise le modèle GPT-4o d'OpenAI pour analyser des images contenant des numéros de dossard. Les numéros extraits sont enregistrés dans `results.json` et automatiquement convertis en `results.csv` pour une analyse ultérieure.

## ✨ Fonctionnalités
✅ **Traitement d'images:** Lit et traite les images pour extraire les numéros de dossard.  
✅ **Reconnaissance basée sur l'IA:** Utilise l'API OpenAI pour une extraction de texte précise.  
✅ **Conversion automatique:** Convertit automatiquement les résultats JSON en CSV.  
✅ **Traitement personnalisable:** Permet une conversion JSON-vers-CSV manuelle si nécessaire.  

## ⚙️ Installation
1️⃣ **Cloner le dépôt:**  
   ```bash
   git clone https://github.com/yaspreure/AI-Image-Processing-BibVision.git
   cd AI-Image-Processing-BibVision
   ```
2️⃣ **Configurer un environnement virtuel (optionnel mais recommandé):**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Sous Windows, utilisez venv\Scripts\activate
   ```
3️⃣ **Installer les dépendances requises:**  
   ```bash
   pip install openai pandas
   ```
4️⃣ **Configurer la clé API OpenAI:**  
   Vous devez **acheter une clé API** auprès d'OpenAI et la définir comme variable d'environnement:  
   ```bash
   export OPENAI_API_KEY="votre_cle_api_ici"
   ```
   Sous Windows (Invite de commandes):  
   ```cmd
   set OPENAI_API_KEY=votre_cle_api_ici
   ```

## ▶️ Utilisation
### **1️⃣ Traiter les images et extraire les numéros de dossard**
📂 **Placez vos images dans le dossier `images/`.**  
▶️ **Exécutez le script principal:**  
   ```bash
   python image_processing.py
   ```
📄 **Les résultats extraits seront enregistrés dans `results.json` et automatiquement convertis en `results.csv`.**  

### **2️⃣ Convertir manuellement JSON en CSV**
Si vous préférez convertir JSON en CSV manuellement, **modifiez `image_processing.py` comme suit**:  
❌ **Supprimez ces deux lignes:**  
   ```python
   import subprocess
   subprocess.run(["python", "json_to_csv.py"])
   ```
✅ **Puis, exécutez le script de conversion manuellement:**  
   ```bash
   python json_to_csv.py
   ```

## 📂 Structure des fichiers
```
AI-Image-Processing-BibVision/
│── images/                 # Dossier contenant les images en entrée (format JPG)
│── results.json            # Fichier de sortie contenant les numéros de dossard extraits
│── results.csv             # Version CSV de results.json
│── image_processing.py     # Script principal pour traiter les images et extraire les numéros
│── json_to_csv.py          # Script pour convertir JSON en CSV
│── README.md               # Documentation du projet
```

## 🔑 Configuration de la clé API
Vous **devez acheter une clé API** auprès d'OpenAI et la définir comme variable d'environnement avant d'exécuter les scripts.

## 🛠️ Personnalisation
- **Modifier l'invite OpenAI** dans `image_processing.py` pour améliorer la précision:
  ```python
  {"type": "text", "text": "Quels sont les numéros de dossard des coureurs sur cette image ?"}
  ```
- **Changer le format de sortie** dans `json_to_csv.py` en modifiant les options `pandas.DataFrame.to_csv()`.

## 🤝 Contribution
Les contributions sont les bienvenues ! N'hésitez pas à **ouvrir des issues** ou **soumettre des pull requests**.

## 📜 Licence
Ce projet est sous licence **MIT**.

---
