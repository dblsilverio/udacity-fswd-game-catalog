from catalog import app
from flask import render_template, request, flash

from catalog.models.category import Category
from catalog.services.category_service import CategoryService
from catalog.services.game_service import GameService


@app.route('/category', methods=['GET'])
def category():
    return render_template("category.html")


@app.route('/category/new', methods=['GET'])
def category_form():
    return render_template("category_form.html")


@app.route('/category/new', methods=['POST'])
def category_new():
    new_category = validate_category()

    if new_category:
        if service().new(new_category):
            flash('New category added', 'success')
        else:
            flash('Error adding category', 'danger')

    return render_template("category_form.html")


@app.route('/category/<int:cid>', methods=['GET'])
def category_detail(cid):
    c = CategoryService().find_by_id(cid)
    gs = GameService().find_by_category(c)
    return render_template("category.html", category=c, games=gs)


def service():
    from catalog.services.category_service import CategoryService
    return CategoryService()


def validate_category():
    name = request.form['name']
    description = request.form['description']
    invalid = False

    if not name or len(name.strip()) < 3:
        invalid = True
        flash('Type a valid name with three or more characters', 'warning')

    if not description or len(description.strip()) == 0:
        invalid = True
        flash('Type some description', 'warning')

    if not invalid:
        return Category(name=name, description=description)
    else:
        return None
