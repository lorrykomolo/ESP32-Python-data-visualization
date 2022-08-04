import serial
import matplotlib.pyplot as plt
import numpy as np

# Initialize x axis
x_axis_start = 0
x_axis_end = 80

plt.axis([x_axis_start, x_axis_end, 0, 1])
plt.ion()
fig = plt.subplot()

i=0
x=list()
y=list()
i=0
ser = serial.Serial("/dev/ttyACM0",115200)
ser.close()
ser.open()

while True:
    data =ser.readline()
    print(data.decode())
    x.append(i)
    y.append(float(data.decode()))

    #plt.scatter(i, float(data.decode()), color='blue')
    plt.plot(x, y, color='red', linewidth=0.3)

    i+=1

    if i % 100 == 0 and i > 1:
        print("Axis should update now!")
        x_axis_start += 100
        x_axis_end += 100
        plt.axis([x_axis_start, x_axis_end, 0, 1])
    # Show the major grid lines with dark grey lines
    plt.grid(b=True, which='major', color='gray', linestyle='-', linewidth=0.5)

    # Show the minor grid lines with very faint and almost transparent grey lines
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    plt.pause(0.0001)
    plt.ylim(-1, 3)
    plt.grid(True)
    plt.suptitle('Electrocardiograph', fontsize=10)
    plt.xlabel("Length")
    plt.ylabel("spike")
    plt.box(True)

    plt.show()

