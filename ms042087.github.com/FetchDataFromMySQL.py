import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="ms084092", db="sensorData")
cur = db.cursor()

cur.execute("SELECT DateTime, Temperature, Humidity FROM sensorData.TempHumid")

print ("%s\t\t%s\t%s\t" %("DateTime","Temperature","Humidity"))

for row in cur.fetchall() :

      dateTime = str(row[0])
      temperature = str(row[1])
      humidity = str(row[2])

      print ("%s\t%s\t\t%s\t" %(dateTime,temperature,humidity))

cur.close()
db.close ()
