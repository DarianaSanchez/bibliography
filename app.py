from flask import Flask, jsonify, Response
from data.models import Book, BookPage

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


def response_error(message):
    return jsonify({'error': message}), 500

@app.route('/')
def home():
    return '<h2>Books API</h2>'

@app.route('/books', methods=['GET'])
def get_all_books():
    try:
        books = Book.get_books()
        return jsonify(books)
    except Exception as ex:
        return response_error(str(ex))
 
@app.route('/book/<int:book_id>', methods=['GET'])
def get_book(book_id):
    try:
        book = Book.get_book_by_id(book_id) 
        return jsonify(book) 
    except Exception as ex:
        return response_error(str(ex))

@app.route(
        '/book/<int:book_id>/page/<int:page_number>/<string:page_format>',
        methods=['GET']
    )
def get_book_page(book_id, page_number, page_format):
    try:
        book_page_content = BookPage.get_page_content(book_id, page_number, page_format)
        response_format = 'text/plain'

        if page_format == 'html':
            response_format = 'text/html'

        return Response(
            response=book_page_content,
            status=200,
            mimetype=response_format
        )
    except Exception as ex:
        return response_error(str(ex))


if __name__ == '__main__':
    app.run(debug=True, port=4000)