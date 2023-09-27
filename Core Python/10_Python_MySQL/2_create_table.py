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
    
    create_table_query = f"""CREATE TABLE IF NOT EXISTS `{tb_name}`(
      std_id INT PRIMARY KEY AUTO_INCREMENT,
      name varchar(50),
      address varchar(50),
      email varchar(100),
      phone varchar(20)
      ) """
      
      # To execute a query
    cursor.execute(create_table_query)
    print(f"Table: {tb_name} created successfully !!")
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