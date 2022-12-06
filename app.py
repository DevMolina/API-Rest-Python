from flask import Flask
from flask_cors import CORS

from config import config

# Routs
from routes import Movie

app = Flask(__name__)

CORS(app, resources={"*": {"origins": "http://localhost:9300"}})


def page_no_found(error):
    return "<h1>Not found page<h1/>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # blueprints
    app.register_blueprint(Movie.main, url_prefix='/api/movies')

    # error handlers
    app.register_error_handler(404, page_no_found)
    app.run()
