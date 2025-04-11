from flask import Flask, render_template, request
from backend.utils import calculate_actual_size
from backend.models import save_specimen, create_table

app = Flask(
    __name__,
    template_folder="web/templates",  # 👈 specify templates folder
    static_folder="web/templates/static"        # 👈 specify static folder
)

create_table()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        username = request.form["username"]
        size = float(request.form["microscope_size"])
        mag = float(request.form["magnification"])
        actual = calculate_actual_size(size, mag)
        save_specimen(username, size, mag, actual)
        result = f"Actual size: {actual:.2f} mm"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=False, port=5001)
