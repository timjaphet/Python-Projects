import sqlite3

conn = sqlite3.connect('test.db')

# Create database and a new table
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtfiles( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_txtfile TEXT \
        )")
    conn.commit()


fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')



with conn:
    cur = conn.cursor()
    for fName in fileList:
        if fName.endswith(".txt"):
            
            cur.execute('INSERT INTO tbl_txtfiles(col_txtfile) VALUES (?)', (fName,))
            conn.commit()



with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_txtfile FROM tbl_txtfiles")
    txtFile = cur.fetchall()
    for file in txtFile:
        txtFile = "The found text file: {}".format(file[0])
        print(txtFile)





    
