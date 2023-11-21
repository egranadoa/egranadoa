import sqlite3 as SQL

db_name = str(input("Ingrese el nombre de la base de datos: "))#Nombre de la Base de Datos

db_con = SQL.connect(db_name)#Creación o Conexión a una Base de Datos nombrada de SQLite

sel_opt1 = int(input('''
Indique la opción de la tarea a realizar:
(1) para consultar las tablas de la base de datos
(2) para consultar las columnas de una tabla existente
(3) para consultar las filas de una tabla existente
(4) para insertar una fila en una tabla existente
(5) para actualizar una fila en una tabla existente
(6) para eliminar una fila en una tabla existente
(7) para hacer Query manualmente
Opción: ''')) #Entrada numérica entera como selector de opciones

if sel_opt1 == 1: #Proceso de la selección 1
    db_tables = db_con.execute("SELECT name FROM sqlite_master") #Query para elegir la tabla a consultar
    print("Tablas de la base de datos:")
    tableNames = db_tables.fetchall() #Extracción de Datos de la tabla elegida
    for i in range(0, len(tableNames)):
        print(i, "--", tableNames[i]) #Muestreo de cada tabla dentro de la Base de Datos
    db_con.close()
        
elif sel_opt1 == 2: #Proceso de la selección 2
    db_tables = db_con.execute("SELECT name FROM sqlite_master") #Query para elegir la tabla a consultar
    print("Tablas de la base de datos:")
    tableNames = db_tables.fetchall() #Extracción de Datos de la tabla elegida
    for i in range(0, len(tableNames)): 
        print(i, "--", tableNames[i]) #Muestreo de cada tabla dentro de la Base de Datos
    
    sel_table = int(input("Según el número de tabla,\nelija la que desea saber sus columnas: ")) #Selector de tabla para mostrar sus columnas
    if tableNames[sel_table] in tableNames: #Condición para validar la existencia de la tabla
        for t in tableNames[sel_table]: #Ciclo de verificación de los datos de la tabla
            if t is not None:
                table_con = t #Extracción del nombre de la tabla de la tupla hacia una variable
        db_table_cols = db_con.execute(f"SELECT name FROM pragma_table_info('{table_con}')") #Query para consultar las columnas de la tabla
    print(db_table_cols.fetchall()) #Muestreo de las columnas extraidas
    db_con.close()

elif sel_opt1 == 3: #Proceso de la selección 3
    db_tables = db_con.execute("SELECT name FROM sqlite_master")
    print("Tablas de la base de datos:")
    tableNames = db_tables.fetchall()
    for i in range(0, len(tableNames)):
        print(i, "--", tableNames[i]) #Muestreo de cada tabla dentro de la Base de Datos
    
    sel_table = int(input("Según el número de tabla,\nelija la que desea saber sus filas: "))
    if tableNames[sel_table] in tableNames:
        for t in tableNames[sel_table]:
            if t is not None:
                table_con = t #Extracción del nombre de la tabla de la tupla hacia una variable
        db_table_cols = db_con.execute(f"SELECT name FROM pragma_table_info('{table_con}')") 
        tableCols = db_table_cols.fetchall() #Extracción de las columnas de la tabla elegida
        db_table_rows = db_con.execute(f"SELECT * FROM {table_con}") #Query para consultar todas las filas de la tabla
        tableRows = db_table_rows.fetchall() #Extracción de las filas de la tabla elegida
    print(tableCols) #Muestreo del nombre de las columnas
    for row in tableRows:
        print(row) #Muestreo de cada fila de la tabla
    db_con.close()

elif sel_opt1 == 4:
    db_tables = db_con.execute("SELECT name FROM sqlite_master")
    print("Tablas de la base de datos:")
    tableNames = db_tables.fetchall()
    for i in range(0, len(tableNames)):
        print(i, "--", tableNames[i]) #Muestreo de cada tabla dentro de la Base de Datos
        
    sel_table = int(input("Según el número de tabla,\nelija la que desea trabajar: "))
    if tableNames[sel_table] in tableNames:
        for t in tableNames[sel_table]:
            if t is not None:
                table_con = t #Extracción del nombre de la tabla de la tupla hacia una variable
        db_table_cols = db_con.execute(f"SELECT name FROM pragma_table_info('{table_con}')") 
        tableCols = db_table_cols.fetchall() #Extracción de las columnas de la tabla elegida
        db_table_rows = db_con.execute(f"SELECT * FROM {table_con}") #Query para consultar todas las filas de la tabla
        tableRows = db_table_rows.fetchall() #Extracción de las filas de la tabla elegida
    print(tableCols) #Muestreo del nombre de las columnas
    ColNums = 0
    for i in range(0, len(tableCols)):
        ColNums += 1
    print("Número de columnas reales de la tabla:", ColNums)
    for row in tableRows:
        print(row) #Muestreo de cada fila de la tabla
    
    print("Escriba los datos a insertar:")
    EntriesL = [] #Lista para Entradas a Registrar
    ColEntries = [] #Lista para Columnas a evaluar
    
    for i in range(1, ColNums):
        if tableCols[i] in tableCols:
            for j in tableCols[i]:
                if j is not None:
                    table_col = j #Extracción del nombre de la tabla de la tupla hacia una lista de columnas
            ColEntries.append(j)
            insert_data = input(f"Dato a ingresar en la columna {table_col}: ")
            EntriesL.append(insert_data)
    ColEntriesT = tuple(ColEntries) #Conversión de listas a tuplas para el Query de inserción
    EntriesT = tuple(EntriesL)
    db_new_data = db_con.execute(f"INSERT INTO {table_con}{ColEntriesT} VALUES{EntriesT}")
    db_con.commit()
    print("REGISTRO REALIZADO CON ÉXITO")
    db_con.close()

