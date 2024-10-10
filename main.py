from flask import Flask, render_template, request, session, redirect
from cryptography.fernet import Fernet
import base64
import hashlib

app = Flask(__name__, template_folder='templates')
app.secret_key = 'secret_key'

def get_key(key):

    hashed_key = hashlib.sha256(key.encode()).digest()
    return base64.urlsafe_b64encode(hashed_key)

@app.route('/', methods=['GET', 'POST'])
def encrypt():
    message = request.form.get('message')
    key = request.form.get('key')

    if message and key:
        hashed_key = get_key(key) 
        cipher = Fernet(hashed_key)

        session['message'] = cipher.encrypt(message.encode())
        session['key'] = hashed_key
        return redirect('/decrypt')

    return render_template('encrypt.html')

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():

    key = request.form.get('key')
    if key:
        try:
            hashed_key = get_key(key) 
            cipher = Fernet(hashed_key)

            session['message'] = cipher.decrypt(session['message']).decode()
            return redirect('/decrypt')
        except:
            return render_template('decrypt.html', message = session['message'], key = session['key'])

    return render_template('decrypt.html', message = session['message'], key = session['key'])

if __name__ == '__main__':
    app.run(debug=True)