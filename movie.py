from random import choice
import sqlite3
#database creation
con = sqlite3.connect('Record.db')
print('db created')
class MyMovie:
    
    def __init__(self):
    #table creation
        self.con.execute('create table if not exists Movie (id int,name text ,actor text, actress text, director text, yearofrelease int)')
        print('table created')

    #For Insertion
    def insert():
        id = input('enter id .:')
        name = input('enter name .:')
        actor = input('enter actor name .:')
        actress = input('enter actress name .:')
        director = input('enter director .:')
        yearofrelease = input('enter year of release .:')

        con.execute('insert into Movie (id, name, actor, actress, director, yearofrelease) Values (?,?,?,?,?,?)',(id,name,actor,actress,director,yearofrelease))
        con.commit()
        print('Record Added')

    #For Deletaion
    def delete():
        idd = input('Enter id for Deletation .:')
        con.execute('delete from Movie where id = ?', idd) 
        con.commit()
        print('record deleted')

     #For Updataion
    def update():
        id = input('enter id for Updation .:')
        name = input('enter Updated name .:')
        actor = input('enter Updated actor name .:')
        actress = input('enter Updated  actress name .:')
        director = input('enter Updated director .:')
        year = input('enter Updated year of release .:')
        con.execute('update Movie set name = ?,actor = ?,actress = ?, director = ?, yearofrelease = ? where id = ?',(name,actor,actress,director,year,id))
        con.commit()
        print('Record Updated')

    def select():
        data = con.execute('select * from Movie')
        for r in data:
            
            print('id :',(r[0]))
            print('Name :',(r[1]))
            print('Actor :',(r[2]))
            print('Actress :',(r[3]))
            print('Director :',(r[4]))
            print('Year of Release  :',(r[5]))
    


M = MyMovie 

print('A : Insert')
print('B : Delete')
print('C : Update')
print('D : Display')
print('E : Exit')

while(True):

    ch = input('enter your choice : ')

    if(ch == 'A'):
        M.insert()
    elif(ch == 'B'):
        M.delete()
    elif(ch == 'C'):
        M.update()
    elif(ch == 'D'):
        M.select()
    elif(ch == 'E'):
        exit()
    else:
        print("Please enter valid Choice")
    

   
    

    