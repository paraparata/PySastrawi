from flask import Flask, jsonify, request, render_template
from build.lib.Sastrawi.Stemmer.StemmerFactory import StemmerFactory


app = Flask(__name__)

# define stemmer with PySastrawi
def sastrawi(text):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    return stemmer.stem(text)

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    # POST request
    if request.method == 'POST':
        print('Incoming..')
        text = request.get_json().get('textToStem')
        stemmedText = sastrawi(text)
        print(text)
        return stemmedText, 200

    # GET request
    else:
        message = {'textToStem': 'Hello from Flask!'}
        return jsonify(message)

@app.route('/test')
def test_page():
    return render_template('index.html')
