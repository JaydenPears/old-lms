from flask import Blueprint, render_template
from get_data import get_info_from_csv

landing = Blueprint('landing', __name__,
                   template_folder='templates',
                   static_folder='static',
                   static_url_path='landing-static')


filename = 'test.csv'
info_for_catalog = get_info_from_csv(filename)
links_for_img = {"1": "https://cdn-icons-png.flaticon.com/512/4645/4645241.png",
                 "2": "https://cdn-icons-png.flaticon.com/512/4645/4645269.png",
                 "3": "https://cdn-icons-png.flaticon.com/512/4645/4645250.png",
                 "4": "https://cdn-icons-png.flaticon.com/512/4645/4645286.png",
                 "5": "https://cdn-icons-png.flaticon.com/512/4645/4645220.png",
                 "6": "https://cdn-icons-png.flaticon.com/512/4645/4645388.png",
                 }


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
        'info_about_courses': info_for_catalog,
        'links': links_for_img,
    }
    return render_template("catalog/catalog.html", **context)