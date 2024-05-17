class Queries:
    CREATE_SURVEY_TABLE = """
        CREATE TABLE IF NOT EXISTS surveys (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            genre TEXT,
            rating INTEGER
        )
    """
    DROP_GENRES_TABLE = "DROP TABLE IF EXISTS genres"
    CREATE_GENRES_TABLE = """
        CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """
    DROP_BOOKS_TABLE = "DROP TABLE IF EXISTS books"
    CREATE_BOOKS_TABLE = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            price FLOAT,
            picture TEXT,
            genre_id INTEGER,
            FOREIGN KEY(genre_id) REFERENCES genres(id)
        )
    """
    POPULATE_GENRES = """
        INSERT INTO genres (name) VALUES
            ('Триллер'),
            ('Хоррор'),
            ('Фантастика')
    """
    POPULATE_BOOKS = """
        INSERT INTO books (name, author, price, picture, genre_id) VALUES
        ('Война и мир', 'Л.Н. Толстой', 300.0, 'images/book1.jpg', 1),
        ('Евгений Онегин', 'А.С. Пушкин', 350.0, 'images/book2.jpg', 2),
        ('Метро 2033', 'Дмитрий Глуховский', 250.0, 'images/book3.jpg', 3)
    """