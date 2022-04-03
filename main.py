#Python code for connecting Arduino to Python

# Here, the arduino port "/dev/cu.usbmodem14401" is connected to Python
arduino = serial.Serial('/dev/cu.usbmodem14401', 9600)
# once this was sucessful, this is printed to the serial board. 
print('Established serial connection to Arduino')

def main_func():
    # reading one line from the Arduino
    arduino_data = arduino.readline()
    print(arduino_data)
    
    # decoding the line sent from arduino
    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    # splitting the line into different numbers every time there is a "x"
    list_values = decoded_values.split('x')

    # append all integers to the list_in_int list
    for item in list_values:
        list_in_int.append(int(item))

    # printing values
    print(f'Collected readings from Arduino: {list_in_int}')

    # clearing both lists
    arduino_data = 0
    list_in_int.clear()
    list_values.clear()
    print('Connection closed')
    print('<----------------------------->')

# Here the raw data is stored (with x's in between code)
list_values = []
# Here the processed data is stored. This list is wiped every time the main_function is run.
list_in_floats = []

print('Program started')

# Data is uploaded from the Arduino every "1" seconds - main_func is run
schedule.every(1).seconds.do(main_func)

# runs the main_funcion repeatedly
while True:
    schedule.run_pending()
    time.sleep(1)
