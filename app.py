from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "change-this-secret-key"  # replace before deploying

PLANTS = [
    {"name": "Monstera", "price": 899, "light": "Bright, indirect light", "care": "Water when the top inch of soil is dry."},
    {"name": "Snake plant", "price": 499, "light": "Low to bright light", "care": "Water every 2-3 weeks."},
    {"name": "Money plant", "price": 299, "light": "Medium light", "care": "Keep soil lightly moist."},
    {"name": "Peace lily", "price": 649, "light": "Low to medium light", "care": "Water when the leaves start to droop."},
    {"name": "Aloe vera", "price": 349, "light": "Direct sun", "care": "Let the soil dry fully between waterings."},
    {"name": "Fern", "price": 549, "light": "Shade", "care": "Keep soil evenly moist and mist often."},
]


@app.route("/")
def home():
    return render_template("home.html", plants=PLANTS[:3])


@app.route("/plants")
def plants():
    return render_template("plants.html", plants=PLANTS)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        message = request.form.get("message", "").strip()
        if not name or not message:
            flash("Add your name and a message, then send again.", "error")
        else:
            # TODO: save to a database or send an email here
            flash(f"Thanks, {name}. We'll reply soon.", "ok")
            return redirect(url_for("contact"))
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
