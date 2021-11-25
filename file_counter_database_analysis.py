# File Counter Database Analysis Project
"""
- Total number of files
- Total number of files of each type
- What day had most files
- Most common file type ever
"""

import os
import sqlalchemy

password = os.environ["DATABASEPASSWORD"]
my_url = f"mysql+pymysql://root:{password}@localhost/filecounterdb"

engine = sqlalchemy.create_engine(my_url)
connection = engine.connect()
metadata = sqlalchemy.MetaData()

table = sqlalchemy.Table('filecounterdb', metadata, autoload=True, autoload_with=engine)
analysis = sqlalchemy.Table('analysis', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.select([table])
result = connection.execute(query)

total = []
total_folder = []
total_pdf = []
total_docx = []
total_txt = []
total_png = []
for mapping in result:
    my_sum = int(mapping['folder'])+int(mapping['pdf'])+int(mapping['docx'])+int(mapping['txt'])+int(mapping['png'])
    total.append(my_sum)
    my_sum = int(mapping['folder'])
    total_folder.append(my_sum)
    my_sum = int(mapping['pdf'])
    total_pdf.append(my_sum)
    my_sum = int(mapping['docx'])
    total_docx.append(my_sum)
    my_sum = int(mapping['txt'])
    total_txt.append(my_sum)
    my_sum = int(mapping['png'])
    total_png.append(my_sum)

a = sum(total)
b = sum(total_folder)
c = sum(total_pdf)
d = sum(total_docx)
e = sum(total_txt)
f = sum(total_png)

# Most common file type ever

most_common = max(b,c,d,e,f)
if most_common == b:
    most_common = "folder"
elif most_common == c:
    most_common = "pdf"
elif most_common == d:
    most_common = "docx"
elif most_common == e:
    most_common = "txt"
else:
    most_common = "png"

# Find what day had most files

max_index = total.index(max(total))
max_query = sqlalchemy.select([table]).where(table.columns.id==max_index+1)
max_result = connection.execute(max_query).fetchall()

max_day = max_result[0]['datetime']

# Insert data found above into analysis table.

insert_query = sqlalchemy.insert(analysis).values(total=a, totalfolder=b, totalpdf=c, totaldocx=d, totaltxt=e, totalpng=f, maxday=max_day, common=most_common)
insert_result = connection.execute(insert_query)