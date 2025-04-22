import os
from flask import Flask, render_template, request
from backend.utils import calculate_actual_size
from backend.models import save_specimen, create_table

app = Flask(
    __name__,
    template_folder="web/templates",  
    # static_folder="web/static"        
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
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)
