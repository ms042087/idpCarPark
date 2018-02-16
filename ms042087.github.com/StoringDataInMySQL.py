import serial
import time
import datetime
import MySQLdb

ser=serial.Serial("/dev/ttyUSB0",9600)
ser.baudrate=9600

db = MySQLdb.connect(host="localhost", user="root", passwd="ms084092", db="sensorData")
cur = db.cursor()

while True:
    line = ser.readline().strip();
    values = line.decode('ascii').split(',')
    temperature, humidity = [int(s) for s in values]

    print("temperature = ",float(temperature),"\nhumidity = ",float(humidity),"\n")
    currentDateTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
   
    sql = "INSERT INTO sensorData.TempHumid (DateTime, Temperature, Humidity) VALUES (%s, %s, %s)"
    data = (currentDateTime, temperature, humidity)
    cur.execute(sql,(data))
    db.commit()
    print("committed")
    time.sleep(5)
    
db.close()
print('end')
    

