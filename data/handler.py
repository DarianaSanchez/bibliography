import sqlite3
from sqlite3 import Error


class DbHandler():
    
    def __init__(self):
        try:
            self.connection = sqlite3.connect('database.db')
        except Error as e:
            print(e)

    def __del__(self):
        self.connection.close()

    def create_table(self, sql_command):
        """
        Creates database table
        :param sql_command:
        :return:
        """
        cursor = self.connection.cursor()
        cursor.execute(sql_command)
        self.connection.commit()

    def setup_db(self):
        """
        Creates books table and pages table
        :return:
        """
        books_table_command = (
            '''
            CREATE TABLE IF NOT EXISTS books(
                id integer PRIMARY KEY,
                title text NOT NULL,
                author text NOT NULL,
                pages_qty integer NOT NULL,
                isbn text
            )
            '''
        )
        pages_table_command = (
            '''
            CREATE TABLE IF NOT EXISTS pages(
                book_id integer NOT NULL,
                page_number integer NOT NULL,
                content text,
                FOREIGN KEY (book_id) REFERENCES books (id)
            )
            '''
        )

        self.create_table(books_table_command)
        self.create_table(pages_table_command)

    def insert_record(self, sql_command, values):
        """
        Inserts record as sql_command indicates
        :param sql_command:
        :param values:
        :return: new record id
        """
        cursor = self.connection.cursor()
        cursor.execute(sql_command, values)
        self.connection.commit()
        return cursor.lastrowid

    def get_records(self, sql_command):
        """
        Gets all record
        :param sql_command:
        :return: list of records
        """
        cursor = self.connection.cursor()
        cursor.execute(sql_command)
        records = cursor.fetchall()
        return records