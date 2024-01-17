from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/confirmation')
def confirmation():
    name = request.args.get("name")
    phone = request.args.get("phn")
    email = request.args.get("email")
    add = request.args.get("add")
    city = request.args.get("city")
    state = request.args.get("state")
    zip = request.args.get("zip")
    print(name)
    props = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": add,
        "city": city,
        "state": state,
        "zip": zip
    }

    return render_template("confirmation.html", data=props)

if __name__ == '__main__':
    app.run(debug=True)

