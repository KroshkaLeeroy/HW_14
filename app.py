from flask import Flask
from application.search.views import search_by_name_blueprint
from application.search.views import search_by_year_to_year_blueprint
from application.search.views import search_by_rating
from application.search.views import search_by_genre

app = Flask(__name__)

app.register_blueprint(search_by_name_blueprint)
app.register_blueprint(search_by_year_to_year_blueprint)
app.register_blueprint(search_by_rating)
app.register_blueprint(search_by_genre)

if __name__ == '__main__':
    app.run(debug=True)
