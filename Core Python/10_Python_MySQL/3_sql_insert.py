import mysql.connector
import os 

def create_table(db_name,tb_name, host, user, password):
  try: 
    # Establish a connection
    connection = mysql.connector.connect(
      database = db_name,
      host = host,
      user = user,
      password = password
    )
    # Create a cursor object to execute a sql query
    cursor = connection.cursor()
    
    insert_into_table_query = f"""INSERT INTO `{tb_name}`(
      `name`, `address`, `email`, `phone`)
      VALUES('Roman Humagain', 'Bhaktapur', 'roman@gmail.com', '9832124522')
      """
      # To execute a query
    cursor.execute(insert_into_table_query)
    
    # To commit the changes
    connection.commit()
    
    print("Successfully inserted data !!")
    return True
  
  except Exception as error:
    print(f"Something went wrong : {error}")
    return False
  
  finally:
    cursor.close()
    connection.close()
    
if __name__ =="__main__":
  TB_NAME = 'students_tb'
  DB_NAME = "python_db"
  
  HOST = os.environ.get('DB_HOST', 'localhost')
  USER = os.environ.get("DB_USER", "root")
  PASSWORD = os.environ.get('DB_PASSWORD', "")
  
  create_table(DB_NAME, TB_NAME, HOST, USER, PASSWORD)