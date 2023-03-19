from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/pet_health'
db = SQLAlchemy(app)


class PetInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Pet %r>' % self.name


class HealthLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet_info.id'), nullable=False)
    record_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    weight = db.Column(db.Float, nullable=False)
    activity_level = db.Column(db.Integer, nullable=False)
    appetite_level = db.Column(db.Integer, nullable=False)
    coat_condition = db.Column(db.String(100), nullable=False)
    stool_condition = db.Column(db.String(100), nullable=False)
    urine_condition = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<HealthLog %r>' % self.record_date


class EventLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet_info.id'), nullable=False)
    event_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    event_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<EventLog %r>' % self.event_date


class PetImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet_info.id'), nullable=False)
    image_path = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<PetImage %r>' % self.image_path


@app.route('/')
def index():
    pets = PetInfo.query.all()
    return render_template('index.html', pets=pets)


# ペットの画像を表示する
@app.route('/pet_images/<int:pet_id>')
def pet_images(pet_id):
    pet_images = PetImage.query.filter_by(pet_id=pet_id).all()
    return render_template('pet_images.html', pet_images=pet_images)


# ペットの詳細を表示する
@app.route('/pet_info/<int:pet_id>')
def pet_info(pet_id):
    pet = PetInfo.query.get_or_404(pet_id)
    health_logs = HealthLog.query.filter_by(pet_id=pet_id).order_by(HealthLog.record_date.desc()).limit(10).all()
    event_logs = EventLog.query.filter_by(pet_id=pet_id).order_by(EventLog.event_date.desc()).limit(10).all()
    return render_template('pet_info.html', pet=pet, health_logs=health_logs, event_logs=event_logs)


# ペットの健康情報を追加する
@app.route('/add_health_log', methods=['GET', 'POST'])
def add_health_log():
    if request.method == 'POST':
        pet_id = request.form['pet_id']
        record_date = datetime.strptime(request.form['record_date'], '%Y-%m-%d')
        weight = request.form['weight']
        activity_level = request.form['activity_level']
        appetite_level = request.form['appetite_level']
        coat_condition = request.form['coat_condition']
        stool_condition = request.form['stool_condition']
        urine_condition = request.form['urine_condition']
        
        new_log = HealthLog(pet_id=pet_id, record_date=record_date, weight=weight, activity_level=activity_level,
                            appetite_level=appetite_level, coat_condition=coat_condition, stool_condition=stool_condition,
                            urine_condition=urine_condition)

        try:
            db.session.add(new_log)
            db.session.commit()
            flash('健康情報が追加されました。')
            return redirect(url_for('pet_info', pet_id=pet_id))
        except:
            db.session.rollback()
            flash('健康情報の追加に失敗しました。')
            return redirect(url_for('add_health_log', pet_id=pet_id))

    pet_id = request.args.get('pet_id')
    pet = PetInfo.query.get_or_404(pet_id)
    return render_template('add_health_log.html', pet=pet)


