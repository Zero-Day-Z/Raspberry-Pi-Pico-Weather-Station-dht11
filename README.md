# Raspberry-Pi-Pico-Weather-Station-dht11
This is a weather station project built on Raspberry Pi Pico with LCD output. The weather station detects temperature and humidity. This is assuming you have a working interface for your raspberry pi pico. This specific tutorial mounts the Raspberry Pi Pico onto the Raspberry Pi and uses Thonny IDE to run micropython code. 
#Materials Needed
#Hardware
1. 1 soldered Raspberry Pi Pico
2. 1 Breadboard
3. 1 dht sensor
4. 1 LCD Display
5. 3 Male-to-Female cables (1 red, 1 yellow, 1 b;ue)
6. 4 Male-to-Female cables (1 red, 1 orange, 1 yellow, 1 black)
Note: the color of the cables do not matter, they just make things easier!

# Software
You will need the following software libraries:
1. esp8266.py
2. pico_12c_lcd.py
3. httpParser.py
4. dht.py
These can be downloaded from the github

# Hardware Connection Setup
1. Mount the soldered Raspberry Pi Pico to the breadboard
2. Connect the dht11 Sensor to the breadboard with the Raspberry Pi Pico using the 3 Male-to-Female cables to match the diagram below: 
![image](https://content.instructables.com/ORIG/FN2/9M5Y/KPEIZSXV/FN29M5YKPEIZSXV.png?auto=webp&frame=1&width=1024&fit=bounds&md=a12203dc41ac3ca5e6f93d8341ae31a0)

| Cable Color   | Unltrasonic Connection      | Pico Connection     |
| ------------- | -------------               | -------- |
| Red           | VCC (Power)                 | Slot 36  |
| Yellow        | Echo                        | Pin4 (GPIO28)  |
| Blue          | GND (ground)                | Pin 38  |


_Note: There are multiple GND connections on the Pico, you may connect to any one. _

If you need extra assistance, you can refer to the Raspberry Pi Pico connection output diagram

2. Connect the LCD Display to the breadboard with the mounted Raspberry Pi Pico using the 4 Male-to-Female cables to match the diagram below:

![image](https://user-images.githubusercontent.com/66813474/152418568-89ebe835-5397-4120-8fc0-d93c8a43a6a6.png)


| Cable Color   | Unltrasonic Connection      | Pico Connection     |
| ------------- | -------------               | -------- |
| Red           | VCC (Power)                 | VBUS (Pin 40)  |
| Orange        | SDA                        | UART 0 RX  - GP0 (Pin 1)  |
| Yellow        | SCL                        | UART 0 RX  - GP0 (Pin 2)  |
| Black         | GND (ground)                | Pin 38  |


_Note: There are multiple GND connections on the Pico, you may connect to any one_

If you need extra assistance, you can refer to the Raspberry Pi Pico connection output diagram

3. Plug in the Raspberry Pi Pico and turn on the Raspberry Pi if it is not turned on already. If the LCD does not light up, this likely means that your connections are wrong or not plugged in all the way. Unplug your Raspberry Pi Pico and check your connections to ensure they are correct. 

# Software Instructions
1. Open Thonny IDE and change to the Raspberry Pi Pico interpreter on the bottom right hand corner.
2. Click File > New > Raspberry Pi Pico. You should see a main directory and a folder called lib. The lib folder is where you will save all of your libraries. 
3. Import the software libraries

    1. Click File>New>Raspberry Pi Pico>lib to create a new file in the lib folder
    2. Download ‘pico_i2c_lcd.py’
    3. Open the file
    4. Copy the contents to the new file you just created
    5. Save the file
    6.  Make sure it is saved as pico_i2c_lcd.py in the Raspberry Pi Pico lib folder
    7.  Complete Steps i-vi using the dht.py, httpParser.py, and esp8266.py files
4. Import main file
    1. Create a new folder in the main directory of the Raspberry Pi Pico. Name it whatever you want.
    2. Create a new micropython file in the folder you just created. This is the main file that will run your program. You can name it whatever you want. Mine is named main.py
    3. Download and open main.py
    4. Open main.py
    5. Copy the contents to the micropython file you just created.
5. Manipulate main file:
    _This step may or may not be needed depending on where your connections on the board are._
    1. At the line that says _‘i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)’_ the SDA and SCL pins may need to be changed to match the GP numbers that they are connected to on the breadboard. Check to make sure they match and change if needed. 
    2. At the line that says _‘pin = Pin(15, Pin.OUT, Pin.PULL_DOWN)’_ the 15 needs to match the Pin used to collect data. In our case, the diagram above uses Pin 4, therefore, 15 in the above line needs to be changed to 4. 
6. Run the program. If all goes well, when you run the program everything should work fine. 

_Other Notes: If you cannot see the output on the LCD display, try turning the blue dial on the back to modify the transparency._ 

