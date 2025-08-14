from flask import Flask, request, render_template, url_for, flash, redirect
import db  # ton fichier db.py
from werkzeug.security import generate_password_hash
import sqlite3

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config.from_mapping(
        SECRET_KEY="dev",  # Doit être changé pour une valeur aléatoire en production
        DATABASE="db.sqlite",
    )
    db.init_app(app)

    @app.route("/")
    def index():
        return "<h1>Bienvenue !</h1><p>La base est prête. <a href='/add_user'>Ajouter un utilisateur</a></p>"
    
    @app.route("/add_user", methods=["GET", "POST"])
    def add_user():
        if request.method == "POST":
            nom = request.form.get("nom")
            mdp = request.form.get("mdp")
            error = None

            if not nom:
                error = "Le nom d'utilisateur est requis."
            elif not mdp:
                error = "Le mot de passe est requis."

            if error is None:
                try:
                    db_con = db.get_db()
                    db_con.execute(
                        "INSERT INTO user (username, password) VALUES (?, ?)",
                        (nom, generate_password_hash(mdp)),
                    )
                    db_con.commit()
                except db_con.IntegrityError:
                    error = f"L'utilisateur {nom} existe déjà."
                else:
                    print(f"L'utilisateur {nom} a été ajouté avec succès.")
                    return redirect(url_for("index"))

            flash(error)

        return render_template("add.html")


    return app

