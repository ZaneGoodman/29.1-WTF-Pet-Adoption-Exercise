from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    IntegerField,
    SelectField,
    URLField,
  
)
from wtforms.validators import InputRequired, NumberRange

class PetForm(FlaskForm):
    """Pet form data structure"""

    name = StringField(
        "Pet Name", validators=[InputRequired(message="Name is required")]
    )

    species = SelectField(
        "Species",
        choices=[
            ("dog", "Dog"),
            ("cat", "Cat"),
            ("porcupine", "Porcupine"),
        ],
    )
    photo_url = URLField(
        "Picture", default="https://animalmicrochips.co.uk/images/default_no_animal.jpg"
    )

    age = IntegerField(
        "Age",
        validators=[
            InputRequired(message="Age is required"),
            NumberRange(min=1, max=30, message="Age must be between 1-30"),
        ],
    )

    notes = StringField("Notes")
