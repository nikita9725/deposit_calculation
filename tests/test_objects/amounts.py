from collections import OrderedDict


input_data = {
    'date': '31.01.2021',
    'periods': 3,
    'amount': 10000,
    'rate': 6
}

output_data = OrderedDict(
    [
        ('31.01.2021', 10050.0),
        ('28.02.2021', 10100.25),
        ('31.03.2021', 10150.75)
    ]
)
