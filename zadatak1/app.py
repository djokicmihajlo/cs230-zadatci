from hashlib import sha256

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    tekst = ""
    hash_vrednost = None
    greska = None

    if request.method == "POST":
        tekst = request.form.get("tekst", "")

        if len(tekst) > 255:
            greska = "Tekst ne sme imati vise od 255 karaktera."
        else:
            hash_vrednost = sha256(tekst.encode("utf-8")).hexdigest()

    return render_template(
        "index.html",
        tekst=tekst,
        hash_vrednost=hash_vrednost,
        greska=greska,
    )


if __name__ == "__main__":
    app.run(debug=True)
