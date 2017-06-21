from catalog import app
from flask import render_template


@app.route('/game/new', methods=['GET'])
def game_form():
    return render_template("game_form.html")


@app.route('/game/<int:id>', methods=['GET'])
def game_detail():
    return render_template("game_form.html")

