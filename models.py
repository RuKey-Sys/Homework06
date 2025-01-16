from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return f'<Record {self.title}>'