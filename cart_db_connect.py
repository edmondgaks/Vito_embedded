import sqlite3

#connect to the database
def connect():
    try:
        conn = sqlite3.connect("cart.db")
        return conn
    except sqlite3.Error as e:
        print("Error in connecting to the database" + str(e))
        return None
    
#insert a record into the database
def insert(conn, values):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO cart (class_name, confidence_score) VALUES (?, ?)", values)
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print("Error in inserting a record" + str(e))
        return None
    
    