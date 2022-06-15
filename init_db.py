
import sqlite3
from sqlite3 import Error
import schema

db_file = "database.db"

def create_connection( db_file ):
    """ Create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    db_connection = None

    try:
        db_connection = sqlite3.connect( db_file )
        return db_connection
    except Error as e:
        print( e )
    return db_connection

def execute_sql_cmd( db_connection, command ):
    """ Run a sql command statement
    :param conn: Connection object
    :param execute_sql_cmd: run sql statement
    :return:
    """
    try:
        c = db_connection.cursor()
        c.execute( command )
    except Error as e:
        print( e )

db_connection = create_connection( db_file )

if db_connection is not None:
    execute_sql_cmd( db_connection, ''.join( schema.sql_create_table_users() ))
    execute_sql_cmd( db_connection, ''.join( schema.sql_create_table_groups() ))
    execute_sql_cmd( db_connection, ''.join( schema.sql_create_table_permissions() ))
else:
    print( "Error! cannot create the database connection." )
db_connection.close()

""" Database test loading, comment out for development."""

db_connection = create_connection( db_file )

c = db_connection.cursor()

try:
    c.execute("INSERT INTO users (name, user_group) VALUES (?, ?)",
                ('root', '0')
                )

    c.execute("INSERT INTO users (name, user_group) VALUES (?, ?)",
                ('Mooch', '1')
                )

    c.execute("INSERT INTO groups (id, name, permissions) VALUES (?, ?, ?)",
                ('0', 'admin', 'ALL')
                )

    c.execute("INSERT INTO groups (id, name, permissions) VALUES (?, ?, ?)",
                ('1', 'guest', 'zero')
                )

    # c.execute("INSERT INTO menus (name) VALUES (?)",
    #             ('crm_infogather')
    #             )
    #
    # c.execute("INSERT INTO menus (name) VALUES (?)",
    #             ('crm_settings')
    #             )
    #
    # c.execute("INSERT INTO menus (name) VALUES (?)",
    #             ('crm_general')
    #             )
    #
    # c.execute("INSERT INTO menus (name) VALUES (?)",
    #             ('crm_contact')
    #             )

    db_connection.commit()
    db_connection.close()
except Exception as e:
    print( e )
    print( "Could not insert all values... ...aborting...")
finally:
    db_connection.close()





def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db_connection()
user_list = conn.execute('SELECT * FROM users').fetchall()
group_list = conn.execute('SELECT * FROM groups').fetchall()
menu_list = conn.execute('SELECT * FROM menus').fetchall()
conn.close()

print("")
print(f"{'Date Created':<15} {'Time Created':<15} {'User ID':<10} {'Name':<10} {'Group ID':<10}")
print("=" * 64)

for user in user_list:
    print( f"{user['createdd']:<15} {user['createdt']:<15} {user['id']:<10} {user['name']:<10} {user['user_group']:<10}" )

for group in group_list:
    print( group['id'], group['name'], group['permissions'] )
