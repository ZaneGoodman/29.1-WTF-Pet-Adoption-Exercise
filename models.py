from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet Model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text, nullable=False)

    species = db.Column(db.Text, nullable=False)

    photo_url = db.Column(db.Text)

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean, default=True, nullable=False)


# class Department(db.Model):
#     """Department Model"""

#     __tablename__ = "departments"

#     dept_code = db.Column(db.Text, primary_key=True)
#     dept_name = db.Column(db.Text, nullable=False, unique=True)
#     phone = db.Column(db.Text)

#     def __repr__(self):
#         return f"<Department {self.dept_code} {self.dept_name} {self.phone} >"
