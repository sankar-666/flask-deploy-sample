import mysql.connector
host = "sql8.freesqldatabase.com"
user = "sql8723850"
password="rQxPuk1U1n"
database="sql8723850"
port = 3306
def select(q):
	cnx=mysql.connector.connect(user=user,password=password,host=host, database=database)
	cur=cnx.cursor(dictionary=True)
	cur.execute(q)
	result=cur.fetchall()
	cur.close()
	cnx.close()
	return result
def update(q):
	cnx=mysql.connector.connect(user=user,password=password,host=host, database=database)
	cur=cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result=cur.rowcount
	cur.close()
	cnx.close()
	return result
def delete(q):
	cnx=mysql.connector.connect(user=user,password=password,host=host, database=database)
	cur=cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result=cur.rowcount
	cur.close()
	cnx.close()
def insert(q):
	cnx=mysql.connector.connect(user=user,password=password,host=host, database=database)
	cur=cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result=cur.lastrowid
	cur.close()
	cnx.close()
	return result

	
