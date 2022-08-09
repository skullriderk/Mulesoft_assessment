
####importing sqlite3 module#####
import sqlite3




####Creating a connection object to sqlite3

conn= sqlite3.connect("fav_movie.db")

print("Database created")

# Creating a table named movies
 
tabl = '''create table if not exists movies (SNo int primary key,
movie VARCHAR(20),
actor VARCHAR(20),
actress VARCHAR(20),
director VARCHAR(20),
release_year int);'''


#### executing the create  statement  
conn.execute(tabl)


#data insertion#
conn.execute("insert into movies values(1,'Avatar','Sam Worthington','Zoe Saldana','James Cameron',2009);")
conn.execute("insert into movies values(2,'Iron Man','Robert Downey Jr.','Gwyneth Paltrow','Jon Favreau',2008);")
conn.execute("insert into movies values(3,'Captain America','Chris Evans','Hayley Atwell','Joe Johnston',2011);")
conn.execute("insert into movies values(4,'Sherlock Holmes','Robert Downey Jr.','Rachel McAdams','Guy Ritchie',2010);")

conn.execute("insert into movies values(5,'Quantum of Solace','Daniel Craig','Olga Kurylenko','Marc Forster',2008);")





conn.commit()


#Querying table


#cursor to query#

curs = conn.execute("select * from movies")

print("\n")
print("Favourite Movies")
print("\n")

#### pointing to each individual row inside the table ####

for row in curs:
    print("S.no       : " ,row[0])
    print("movie_name : " ,row[1])
    print("actor      : ",row[2])
    print("actress    : ",row[3])
    print("director   : ",row[4])
    print("year_of_release : ",row[5])
    print("\n")


#querying using actor name#

print("----querying using actor name----")
print("\n")



curs = conn.execute("select * from movies where actor='Robert Downey Jr.'")


for row in curs:
    print("S.no       : " ,row[0])
    print("movie_name : " ,row[1])
    print("actor      : ",row[2])
    print("actress    : ",row[3])
    print("director   : ",row[4])
    print("year_of_release : ",row[5])
    print("\n")



#querying using director name#
print("----querying using director name----")
print("\n")



curs = conn.execute("select * from movies where director='James Cameron'")


for row in curs:
    print("S.no       : " ,row[0])
    print("movie_name : " ,row[1])
    print("actor      : ",row[2])
    print("actress    : ",row[3])
    print("director   : ",row[4])
    print("year_of_release : ",row[5])
    print("\n")


#querying using Year of release#
print("----Querying using release_year----")
print("\n")


curs = conn.execute("select * from movies where release_year=2008")


for row in curs:
    print("S.no       : " ,row[0])
    print("movie_name : " ,row[1])
    print("actor      : ",row[2])
    print("actress    : ",row[3])
    print("director   : ",row[4])
    print("release_year : ",row[5])
    print("\n")


    









