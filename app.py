from flask import Flask, render_template, request

app = Flask(__name__)

CURRENCIES = {
    "ZAR": "R",
    "USD": "$",
    "EUR": "€",
    "GBP": "£",
    "JPY": "¥",
    "AUD": "A$",
    "CAD": "C$",
    "INR": "₹",
    "NGN": "₦",
    "KES": "KSh",
    "GHS": "GH₵",
    "BRL": "R$",
    "CHF": "CHF",
    "CNY": "¥"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/discount", methods=["GET", "POST"])
def discount():
    result = None

    if request.method == "POST":
        price = float(request.form["price"])
        percentage = float(request.form["percentage"])
        currency = request.form["currency"]

        if currency not in CURRENCIES:
            currency = "ZAR"

        saved = price * (percentage / 100)
        final_price = price - saved

        result = {
            "saved": round(saved, 2),
            "final_price": round(final_price, 2),
            "symbol": CURRENCIES[currency]
        }

    return render_template(
        "discount.html",
        result=result,
        currencies=CURRENCIES
    )

if __name__ == "__main__":
    app.run(debug=True)