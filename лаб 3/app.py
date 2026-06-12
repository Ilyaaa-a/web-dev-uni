from flask import Flask, render_template, session, request, flash, redirect, url_for
from flask_session import Session

from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)

app.config['SECRET_KEY'] = '123456789'

app.config['SESSION_PERMANENT'] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

# __________________________________________________________

# для авторизации
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

users = {
    '1' : User(id='1', username='user', password='qwerty')
}

# поиск юзера по юзернейму
def get_user_by_username(username):
    for user in users.values():
        if user.username == username:
            return user
    return None

# загрузка пользователя по айди из куки
@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

# __________________________________________________________

@app.route('/')
def index():
    return render_template('base.html')


@app.route('/counter')
def counter():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1

    return render_template('counter.html', visits=session.get('visits'))


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    # форма
    if request.method == "POST":
        form_test = request.form.to_dict()

        username = request.form.get("login")
        password = request.form.get("password")
        remember = True if request.form.get("remember_me") == 'on' else False
        next_page = request.form.get("next")

        cur_user = get_user_by_username(username)

        if cur_user and cur_user.password == password:
            login_user(cur_user, remember=remember)
            if next_page:
                return redirect(next_page)
            return redirect(url_for('index'))
        else:
            return render_template('auth.html', error = "not_log_pass")


    if request.method == "GET":
        return render_template('auth.html')

    
@app.route('/secret')
@login_required
def secret():
    return render_template("secret.html")

@app.errorhandler(401)
def forbidden(e):
    next_page = request.url
    return redirect(url_for('auth', next=next_page, error='need_auth'))


if __name__ == '__main__':
    app.run(debug=True)
