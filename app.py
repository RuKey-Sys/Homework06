from flask import Flask, request, render_template, redirect, url_for
from models import db, Record

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/add', methods=['GET', 'POST'])
def add_record():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        new_record = Record(title=title, description=description)
        db.session.add(new_record)
        db.session.commit()
        return redirect(url_for('view_records'))
    return render_template('add_record.html')

@app.route('/records')
def view_records():
    records = Record.query.all()
    return render_template('view_records.html', records=records)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
