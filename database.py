import sqlite3

class Database:
    def __init__(self, db_name='facebook_accounts.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            cookies TEXT NOT NULL
        )''')
        self.connection.commit()

    def add_account(self, username, password, cookies):
        self.cursor.execute('''INSERT INTO accounts (username, password, cookies) VALUES (?, ?, ?)''', (username, password, cookies))
        self.connection.commit()

    def fetch_all_accounts(self):
        self.cursor.execute('SELECT * FROM accounts')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

# Example usage:
# db = Database()
# db.add_account('user1', 'password123', 'cookie_data')
# accounts = db.fetch_all_accounts()
# db.close()