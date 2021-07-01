import sqlite3

db = sqlite3.connect("medicine.db")
cursor = db.cursor()

registration = """
               CREATE TABLE registrated_clients( 
                                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                id_telegram INTEGER ,
                                                first_last_name VARCHAR(25),
                                                age VARCHAR(5),
                                                gender  VARCHAR(15),
                                                blood_type  VARCHAR(15),
                                                number  VARCHAR(12),
                                                proverka VARCHAR(10)
                                                )
               """

terapeft = """
          CREATE TABLE terapeft( 
                                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                time0900 BOOLEAN,
                                                time1000 BOOLEAN,
                                                time1100 BOOLEAN, 
                                                time1200 BOOLEAN,
                                                time1340 BOOLEAN,
                                                time1440 BOOLEAN,
                                                time1540 BOOLEAN,
                                                time1640 BOOLEAN,
                                                time1740 BOOLEAN
                                                
                                                )
          """

lor = """
          CREATE TABLE lor( 
                                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                time0900 BOOLEAN,
                                                time1000 BOOLEAN,
                                                time1100 BOOLEAN, 
                                                time1200 BOOLEAN,
                                                time1340 BOOLEAN,
                                                time1440 BOOLEAN,
                                                time1540 BOOLEAN,
                                                time1640 BOOLEAN,
                                                time1740 BOOLEAN
                                                )
          """

hirurg = """
          CREATE TABLE hirurg( 
                                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                time0900 BOOLEAN,
                                                time1000 BOOLEAN,
                                                time1100 BOOLEAN, 
                                                time1200 BOOLEAN,
                                                time1340 BOOLEAN,
                                                time1440 BOOLEAN,
                                                time1540 BOOLEAN,
                                                time1640 BOOLEAN,
                                                time1740 BOOLEAN
                                                )
          """

oculist = """
          CREATE TABLE oculist( 
                                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                time0900 BOOLEAN,
                                                time1000 BOOLEAN,
                                                time1100 BOOLEAN, 
                                                time1200 BOOLEAN,
                                                time1340 BOOLEAN,
                                                time1440 BOOLEAN,
                                                time1540 BOOLEAN,
                                                time1640 BOOLEAN,
                                                time1740 BOOLEAN
                                                )
          """

pediatr = """
          CREATE TABLE pediatr( 
                                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                time0900 BOOLEAN,
                                                time1000 BOOLEAN,
                                                time1100 BOOLEAN, 
                                                time1200 BOOLEAN,
                                                time1340 BOOLEAN,
                                                time1440 BOOLEAN,
                                                time1540 BOOLEAN,
                                                time1640 BOOLEAN,
                                                time1740 BOOLEAN
                                                )
          """

nevrolog = """
          CREATE TABLE nevrolog( 
                                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                time0900 BOOLEAN,
                                                time1000 BOOLEAN,
                                                time1100 BOOLEAN, 
                                                time1200 BOOLEAN,
                                                time1340 BOOLEAN,
                                                time1440 BOOLEAN,
                                                time1540 BOOLEAN,
                                                time1640 BOOLEAN,
                                                time1740 BOOLEAN
                                                )
          """

waiting = """
          CREATE TABLE waiting(
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               id_telegram VARCHAR(15),
                               inn VARCHAR(15),
                               type_doctor VARCHAR(15),
                               time VARCHAR(15),
                               t BOOLEAN
                                
                              )
          """
'''
cursor.execute("""
                                   INSERT INTO terapeft(
                                                time0900,
                                                time1000,
                                                time1100, 
                                                time1200,
                                                time1340,
                                                time1440,
                                                time1540,
                                                time1640,
                                                time1740   
                                   ) VALUES(?,?,?,?,?,?,?,?,?) """, (1,1,1,1,1,1,1,1,1))
db.commit()

'''

'''
cursor.execute("""
                                   INSERT INTO lor(
                                                time0900,
                                                time1000,
                                                time1100, 
                                                time1200,
                                                time1340,
                                                time1440,
                                                time1540,
                                                time1640,
                                                time1740   
                                   ) VALUES(?,?,?,?,?,?,?,?,?) """, (1,1,1,1,1,1,1,1,1))
db.commit()

cursor.execute("""
                                   INSERT INTO hirurg(
                                                time0900,
                                                time1000,
                                                time1100, 
                                                time1200,
                                                time1340,
                                                time1440,
                                                time1540,
                                                time1640,
                                                time1740   
                                   ) VALUES(?,?,?,?,?,?,?,?,?) """, (1,1,1,1,1,1,1,1,1))
db.commit()

cursor.execute("""
                                   INSERT INTO oculist(
                                                time0900,
                                                time1000,
                                                time1100, 
                                                time1200,
                                                time1340,
                                                time1440,
                                                time1540,
                                                time1640,
                                                time1740   
                                   ) VALUES(?,?,?,?,?,?,?,?,?) """, (1,1,1,1,1,1,1,1,1))
db.commit()

cursor.execute("""
                                   INSERT INTO pediatr(
                                                time0900,
                                                time1000,
                                                time1100, 
                                                time1200,
                                                time1340,
                                                time1440,
                                                time1540,
                                                time1640,
                                                time1740   
                                   ) VALUES(?,?,?,?,?,?,?,?,?) """, (1,1,1,1,1,1,1,1,1))
db.commit()

cursor.execute("""
                                   INSERT INTO nevrolog(
                                                time0900,
                                                time1000,
                                                time1100, 
                                                time1200,
                                                time1340,
                                                time1440,
                                                time1540,
                                                time1640,
                                                time1740   
                                   ) VALUES(?,?,?,?,?,?,?,?,?) """, (1,1,1,1,1,1,1,1,1))
db.commit()
'''

'''
list_table = [registration, terapeft, lor, hirurg, oculist, pediatr, nevrolog, waiting]

for list in list_table:
    cursor.execute(list)
'''

#spravka_ = "DROP TABLE sport"
#cursor.execute(spravka_)

#sport_s = "DROP TABLE sport_spravka"
#cursor.execute(sport_s)

#sport_s = "CREATE TABLE sport_spravka(id INTEGER PRIMARY KEY AUTOINCREMENT, inn VARCHAR(15), t BOOLEAN)"
#cursor.execute(sport_s)

#sport_s = "CREATE TABLE sport_086(id INTEGER PRIMARY KEY AUTOINCREMENT, inn VARCHAR(15), t BOOLEAN)"
#cursor.execute(sport_s)

#sport_s = "CREATE TABLE sport_job(id INTEGER PRIMARY KEY AUTOINCREMENT, inn VARCHAR(15), t BOOLEAN)"
#cursor.execute(sport_s)
