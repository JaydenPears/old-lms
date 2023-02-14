from flask import Blueprint, render_template

landing = Blueprint('landing', __name__,
                   template_folder='templates',
                   static_folder='static',
                   static_url_path='landing-static')


@landing.route("/")
def main_page():
    context = {
        'title': "Learning Management System | Главная страница",
    }
    return render_template("landing/landing.html", **context)


@landing.route("/catalog/")
def catalog():
    context = {
        'title': "Learning Management System | Каталог курсов",
        'num_of_courses': 0,
    }
    return render_template("catalog/catalog.html", **context)