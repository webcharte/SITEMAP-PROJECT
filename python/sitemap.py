import mysql.connector

/** CONFIGURATION */
url = 'https://mydomain.com'
usr = "user12"
pwd = "12user"
dbn = "db"

cnx = mysql.connector.connect(user=usr, password=pwd, host='127.0.0.1', database=dbn)



cnx.close()