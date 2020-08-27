import pyodbc

def read(conn):
    print("Read")
    cursor= conn.cursor()
    cursor.execute("select * from DUMMY")
    for row in cursor:
        print(f'row = {row}')
    print()
# def create(conn):
#     print("Create")
#     cursor = conn.cursor()
#     cursor.execute(
#         'insert into '
#     )
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-SQGOGNA;"
    "Database=Test;"
    "Trusted_Connection=yes;"
)

read(conn)
# create(conn)
# update(conn)
# delete(conn)

conn.close()