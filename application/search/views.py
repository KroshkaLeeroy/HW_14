from flask import Blueprint, render_template, current_app, jsonify
from utils import DataBase

search_by_name_blueprint = Blueprint("search_by_name_blueprint", __name__, )
search_by_year_to_year_blueprint = Blueprint("search_by_year_to_year_blueprint", __name__, template_folder="templates")
search_by_rating = Blueprint("search_by_rating", __name__)
search_by_genre = Blueprint("search_by_genre", __name__)


@search_by_name_blueprint.route('/movie/<title>')
def result_page(title):
    result = DataBase()
    return result.search_by_name(title)


@search_by_year_to_year_blueprint.route('/movie/<int:year_1>/to/<int:year_2>')
def year_to_year_page(year_1, year_2):
    result = DataBase()
    requests = result.search_by_range_of_years(year_1, year_2)
    return render_template("page.html", requests=requests)


@search_by_rating.route('/rating/<rating>')
def rating_page(rating):
    result = DataBase()
    requests = result.search_by_rating(rating)
    return render_template("page1.html", requests=requests)

@search_by_genre.route('/genre/<genre>')
def genre_page(genre):
    result = DataBase()
    requests = result.search_by_genre(genre)
    return render_template("page3.html", requests=requests)