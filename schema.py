
"""
Use this file as hack to get around SQLite only accepting one command at a time.
Call the functions in this file from another, and the return will get inserted into a database.

- Create SQL tables as normal
- Create an appropriately named function in this file
- Paste one (1) SQL table per function in between multi line comments
- Return SQL table definition as tuple
- Add function to import function inside init_db.py and join to remove tuple

return: SQL create command string as a tuple

# In this file
def example_table():
    table = '''
    CREATE TABLE table_name (
      id INTEGER,
      name VARCHAR
    );
    '''
    return (table,)

# In init_db.py
''.join( schema.example_table() )
"""

def sql_create_table_users():
    table = """
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      createdd TIMESTAMP NOT NULL DEFAULT CURRENT_DATE,
      createdt TIMESTAMP NOT NULL DEFAULT CURRENT_TIME,
      name VARCHAR NOT NULL,
      user_group INTEGER NOT NULL
    );
    """
    return (table,)


def sql_create_table_groups():
    table = """
    CREATE TABLE IF NOT EXISTS groups (
      id INTEGER NOT NULL,
      name VARCHAR NOT NULL,
      permissions VARCHAR NOT NULL,
      FOREIGN KEY(id) REFERENCES users(user_group)
    );
    """
    return (table,)


def sql_create_table_permissions():
    table = """
    CREATE TABLE IF NOT EXISTS menus (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name VARCHAR NOT NULL
    );
    """
    return (table,)
