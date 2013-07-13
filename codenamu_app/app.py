#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, url_for
import settings

def create_app():
    app = Flask(__name__)
    app.config.from_object(settings.SERVER_SETTINGS)
    @app.route('/')
    def main():
        return render_template('index.html')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(**settings.SERVER_SETTINGS)
