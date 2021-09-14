import sqlite3
conn = sqlite3.connect('identifier.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Users(
TG_ID int,
Counter int
)''')

first_insert = '''
INSERT INTO Users VALUES('{}', 0)
'''

counter_in_table = '''
SELECT Counter
FROM Users
WHERE TG_ID = '{}'
'''
tg_id_in_table = '''
SELECT TG_ID
FROM Users
WHERE TG_ID = '{}'
'''

update_counter = '''
UPDATE Users
SET Counter = '{}'
WHERE TG_ID = '{}'
'''