from .handler import DbHandler
import functools


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