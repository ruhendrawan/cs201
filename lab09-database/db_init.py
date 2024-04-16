# use sqlite3 to create a database and table, and insert some data
import sqlite3

# connect to the database
db = sqlite3.connect('poems.db')

# get a cursor object
# cursor is used to interact with the database
cursor = db.cursor()

# remove the table if it exists
# this is just for learning purposes
cursor.execute('''
DROP TABLE IF EXISTS poems;
''')

# create a table -- data definition language (DDL)
cursor.execute('''
CREATE TABLE poems (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    poem_text TEXT
);
''')


poems = [
    ['The Road Not Taken', 'Robert Frost', 'Two roads diverged in a yellow wood, And sorry I could not travel both...'],
    ['Ozymandias', 'Percy Bysshe Shelley', 'I met a traveller from an antique land Who said: Two vast and trunkless legs of stone...'],
    ['Daffodils', 'William Wordsworth', 'I wandered lonely as a cloud That floats on high o''er vales and hills...'],
    ['Sonnet 18', 'William Shakespeare', 'Shall I compare thee to a summer''s day? Thou art more lovely and more temperate...'],
    ['The Raven', 'Edgar Allan Poe', 'Once upon a midnight dreary, while I pondered, weak and weary...'],
]

# insert some data -- data manipulation language (DML)
for poem in poems:
    cursor.execute('''
    INSERT INTO poems (title, author, poem_text)
    VALUES (?, ?, ?)
    ''', (poem[0], poem[1], poem[2]))

# commit the changes
# this saves the changes from memory to the database
db.commit()

# close the connection
db.close()

# test the database
db = sqlite3.connect('poems.db')
cursor = db.cursor()
data = cursor.execute('SELECT * FROM poems;').fetchall()
print(data)
db.close()