from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Set your username and password here.It is taken 00000 and 00009 so that it will consume less time to brute force
username = '00000'
password = '00009'


@app.route('/login1', methods=['GET', 'POST'])
def login1():
    if request.method == 'POST':
        if request.form['username'] != username or request.form['password'] != password:
            return jsonify({'message': 'Invalid username or password. Please try again', 'success': False})
        else:
            return jsonify({'message':'Login Successful', 'success': True})

if __name__ == "__main__":
    app.run(debug=True)
