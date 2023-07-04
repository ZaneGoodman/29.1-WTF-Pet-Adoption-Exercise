from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    FloatField,
    BooleanField,
    IntegerField,
    RadioField,
    SelectField,
    URLField,
    IntegerRangeField,
)
from wtforms.validators import InputRequired, NumberRange


# class AddSnackForm(FlaskForm):
#     name = StringField(
#         "Snack Name", validators=[InputRequired(message="Snack name cannot be blank")]
#     )
#     price = FloatField("Price in USD")
#     quantity = IntegerField("How many?")
#     is_healthy = BooleanField("This is a healthy snack")


#     category = SelectField(
#         "Category",
#         choices=[
#             ("ic", "Ice Cream"),
#             ("chips", "Potato Chips"),
#             ("candy", "Candy/Sweets"),
#         ],
#     )
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
