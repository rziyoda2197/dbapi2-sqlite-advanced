import sqlite3
from sqlite3 import Error

def advanced_query():
    try:
        # SQLite database connection
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()

        # CREATE TABLE
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        ''')

        # CREATE TABLE
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                order_date DATE NOT NULL,
                total REAL NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')

        # INSERT DATA
        cursor.execute("INSERT INTO users (name, age) VALUES ('John Doe', 30)")
        cursor.execute("INSERT INTO users (name, age) VALUES ('Jane Doe', 25)")
        cursor.execute("INSERT INTO orders (user_id, order_date, total) VALUES (1, '2022-01-01', 100.0)")
        cursor.execute("INSERT INTO orders (user_id, order_date, total) VALUES (1, '2022-01-15', 200.0)")
        cursor.execute("INSERT INTO orders (user_id, order_date, total) VALUES (2, '2022-02-01', 50.0)")

        # COMMIT CHANGES
        conn.commit()

        # ADVANCED QUERY
        query = '''
            SELECT u.name, SUM(o.total) as total_spent
            FROM users u
            JOIN orders o ON u.id = o.user_id
            GROUP BY u.name
            ORDER BY total_spent DESC
        '''
        cursor.execute(query)

        # FETCH RESULTS
        results = cursor.fetchall()

        # PRINT RESULTS
        for row in results:
            print(f"Name: {row[0]}, Total Spent: {row[1]}")

    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()

advanced_query()
