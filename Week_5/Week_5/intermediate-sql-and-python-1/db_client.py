import psycopg2

#########
# 1.0 Connect to the database
# it is good practice to not hardcode your credentials in your code, so we woul apply our I/O knowlwdge here
#  fill the secrets.txt file with youer credentials and watch them come in here with the values.

with open("secrets.txt") as f:
    secrets = f.readlines()
    # secrets = ['database=yourdbname','user=username']
    # x = ['metrobank',dinmaobi21, ]
    # split each line at the = symbol and get the item at index 1 also strip it of any white space
    secrets = [x.split("=")[1].strip() for x in secrets]


def connect_to_db():
    try:
        conn = psycopg2.connect(
            database=secrets[0],
            user=secrets[1],
            password=secrets[2],
            host= secrets[3], #"127.0.0.1" for localhost,
            port=secrets[4] #"5432" #"5432" for default postgres port
)

    except Exception as e:
        print(f"Error connecting to db -> {e}")
        raise e
    print("Successfully connected to db")
    return conn

if __name__ == "__main__":
            

    # Now let us create a cursor object using the cursor() method
    connection = connect_to_db()
    cursor = connection.cursor()

    #TODO:2.0 create a table in the db named regions
    cursor.execute("CREATE TABLE IF NOT EXISTS regions   (region_id int, region_name varchar(25));")
    # # commit the transaction (to save what you have just done to the db)
    connection.commit()
    print("Table created successfully in PostgreSQL")



    # #TODO: 3.0 Insert data into the table
    #cursor.execute("""INSERT INTO regions (region_id, region_name) 
    #               VALUES 
    #               (1, 'Europe'),
    #               (2,'Africa'),
    #               (3,'America');""")
    # # query the table on your db to see if the data has been inserted without commiting, what did you observe?

    # # TODO: Add a line to commit the transaction
#connection.commit()

    # #TODO: 4.0 Retreive data from the database.
        #cursor.execute("SELECT * FROM regions;")

        #raw_data = cursor.fetchall()  #what data type is returned?
        #print(raw_data)

    # #TODO: 5.0 delete a row from the database 
    # cursor.execute("DELETE FROM regions WHERE region_id = 1;")
    # connection.commit()
    # print("Row deleted successfully")

    # # validate your deletion
    # cursor.execute("SELECT * FROM regions;")
    # print(cursor.fetchall())