from catalog import app
from flask import render_template, request, flash, redirect

from .security import protected

from catalog.models.category import Category
from catalog.services.category_service import CategoryService
from catalog.services.game_service import GameService


@app.route('/category', methods=['GET'])
def category():
    categories = CategoryService().all()
    return render_template("category_index.html", categories=categories)


@protected
@app.route('/category/new', methods=['GET'])
def category_form():
    return render_template("category_form.html", target_url="/category/new",
                           category=Category(name='', description=''))


@protected
@app.route('/category/new', methods=['POST'])
def category_new():
    new_category = validate_category()

    if new_category:
        if CategoryService().new(new_category):
            flash('New category added', 'success')
        else:
            flash('Error adding category', 'danger')

    return redirect('/category')


@app.route('/category/<int:cid>', methods=['GET'])
def category_detail(cid):
    c = CategoryService().find_by_id(cid)
    if not c:
        flash('Category not found', 'warning')
        return redirect('/category')

    gs = GameService().find_by_category(c)

    return render_template("category.html", category=c, games=gs)


@protected
@app.route('/category/<int:cid>/delete', methods=['POST'])
def delete_category(cid):
    category_service = CategoryService()
    cat = category_service.find_by_id(cid)

    if not cat:
        flash('Category does not exists', 'warning')

    try:
        category_service.delete(cat)
        flash('Category removed', 'info')
    except Exception as e:
        flash("Error deleting category: %s" % e.message, 'danger')

    return redirect('/category')


@protected
@app.route('/category/<int:cid>/update', methods=['GET'])
def update_category_form(cid):
    cat = CategoryService().find_by_id(cid)

    if not cat:
        flash('Category does not exists')
        return redirect('/category')

    return render_template("category_form.html", category=cat,
                           target_url="/category/%d/update" % cat.id)


@protected
@app.route('/category/<int:cid>/update', methods=['POST'])
def update_category(cid):
    updated_category = validate_category()

    if updated_category:
        updated_category.id = cid

        if CategoryService().new(updated_category):
            flash('Category updated', 'success')
        else:
            flash('Error updating category', 'danger')

    return redirect('/category')


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
