input_data = [12, '334', {'age': 16, 'name': 'Rob'}, 556, 123]

if isinstance(input_data, list) and len(input_data) == 5 and isinstance(input_data[2], dict):
    if input_data[2].get('age') and isinstance(input_data[2].get('age'), int):
        if input_data[2]['age'] < 18:
            pass
        else:
            pass
    else:
        pass
else:
    pass