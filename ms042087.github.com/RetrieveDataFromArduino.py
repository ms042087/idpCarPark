import serial

ser=serial.Serial("/dev/ttyUSB2",9600)
ser.baudrate=9600

while True:
    line = ser.readline().strip();
    values = line.decode('ascii').split(',')
    temperature, humidity = [int(s) for s in values]

    print("temperature = ",float(temperature),"\nhumidity = ",float(humidity),"\n")
