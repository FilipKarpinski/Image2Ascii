from urllib import request
from flask import Flask, request, json
from flask_cors import CORS, cross_origin

from main import convert

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/generate_ascii', methods=['GET', 'POST'])
@cross_origin()
def generate_ascii():
    data = request.form.to_dict()
    print(data)
    file = request.files['file']
    bytes_file = file.read()
    ascii_text = convert(file_bytes=bytes_file, quality=data['quality'], invert=data.get('invert', False))
    return {
        'ascii_text': ascii_text,
        'quality': data['quality'],
        }

app.run()