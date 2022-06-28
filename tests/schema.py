
"""
Use this file as hack to get around SQLite only accepting one command at a time.

- Create an appropriately named function
- Create SQL as normal
- Paste SQL 1 per function in between multi line comments
- Add function to import function in init_db.py and join to remove tuple

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
      name VARCHAR NOT NULL,
      user_group INTEGER NOT NULL
    );
    """
    return (table,)


def sql_create_table_menus():
    table = """
    CREATE TABLE IF NOT EXISTS menus (
      id INTEGER NOT NULL,
      text VARCHAR NOT NULL,
      link VARCHAR NOT NULL,
      FOREIGN KEY(id) REFERENCES users(user_group)
    );
    """
    return (table,)
