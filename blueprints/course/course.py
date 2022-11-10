from flask import Blueprint, render_template

course = Blueprint('course', __name__, template_folder='templates', static_folder='static')


@course.route("/")
def index():
    context = {
        'title': "Главная страница",
        'text': 123,
    }
    return render_template("course.html", **context)