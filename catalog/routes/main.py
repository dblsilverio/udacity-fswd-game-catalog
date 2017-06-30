""" Routes for main page """
from flask import render_template, jsonify

from catalog.infra.flask_factory import app
from catalog.services.utils import config
from catalog.services.game_service import GameService


@app.route('/')
@app.route('/catalog')
def index():
    game_service = GameService()

    latest_games = latest(game_service)
    top10 = game_service.top10()

    return render_template('index.html', latest_games=latest_games,
                           top10=top10)


@app.route('/latest.json')
def latest_json():
    return jsonify([l.to_short_json() for l in latest(GameService())])


@app.route('/top10.json')
def top_json():
    return jsonify([t.to_short_json() for t in GameService().top10()])


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


def latest(game_service):
    return game_service.latest(config.getint('GameCatalog',
                                             'catalog.latest_count'))
