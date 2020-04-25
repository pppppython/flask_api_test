from flask import Flask,render_template,request
import os
from T.labbeng.main import main_bp


def create_app():
    app=Flask('T')
    app.register_blueprint(main_bp)
    return app