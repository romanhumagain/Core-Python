import mysql.connector
import os # for environment variable management

def create_database(db_name, host, user, password):
  try:
    # Establish a connection 
    connection = mysql.connector.connect(
      host = host,
      user = user,
      password = password
    )
    # Create a cursor object to execute sql query
    cursor = connection.cursor()
    
    # query to create a db 
    CREATE_DB_QUERY = f"CREATE DATABASE {db_name}"
    
    # To execute a sql query
    cursor.execute(CREATE_DB_QUERY)
    
    print(f"Database: {db_name} created succesfully !!")
    return True
    
  except mysql.connector.Error as error:
    if error.errno == mysql.connector.errorcode.ER_DB_CREATE_EXISTS:
      print(f"Database '{db_name}' already exists.")
    else:
      print(f"Something went wrong {error}:")
    return False
    
  finally:
    cursor.close()
    connection.close()
    
# CREATING A MAIN METHOD TO CALL THE ABOVE FUNCTION
if __name__== "__main__":
  HOST = os.environ.get('DB_HOST', 'localhost')
  PASSWORD = os.environ.get('DB_PASSWORD', "")
  USER = os.environ.get("DB_USER", "root")
  DB_NAME = "python_db"
  
  create_database(DB_NAME, HOST, USER, PASSWORD)