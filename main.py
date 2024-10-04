from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def encrypt():
    message = request.form.get('message')
    key = request.form.get('key')
    print(message)
    print(key)
    return render_template('encrypt.html')

@app.route('/decrypt')
def decrypt():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)