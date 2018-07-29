import flask
import json
from flask import request, jsonify, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = []
with open('jsonData/bookdata.json') as f:
    books = json.load(f)

@app.route('/', methods=['GET'])
def home():
    return render_template('intro.html')

@app.route('/api/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/books/id', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Sorry, no id field provided. Please provide an id."

    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)

    return jsonify(results)

@app.route('/api/books/title', methods=['GET'])
def api_title():
    if 'title' in request.args:
        title = request.args['title']
    else:
        return "Sorry, no title field provided. Please provide a title."

    results = []
    for book in books:
        if title in str(book['title']):
            results.append(book)

    return jsonify(results)

@app.route('/api/books/author', methods=['GET'])
def api_author():
    if 'author' in request.args:
        author = request.args['author']
    else:
        return "Sorry, no author field provided. Please provide an author."

    results = []
    for book in books:
        if author in str(book['author']):
            results.append(book)

    return jsonify(results)

@app.route('/api/books/year', methods=['GET'])
def api_year():
    if 'year' in request.args:
        year = request.args['year']
    else:
        return "Sorry, no year field provided. Please provide a year."

    results = []
    for book in books:
        if year in str(book['published']):
            results.append(book)

    return jsonify(results)

app.run()

