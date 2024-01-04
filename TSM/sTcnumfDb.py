import sqlite3 as sql3

def sTcnumfDb():
    selDb = str(input("Indique la base de datos a usar: "))
    if selDb[-3:] != ".db":
        selDb = selDb + ".db"
    tc_code = str(input("Escriba el código del ticket: "))
    db_con = sql3.connect(selDb)
    tc_code_query = db_con.execute(f"SELECT * FROM tickets WHERE tc_code='{tc_code}'")
    tc_codes = tc_code_query.fetchall()
    tc_data = []
    for datas in tc_codes:
        for data in datas:
            tc_data.append(data)

