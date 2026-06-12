from flask import Flask, render_template, session, request, flash, redirect, url_for
from functools import wraps

from flask_session import Session

from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

import os

import re

app = Flask(__name__)

app.config['SECRET_KEY'] = '123456789'

app.config['SESSION_PERMANENT'] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

# __________________________________________________________

# БАЗА ДАННЫХ

# users.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# роль
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))

    # у роли может быть много пользователей
    users = db.relationship('User', backref='role', lazy=True)

# пользователь
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    surname = db.Column(db.String(50), nullable=True)
    name = db.Column(db.String(50), nullable=False)
    patronymic = db.Column(db.String(50), nullable=True)

    # ссылка на таблицу roles
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
# логи
class VisitLogs(UserMixin, db.Model):
    __tablename__ = 'visit_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref='logs')

# создание бд
with app.app_context():
    db.create_all()

    if not Role.query.first():
        admin_r = Role(name='Admin', description='Администратор')
        user_r = Role(name='User', description='Пользователь')
        db.session.add(admin_r)
        db.session.add(user_r)

        admin = User(login='admin', name='Админ',
            surname='Админкин', role=admin_r)
        admin.set_password('admin')
        db.session.add(admin)
        
        user0 = User(login='user', name='user',
            surname='Пользователь', role=user_r)
        user0.set_password('user')
        db.session.add(user0)

        user1 = User(login='dima_minekrafttt', name='Димка',
            surname='Майнкрафтин', patronymic='Майнкрафтович', role=user_r)
        user1.set_password('minecrafft')
        db.session.add(user1)

        user2 = User(login='alinka_i_love_reels', name='Алина',
            surname='Рилсы', role=user_r)
        user2.set_password('minecrafft')
        db.session.add(user2)

        user3 = User(login='sasha_vibe', name='Сашка',
            surname='Крэйзи', role=user_r)
        user3.set_password('minecrafft')
        db.session.add(user3)

        user4 = User(login='nasty_DOTA', name='Настя',
            surname='Игроманова', patronymic='Дотовна', role=user_r)
        user4.set_password('minecrafft')
        db.session.add(user4)

        user5 = User(login='nastya_DYSNEY', name='Анастасия',
            surname='Фендько', role=user_r)
        user5.set_password('minecrafft')
        db.session.add(user5)

        db.session.commit()

# __________________________________________________________

# для авторизации
login_manager = LoginManager()
login_manager.init_app(app)

# загрузка пользователя по айди из куки
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# __________________________________________________________

