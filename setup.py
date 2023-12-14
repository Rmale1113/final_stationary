import sqlite3

connection = sqlite3.connect("stationary.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table customers")
    cursor.execute("drop table products")
except:
    pass

cursor.execute("CREATE TABLE customers(cust_id integer primary key,cust_name text,ph_no integer,email text,pid int,foreign key(pid) references products(prod_id))")
cursor.execute("CREATE TABLE products(prod_id int primary key,prod_name text,use_by_date text)")

cursor.execute("insert into customers values(23,'Raghu', 13594993, 'rasdsa@gmail.com', 49340 )")
cursor.execute("insert into products values(34,'penbox', '10-10-2022')")
connection.commit()
connection.close()
print("done.")