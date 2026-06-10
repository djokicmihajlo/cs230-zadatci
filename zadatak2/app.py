from queue import Queue
from threading import Lock, Thread
from time import sleep

from flask import Flask, redirect, render_template, request


app = Flask(__name__)
red = Queue()
porudzbine = []
lock = Lock()
brojac = 1


def kuvar(ime):
    while True:
        porudzbina_id = red.get()

        with lock:
            for porudzbina in porudzbine:
                if porudzbina["id"] == porudzbina_id:
                    porudzbina["status"] = "priprema"
                    porudzbina["kuvar"] = ime

        sleep(2)

        with lock:
            for porudzbina in porudzbine:
                if porudzbina["id"] == porudzbina_id:
                    porudzbina["status"] = "gotovo"

        red.task_done()


for i in range(1, 4):
    Thread(target=kuvar, args=(f"Kuvar {i}",), daemon=True).start()


@app.route("/", methods=["GET", "POST"])
def index():
    global brojac

    if request.method == "POST":
        jelo = request.form.get("jelo", "")

        if jelo.strip():
            with lock:
                porudzbine.append({
                    "id": brojac,
                    "jelo": jelo,
                    "status": "ceka",
                    "kuvar": "",
                })
                red.put(brojac)
                brojac += 1

        return redirect("/")

    with lock:
        lista = porudzbine.copy()

    return render_template("index.html", porudzbine=lista)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
