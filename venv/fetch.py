from database import cursor, db

def fetch(**kwargs):
    for column_name, table_name in kwargs.items():
        c = "SELECT {} FROM {}".format(column_name, table_name)
        cursor.execute(c)
        lst = cursor.fetchall()
    #print(lst)
    time_doctor = 0
    for i in lst:
        le = int(''.join(map(str, i)))
        time_doctor = le
    #print(time_doctor)

    return time_doctor

lst = ['time0900','time1000','time1100','time1200','time1340','time1440','time1540','time1640', 'time1740']

table_n = 'terapeft'

#p = fetch(time0900='terapeft')
#print(type(p))



