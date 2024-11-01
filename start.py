#open a terminal and write:

#sudo apt-get update
#sudo apt-get install sense-hat
#pip install azure-iot-device
#pip install requests
#sudo reboot

#För att kunna starta RPI utan skärm inkopplad:
#öppna en terminal och skriv :
#sudo nano /boot/config.txt
#Gå ner till du ser:
#hdmi_force_hotplug=1
#ta bort # för att aktivera den raden



# !!!!!! Om man ska starta scriptet via systemctl, se till att denna app är stängd. 
#och att inte .py filerna är öppna i något program, annars kan inte systemctl 
# komma åt filerna och man får EOF exception i loggarna!!!!!!


#För att få Bound att starta när datorn startas gör detta:
#1. öppna en terminal och skriv: (INGET sudo)
#- mkdir /home/pi/.config/autostart
#- nano /home/pi/.config/autostart/clock.desktop

# i filen skriv:
## [Desktop Entry]
## Type=Application
## Name=Clock
## Exec=/usr/bin/python3 /home/pi/Desktop/BoundDevicePySplit/start.py


#Se till att start.py ligger i rätt katalog
#starta om datorn för att kolla ifall det funkar





#Aktuellt:

#Ifall det ligger flera meddelanden som tex "restartDevice", "online" osv kommer de att köras tills alla meddelanden är borta

import os
from sense_hat import SenseHat
from azure.iot.device import IoTHubDeviceClient, exceptions, Message
import random
import utils
import iothubManager
import tkinter as tk
import threading

class UserData:
    delaytime = 20
    reps = 0
    moving = True
    deviceSensitivity = 0
    sense = SenseHat()
    conn_str = ""
    startExcersice = False
    startCheckingForDeviceMovements = False
    totalPause=0
    weight = 0
    hasLoggedInOnDevice = False
    pauseSinceLastRep = 0
    currentMethod=None
    email = ""
    firstname= "sdfsdf"
    lastname= "sdfsdf"
    machinename = ""
    status = ""
    totalReps = 0
    isLoopRunning = False
    isFirstTimeStarted=True
    exception=""
    isDebug=True
    totalSecUntilRestartExcersise = 0
    data=None

if __name__ == "__main__":     
    
    try:
        utils.checkConnectionToBoundHub()
    except Exception as e:
        utils.setRedDot()
        print("No internet connection...")
        
        utils.logToFile(str(e))
        utils.restart_device()
    
    BoundUI=tk.Tk()
    conn_str = open("/home/pi/Desktop/BoundDevicePySplit/connectionstring","r").readline()
    try:
        utils.setGreenDot()
        utils.sendDebugTextToTablet("[Main] Starting up device")
        BoundUI.title("Bound Device")
        print("[Main] Device started")
        iothubManager.Program.setup(conn_str)
        BoundUI.mainloop()
        input("Press Enter to exit...")

    except Exception as e:
        utils.setRedDot()
        exception = str(e)
        utils.logToFile(exception)
        utils.restart_device()
