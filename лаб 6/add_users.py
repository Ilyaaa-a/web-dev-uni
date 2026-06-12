
from models import db, User
user1 = User(first_name='Авдотий', last_name='Бырков', login='lala')
user1.set_password('123123')
db.session.add(user1)
db.session.commit()

from models import db, User
user1 = User(first_name='Жоркин', last_name='Лыпов', login='lala1')
user1.set_password('123123')
db.session.add(user1)
db.session.commit()