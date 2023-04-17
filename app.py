from flask import Flask
# from data.handler import DbHandler
# from data.seeder import DbSeeder

app = Flask(__name__)

@app.route('/')
def home():
    return '<h2>Books API</h2>'


if __name__ == '__main__':
    app.run(debug=True, port=4000)


# def main():
#     DbHandler.setup_db()
#     DbSeeder.run()

# if __name__ == '__main__':
#     main()