from flask import Flask, render_template, request
from database import db_session, init_db
app = Flask(__name__)

@app.before_first_request
def init():
    init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def start():
    return 'Hello, World!'

@app.route('/create_restaurant',methods=['GET', 'POST'])
def create_restaurant():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        site_url = request.form.get('site_url')
        #Test comment
        return '{}, {}, {}' .format(name, description, site_url)
    return render_template('create_restaurant.html')


class Restaurants:
    pass


@app.route('/restaurants')
def restaurant_list():
    restaurants = Restaurants.query.all()

    return render_template('restaurant.html', nav='restaurant', restaurants=restaurants)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.run(debug=True)
