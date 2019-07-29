from flask import Flask, render_template, request, url_for, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('notfound.html')

if __name__ == '__main__':
    app.run(debug=True)