import sqlite3

# connect to to file example.sqlite3
conn = sqlite3.connect('example.sqlinte3')

# get "cursor" to interact with database
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS NoSuchTable')
#Delets table named "NoSuchTable", checks if it exists first

cur.execute('CREATE TABLE IF NOT EXISTS Characters (name TEXT, job TEXT, species TEXT, gender TEXT, isForceUser INTEGER)')
# creates a table named "Characters" with several fields - mostly text, one integer

cur.execute('INSERT INTO Characters (name, job, species, gender, isForceUser) VALUES ("Kyle Katarn", "Jedi Knight", "Human", "Male", "1")')
# Adds a row to the table

cur.execute('CREATE TABLE Factions (name TEXT, type TEXT)')
cur.execute('CREATE TABLE FactionRelations (faction1 TEXT, faction2 TEXT, relatin TEXT)')
# creates a table called "Factions"
# Creates a table called "FactionRelations" to store relations between factions - enemy, ally, etc.
#   this table would have an entry for every possible pairing of two factions

cur.execute('CREATE TABLE CharacterFactionRelations (character TEXT, faction TEXT, relation TEXT)')
# character-to-faction relations may be more complicated than each character belonging to a single faction

cur.execute('DELETE FROM Characters WHERE job = "Jedi Knight"')
# deletes all Jedi Knight characters from Characters table

cur.execute('SELECT name, job FROM Characters WHERE species = "Human" ORDER BY job')
for row in cur :
    print(row)
# get list of all human characters, sorted by job
# iterate through all rows returned by SELECT, print list of characters returned

conn.commit()
# commits changes back to file
