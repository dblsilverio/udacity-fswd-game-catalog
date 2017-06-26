from catalog import app
from flask import render_template, request, flash, redirect

from .security import protected

from catalog.models.game import Game
from catalog.services.category_service import CategoryService
from catalog.services.game_service import GameService


@app.route('/game', methods=['GET'])
def game():
    return render_template("game_index.html", games_scope="All Games",
                           games=GameService(

    ).all())


@app.route('/game/new', methods=['GET'])
@protected
def game_form():
    categories = CategoryService().all()

    if not categories.count():
        flash('Please, register at least one category.', 'info')
        return redirect("/category/new")

    return render_template("game_form.html", categories=categories,
                           game=Game().reset(), target_url="/game/new")


@protected
@app.route('/game/new', methods=['POST'])
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
        return redirect("/game")

    return render_template("game.html", game=game)


@protected
@app.route('/game/<int:gid>/delete', methods=['POST'])
def delete_game(gid):
    game_service = GameService()

    g = game_service.find_by(gid)

    if not g:
        flash('Game not found', 'warning')

    try:
        game_service.delete(g)
        flash('Game removed', 'info')
    except Exception as e:
        flash('Error deleting game: %s' % e.message, 'danger')

    return redirect('/game')


@protected
@app.route('/game/<int:gid>/update', methods=['GET'])
def update_game_form(gid):
    game_service = GameService()
    category_service = CategoryService()

    g = game_service.find_by(gid)

    if not g:
        flash('Game not found', 'warning')
        return redirect('/game')

    return render_template("game_form.html", game=g,
                           target_url="/game/%d/update" % g.id,
                           categories=category_service.all())


@protected
@app.route('/game/<int:gid>/update', methods=['POST'])
def update_game(gid):
    updated_game = validate_game()

    if updated_game:
        updated_game.id = gid

        if GameService().new(updated_game):
            flash('Game updated', 'success')
        else:
            flash('Error updating game', 'danger')

    return redirect('/game')


@app.route('/game/platform/<string:plat>', methods=['GET'])
def platform_games(plat):
    platform_results = GameService().find_by_platform(plat)

    if not platform_results['platform']:
        flash('Invalid platform provided', 'warning')
        return redirect('/game')

    return render_template('game_index.html',
                           games_scope=platform_results['platform'],
                           games=platform_results['games'])


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
        return Game(name=name, developer=developer, publisher=publisher,
                    platform=platform, thumb=thumb,
                    synopsis=synopsis, category_id=category)
    else:
        return None