# ДЕКОРАТОР ДЛЯ ПРОВЕРКИ ПРАВ
def check_rights(required_role_name):
    """
    Декоратор для проверки прав пользователя.
    required_role_name - название требуемой роли ('Admin' или 'User')
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                flash('У вас недостаточно прав для доступа к данной странице.', 'warning')
                return redirect(url_for('index'))
            
            if current_user.role is None or current_user.role.name != required_role_name:
                flash('У вас недостаточно прав для доступа к данной странице.', 'warning')
                return redirect(url_for('index'))
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# __________________________________________________________

@app.before_request
def log_visit():
    if request.endpoint and 'static' in request.endpoint:
        return None

    from flask_login import current_user
    
    user_id = None
    if current_user.is_authenticated:
        user_id = current_user.id

    new_log = VisitLogs(
        path=request.path,
        user_id=user_id
    )
    
    db.session.add(new_log)
    db.session.commit()

    return None

@app.route('/')
def index():
    all_users = User.query.all()
    return render_template('index.html', all_users=all_users)


@app.route('/view_user')
@login_required
@check_rights('Admin')
def view_user():
    user_id = request.args.get('id')
    user = User.query.get(user_id)
    return render_template('view_user.html', user=user)


def check_pswrd_valid(password):
    pwd_errors = []

    # длина
    if len(password) < 8:
        pwd_errors.append("не менее 8 символов")
    if len(password) > 128:
        pwd_errors.append("не более 128 символов")

    # пробелы
    if ' ' in password:
        pwd_errors.append("без пробелов")

    # заглавная буква
    if not re.search(r'[A-Z]', password):
        pwd_errors.append("как минимум одна заглавная буква (латиница)")

    # строчная буква (латиница или кириллица)
    if not re.search(r'[a-zа-яё]', password):
        pwd_errors.append(
            "как минимум одна строчная буква (латиница или кириллица)")

    # цифра (арабская)
    if not re.search(r'[0-9]', password):
        pwd_errors.append("как минимум одна цифра")

    allowed_pattern = r'^[a-zA-Zа-яА-ЯёЁ0-9~!?@#$%^&*_\-+()\[\]{}><\\/\"\'.,:;]+$'

    if not re.match(allowed_pattern, password):
        pwd_errors.append("содержит недопустимые символы")

    if pwd_errors:
        return "; ".join(pwd_errors) + "."
    else:
        return None


def check_login_valid(login):
    errors = []

    if not login or len(login.strip()) == 0:
        errors.append("Поле не может быть пустым")
    elif len(login) < 5:
        errors.append("Логин должен содержать не менее 5 символов")
    elif not re.match(r'^[a-zA-Z0-9]+$', login):
        errors.append("Логин должен состоять только из латинских букв и цифр")

    return errors


def check_field_empty(value, field_name):
    if not value or len(value.strip()) == 0:
        return f"{field_name} не может быть пустым"
    return None


@app.route('/create_user', methods=['GET', 'POST'])
@login_required
@check_rights('Admin')
def create_user():
    if request.method == "POST":
        new_user = request.form.to_dict()

        login = new_user.get('login', '').strip()
        password = new_user.get('password', '')
        surname = new_user.get('surname', '').strip()
        name = new_user.get('name', '').strip()
        patronymic = new_user.get('patronymic', '').strip()
        role_id = new_user.get('role')

        # сбор ошибок
        form_errors = {}

        # проверка логина
        login_errors = check_login_valid(login)
        if login_errors:
            form_errors['login'] = login_errors

        # проверка пароля
        pwd_error = check_pswrd_valid(password)
        if pwd_error:
            form_errors['password'] = pwd_error

        # проверка фамилии
        surname_error = check_field_empty(surname, 'Фамилия')
        if surname_error:
            form_errors['surname'] = surname_error

        # проверка имени
        name_error = check_field_empty(name, 'Имя')
        if name_error:
            form_errors['name'] = name_error

        # форма с ошибками
        if form_errors:
            all_roles = Role.query.all()
            return render_template('create_user.html',
                all_roles=all_roles,
                form_errors=form_errors,
                form_data={'login': login, 'surname': surname, 'name': name, 'patronymic': patronymic, 'role_id': role_id})

        # уникальность логина
        existing_user = User.query.filter_by(login=login).first()
        if existing_user:
            all_roles = Role.query.all()
            form_errors['login'] = [
                'Пользователь с таким логином уже существует']
            return render_template('create_user.html',
                all_roles=all_roles,
                form_errors=form_errors,
                form_data={'login': login, 'surname': surname, 'name': name, 'patronymic': patronymic, 'role_id': role_id})

        # создание пользователя
        user_db = User(login=login, name=name, surname=surname, patronymic=patronymic, role_id=role_id)
        user_db.set_password(password)
        db.session.add(user_db)
        db.session.commit()

        flash(f'Пользователь {surname} {name} успешно создан!', 'success')
        return redirect(url_for('index'))

    if request.method == "GET":
        all_roles = Role.query.all()
        return render_template('create_user.html', all_roles=all_roles, form_errors={}, form_data={})


@app.route('/edit_user', methods=['GET', 'POST'])
@login_required
@check_rights('Admin')
def edit_user():
    if request.method == "POST":
        user_id = request.form.get("user_id")
        user = User.query.get(int(user_id)) if user_id else None

        if not user:
            flash('Пользователь не найден', 'danger')
            return redirect(url_for('index'))

        surname = request.form.get("surname", '').strip()
        name = request.form.get("name", '').strip()
        patronymic = request.form.get("patronymic", '').strip()
        role_id = request.form.get("role")

        # сбор ошибок
        form_errors = {}

        # проверка фамилии
        surname_error = check_field_empty(surname, 'Фамилия')
        if surname_error:
            form_errors['surname'] = surname_error

        # проверка имени
        name_error = check_field_empty(name, 'Имя')
        if name_error:
            form_errors['name'] = name_error

        # форма с ошибками
        if form_errors:
            all_roles = Role.query.all()
            return render_template('edit_user.html',
                all_roles=all_roles,
                user=user,
                form_errors=form_errors,
                form_data={'surname': surname, 'name': name, 'patronymic': patronymic, 'role_id': role_id})

        user.surname = surname
        user.name = name
        user.patronymic = patronymic
        user.role_id = role_id

        db.session.commit()

        flash(f'Данные пользователя {surname} {name} успешно обновлены!', 'success')
        return redirect(url_for('index'))

    if request.method == "GET":
        user_id = request.args.get('id')
        user = User.query.get(int(user_id)) if user_id else None
        
        if not user:
            flash('Пользователь не найден', 'danger')
            return redirect(url_for('index'))
            
        all_roles = Role.query.all()
        return render_template('edit_user.html', all_roles=all_roles, user=user, form_errors={}, form_data={})


@app.route('/delete_user/<int:id>', methods=['POST'])
@login_required
@check_rights('Admin')
def delete_user(id):
    try:
        user = User.query.get_or_404(id)
        user_fio = f"{user.surname} {user.name} {user.patronymic or ''}".strip()

        db.session.delete(user)
        db.session.commit()

        flash(f'Пользователь {user_fio} успешно удалён!', 'success')
    except Exception as e:
        flash(f'Ошибка при удалении пользователя: {str(e)}', 'danger')

    return redirect(url_for('index'))


# Маршрут для редактирования своего профиля (доступен всем авторизованным)
@app.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    user = current_user
    
    if request.method == "POST":
        surname = request.form.get("surname", '').strip()
        name = request.form.get("name", '').strip()
        patronymic = request.form.get("patronymic", '').strip()
        # role_id игнорируется для безопасности - пользователь не может менять свою роль

        # сбор ошибок
        form_errors = {}

        # проверка фамилии
        surname_error = check_field_empty(surname, 'Фамилия')
        if surname_error:
            form_errors['surname'] = surname_error

        # проверка имени
        name_error = check_field_empty(name, 'Имя')
        if name_error:
            form_errors['name'] = name_error

        # форма с ошибками
        if form_errors:
            all_roles = Role.query.all()
            return render_template('edit_user.html',
                all_roles=all_roles,
                user=user,
                form_errors=form_errors,
                form_data={'surname': surname, 'name': name, 'patronymic': patronymic, 'role_id': user.role_id})

        user.surname = surname
        user.name = name
        user.patronymic = patronymic
        # role_id не меняется

        db.session.commit()

        flash(f'Ваши данные успешно обновлены!', 'success')
        return redirect(url_for('index'))

    if request.method == "GET":
        all_roles = Role.query.all()
        return render_template('edit_user.html', all_roles=all_roles, user=user, form_errors={}, form_data={})


# Маршрут для просмотра своего профиля (доступен всем авторизованным)
@app.route('/profile')
@login_required
def view_profile():
    user = current_user
    return render_template('view_user.html', user=user)


@app.route('/visit_logs')
@login_required
def visit_logs():
    # Администратор видит все записи, пользователь - только свои
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    if current_user.role and current_user.role.name == 'Admin':
        pagination = VisitLogs.query.order_by(VisitLogs.created_at.desc()).paginate(
            page=page, per_page=per_page, error_out=False)
    else:
        # Пользователь видит только свои записи
        pagination = VisitLogs.query.filter_by(user_id=current_user.id).order_by(
            VisitLogs.created_at.desc()).paginate(page=page, per_page=per_page, error_out=False)
    
    all_logs = pagination.items
    return render_template('visit_logs.html', all_logs=all_logs, pagination=pagination)



@app.route('/counter')
def counter():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1

    return render_template('counter.html', visits=session.get('visits'))


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == "POST":
        username = request.form.get("login")
        password = request.form.get("password")
        remember = True if request.form.get("remember_me") == 'on' else False
        next_page = request.form.get("next")

        cur_user = User.query.filter_by(login=username).first()

        if cur_user and cur_user.check_password(password):
            login_user(cur_user, remember=remember)
            if next_page:
                return redirect(next_page)
            return redirect(url_for('index'))
        else:
            flash('Неверный логин или пароль', 'danger')
            return redirect(url_for('auth'))

    if request.method == "GET":
        return render_template('auth.html')


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash('Вы успешно вышли из системы', 'info')
    return redirect(url_for('index'))


@app.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == "GET":
        return render_template("change_password.html", form_errors={})

    if request.method == "POST":
        old_password = request.form.get('old_password')
        new_password_1 = request.form.get('new_password_1')
        new_password_2 = request.form.get('new_password_2')

        form_errors = {}

        if not current_user.check_password(old_password):
            flash('Неверный старый пароль', 'danger')
            return render_template("change_password.html", form_errors=form_errors)

        if new_password_1 != new_password_2:
            flash('Пароли не совпадают', 'danger')
            return render_template("change_password.html", form_errors=form_errors)

        pwd_error = check_pswrd_valid(new_password_1)
        if pwd_error:
            form_errors['new_password_1'] = pwd_error
            return render_template("change_password.html", form_errors=form_errors)

        # смена пароля
        current_user.set_password(new_password_1)
        db.session.commit()

        flash('Пароль успешно изменён!', 'success')
        return redirect(url_for('index'))


@app.errorhandler(401)
def forbidden(e):
    next_page = request.url
    return redirect(url_for('auth', next=next_page))


# Регистрация blueprint для статистики
from stats import stats_bp
app.register_blueprint(stats_bp)


if __name__ == '__main__':
    app.run(debug=True)
