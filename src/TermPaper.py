# imoprting module for data crawling
# Collect Part
import crawling
from process import Process
import store

# Collect Part
# Storing Danningn URL address in url variable.
url = "https://www.daangn.com/region/%EC%A0%9C%EC%A3%BC%ED%8A%B9%EB%B3%84%EC%9E%90%EC%B9%98%EB%8F%84"

# Save the response html in a variable called req
# req=requests.get(url)

# # Parse the html saved in req and store it in a variable called soup
# soup=BeautifulSoup(req.content, 'html.parser')

# Collect data from a specific url using crawling module
soup = crawling.get_and_parse(url)

# Extract the card-title (Item Name)
# item_name = soup.find_all('h2', class_="card-title")

# Extract the card-region-name (Region Name)
# region_name = soup.find_all('div', class_="card-region-name")

# Extract the card-counts (Card Count)
# card_counts = soup.find_all('div', class_="card-counts")

# Process Part
# Making item column
# item_column = []
# for item in item_name:
#     item_column.append(item.text)

# Making region column
# region_list = []
# region_column = []
# for i, region in enumerate(region_name):
#     region_list.append(region.text.split('\n'))
#     # print(region_list[i][1])
#     region_column.append(region_list[i][1])
#     # print(split_list[i][2].replace(" ",""), split_list[i][6].replace(" ",""))
#     # print(split_list)

# # Making like and chat columns
# split_list = []
# like_column = []
# chat_column = []
# for i, count in enumerate(card_counts):
#     split_list.append(count.text.split("\n"))
#     like_column.append(split_list[i][2].replace(" ","")[-1])
#     chat_column.append(split_list[i][6].replace(" ","")[-1])
# # print(like_column)
# # print(chat_column)

pro = Process(soup)
item_column = pro.extract_item_name()
region_column = pro.extract_region_name()
like_column, chat_column = pro.extract_like_and_chat()


# # Save time Date
# import datetime as dt

# date = dt.datetime.now()
# # print(date.strftime("%Y %m %d %X"))

# # make date data by using strptime function
# date_data = str(date.strptime(date.strftime("%Y %m %d %X"), '%Y %m %d %X'))
# # print(date_data)

# # make a dataframe
# raw_data = {
#     'local_name' : region_column,
#     'item' : item_column,
#     'like' : like_column,
#     'chat' : chat_column
# }

# raw_data_df = pd.DataFrame(raw_data, columns=['local_name', 'item', 'like', 'chat'])
# raw_data_df['date'] = date_data
# # raw_data_df

# make a dataframe
raw_data_df = pro.make_dataframe()

# # set a path variable
# DATA_ROOT = os.path.join(settings.PROJ_ROOT, "data")

# # make a csv file
# raw_data_df.to_csv(f"{DATA_ROOT}/raw_data.csv")

# # Making a JSON file from DataFrame
# raw_data_df.to_json(f"{DATA_ROOT}/raw_data.json")

# get a file path
DATA_ROOT =  pro.get_project_path()

# save a csv file
raw_data_df.to_csv(f"{DATA_ROOT}/raw_data.csv")

# save a JSON file
raw_data_df.to_json(f"{DATA_ROOT}/raw_data.json")


# # Store Part - SQL

# # Now it is time for you to create a database! Here is how you would create a SQLite database with Python. First, you import sqlite3 and then you use the connect() function, which takes the path to the database file as an argument. If the file does not exist, the sqlite3 module will create an empty database. Once the database file has been created, you need to add a table to be able to work with it. The basic SQL command you use for doing this is as follows:

# # Import sqlite3 module into

# # Create a connection object,
# # Make a new db if not exist already 
# # and connect it, if exist then connect.
# connection = sqlite3.connect("daangn.db")

# # Create a new file named 
# cursor = connection.cursor()

# make a object of store module
sql = store.SQL()

# Create a connection object,
# Make a new db if not exist already 
# and connect it, if exist then connect.
# Create a new file named  
cursor = sql.get_cur_with_db("danagn.db")

# create a table
cursor.execute("CREATE TABLE IF NOT exists ALL_DATA" +
    "(local_name TEXT, Item TEXT, Like INTEGER, Chat INTEGER, Date TEXT)")

# Load CSV data into Pandas DataFrame and write the data to a sqlite db table
# raw_data_csv = pd.read_csv(f"{DATA_ROOT}/raw_data.csv")
# raw_data_csv.to_sql('ALL_DATA', connection, if_exists='replace', index=False)

# Load CSV data into Pandas DataFrame and write the data to a sqlite db table
sql.load_csv_and_create_table("ALL_DATA", f"{DATA_ROOT}/raw_data.csv")


# Store Part - NoSQL
# Make a object of elastic search
# es = Elasticsearch("http://localhost:9200")
host = "http://localhost:9200"
ES = store.Elastic(host)
es = ES.get_es()

# # Read a json file
# raw_data_json = pd.read_json(f"{DATA_ROOT}/raw_data.json")


# # Convert this json file to dictionary
# raw_data_json_copy = raw_data_json.copy()
# raw_data_json_index = raw_data_json_copy.to_dict('index')

# # make a index in Elasticsearch
# resp = es.index(index="daangn-index", id=1, document=raw_data_json_index)

document = ES.load_and_convert_json(f"{DATA_ROOT}/raw_data.json")
resp = es.index(index='daangn-index', id=1, document = document)

# Query Part - SQL

# Run select sql query

# # Fetch all records
# # as list of tuples
# records = cursor.fetchall()
 
# # Display result
# for row in records:
#     # show row
#     print(row)

cursor.execute('select * from ALL_DATA')
for row in cursor.fetchall():
    print(row)

# # Close connection to SQLite database
# connection.close()
sql.close()

# # Query Part - NoSQL
response = es.get(index='daangn-index', id=1)
print(response['_source'])