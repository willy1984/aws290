import pymysql

db_host = 'bdaws-290.cbm0w8aki8h0.us-east-1.rds.amazonaws.com'
db_user = 'wil'
db_password = 'Wilfaver1234'

try:
    connection = pymysql.connect(
        host = db_host,
        user = db_user,
        password = db_password
    )
except Exception as err:
    print("Error:", err)
    connection = None

def add_user(id, name, lastname, birthday):
    instruction_sql = "INSERT INTO db_users.users (id, name, lastname, birthday) VALUES ('"+id+"', '"+name+"', '"+lastname+"', '"+birthday+"')"
    try:
        cursor = connection.cursor()
        cursor.execute(instruction_sql)
        connection.commit()
        print("User added")
        #print(connection)
    except Exception as err:
        print("Error:", err)

add_user()