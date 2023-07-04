from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, Pet, db

from forms import PetForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "chickenzarecool21837"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def pets_home_page():
    pets = Pet.query.all()
    return render_template("pets_home_page.html", pets=pets)


@app.route("/add-pet-form", methods=["GET", "POST"])
def add_pet_form():
    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(
            name=name, species=species, photo_url=photo_url, age=age, notes=notes
        )
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_pet_form.html", form=form)


@app.route("/details/<int:pet_id>")
def pet_details(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return render_template("pet_details.html", pet=pet)


@app.route("/details/<int:pet_id>/edit-form", methods=["GET", "POST"])
def pet_edit_form(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        db.session.add(pet)
        db.session.commit()
        return redirect(f"/details/{pet_id}")
    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)
