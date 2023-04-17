from .handler import DbHandler
import functools
import html2text


class Book():
  def __init__(self, title, author, pages_qty, isbn=None):
    self.id = None
    self.title = title
    self.author = author
    self.pages_qty = pages_qty
    self.isbn = isbn

  def __str__(self):
    return f'{self.title} by author {self.author}'
  
  def save_book(self):
    dbHandler = DbHandler()

    new_book_cmd = 'INSERT INTO books(title,author,pages_qty,isbn) VALUES(?,?,?,?)'
    book_vals = (self.title, self.author, self.pages_qty, self.isbn)
    new_book_id = dbHandler.insert_record(new_book_cmd, book_vals)

    return new_book_id

  @classmethod
  def map_records(self, records):
    def get_dict(rec):
      return {
        'id': rec[0],
        'title': rec[1],
        'author': rec[2],
        'pages_qty': rec[3],
      } 

    return [get_dict(row) for row in records]

  @classmethod
  def get_books(self):
    dbHandler = DbHandler()

    sql_query = 'SELECT id, title, author, pages_qty FROM books'
    books = dbHandler.get_records(sql_query)
    return self.map_records(books)
  
  @classmethod
  def get_book_by_id(self, book_id):
    dbHandler = DbHandler()

    sql_query = f'SELECT id, title, author, pages_qty FROM books WHERE id = {book_id}'
    books = dbHandler.get_records(sql_query)

    if not len(books):
      raise Exception(f'Book Id: {book_id} not found')

    return self.map_records(books)


class BookPage():
  def __init__(self, book_id, page_number, content, format):
    self.book_id = book_id
    self.page_number = page_number
    self.content = content
    self.format = format

  def save_book_page(self):
    dbHandler = DbHandler()

    new_page_cmd = 'INSERT INTO books(book_id,page_number,content,format) VALUES(?,?,?,?)'
    page_vals = (self.title, self.author, self.pages_qty, self.isbn)
    new_page_id = dbHandler.insert_record(new_page_cmd, page_vals)

    return new_page_id
  
  @classmethod
  def seed_book_pages(self, book_id, pages_qty):
    dbHandler = DbHandler()

    book_pages_cmd = f'''INSERT INTO pages(book_id,page_number,content,format)
                         VALUES{",".join(["(?,?,?,?)"] * pages_qty)}'''
    book_pages_vals = [(book_id, x, f'page {x} content', 'plain') 
                        for x in range(1, pages_qty + 1)]
    all_book_pages = functools.reduce(lambda x, y: x + y, book_pages_vals)

    dbHandler.insert_record(book_pages_cmd, all_book_pages)
  
  @classmethod
  def format_page(self, content):
    converter = html2text.HTML2Text()
    converter.ignore_links = True
    return converter.handle(content)

  @classmethod
  def get_page_content(self, book_id, page_number, page_format):
    dbHandler = DbHandler()

    sql_query = f'''SELECT content, format FROM pages 
                    WHERE book_id = {book_id} AND page_number = {page_number}'''
    pages = dbHandler.get_records(sql_query)

    if not len(pages):
      raise Exception(f'Page {page_number} of Book Id: {book_id} not found')
    
    (content, format) = pages[0]

    if format != page_format and format == 'html':
      return self.format_page(content)

    return content