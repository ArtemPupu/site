from app import db

class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    education = db.Column(db.String(200), nullable=False)
    profession = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    motivation = db.Column(db.Text, nullable=False)
    willing_to_stay = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'surname': self.surname,
            'name': self.name,
            'email': self.email,
            'education': self.education,
            'profession': self.profession,
            'gender': self.gender,
            'motivation': self.motivation,
            'willing_to_stay': self.willing_to_stay
        }