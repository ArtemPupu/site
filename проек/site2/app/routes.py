from flask import Blueprint, render_template, request, jsonify
from app.models import Participant
from app import db
from app.utils import validate_participant_data

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    count = Participant.query.count()
    
    if request.method == 'POST':
        try:
            data = request.get_json()
            
            # Валидация данных
            validation_error = validate_participant_data(data)
            if validation_error:
                return jsonify({
                    'success': False,
                    'message': validation_error
                })
            
            # Проверка на существующего участника
            if Participant.query.filter_by(email=data['email']).first():
                return jsonify({
                    'success': False,
                    'message': 'Этот email уже зарегистрирован!'
                })
            
            # Создание нового участника
            new_participant = Participant(
                surname=data['surname'],
                name=data['name'],
                email=data['email'],
                education=data['education'],
                profession=data.get('profession', 'Не указано'),
                gender=data['gender'],
                motivation=data['motivation'],
                willing_to_stay=data['willing_to_stay']
            )
            
            db.session.add(new_participant)
            db.session.commit()
            
            return jsonify({
                'success': True,
                'count': Participant.query.count()
            })
            
        except Exception as e:
            db.session.rollback()
            return jsonify({
                'success': False,
                'message': 'Произошла ошибка при регистрации. Пожалуйста, попробуйте снова.'
            })
    
    return render_template('index.html', count=count)