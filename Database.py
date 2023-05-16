import sqlite3
from datetime import datetime

def createtable():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS files
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  file_name TEXT NOT NULL,
                  file_path TEXT NOT NULL,
                  upload_time TEXT NOT NULL,
                  file_author TEXT)''')

    conn.commit()
    conn.close()

def addFile(file_name,file_path,file_author):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO files (file_name,file_path,upload_time, file_author) VALUES (?, ?, ?, ?)", (file_name,file_path, str(datetime.now().date()), file_author))

    conn.commit()
    conn.close()

def readFiles():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM files")
    rows = cursor.fetchall()

    conn.commit()
    conn.close()

    files=[]
    for row in rows:
        file= {
            "name":row[1],
            "path":row[2],
            "time":row[3],
            'author':row[4]
        }
        files.append(file)

    return files

def deleteFile(file_name):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM files WHERE file_name=?", (file_name,))

    conn.commit()
    conn.close()

