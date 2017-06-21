from catalog import app
from flask import render_template


@app.route('/category', methods=['GET'])
def category():
    return render_template("category.html")


@app.route('/category/new', methods=['GET'])
def category_form():
    return render_template("category_form.html")


@app.route('/category/<int:id>', methods=['GET'])
def category_detail():
    return render_template("category_form.html")
