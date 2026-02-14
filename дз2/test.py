import subprocess
import pytest

from plane_angle import Point

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

def run_script2(filename, input_args=None):
    cmd = [INTERPRETER, filename]
    if input_args:
        cmd.extend(input_args)
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()

test_data = {
    'fact_it': [
        (5, 120),
        (-2, "Error"),
        (-10, "Error")
    ],

    'fact_rec': [
        (5, 120),
        (-2, "Error"),
        (-10, "Error")
    ],

    'show_employee': [
        (('Илья', 1000), ('Илья: 1000 ₽')),
        (('Жора', ), ('Жора: 100000 ₽'))

    ],

    'sum_and_sub': [
        ((2, 3), (5, -1)),
        ((14, 53), (67, -39)),
        ((-53, 12), (-41, -65)),
    ],
    
    'process_list': [
    ([1, 2, 3, 4], [1, 4, 27, 16]),
    ([0], [0]),                
    ([-2, -3], [4, -27]),         
    ([], 'Error'),                    
    ([5], [125]),                
    ([10], [100]),                
    ],
    
    'process_list_gen': [
    ([1, 2, 3, 4], [1, 4, 27, 16]),
    ([0], [0]),                
    ([-2, -3], [4, -27]),         
    ([], ['Error']),                    
    ([5], [125]),                
    ([10], [100]),                
    ],

    'my_sum': [
        ((2, 3, 4, 5), (14)),
        ((4, 2, 123), (129)),
        ((124, -32, -1), (91)),
        ((432, -32), (400)),
    ],

    'my_sum_argv': [
    (['2', '3', '4', '5'], '14'),
    (['4', '2', '123'], '129'),
    (['124', '-32', '-1'], '91'),
    (['432', '-32'], '400'),
    (['0'], '0'),
    ([], '0'),
    ],

    'files_sort': [
    ('C:\\Users\\Илья\\Desktop\\exam', ['account.html', 'index.html', 'api_key.txt']),
    ],

    'search_file': [
    ('fact.py', ['def fact_it(n):']),
    ], 

    'email_validation': [
    ('lara@mospolytech.ru', True),
    ('brian-23@mospolytech.ru', True),
    ('britts_54@mospolytech.ru', True),
    ('user@domain.toolong', False),
    ('user@domain', False),
    ('user@domain_.com', False),
    ],

    'fibonacci': [
        (5, [0, 1, 1, 8, 27]),
        (-2, "Error"),
        (25, 'Error'),
    ],

    'compute_average_scores': [
        (
            [
                (89, 90, 78, 93, 80),
                (90, 91, 85, 88, 86),
                (91, 92, 83, 89, 90.5)
            ],
            (90.0, 91.0, 82.0, 90.0, 85.5)
        ),
        
        (
            [(1,) * 101],
            "Error"
        ),
        
        (
            [( -1, 50 )],
            "Error"
        ),
        
        (
            [( 101, 50 )],
            "Error"
        ),
        
         (
            [(1, 2), (3,)],
            "Error"
        ),  
        
    ],
    
    'plane_angle': [
    (
        (
            Point(0, 4, 5),
            Point(1, 7, 6),
            Point(0, 5, 9),
            Point(1, 7, 2)
        ),
        "171.81"
    ),

    (
        (
            Point(0, 0, 0),
            Point(1, 0, 0),
            Point(0, 1, 0),
            Point(0, 1, 1)
        ),
        "90.00"
    ),
    ],
    
    'phone_number': [
    (
        ["07895462130", "89875641230", "9195969878"],
        [
            "+7 (789) 546-21-30",
            "+7 (919) 596-98-78",
            "+7 (987) 564-12-30"
        ]
    ),
    
    (
        ["+7(916)123-45-67", "8 916 123 45 67", "9161234567"],
        [
            "+7 (916) 123-45-67",
            "+7 (916) 123-45-67",
            "+7 (916) 123-45-67"
        ]
    ),
    ],
    
    'name_format': [
    (
        [
            ["Mike", "Thomson", "20", "M"],
            ["Robert", "Bustle", "32", "M"],
            ["Andria", "Bustle", "30", "F"]
        ],
        [
            "Mr. Mike Thomson",
            "Ms. Andria Bustle",
            "Mr. Robert Bustle"
        ]
    )
    ],
    
    'complex_numbers': [
    (
        (2, 1, 5, 6),
        [
            "7.00+7.00i",
            "-3.00-5.00i",
            "4.00+17.00i",
            "0.26-0.11i",
            "2.24+0.00i",
            "7.81+0.00i"
        ]
    ),

    (
        (0, 1, 0, 1),
        [
            "0.00+2.00i",
            "0.00+0.00i",
            "-1.00+0.00i",
            "1.00+0.00i",
            "1.00+0.00i",
            "1.00+0.00i"
        ]
    ),
    
]
    
    


}

