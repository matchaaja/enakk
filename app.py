from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, buka file http://127.0.0.1:5000/foryou.html secara manual ya!'

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Ganti dengan username/password kamu
    if username == 'fahim' and password == 'loveyou':
        return redirect('/surprise')
    else:
        return 'Username atau password salah!'

@app.route('/surprise')
def surprise():
    return render_template('http://127.0.0.1:5500/suprise.html')

if __name__ == '__main__':
    app.run(debug=True)