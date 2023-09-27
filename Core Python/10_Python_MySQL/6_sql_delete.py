import mysql.connector
import os 

def delete_data(db_name, tb_name,id, host, user, password):
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
    
    delete_data_query = f"""DELETE FROM `{tb_name}` WHERE std_id =  %s """
    values = (id,)
      # To execute a query
    cursor.execute(delete_data_query, values)
    
    # Commit the update
    '''The connection.commit() method is used to save (commit) any changes made to the database that result from SQL statements that modify data. '''
    connection.commit()
    
    print(f"Successfully deleted data from table whose id is {id} !!")
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
  
  delete_data(DB_NAME, TB_NAME,1,  HOST, USER, PASSWORD)