from fact import fact_it
from fact import fact_rec

@pytest.mark.parametrize("input_data, expected", test_data['fact_it'])
def test_fact_it(input_data, expected):
    assert fact_it(input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['fact_rec'])
def test_fact_rec(input_data, expected):
    assert fact_rec(input_data) == expected

from show_employee import show_employee

@pytest.mark.parametrize("input_data, expected", test_data['show_employee'])
def test_show_employee(input_data, expected):
    assert show_employee(*input_data) == expected

from sum_and_sub import sum_and_sub_func

@pytest.mark.parametrize("input_data, expected", test_data['sum_and_sub'])
def test_sum_and_sub(input_data, expected):
    assert sum_and_sub_func(*input_data) == expected
    
from process_list import process_list, process_list_comp, process_list_gen

@pytest.mark.parametrize("input_arr, expected", test_data['process_list'])
def test_process_list(input_arr, expected):
    assert process_list(input_arr) == expected

@pytest.mark.parametrize("input_arr, expected", test_data['process_list'])
def test_process_list_comp(input_arr, expected):
    assert process_list_comp(input_arr) == expected

@pytest.mark.parametrize("input_arr, expected", test_data['process_list_gen'])
def test_process_list_gen(input_arr, expected):
    assert list(process_list_gen(input_arr)) == expected

from my_sum import my_sum 

@pytest.mark.parametrize("input_data, expected", test_data['my_sum'])
def test_my_sum(input_data, expected):
    assert my_sum(*input_data) == expected

@pytest.mark.parametrize("input_args, expected", test_data['my_sum_argv'])
def test_my_sum_argv(input_args, expected):
    assert run_script2('my_sum_argv.py', input_args) == expected

from files_sort import sort_files

@pytest.mark.parametrize("input_data, expected", test_data['files_sort'])
def test_files_sort(input_data, expected):
    assert sort_files(input_data) == expected

from file_search import search_file

@pytest.mark.parametrize("input_data, expected", test_data['search_file'])
def test_file_search(input_data, expected):
    assert search_file(input_data) == expected
    
from email_validation import fun

@pytest.mark.parametrize("input_data, expected", test_data['email_validation'])
def test_email_validation(input_data, expected):
    assert fun(input_data) == expected

from fibonacci import fibonacci

@pytest.mark.parametrize("input_data, expected", test_data['fibonacci'])
def test_fibonacci(input_data, expected):
    assert fibonacci(input_data) == expected

from average_scores import compute_average_scores

@pytest.mark.parametrize("input_data, expected", test_data['compute_average_scores'])
def test_compute_average_scores(input_data, expected):
    assert compute_average_scores(input_data) == expected

from plane_angle import plane_angle

@pytest.mark.parametrize("input_data, expected", test_data['plane_angle'])
def test_plane_angle(input_data, expected):
    assert plane_angle(*input_data) == expected

from phone_number import sort_phone

@pytest.mark.parametrize("input_data, expected", test_data['phone_number'])
def test_phone_number(input_data, expected):
    assert sort_phone(input_data) == expected
    
from people_sort import name_format

@pytest.mark.parametrize("input_data, expected", test_data['name_format'])
def test_people_sort(input_data, expected):
    assert name_format(input_data) == expected
    
from complex_numbers import Complex
    
@pytest.mark.parametrize("input_params, expected", test_data['complex_numbers'])
def test_complex_numbers(input_params, expected):
    r1, i1, r2, i2 = input_params
    c = Complex(r1, i1)
    d = Complex(r2, i2)
    
    results = [
        str(c + d),
        str(c - d),
        str(c * d),
        str(c / d),
        str(c.mod()),
        str(d.mod())
    ]
    
    assert results == expected

