from flask import Flask, Blueprint
from blueprints.course.course import course

app = Flask(__name__)

app.register_blueprint(course, url_prefix='/')

def main():
    app.run(debug=True, host='0.0.0.0', port=80)

if __name__ == "__main__":
    main()