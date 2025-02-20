# **Projet Flask : Formulaire d'Identification Sécurisé**

## **Description du projet**
Ce projet est une application web Flask permettant aux utilisateurs de se connecter via un formulaire sécurisé. 

Fonctionnalités principales :
- Connexion via un formulaire HTML
- Vérification des identifiants avec une base de données SQLite
- Sécurisation des mots de passe avec `bcrypt`
- Création de nouveaux comptes
- Gestion des erreurs et affichage des messages d'état

---

## **Technologies utilisées**

- **Python 3** (Flask, SQLite3, bcrypt)
- **HTML/CSS** (Interface utilisateur)
- **JavaScript (Fetch API)** (Requêtes AJAX pour la connexion et l'ajout de compte)

---

## **Installation et Configuration**

### **1. Cloner le projet**
```bash
git clone https://github.com/imad859/projet-flask.git
cd projet-flask
```

### **2. Créer un environnement virtuel (optionnel mais recommandé)**
- **Sur macOS/Linux :**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- **Sur Windows :**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### **3. Installer les dépendances**
```bash
pip install -r requirements.txt
```

### **4. Lancer l'application Flask**
```bash
python app.py
```
Par défaut, le serveur tourne sur **http://127.0.0.1:5001/**

---

## **Identifiants de test**
| Identifiant | Mot de passe |
|-------------|-------------|
| `admin`     | `password`  |

Si vous souhaitez ajouter un compte, entrez simplement un nouvel identifiant et mot de passe, puis cliquez sur "Créer un compte".

---

## **Structure du projet**
```bash
projet-flask/
│── static/
│   ├── css/
│   │   ├── style.css
│   ├── js/
│   │   ├── script.js
│   ├── images/
│   │   ├── logo.png
│── templates/
│   ├── interface.html
│── app.py  # Code principal Flask
│── requirements.txt  # Dépendances
│── database.db  # Base de données SQLite (générée après le premier lancement)
│── README.md  # Documentation
```

---

## **Utilisation**

1. **Ouvrir l'application** dans un navigateur : `http://127.0.0.1:5001/`  
2. **Se connecter** avec un compte existant ou en créer un  
3. **Tester les erreurs** : entrer un mauvais mot de passe pour voir le message d'erreur  
4. **Ajouter un compte** en remplissant le formulaire et tester la connexion  

---

## **Sécurité Implémentée**
- **Hashage des mots de passe** avec `bcrypt`  
- **Protection contre les doublons** lors de la création d'un compte  
- **Validation côté client** (JavaScript) et serveur (Flask)  

---

## **Améliorations possibles**
- [ ] Ajouter la gestion des sessions pour une connexion persistante
- [ ] Améliorer l'interface avec Bootstrap/Tailwind
- [ ] Ajouter une page de profil utilisateur

---

## **Auteur**
Projet développé par **Imad OUADI**.  