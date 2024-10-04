from flask import Flask, render_template, request, session

app = Flask(__name__, template_folder='templates')
app.secret_key = 'secret_key'

@app.route('/', methods=['GET', 'POST'])
def encrypt():
    session['message'] = request.form.get('message')
    session['key'] = request.form.get('key')
    return render_template('encrypt.html')

@app.route('/decrypt')
def decrypt():
    print(session['message'])
    print(session['key'])
    return render_template('decrypt.html', message = session['message'], key = session['key'])

if __name__ == '__main__':
    app.run(debug=True)