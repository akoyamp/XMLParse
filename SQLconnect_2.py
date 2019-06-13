import sqlite3
global con
global cc

con = sqlite3.connect('DataFinal.db')
cc = con.cursor()


def connectandcreate():
    con = sqlite3.connect('DataFinal.db')
    cc = con.cursor()
    cc.execute(
        "CREATE TABLE IF NOT EXISTS processInfo (id INTEGER PRIMARY KEY, primkey TEXT, indicatorkey TEXT, key VARCHAR, "
        "name TEXT, functionalunit VARCHAR, location TEXT, parentclass TEXT, childclass TEXT, subclass TEXT,"
        " refYear INTEGER, validYear INTEGER, description TEXT)")
    con.commit()
    con.close()

def createexchangetable(key):
    con = sqlite3.connect('DataFinal.db')
    cc = con.cursor()
    cc.execute("CREATE TABLE IF NOT EXISTS "+key+" (id INTEGER PRIMARY KEY, indicator_id TEXT, exchange_name TEXT,"
                                                 " exchange_direction TEXT, A1 FLOAT, A2 FLOAT, A3 FLOAT,"
                                                 " A4 FLOAT, A5 FLOAT,"
                                                 " A1A3 FLOAT,  B1 FLOAT, B2 FLOAT, B3 FLOAT, B4 FLOAT, "
                                                 "B5 FLOAT, B6 FLOAT, B7 FLOAT, C FLOAT, C1 FLOAT, C2 FLOAT,"
                                                 " C3 FLOAT, C4 FLOAT,"
                                                 " D FLOAT, exchange_unit TEXT)")
    con.commit()
    con.close()



def inputexchangetable(key, indikey, exchangename,exdirection,dict,exunit):
    global A1 , A2 , A3 , A4 , A5 , A13 ,  B1 , B2 , B3 , B4 , B5 , B6 , B7 , C , C1 , C2 , C3 , C4 ,D
    A1, A2, A3, A4, A5, A13, B1, B2, B3, B4, B5, B6, B7, C, C1, C2, C3, C4, D = '','','','','','','','','','','','','','','','','','',''
    positions = list(dict.keys())
    # print(dict)
    for i in range(len(positions)):
        clé = positions[i]
        if clé == 'A1':
            if dict[clé] != None:
                A1 = dict[clé]
        if clé == 'A2':
            if dict[clé] != None:
                A2 = dict[clé]
        if clé == 'A3':
            if dict[clé] != None:
                A3 = dict[clé]
        if clé == 'A4':
            if dict[clé] != None:
                A4 = dict[clé]
        if clé == 'A5':
            if dict[clé] != None:
                A5 = dict[clé]
        if clé == 'A1-A3':
            if dict[clé] != None:
                A13 = dict[clé]
        if clé == 'B1':
            if dict[clé] != None:
                B1 = dict[clé]
        if clé == 'B2':
            if dict[clé] != None:
                B2 = dict[clé]
        if clé == 'B3':
            if dict[clé] != None:
                B3 = dict[clé]
        if clé == 'B4':
            if dict[clé] != None:
                B4 = dict[clé]
        if clé == 'B5':
            if dict[clé] != None:
                B5 = dict[clé]
        if clé == 'B6':
            if dict[clé] != None:
                B6 = dict[clé]
        if clé == 'B7':
            if dict[clé] != None:
                B7 = dict[clé]
        if clé == 'C':
            if dict[clé] != None:
                C = dict[clé]
        if clé == 'C1':
            if dict[clé] != None:
                C1 = dict[clé]
        if clé == 'C2':
            if dict[clé] != None:
                C2 = dict[clé]
        if clé == 'C3':
            if dict[clé] != None:
                C3 = dict[clé]
        if clé == 'C4':
            if dict[clé] != None:
                C4 = dict[clé]
        if clé == 'D':
            if dict[clé] != None:
                D = dict[clé]


    con = sqlite3.connect('DataFinal.db')
    cc = con.cursor()
    cc.execute('INSERT INTO '+key+' VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?'
                                  ',?,?,?,?,?,?,?,?,?,?)', (indikey, exchangename, exdirection, A1 , A2 , A3 , A4 , A5 , A13 ,  B1 , B2 , B3 , B4 , B5 , B6 , B7 , C , C1 , C2 , C3 , C4 ,D , exunit))

    con.commit()
    con.close()

def createindicatortable(indikey):
    con = sqlite3.connect('DataFinal.db')
    cc = con.cursor()
    cc.execute("CREATE TABLE IF NOT EXISTS "+indikey+" (id INTEGER PRIMARY KEY,exchange_id TEXT, indicator_name TEXT,"
                                                     "  indicator_value FLOAT, indicator_unit TEXT)")
    con.commit()
    con.close()

def inputindicatortable(key, indikey, indicatortext,value,unit):
    con = sqlite3.connect('DataFinal.db')
    cc = con.cursor()
    cc.execute('INSERT INTO '+indikey+' VALUES (NULL,?,?,?,?)', (key,  indicatortext, value , unit))
    con.commit()
    con.close()



def createID(primkey, indikey, key, name,func,loc, parentclass, childclass, subclass, refYear, validYear, description):
    con = sqlite3.connect('DataFinal.db')
    cc = con.cursor()
    cc.execute('INSERT INTO processInfo VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?)', (primkey, indikey, key, name,func, loc, parentclass, childclass, subclass, refYear, validYear, description))
    con.commit()
    con.close()

def Read():
    conn = sqlite3.connect('DataFinal.db')
    cc = conn.cursor()
    cc.execute('SELECT * FROM processInfo')
    cc.execute('SELECT * FROM lciaInfo')
    rows = cc.fetchall()
    conn.commit()
    conn.close()
    return rows
