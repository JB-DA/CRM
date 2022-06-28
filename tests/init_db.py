
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
    execute_sql_cmd( db_connection, ''.join( schema.sql_create_table_menus() ))
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

    c.execute("INSERT INTO menus (id, text, link) VALUES (?, ?, ?)",
                ('1', 'home', '/')
                )

    c.execute("INSERT INTO menus (id, text, link) VALUES (?, ?, ?)",
                ('1', 'assets', '/assets')
                )

    c.execute("INSERT INTO menus (id, text, link) VALUES (?, ?, ?)",
                ('1', 'liabilities', '/liabilities')
                )

    c.execute("INSERT INTO menus (id, text, link) VALUES (?, ?, ?)",
                ('1', 'info', '/info')
                )

    db_connection.commit()
    db_connection.close()
except Exception as e:
    print( e )
    print( "Could not insert all values... aborting...")
finally:
    db_connection.close()


# def get_db_connection():
#     conn = sqlite3.connect('database.db')
#     conn.row_factory = sqlite3.Row
#     return conn
#
# conn = get_db_connection()
# user_list = conn.execute('SELECT * FROM users').fetchall()
# menu_list = conn.execute('SELECT * FROM menus').fetchall()
# conn.close()
