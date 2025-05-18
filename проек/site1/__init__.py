from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

events = [
    {
        "id": 1,
        "title": "Благотворительный концерт",
        "image": "img2.png",
        "description": "Описание концерта для поддержки детей с ограниченными возможностями"
    },
    {
        "id": 2,
        "title": "Спортивный фестиваль",
        "image": "img3.png",
        "description": "Адаптивные спортивные мероприятия для детей"
    },
    {
        "id": 3,
        "title": "Творческий мастер-класс",
        "image": "img4.png",
        "description": "Развитие творческих способностей у детей"
    },
    {
        "id": 4,
        "title": "Творческий мастер-класс",
        "image": "img5.png",
        "description": "Развитие творческих способностей у детей"
    }
]

participants_count = 0

@app.route('/')
def index():
    return render_template('index.html', events=events)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    global participants_count
    
    email = request.form.get('email')
    is_duplicate = False
    
    if is_duplicate:
        return jsonify({
            "success": False,
            "count": participants_count
        })
    else:
        participants_count += 1
        return jsonify({
            "success": True,
            "count": participants_count
        })

@app.route('/get_event/<int:event_id>')
def get_event(event_id):
    event = next((e for e in events if e['id'] == event_id), None)
    if event:
        return jsonify(event)
    else:
        return jsonify({"error": "Event not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)