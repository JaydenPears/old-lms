from flask import Blueprint, render_template

landing = Blueprint('landing', __name__,
                   template_folder='templates',
                   static_folder='static',
                   static_url_path='landing-static')


@landing.route("/")
def index():
    context = {
        'title': "Learning Management System | Главная страница",
        'num_of_courses': 6,
    }
    return render_template("landing/landing.html", **context)