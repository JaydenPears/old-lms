from flask import Flask, Blueprint
from blueprints.landing.landing import landing

app = Flask(__name__)

app.register_blueprint(landing, url_prefix='/')

def main():
    app.run(debug=True, host='0.0.0.0', port=80)

if __name__ == "__main__":
    main()
#check