elif sel_opt1 == 5:
    db_tables = db_con.execute("SELECT name FROM sqlite_master")
    print("Tablas de la base de datos:")
    tableNames = db_tables.fetchall()
    for i in range(0, len(tableNames)):
        print(i, "--", tableNames[i]) #Muestreo de cada tabla dentro de la Base de Datos
        
    sel_table = int(input("Según el número de tabla,\nelija la que desea trabajar: "))
    if tableNames[sel_table] in tableNames:
        for t in tableNames[sel_table]:
            if t is not None:
                table_con = t #Extracción del nombre de la tabla de la tupla hacia una variable
        db_table_cols = db_con.execute(f"SELECT name FROM pragma_table_info('{table_con}')") 
        tableCols = db_table_cols.fetchall() #Extracción de las columnas de la tabla elegida
        db_table_rows = db_con.execute(f"SELECT * FROM {table_con}") #Query para consultar todas las filas de la tabla
        tableRows = db_table_rows.fetchall() #Extracción de las filas de la tabla elegida
    print("\nAtributos de la tabla:")
    print(tableCols) #Muestreo del nombre de las columnas
    print("\nFilas actuales de la tabla:")
    for row in tableRows:
        print(row) #Muestreo de cada fila de la tabla
    
    for i in range(0, len(tableCols)):
        print(i, "--", tableCols[i]) #Muestreo de cada tabla dentro de la Base de Datos
    sel_col = int(input("\nSegún el número de columna,\nelija la que desea actualizar: "))
    for i in range(0, len(tableRows)):
        print(i, "--", tableRows[i]) #Muestreo de cada tabla dentro de la Base de Datos
    sel_row = int(input("\nSegún el número de fila,\nelija la que desea actualizar: "))
    ToUpdateData = input("Ingrese el valor nuevo: ")
    if tableCols[sel_col] in tableCols:
        for col in tableCols[sel_col]:
            if col is not None:
                col_con = col #Extracción del nombre de la columna de la tupla hacia una variable
    for col in tableCols[0]:
        if col is not None:
            KeyCol = col
    RowData = []
    if tableRows[sel_row] in tableRows:
        for row in tableRows[sel_row]:
            if row is not None:
                row_con = row #Extracción del nombre de la fila de la tupla hacia una variable
                RowData.append(row)

    if type(ToUpdateData) == str:
        db_uptade_data = db_con.execute(f"UPDATE {table_con} SET {col_con}='{ToUpdateData}' WHERE {KeyCol}={RowData[0]}")
    elif type(ToUpdateData) == int or type(ToUpdateData) == float:
        db_uptade_data = db_con.execute(f"UPDATE {table_con} SET {col_con}={ToUpdateData} WHERE {KeyCol}={RowData[0]}")
    db_con.commit()
    print("REGISTRO ACTUALIZADO CON ÉXITO")
    db_con.close()
    
elif sel_opt1 == 6:
    db_tables = db_con.execute("SELECT name FROM sqlite_master")
    print("Tablas de la base de datos:")
    tableNames = db_tables.fetchall()
    for i in range(0, len(tableNames)):
        print(i, "--", tableNames[i]) #Muestreo de cada tabla dentro de la Base de Datos
        
    sel_table = int(input("Según el número de tabla,\nelija la que desea trabajar: "))
    if tableNames[sel_table] in tableNames:
        for t in tableNames[sel_table]:
            if t is not None:
                table_con = t #Extracción del nombre de la tabla de la tupla hacia una variable
        db_table_cols = db_con.execute(f"SELECT name FROM pragma_table_info('{table_con}')") 
        tableCols = db_table_cols.fetchall() #Extracción de las columnas de la tabla elegida
        db_table_rows = db_con.execute(f"SELECT * FROM {table_con}") #Query para consultar todas las filas de la tabla
        tableRows = db_table_rows.fetchall() #Extracción de las filas de la tabla elegida
    print("\nAtributos de la tabla:")
    print(tableCols) #Muestreo del nombre de las columnas
    print("\nFilas actuales de la tabla:")
    for row in tableRows:
        print(row) #Muestreo de cada fila de la tabla
    
    for i in range(0, len(tableRows)):
        print(i, "--", tableRows[i]) #Muestreo de cada tabla dentro de la Base de Datos
    sel_row = int(input("\nSegún el número de fila,\nelija la que desea eliminar: "))
    for col in tableCols[0]:
        if col is not None:
            KeyCol = col
    RowData = []
    if tableRows[sel_row] in tableRows:
        for row in tableRows[sel_row]:
            if row is not None:
                row_con = row #Extracción del nombre de la fila de la tupla hacia una variable
                RowData.append(row)
    db_delete_data = db_con.execute(f"DELETE FROM {table_con} WHERE {KeyCol}={RowData[0]}")
    db_con.commit()
    print("REGISTROS ELIMINADOS CON EXITO")
    db_con.close()
    
elif sel_opt1 == 7:
    SQL_CMD_DICT = ["INSERT", "UPDATE", "DELETE", 
                    "insert", "update", "delete"]
    query_entry = str(input("Escriba el Query: "))
    for CMDS in SQL_CMD_DICT:
        if SQL_CMD_DICT[CMDS] in query_entry:

            db_result = db_con.execute(query_entry)
            result = db_result.fetchall()
    print("Query Ejecutado")
    if result is not None:
        print("Resultado:")
        print(result)
    db_con.close