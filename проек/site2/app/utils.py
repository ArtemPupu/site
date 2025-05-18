def validate_participant_data(data):
    required_fields = [
        'surname', 'name', 'email', 'education',
        'gender', 'motivation', 'willing_to_stay'
    ]
    
    for field in required_fields:
        if not data.get(field):
            return f'Поле {field} обязательно для заполнения'
    
    if '@' not in data['email']:
        return 'Пожалуйста, введите корректный email'
    
    if len(data['motivation']) < 20:
        return 'Мотивация должна содержать не менее 20 символов'
    
    return None