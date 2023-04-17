from flask_seeder import Faker, generator
from .models import Book, BookPage

import os
from dotenv import load_dotenv

load_dotenv()


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

      books_amount = int(os.getenv('BOOKS_AMOUNT') or 5)
      for book in faker.create(books_amount):
        new_book_id = book.save_book()
        BookPage.seed_book_pages(new_book_id, book.pages_qty)