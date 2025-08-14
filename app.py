from flask import Flask, request, render_template, url_for, flash, redirect
import db  # ton fichier db.py
from werkzeug.security import generate_password_hash, check_password_hash
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
        db_con = db.get_db()
        liste_user = db_con.execute(
            "SELECT user.id, user.username FROM user "
        ).fetchall()
        return render_template("index.html", liste_user=liste_user)
    
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
                except sqlite3.IntegrityError:
                    error = f"L'utilisateur {nom} existe déjà."
                else:
                    print(f"L'utilisateur {nom} a été ajouté avec succès.")
                    return redirect(url_for("index"))

            flash(error)

        return render_template("add.html")

    @app.route("/<int:id>/update", methods=["GET", "POST"])
    def update(id):
        db_con = db.get_db()
        user = db_con.execute(
            "SELECT * FROM user WHERE id = ?", (id,)
        ).fetchone()

        if request.method == "POST":
            nom = request.form.get("nom")
            mdp = request.form.get("mdp")
            error = None

            if not nom:
                error = "Le nom d'utilisateur est requis."
            elif not mdp:
                error = "Le mot de passe est requis."

            if error is None:
                if check_password_hash(user["password"], mdp):
                    db_con.execute(
                        "UPDATE user SET username = ? WHERE id = ?", (nom, id)
                    )
                    db_con.commit()
                    return redirect(url_for("index"))
                else:
                    error = "Mot de passe incorrect."

            flash(error)
        
        return render_template("update.html", user=user)
    
    @app.route("/<int:id>/delete", methods=["POST"])
    def delete(id):
        db_con = db.get_db()
        db_con.execute("DELETE FROM user WHERE id = ?", (id,))
        db_con.commit()

        return redirect(url_for("index"))

    return app
