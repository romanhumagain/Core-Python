import mysql.connector
import os

def fetch_data(db_name, tb_name, host, user, password):
  try:
    # Establish a connection
    connection = mysql.connector.connect(
      host = host,
      user = user,
      password = password,
      database = db_name
    )
    # Creating a cursor object to execute a query
    cursor = connection.cursor()
    
    # Select query
    select_data = f"""SELECT * FROM `{tb_name}`"""
    
    # To execute a query
    cursor.execute(select_data)
    
    # To fetch the data
    results = cursor.fetchall()
    
    for result in results:
      print(result)
    
    
  except mysql.connector.Error as error:
    print(f"Something went wrong: {error}")
  finally:
    cursor.close()
    connection.close()
    
# Creating a main method to call the function
if __name__ == "__main__":
  TB_NAME = 'students_tb'
  DB_NAME = "python_db"
  
  HOST = os.environ.get('DB_HOST', 'localhost')
  USER = os.environ.get('DB_USER', 'root')
  PASSWORD = os.environ.get('DB_PASSWORD', '')
 
  fetch_data(DB_NAME, TB_NAME, HOST, USER, PASSWORD)
  
  