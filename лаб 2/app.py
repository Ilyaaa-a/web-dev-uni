import re
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')

# http://127.0.0.1:5000/req?user=Ilya&project=Lab2


@app.route('/req', methods=['GET'])
def req():

    all_args = request.args.to_dict()

    headers = request.headers

    cookies = request.cookies.to_dict()

    return render_template('req.html', url_params=all_args, headers=headers, cookies=cookies)


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        form = request.form.to_dict()
        return render_template('form.html', form=form)

    if request.method == 'GET':
        return render_template('form.html')

# кортеж (валидность, ошибка, отформатированный номер)
def phone_number(ph):

    if not ph:
        return False, 'Поле не можети быть пустым', None

    pattern = r'^[0-9\s\(\)\-\.\+]+$'
    if not re.match(pattern, ph):
        return False, "Недопустимые символы в номере телефона. Разрешены: цифры пробел () - . +", None

    only_digits = re.sub(r'\D', '', ph)
    count = len(only_digits)

    expected_length = 10
    starts_with_sp = False  # начинается с +7 или 8

    if ph.strip().startswith('+7') or ph.strip().startswith('8'):
        expected_length = 11
        starts_with_sp = True

    if count != expected_length:
        return False, "Неверное количество чисел в телефоне", None

    phone_8 = ''  # цифры телефона с 8 начинаются

    if expected_length == 10:
        phone_8 = '8' + only_digits
    elif expected_length == 11:
        phone_8 = '8' + only_digits[1:]

    # к формату 8-***-***-**-**
    formated = f"{phone_8[0]}-{phone_8[1:4]}-{phone_8[4:7]}-{phone_8[7:9]}-{phone_8[9:11]}"

    return True, None, formated


@app.route('/phone', methods=['GET', 'POST'])
def phone():
    if request.method == 'POST':

        input_numb = request.form.to_dict()['phone']
        is_valid, error_msg, formated = phone_number(input_numb)
        submitted = False
        
        if is_valid:
            return render_template('phone.html', error_msg='', formated=formated, input_numb=input_numb, submitted = True)
        else: 
            return render_template('phone.html', error_msg=error_msg, formated='', input_numb=input_numb, submitted = False)

    if request.method == 'GET':
        return render_template('phone.html', error_msg='', formated='', input_numb='', submitted = False)


if __name__ == '__main__':
    app.run(debug=True)
