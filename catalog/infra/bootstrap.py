# coding=utf-8
"""
Bootstraps category models.
Categories and descriptions from http://vsrecommendedgames.wikia.com/wiki/A_List_and_Guide_to_Game_Genres
"""
import os
from catalog.services.category_service import CategoryService
from catalog.models.category import Category


class Bootstrap:

    def __init__(self):
        pass

    @staticmethod
    def create_categories():

        category_service = CategoryService()
        if not category_service.all().count():
            print "Creating categories..."
            f = open(os.getcwd() + '/catalog/resources/categories.csv', 'r')
            for line in f:
                if line.startswith("#"):
                    continue
                category_line = line.split('\t')
                category = Category(name=category_line[0],
                                    description=category_line[1])
                category_service.new(category)
        else:
            print "Category table already populated."

        print "Done."
