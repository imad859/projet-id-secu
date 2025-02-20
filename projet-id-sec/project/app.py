import sqlite3
import bcrypt
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def init_db():
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

init_db()  

@app.route('/')
def home():
    return render_template('interface.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password').encode('utf-8') 

    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

    if user and bcrypt.checkpw(password, user[0]):  
        return jsonify(success=True, message="Connexion réussie !")
    return jsonify(success=False, message="Identifiant ou mot de passe incorrect.")

@app.route('/add_account', methods=['POST'])
def add_account():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify(success=False, message="Veuillez remplir tous les champs.")

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) 

    try:
        with sqlite3.connect("database.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
        return jsonify(success=True, message="Compte créé avec succès.")
    except sqlite3.IntegrityError:
        return jsonify(success=False, message="Erreur : Identifiant déjà utilisé.")

if __name__ == '__main__':
    app.run(debug=True, port=5001)