from catalog import app
from flask import render_template, request, flash, redirect

from .security import protected

from catalog.models.game import Game
from catalog.services.category_service import CategoryService
from catalog.services.game_service import GameService


@app.route('/game/new', methods=['GET'])
def game_form():
    categories = CategoryService().all()

    if not categories.count():
        flash('Please, register at least one category.', 'info')
        return render_template("category_form.html")

    return render_template("game_form.html", categories=categories)


@app.route('/game/new', methods=['POST'])
@protected
def game_new():
    game = validate_game()
    print game
    if game:
        if GameService().new(game):
            flash('New game added', 'success')
        else:
            flash('Error adding game', 'danger')

    return redirect('/game/new')


@app.route('/game/<int:gid>', methods=['GET'])
def game_detail(gid):
    game = GameService().find_by(gid)

    if not game:
        flash("Game with id %d not found" % gid, "warning")
        return redirect("/")

    return render_template("game.html", game=game)


def validate_game():
    name = request.form['name']
    developer = request.form['developer']
    publisher = request.form['publisher']
    platform = request.form.getlist('platform')
    thumb = request.form['thumb_url']
    synopsis = request.form['synopsis']
    category = request.form['category']

    invalid = False

    if not name or len(name.strip()) == 0:
        invalid = True
        flash('Name is required', 'danger')

    if not developer or len(developer.strip()) == 0:
        invalid = True
        flash('Developer is required', 'danger')

    if not publisher or len(publisher.strip()) == 0:
        invalid = True
        flash('Publisher is required', 'danger')

    if not platform or len(platform) == 0:
        invalid = True
        flash('At least one Platform is required', 'danger')
    else:
        platform = '|'.join(platform)

    if not category or not category.strip().isdigit():
        invalid = True
        flash('Publisher is required', 'danger')
    else:
        category = int(category)

    if not thumb or len(thumb.strip()) == 0:
        flash('One thumb image might be interesting for other gamer!', 'warning')

    if not synopsis or len(synopsis.strip()) == 0:
        flash('Come back later and write a good synopsis to help other players!', 'warning')

    if not invalid:
        return Game(name=name, developer=developer, publisher=publisher, platform=platform, thumb=thumb,
                    synopsis=synopsis, category_id=category)
    else:
        return None
