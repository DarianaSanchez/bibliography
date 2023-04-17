from .handler import DbHandler
from .seeder import DbSeeder

def setup():
    DbHandler().setup_db()
    DbSeeder.run()

if __name__ == '__main__':
    setup()