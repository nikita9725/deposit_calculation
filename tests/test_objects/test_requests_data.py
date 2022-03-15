wrong_input_data_list = [
    {
        'date': '31.01.2021',
        'periods': 'three',
        'amount': '10 000',
        'rate': '6%'
    },
    {
        'date': '31.01.2021',
        'periods': 3,
        'amount': '10 k',
        'rate': 20
    },
    {
        'date': '31.01.2021',
        'periods': 1000,
        'amount': 10000000,
        'rate': '1'
    }
]

correct_input_data = {
    'date': '31.01.2021',
    'periods': 10,
    'amount': 10000,
    'rate': 6
}
