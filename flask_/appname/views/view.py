import sys,os
sys.path.append(os.getcwd())

from flask import request, jsonify,Blueprint,render_template,flash, redirect, url_for
import main
import logging

bp = Blueprint("main", __name__)

@bp.route("/", methods=['GET'])
def mid_long_year():
    # data = request.get_json()['points']
    user = main.getuser()
    contents = main.get_contents()
    return render_template('home.html', user=user, contents=contents)

@bp.route("/signUp", methods=['GET'])
def asdf():
    # data = request.get_json()['points']
    # user = main.getuser()
    # contents = main.get_contents()
    return render_template('sign_up.html')

@bp.route("/login", methods=['GET'])
def dfgh():
    return render_template('login.html')


@bp.route("/about", methods=['GET'])
def qwer():
    return render_template('about.html')
