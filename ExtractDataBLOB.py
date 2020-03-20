import cx_Oracle
import numpy

hostName = ''
porta = 1521
sidName = ''
userName = ''
passWord = ''
mesReferencia=8
anoReferencia=2013

dsn_tns = cx_Oracle.makedsn(hostName, porta, service_name=sidName)
con = cx_Oracle.connect(user=userName, password=passWord, dsn=dsn_tns)

cursor = con.cursor()
cursor.execute ('SELECT DADOS FROM <SCHEMA>.<TABLE> WHERE '
                'EXTRACT(MONTH FROM DAT_REFER) ='+str(mesReferencia)+'AND EXTRACT(YEAR FROM DAT_REFER) ='+str(anoReferencia))

rows = cursor.fetchall()

filename="C:\\Tiago\\ExtractBLOB\\blobTest_1500.xml"

for row in rows:
    print(row)
    blobdata=numpy.array(row[1].read())
    # cursor.close()

con.close()
f=open(filename, "wb")
binary_format = bytearray(blobdata)
f.write(binary_format)
f.close()