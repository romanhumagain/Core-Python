import mysql.connector
import os 

def update_table(db_name, tb_name,updated_name,update_address, id, host, user, password):
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
    
    update_table_query = f"""UPDATE `{tb_name}` SET name = %s, address = %s WHERE std_id =  %s """
    values = (updated_name,update_address, id)
      # To execute a query
    cursor.execute(update_table_query, values)
    
    # Commit the update
    '''The connection.commit() method is used to save (commit) any changes made to the database that result from SQL statements that modify data. '''
    connection.commit()
    
    print("Successfully updated data !!")
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
  
  update_table(DB_NAME, TB_NAME,"Mr Roman Humagain","Banepa", 1,  HOST, USER, PASSWORD)