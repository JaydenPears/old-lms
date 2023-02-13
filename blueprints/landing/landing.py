from flask import Blueprint, render_template
import csv

landing = Blueprint('landing', __name__,
                   template_folder='templates',
                   static_folder='static',
                   static_url_path='landing-static')


@landing.route("/")
def index():
    context = {
        'title': "LMS - Learning Management System",
        'array': None, # данные по курсам из csv передать
    }
    return render_template("landing.html", **context)