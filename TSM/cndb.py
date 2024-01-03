def cndb():
    print("*-CREACIÓN DE BASE DE DATOS-*")
    db_name = str(input("Ingrese el nombre de la BD: "))
    if db_name[-3:] != ".db":
        db_name = db_name + ".db"
    use_query = str(input("Desea usar un archivo SQL para crear las tablas? s/n: "))
    if use_query != 's':
        db_con = sql3.connect(db_name)
        db_con.close()
    else:
        is_active = True
        while is_active:
            filepath = str(input("Escriba la dirección exacta del archivo: "))
            with os.scandir(filepath) as fp:
                fp = [file.name for file in fp if file.is_file()
                    and file.name.endswith('.sql')]
            print("Archivos SQL disponibles:")
            for i in range(0, len(fp)):
                print([i], "--", fp[i])
            sel_file = int(input("\nSegún el número,\nelija el archivo a ejecutar: "))
            with open(filepath + fp[sel_file]) as sql_file:
                db_con = sql3.connect(db_name)
                try:
                    db_con.execute(sql_file.read())
                    print("Base de datos y tabla creada")
                except sql3.OperationalError:
                    print("Ya existe esta tabla")
            eos = str(input("Desea crear otra tabla? s/n: "))
            if eos != 's':
                is_active = False
            else:
                pass
