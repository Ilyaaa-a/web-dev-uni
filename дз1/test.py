import subprocess
import pytest

# Для Windows
INTERPRETER = 'python'
# Для MAC
# INTERPRETER = 'python3' 

def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()

test_data = {
    'python_if_else': [
        ('1', 'Weird'),
        ('4', 'Not Weird'),
        ('3', 'Weird'),
        ('6','Weird'),
        ('22', 'Not Weird'),
        ('123', 'Error'),
        ('-10', 'Error')
    ],

    'arithmetic_operators': [
        (['1', '2'], ['3', '-1', '2']),
        (['10', '5'], ['15', '5', '50']),
        (['-10', '5'], ['Error']),
        (['1640', str(10**20)], ['Error']),
    ],

    'division': [
        (['4', '2'], ['2', '2.0']),
        (['48', '4'], ['12', '12.0']),
        (['48', '5'], ['9', '9.6']),
    ],

    'loops': [
        (['3'], ['0', '1', '4']),
        (['4'], ['0', '1', '4', '9']),
        (['5'], ['0', '1', '4', '9', '16']),
        (['6'], ['0', '1', '4', '9', '16', '25']),
        (['-1'], ['Error']),
        (['30'], ['Error']),

    ],

    'print_function': [
        (['3'], ['0123']),
        (['6'], ['0123456']),
        (['10'], ['012345678910']),
        (['20'], ['01234567891011121314151617181920']),
        (['-1'], ['Error']),
        (['30'], ['Error']),
    ],

    'second_score': [
        (['5', '2 3 6 6 5'], ['5']),
        (['9', '2 3 3 6 6 8 8 9 5'], ['8']),
        (['8', '2 10 3 6 6 7 6 9 2'], ['9']),
        (['12', '2 1 3 6 6 7 6 9 2 5 2 6 9'], ['7']),
        (['10', '2 1 3 6 5 8 6 7 6 9 2'], ['8']),
    ],

    'nested_list': [
        (['5', 'Гарри', '37.21', 'Берри', '37.21', 'Тина', '37.2', 'Акрити', '41', 'Харш', '39'], ['Берри', 'Гарри']),
        (['1'], ['Error']),
        (['6'], ['Error']),
    ],

    'lists': [
    ([
        '12',
        'insert 0 5',
        'insert 1 10',
        'insert 0 6',
        'print',
        'remove 6',
        'append 9',
        'append 1',
        'sort',
        'print',
        'pop',
        'reverse',
        'print'
    ], [
        '[6, 5, 10]',
        '[1, 5, 9, 10]',
        '[9, 5, 1]'
    ]),
    ],

    'swap_case' : [
        (['Pythonist 2'], ['pYTHONIST 2']),
        (['Www.MosPolytech.ru'], ['wWW.mOSpOLYTECH.RU']),
        (['PythOOOnist 3 dfd'], ['pYTHoooNIST 3 DFD']),
    ],

    'split_and_join': [
    (['this is a string'], ['this-is-a-string']),
    (['hello world'], ['hello-world']),
    (['a b c d e'], ['a-b-c-d-e']),
],

'anagram': [
    (['listen', 'silent'], ['YES']),
    (['hello', 'bello'], ['NO']),
    (['abc', 'bca'], ['YES']),
    (['a', 'aa'], ['NO']), # abba baab 
    (['abba', 'baab'], ['YES']),
    (['AAA', 'aaa'], ['NO']),

],

'metro':[
    (['3', '5 10', '1 7', '8 12', '6'], '2'), 
    (['3', '5 10', '1 7', '8 12', '5'], '2'),
    (['3', '5 10', '1 7', '8 12', '10'], '2'),
    (['1', '0 60', '0'], '1'),
    (['1', '0 60', '61'], '0'),
    (['3', '0 10', '20 30', '40 50', '15'], '0'),
    (['3', '0 100', '20 80', '40 60', '50'], '3'),
    (['4', '0 10', '20 30', '40 50', '60 70', '15'], '0'),
],

'minion_game':[
    (['BANANA'], 'Стюарт 12'),
    (['A'], 'Кевин 1'), 
    (['B'], 'Стюарт 1'),
    (['AAA'], 'Кевин 6'),
    (['BCD'], 'Стюарт 6'),
    ([str(10**7 * "A")], 'Error'),
],

'is_leap': [
    (['2000'], ['True']),
    (['1900'], ['False']),
    (['2024'], ['True']),
    (['2025'], ['False']),
    (['2100'], ['False']),
    (['1800'], ['Error']),
    ([str(10**7 * "A")], ['Error']),

    
],

'happiness': [
    (['3 2', '1 5 3', '3 1', '5 7'], ['1']),
    (['5 3', '1 2 3 4 5', '1 2 3', '4 5 6'], ['1']),
    (['1 1', '10', '10', '20'], ['1']),
    (['1 1', '-1', str(10**10), '20'], ['Error']),
],

'pirate_ship': [
    ([
        '50 3',
        'золото 20 100',
        'серебро 50 200',
        'жемчуг 30 120'
    ], [
        'золото 20.00 100.00',
        'серебро 30.00 120.00'
    ]),
    ([
        '10 2',
        'A 10 50',
        'B 5 30'
    ], [
        'B 5.00 30.00',
        'A 5.00 25.00'
    ]),

    ([
        '10 2',
        'A 11 50',
        'B 6 30'
    ], [
        'B 6.00 30.00',
        'A 4.00 18.18'
    ]),
],

'matrix_mult': [
    ([
        '2',
        '1 2',
        '3 4',
        '5 6',
        '7 8'
    ], [
        '19 22',
        '43 50'
    ]),
    ([
        '3',
        '1 0 0',
        '0 1 0',
        '0 0 1',
        '2 3 4',
        '5 6 7',
        '8 9 10'
    ], [
        '2 3 4',
        '5 6 7',
        '8 9 10'
    ]),

    ([
        '20',
        '1 0 0',
        '0 1 0',
        '0 0 1',
        '2 3 4',
        '5 6 7',
        '8 9 10'
    ], [
        'Error'
    ]),
],
    
}

