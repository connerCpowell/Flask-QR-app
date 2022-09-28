from flask import Flask, render_template
# from qr import qr_maker
# from PIL import Image

app = Flask(__name__)

@app.route("/")
def index():
   
    #img1, img2 = qr_maker(data)

    #img1.show()
    #img2.show()

    #return "Congrats broheimia, you like finally made it to the page"
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/<int:celsius>")
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        stg = str(celsius) + "\u00B0 Celsius is equal to " + str(fahrenheit) + "\u00B0 Fahrenheit!"
        return str(stg)
    except ValueError:
        return "invalid input"

    



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
