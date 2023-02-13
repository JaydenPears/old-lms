from flask import Blueprint, render_template

course = Blueprint('course', __name__,
                   template_folder='../templates',
                   static_folder='../static',
                   static_url_path='course-static')


@course.route("/")
def index():
    context = {
        'title': "Главная страница",
        'num_of_courses': 6,
        'text': 123,
    }
    return render_template("course/course.html", **context)