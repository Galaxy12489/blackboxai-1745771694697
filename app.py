from flask import Flask, render_template, request

app = Flask(__name__)

# Laptop models data
laptops = {
    "Lenovo IdeaPad 3 15ITL6": {
        "price_rub": 45000,
        "upgrades": ["Процессор", "Оперативная память", "Накопитель"]
    },
    "Acer Aspire 5 A515-56": {
        "price_rub": 60000,
        "upgrades": ["Процессор", "Видеокарта", "Оперативная память", "Накопитель"]
    },
    "HP 15s-eq2": {
        "price_rub": 55000,
        "upgrades": ["Оперативная память", "Накопитель"]
    },
    "ASUS VivoBook 15 X515EA": {
        "price_rub": 70000,
        "upgrades": ["Процессор", "Оперативная память", "Накопитель"]
    },
    "Dell Inspiron 15 3501": {
        "price_rub": 75000,
        "upgrades": ["Процессор", "Видеокарта", "Оперативная память", "Накопитель"]
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    selected_model = None
    upgrades = []
    if request.method == "POST":
        selected_model = request.form.get("laptop_model")
        if selected_model in laptops:
            upgrades = laptops[selected_model]["upgrades"]
    return render_template("index.html", laptops=laptops, selected_model=selected_model, upgrades=upgrades)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
