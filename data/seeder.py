from flask_seeder import Faker, generator
from .handler import DbHandler
import functools


class Book():
  def __init__(self, title, author, pages_qty, isbn=None):
    self.title = title
    self.author = author
    self.pages_qty = pages_qty
    self.isbn = isbn

  def __str__(self):
    return f'{self.title} by author {self.author}'
  
  def get_vals(self):
    return (self.title, self.author, self.pages_qty, self.isbn)


class DbSeeder():

    @classmethod
    def run(self):
      faker = Faker(
        cls=Book,
        init={
          'title': generator.Name(),
          'author': generator.Name(),
          'pages_qty': generator.Integer(start=5, end=8),
          'isbn': ''
        }
      )

      # TODO: create as many books as config indicates
      book_batch = 5
      handler = DbHandler()
      new_book_cmd = 'INSERT INTO books(title,author,pages_qty,isbn) VALUES(?,?,?,?)'

      for book in faker.create(book_batch):
        # print(f'New book: {book}')
        new_book_id = handler.insert_record(new_book_cmd, book.get_vals())
        
        book_pages_cmd = f'''INSERT INTO pages(book_id,page_number,content)
                                VALUES{",".join(["(?,?,?)"] * book.pages_qty)}'''
        book_pages_vals = [(new_book_id, x, f'page {x} content') 
                            for x in range(1, book.pages_qty + 1)]
        all_book_pages = functools.reduce(lambda x, y: x + y, book_pages_vals)
        handler.insert_record(book_pages_cmd, all_book_pages)