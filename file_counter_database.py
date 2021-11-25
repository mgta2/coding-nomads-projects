# File Counter Database Project

import pathlib
import os
import sqlalchemy
import datetime

password = os.environ["DATABASEPASSWORD"]
my_url = f"mysql+pymysql://root:{password}@localhost/filecounterdb"

x = datetime.datetime.now()
time_str = f"{x.year}-{x.month}-{x.day}-{x.hour}-{x.minute}-{x.second}"

engine = sqlalchemy.create_engine(my_url)
connection = engine.connect()
metadata = sqlalchemy.MetaData()

desktop = pathlib.Path("/mnt/c/Users/Matthew/Desktop")

# Create dictionary to see frequency of each file type.

file_types = ["", ".pdf", ".docx", ".txt", ".png"]

my_dict = {"": 0, ".pdf": 0, ".docx": 0, ".txt": 0, ".png": 0}
for filepath in desktop.iterdir():
    suf = filepath.suffix
    if suf in file_types:
        if suf in my_dict.keys():
            my_dict[suf] += 1
        else:
            my_dict[suf] = 1

new_dict = {}
for key, value in my_dict.items():
    if key == "":
        new_dict['folder'] = my_dict[""]
    else:
        new_dict[key] = my_dict[key]

# Add to database.

table = sqlalchemy.Table('filecounterdb', metadata, autoload=True, autoload_with=engine)
query = sqlalchemy.insert(table).values(folder=new_dict['folder'], pdf=new_dict['.pdf'], docx=new_dict['.docx'], txt=new_dict['.txt'], png=new_dict['.png'], datetime=time_str)
result = connection.execute(query)