import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "elmolovesyou10!",
                           db = "redo")
    c = conn.cursor()
    
    return c, conn