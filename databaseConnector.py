import psycopg2

hostname = 'csci233project.cxhulli2pmzg.us-east-1.rds.amazonaws.com'
username = 'postgres'
database = 'postgres'
pwd = 'school5432'
port_id = '5432'

try:
    connection = psycopg2.connect(host = hostname, 
                            dbname = database, 
                            user = username, 
                            password = pwd, 
                            port = port_id)
    cursor = connection.cursor()
    
    createUser = input("Enter New Username: ")
    createPassword = input("Enter Password: ")

    postgres_insert_query = """ INSERT INTO login (username, password) VALUES (%s,%s)"""
    record_to_insert = (createUser,createPassword)
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print(count, "Sucessfully Created an Account")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into mobile table", error)

print()

connection.close()