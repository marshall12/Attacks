from flask import Flask, render_template, request, redirect, url_for,jsonify
app = Flask(__name__)
@app.route('/')
def home():
    return '<h1>LOGIN SUCCESSFUL</h1>'


@app.route('/login1', methods=['GET','POST'])
def login1():
    error = None
    if request.method == 'POST':
        if request.form['username'] != '00000' or request.form['password'] != '00005':
            error = 'Invalid username or password. Please try again'
            return jsonify({'message': error, 'success': False})

        else:
            return jsonify({'success': True})
            return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
