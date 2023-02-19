from flask import Blueprint, render_template
from get_data import get_info_from_csv

landing = Blueprint('landing', __name__,
                   template_folder='templates',
                   static_folder='static',
                   static_url_path='landing-static')


filename_courses = 'test.csv'
filename_teachers = 'teachers.csv'
filename_descriptions = 'courses-description.csv'
list_of_courses = get_info_from_csv(filename_courses)
list_of_teachers = get_info_from_csv(filename_teachers)
list_of_descriptions = get_info_from_csv(filename_descriptions)
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
        'info_about_courses': list_of_courses,
        'links': links_for_img,
    }
    return render_template("catalog/catalog.html", **context)


@landing.route("/catalog/course/<id>")
def info_about_course(id):
    course = None
    for elem in list_of_courses:
        if elem['id_course'] == id:
            course = elem.copy()
            break
    context = {
        'title': f"{course['name']}",
        'info_about_courses': list_of_courses,
        'links': links_for_img,
        'days': ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс'],
    }
    return render_template("catalog/course-info.html", **context)