# hello_world.py
def test_hello_world():
    assert run_script('hello_world.py') == 'Hello, world!'

# python_if_else.py
@pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])
def test_python_if_else(input_data, expected):
    assert run_script('python_if_else.py', [input_data]) == expected

# arithmetic_operators.py
@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', input_data).split('\n') == expected

# division.py
@pytest.mark.parametrize("input_data, expected", test_data['division'])
def test_division(input_data, expected):
    assert run_script('division.py', input_data).split('\n') == expected

# loops.py
@pytest.mark.parametrize("input_data, expected", test_data['loops'])
def test_loops(input_data, expected):
    assert run_script('loops.py', input_data).split('\n') == expected

# print_function.py
@pytest.mark.parametrize("input_data, expected", test_data['print_function'])
def test_print_function(input_data, expected):
    assert run_script('print_function.py', input_data).split('\n') == expected

# second_score.py
@pytest.mark.parametrize("input_data, expected", test_data['second_score'])
def test_second_score(input_data, expected):
    assert run_script('second_score.py', input_data).split('\n') == expected

# nested_list.py
@pytest.mark.parametrize("input_data, expected", test_data['nested_list'])
def test_nested_list(input_data, expected):
    assert run_script('nested_list.py', input_data).split('\n') == expected

# lists.py
@pytest.mark.parametrize("input_data, expected", test_data['lists'])
def test_lists(input_data, expected):
    assert run_script('lists.py', input_data).split('\n') == expected

# swap_case.py
@pytest.mark.parametrize("input_data, expected", test_data['swap_case'])
def test_swap_case(input_data, expected):
    assert run_script('swap_case.py', input_data).split('\n') == expected

# split_and_join.py
@pytest.mark.parametrize("input_data, expected", test_data['split_and_join'])
def test_split_and_join(input_data, expected):
    assert run_script('split_and_join.py', input_data).split('\n') == expected

# max_word.py
def test_max_word():
    assert run_script('max_word.py') == 'сосредоточенности'

# price_sum.py
def test_price_sum():
    assert run_script('price_sum.py') == '6842.84 5891.06 6810.90'

# anagram.py
@pytest.mark.parametrize("input_data, expected", test_data['anagram'])
def test_anagram(input_data, expected):
    assert run_script('anagram.py', input_data).split('\n') == expected

# metro.py
@pytest.mark.parametrize("input_data, expected", test_data['metro'])
def test_metro(input_data, expected):
    assert run_script('metro.py', input_data) == expected

# minion_game.py
@pytest.mark.parametrize("input_data, expected", test_data['minion_game'])
def test_minion_game(input_data, expected):
    assert run_script('minion_game.py', input_data) == expected

# is_leap.py
@pytest.mark.parametrize("input_data, expected", test_data['is_leap'])
def test_is_leap(input_data, expected):
    assert run_script('is_leap.py', input_data).split('\n') == expected

# happiness.py
@pytest.mark.parametrize("input_data, expected", test_data['happiness'])
def test_happiness(input_data, expected):
    assert run_script('happiness.py', input_data).split('\n') == expected

# pirate_ship.py
@pytest.mark.parametrize("input_data, expected", test_data['pirate_ship'])
def test_pirate_ship(input_data, expected):
    assert run_script('pirate_ship.py', input_data).split('\n') == expected

# matrix_mult.py
@pytest.mark.parametrize("input_data, expected", test_data['matrix_mult'])
def test_matrix_mult(input_data, expected):
    assert run_script('matrix_mult.py', input_data).split('\n') == expected

