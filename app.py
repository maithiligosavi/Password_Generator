
from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    if request.method == 'POST':
        try:
            length = int(request.form['length'])
            if length < 4:
                password = "Password must be at least 4 characters."
            if length > 8:
                password = "Password must not be more than 8 characters."
            
            else:
                password = generate_password(length)
        except:
            password = "Invalid input."
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    if request.method == 'POST':
        try:
            length = int(request.form['length'])
            if length < 4:
                password = "Password must be at least 4 characters."
            if length > 8:
                password = "Password must not be more than 8 characters."
            
            else:
                password = generate_password(length)
        except:
            password = "Invalid input."
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
