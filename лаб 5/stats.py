from flask import Blueprint, render_template, make_response, current_app
from flask_login import login_required, current_user
import csv
import io

stats_bp = Blueprint('stats', __name__)


def get_check_rights():
    from app import check_rights
    return check_rights


@stats_bp.route('/users_stats')
@login_required
def users_stats():
    check_rights = get_check_rights()
    check_rights('Admin')(lambda: None)()  # Применяем проверку прав
    
    from app import User, VisitLogs
    db = current_app.extensions['sqlalchemy']

    # статистика по пользователям: количество посещений для каждого пользователя
    stats = db.session.query(
        VisitLogs.user_id,
        db.func.count(VisitLogs.id).label('visit_count'),
        User
    ).outerjoin(User, VisitLogs.user_id == User.id)\
    .group_by(VisitLogs.user_id).order_by(db.func.count(VisitLogs.id).desc()).all()

    return render_template('users_stats.html', stats=stats)


@stats_bp.route('/pages_stats')
@login_required
def pages_stats():
    check_rights = get_check_rights()
    check_rights('Admin')(lambda: None)()  # Применяем проверку прав
    
    from app import VisitLogs
    db = current_app.extensions['sqlalchemy']

    # статистика по страницам: количество посещений для каждой страницы
    stats = db.session.query(
        VisitLogs.path,
        db.func.count(VisitLogs.id).label('visit_count')
    ).group_by(VisitLogs.path).order_by(db.func.count(VisitLogs.id).desc()).all()

    return render_template('pages_stats.html', stats=stats)


@stats_bp.route('/pages_stats/export')
@login_required
def export_pages_stats():
    check_rights = get_check_rights()
    check_rights('Admin')(lambda: None)()  # Применяем проверку прав
    
    from app import VisitLogs
    db = current_app.extensions['sqlalchemy']

    stats = db.session.query(
        VisitLogs.path,
        db.func.count(VisitLogs.id).label('visit_count')
    ).group_by(VisitLogs.path).order_by(db.func.count(VisitLogs.id).desc()).all()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['№', 'Страница', 'Количество посещений'])

    for idx, stat in enumerate(stats, 1):
        writer.writerow([idx, stat.path, stat.visit_count])

    output.seek(0)

    response = make_response(output.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=pages_stats.csv'
    response.headers['Content-type'] = 'text/csv'
    return response


@stats_bp.route('/users_stats/export')
@login_required
def export_users_stats():
    check_rights = get_check_rights()
    check_rights('Admin')(lambda: None)()  # Применяем проверку прав
    
    from app import User, VisitLogs
    db = current_app.extensions['sqlalchemy']

    stats = db.session.query(
        VisitLogs.user_id,
        db.func.count(VisitLogs.id).label('visit_count'),
        User
    ).outerjoin(User, VisitLogs.user_id == User.id)\
    .group_by(VisitLogs.user_id).order_by(db.func.count(VisitLogs.id).desc()).all()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['№', 'Пользователь', 'Количество посещений'])

    for idx, stat in enumerate(stats, 1):
        user_id, visit_count, user_obj = stat
        if user_id and user_obj:
            user_name = f"{user_obj.surname} {user_obj.name} {user_obj.patronymic or ''}".strip()
        else:
            user_name = "Неаутентифицированный пользователь"
        writer.writerow([idx, user_name, visit_count])

    output.seek(0)

    response = make_response(output.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=users_stats.csv'
    response.headers['Content-type'] = 'text/csv'
    return response
