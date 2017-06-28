from catalog import app
from flask import render_template, request

import facebook

from catalog.services.game_service import GameService


@app.route('/')
@app.route('/catalog')
def index():
    game_service = GameService()

    latest_games = game_service.latest(6)
    top10 = game_service.top10()

    return render_template('index.html', latest_games=latest_games, top10=top10)


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')
