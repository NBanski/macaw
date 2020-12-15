import os
import sqlite3

# Database/db directory path.
workingDirectory = os.path.dirname(__file__)
directoryPath = os.path.normpath(os.path.join(workingDirectory, "..", "database"))
dbPath = os.path.normpath(os.path.join(workingDirectory, "..", "..", "database", "macaw.db"))

# Check if database directory exists/create it.
def createDbDirectory():
    if os.path.exists(directoryPath):
        print("Database directory exists.")
    else:
        print("Database directory doesn't exist. Creating...")
        os.makedirs(directoryPath)

# Check if database exists/create it.
def createDb():
    conn = None
    try:
        conn = sqlite3.connect(dbPath)
        print(sqlite3.version)
        print("Database succesfully connected.")
    except Exception as e:
        print(e)
    finally:
        if conn:
            conn.close()

