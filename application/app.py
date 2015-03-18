from flask import Flask
from handlers import account, home, user, news


def create_app():
    app = Flask(__name__)

    app.register_blueprint(home.bp)
    app.register_blueprint(account.bp, url_prefix='/account')
    app.register_blueprint(user.bp, url_prefix='/user')
    app.register_blueprint(news.bp, url_prefix='/news')

    return app

