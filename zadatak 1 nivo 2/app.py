from time import sleep, time

from flask import Flask, render_template, request


app = Flask(__name__)
kes = {}


def interceptor(funkcija):
    def wrapper(*args):
        kljuc = (funkcija.__name__, args)

        if kljuc in kes:
            return kes[kljuc], True

        rezultat = funkcija(*args)
        kes[kljuc] = rezultat
        return rezultat, False

    return wrapper


@interceptor
def skupa_funkcija(a, b):
    sleep(2)
    return a ** b


@app.route("/", methods=["GET", "POST"])
def index():
    a = ""
    b = ""
    rezultat = None
    iz_kesa = None
    trajanje = None
    greska = None

    if request.method == "POST":
        a = request.form.get("a", "")
        b = request.form.get("b", "")

        try:
            a_broj = int(a)
            b_broj = int(b)
            pocetak = time()
            rezultat, iz_kesa = skupa_funkcija(a_broj, b_broj)
            trajanje = round(time() - pocetak, 3)
        except ValueError:
            greska = "Unesite cele brojeve."

    return render_template(
        "index.html",
        a=a,
        b=b,
        rezultat=rezultat,
        iz_kesa=iz_kesa,
        trajanje=trajanje,
        greska=greska,
    )


if __name__ == "__main__":
    app.run(debug=True)
