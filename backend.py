import sqlite3

def connect():
    conn =sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer, cost integer, stock integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn, cost,stock):
    conn =sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("INSERT INTO bookstore VALUES(NULL, ?,?,?,?,?,?)", (title,author,year,isbn,cost,stock))
    conn.commit()
    conn.close()


def view():
    conn =sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM bookstore")
    rows =cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn="", cost="", stock=""):
    conn =sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM bookstore WHERE title=? OR author=? OR year=? OR isbn=? OR cost=? OR stock=?",(title,author,year,isbn,cost,stock))
    rows =cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn =sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("DELETE FROM bookstore WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn, cost, stock ):
    conn =sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("UPDATE bookstore SET title=?, author=?, year=?, isbn=?, cost=?, stock=? WHERE id=?",(title, author, year, isbn, cost, stock, id))
    conn.commit()
    conn.close()
    conn.close()

connect()

