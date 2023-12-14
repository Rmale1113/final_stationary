import sqlite3

connection = sqlite3.connect("stationary.db")
def get_customers(id=None):
    cursor = connection.cursor()

    if id is None:
        cursor.execute("SELECT * FROM customers")
    else:
        cursor.execute(f"SELECT * FROM customers WHERE cust_id={id}")

    rows = cursor.fetchall()
    customers = [{'cust_id': row[0], 'cust_name': row[1], 'ph_no':row[2], 'email': row[3], 'pid': row[4]} for row in rows]

    return customers
def get_items(id=None):
    cursor = connection.cursor()
    if id == None:
        rows = cursor.execute("select * from products")
    else:
        rows = cursor.execute(f"select * from products where prod_id={id}")
    rows = cursor.fetchall()
    rows = list(rows)
    products = [{'prod_id': row[0], 'prod_name': row[1], 'use_by_date': row[2]} for row in rows]
    return products


def add_cust(cust_id,cust_name,ph_no,email,prod_id):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Customers (Customer Id,customer name,Phone number,Email,Product Id) VALUES (?, ?, ?)", (cust_id,cust_name,ph_no,email,prod_id))
    connection.commit()

def add_prod(prod_id,prod_name,use_by_date):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Products (Product Id,Product Name,Use By Date) VALUES (?, ?, ?)", (prod_id,prod_name,use_by_date))
    connection.commit()

def delete_cust(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from customers where cust_id={id}")
    connection.commit()
def delete_prod(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from products where prod_id={id}")
    connection.commit()
def update_cust(cust_id,cust_name,ph_no,email,prod_id):
    cursor = connection.cursor()
    cursor.execute(f"update customers set prod_id='{prod_id}',customer Id='{cust_id}',Customer name='{cust_name}',Phone number='{ph_no},Email='{email}' where Product Id={prod_id}")
    connection.commit()    
def update_prod(prod_id,prod_name,use_by_date):
    cursor = connection.cursor()
    cursor.execute(f"update products set Product Id='{prod_id}',Product Name='{prod_name}',Use By Date='{use_by_date}' where Product Id={prod_id}")
    connection.commit()
def search_prod(title):
    cursor = connection.cursor()
    cursor.execute(f"SELECT customers.cust_id, customers.cust_name,customers.ph_no, customers.email,products.prod_id,customers.pid FROM products JOIN customers ON products.prod_id = customers.pid WHERE products.prod_id= '{'prod_id'}'")
    connection.commit()
    results = cursor.fetchall()
    return results