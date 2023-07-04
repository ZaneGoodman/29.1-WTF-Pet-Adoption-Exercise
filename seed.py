#   id = db.Column(db.Integer, primary_key=True, autoincrement=True)

#     name = db.Column(db.Text, nullable=False)

#     species = db.Column(db.Text, nullable=False)

#     photo_url = db.Column(db.Text, unique=True)

#     age = db.Column(db.Integer)

#     notes = db.Column(db.Text)

#     available = db.Column(db.Boolean, nullable=False, server_default=True)

"""Seed file to make sample data for db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()


pet1 = Pet(
    name="Sparky",
    species="porcupine",
    photo_url="https://nationalzoo.si.edu/sites/default/files/styles/1400_scale/public/animals/naporcupine-01.jpg?itok=-jOynEZE",
    age=4,
    notes="Good with kids, Potty Trained, Likes to chew on shoes",
    available=True,
)

pet2 = Pet(
    name="Bella",
    species="dog",
    photo_url="https://hips.hearstapps.com/hmg-prod/images/small-fuffy-dog-breeds-1623362663.jpg?crop=1.00xw:0.753xh;0,0.0719xh&resize=1200:*",
    age=6,
    notes="Bella is full of energy and needs a home where she can run and play",
    available=True,
)

pet3 = Pet(
    name="Sally",
    species="cat",
    photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/1920px-Cat_August_2010-4.jpg",
    age=10,
    notes="In Sally's old age she loves to nap and isn't fond of kids",
    available=True,
)

pet4 = Pet(
    name="Ari",
    species="dog",
    photo_url="https://cdn.psychologytoday.com/sites/default/files/styles/article-inline-half-caption/public/field_blog_entry_images/2020-06/angry_chihuahua.png?itok=TWxYDbOT",
    age=7,
    notes="Ari is very overweight and needs a family that will help her get healthy",
    available=False,
)

pet5 = Pet(
    name="Waffle",
    species="porcupine",
    photo_url="https://nationalzoo.si.edu/sites/default/files/styles/1400_scale/public/animals/naporcupine-03.jpg?itok=l-gWUXam",
    age=1,
    notes="Waffle is very loving and wants lots of attention",
    available=True,
)

db.session.add_all([pet1, pet2, pet3, pet4, pet5])
db.session.commit()
