from flask_seeder import Faker, generator
from .models import Book, BookPage


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

      for book in faker.create(book_batch):
        new_book_id = book.save_book()
        BookPage.seed_book_pages(new_book_id, book.pages_qty)