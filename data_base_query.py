import mysql.connector
import csv
import config


db_name = "flights"

def download_data(min_lat, max_lat, min_lon, max_lon):
    
    myconn = mysql.connector.connect(host=config.your_host,
                                     user=config.user_ID,
                                     password=config.passwd,
                                     database= db_name)
    cursor = myconn.cursor()
    
    select_data_query = """
    SELECT city, country, iata, latitude, longitude FROM airports
    WHERE latitude BETWEEN %s AND %s AND
    longitude BETWEEN %s AND %s""" 
    
    cursor.execute(select_data_query, (min_lat, max_lat, min_lon, max_lon))
    
    data = cursor.fetchall()

    with open("out.csv", "w", newline='', encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(data)

    cursor.close()    
    
def show_data(min_lat, max_lat, min_lon, max_lon):
    
    myconn = mysql.connector.connect(host=config.your_host,
                                     user=config.user_ID,
                                     password=config.passwd,
                                     database= db_name)
    cursor = myconn.cursor()
    
    select_data_query = """
    SELECT city, country, iata, latitude, longitude FROM airports
    WHERE latitude BETWEEN %s AND %s AND
    longitude BETWEEN %s AND %s""" 
    
    cursor.execute(select_data_query, (min_lat, max_lat, min_lon, max_lon))
    
    data_lst = []
    for (city, country, iata, latitude, longitude) in cursor:
      data_lst.append((city, country, iata, latitude, longitude))
    
    cursor.close()    
    return data_lst

def get_city(city):
    
    myconn = mysql.connector.connect(host=config.your_host,
                                     user=config.user_ID,
                                     password=config.passwd,
                                     database= db_name)
    cursor = myconn.cursor()
    
    select_data_query = """
    SELECT city, country, iata, latitude, longitude FROM airports
    WHERE city=%s""" 
    
    cursor.execute(select_data_query, (city,))
    
    city_lst = []
    for (city, country, iata, latitude, longitude) in cursor:
      city_lst.append((city, country, iata, latitude, longitude))
    
    #print(city_lst)
    
    cursor.close()    
    return city_lst
    
#city="Boston"  
#load = get_city(city)  
