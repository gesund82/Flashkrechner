from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        zahl1 = float(request.form["zahl1"])
        zahl2 = float(request.form["zahl2"])
        result = zahl1 + zahl2

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)