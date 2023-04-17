from flask import Flask, jsonify, Response
from data.models import Book, BookPage

# from data.handler import DbHandler
# from data.seeder import DbSeeder


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def home():
    return '<h2>Books API</h2>'

@app.route('/books', methods=['GET'])
def get_all_books():
    books = Book.get_books()
    return jsonify(books) 

@app.route('/book/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.get_book_by_id(book_id) 
    return jsonify(book) 

@app.route(
        '/book/<int:book_id>/page/<int:page_number>/<string:page_format>',
        methods=['GET']
    )
def get_book_page(book_id, page_number, page_format):
    book_page_content = BookPage.get_page_content(book_id, page_number, page_format)
    response_format = 'text/plain'

    if page_format == 'html':
        response_format = 'text/html'

    return Response(
        response=book_page_content,
        status=200,
        mimetype=response_format
    )


if __name__ == '__main__':
    app.run(debug=True, port=4000)


# def main():
#     DbHandler().setup_db()
#     DbSeeder.run()

# if __name__ == '__main__':
#     main()