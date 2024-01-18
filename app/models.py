from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class HeroModel(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable= False)
    super_name = db.Column(db.Text, nullable= False)
    created_at = db.Column(db.TIMESTAMP, server_default = db.func.now())
    updated_at = db.Column(db.TIMESTAMP, onupdate = db.func.now())


class HeroPowersModel(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable= False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default = db.func.now())
    updated_at = db.Column(db.TIMESTAMP, onupdate = db.func.now())


class PowersModel(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable= False)
    name = db.Column(db.String, nullable= False)
    created_at = db.Column(db.TIMESTAMP, server_default = db.func.now())
    updated_at = db.Column(db.TIMESTAMP, onupdate = db.func.now())




# add any models you may need. 