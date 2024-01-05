import sqlite3 as sql3

def stfDb(db_name):
    db_con = sql3.connect(db_name)
    techs_query = db_con.execute("SELECT * FROM technician")
    t_datas = techs_query.fetchall()
    print("Técnicos disponibles:")
    for datas in t_datas:
        for data in datas:
            if data == datas[-1]:
                print(data)
            else:
                print(data, end=', ')
    sel_tech = int(input("\nSegún el ID, elija al técnico: "))
    tech = db_con.execute(f"SELECT t_name, t_phone, t_email FROM technician WHERE t_sys_id={sel_tech}")
    tech_info = tech.fetchall()
    for info in tech_info:
        t_info = info
    
    return t_info
