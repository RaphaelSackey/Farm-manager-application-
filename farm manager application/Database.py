import sqlite3
connection = sqlite3.connect("animals.db")
cursor = connection.cursor()
#cursor.execute("create table restaurants (id integer, restaurant_name text, city text)")

cursor.execute("create table animals (animal_name text, mumber integer)")

# restaurant_info = [
#     (1, "Danes", "Plattsbutgh"),
#     (2, "twisted Carrot", "Flushin"),
#     (3, "Four loco", "Long island"),
#     (4, "Mamis Goody", "Burlington"),
    

# ]

#cursor.executemany("insert into restaurants values (?,?,?)",restaurants_info )


ani_info = [
    ("chicken",200),
    ("turkey", 229),
    ("cow", 50),
    ( "goat", 30),
    ("horse", 20),
    ("sheep", 80),
    ("cattle", 60),
    ("donkey",70 ),
    ("Texas Longhorn", 500),
    ("alpaca", 12),
    ("camel", 45),
    ("liama", 100 ),
    ("pig", 577),
    ("Serama",34 ),
    ("Domestic yak",66 ),
    ("Boer goat",79 ),
    ("Broiler",35 )
]
cursor.executemany("insert into animals values (?,?)",ani_info )


# for row in cursor.execute("select * from restaurants"):
#     print (row)
# for row in cursor.execute("select * from foods"):
#     print (row)


connection.commit()

connection.close()