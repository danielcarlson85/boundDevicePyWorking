open a terminal and write:

i windows:
install Raspberry PI OS from Rasperry pi imager
 på RPI 3 - välj RPI 3 32 bit os

https://www.raspberrypi.com/software/

Kopiera över boundDevicePyWorking katalogen till boot enheten som finns i utforskaren:

På RPI:

- i /boot/firmware finns boundDevicePyWorking
- kopiera den till skrivbordet

- Logga in på trådlösanätverket hemma / mobilen
- Aktivera vnc i inställningar.
- logga in med RealVNC på ip som 
update RPI linux:
- sudo apt update
- sudo apt upgrade

#skapa en virtuell miljö i boundDeviceWorkingPy katalogen:
- sudo apt install python3-venv
- python3 -m venv myenv
- source myenv/bin/activate
- nu ska det li en (myenv) i terminalen
- pip3 install azure-iot-device
- sudo apt install sense-hat

#  Sense-Hat calibrering:

- sudo apt update
- sudo apt install octave -y
- cd
- cp /usr/share/librtimulib-utils/RTEllipsoidFit ./ -a
- cd RTEllipsoidFit
- RTIMULibCal

# När det är klart startas programmet
Calibrate
Install the necessary software and run the calibration program as follows:


sudo apt update
sudo apt install octave -y
cd
cp /usr/share/librtimulib-utils/RTEllipsoidFit ./ -a
cd RTEllipsoidFit
RTIMULibCal
The calibration program displays the following menu:

Options are:

  m - calibrate magnetometer with min/max
  e - calibrate magnetometer with ellipsoid (do min/max first)
  a - calibrate accelerometers
  x - exit

Enter option:
Press lowercase m. The following message will then show. Press any key to start.

Magnetometer min/max calibration
-------------------------------
Waggle the IMU chip around, ensuring that all six axes
(+x, -x, +y, -y and +z, -z) go through their extrema.
When all extrema have been achieved, enter 's' to save, 'r' to reset
or 'x' to abort and discard the data.

Press any key to start...
After it starts, you should see output similar to the following scrolling up the screen:

Min x:  51.60  min y:  69.39  min z:  65.91
Max x:  53.15  max y:  70.97  max z:  67.97
Focus on the two lines at the very bottom of the screen, as these are the most recently posted measurements from the program.

Now, pick up the Raspberry Pi and Sense HAT and move it around in every possible way you can think of. It helps if you unplug all non-essential cables to avoid clutter.

Try and get a complete circle in each of the pitch, roll and yaw axes. Take care not to accidentally eject the SD card while doing this. Spend a few minutes moving the Sense HAT, and stop when you find that the numbers are not changing any more.

Now press lowercase s then lowercase x to exit the program. If you run the ls command now, you’ll see a new RTIMULib.ini file has been created.

In addition to those steps, you can also do the ellipsoid fit by performing the steps above, but pressing e instead of m.

When you’re done, copy the resulting RTIMULib.ini to /etc/ and remove the local copy in ~/.config/sense_hat/:

rm ~/.config/sense_hat/RTIMULib.ini
sudo cp RTIMULib.ini /etc


- sudo reboot

# För att kunna starta RPI utan skärm inkopplad:
- öppna en terminal och skriv :
- sudo nano /boot/config.txt
- Gå ner till du ser:
- hdmi_force_hotplug=1
- ta bort # för att aktivera den raden



 !!!!!! Om man ska starta scriptet via systemctl, se till att denna app och alla filer är stängda. 
och att inte .py filerna är öppna i något program, annars kan inte systemctl 
 komma åt filerna och man får EOF exception i loggarna!!!!!!


För att få Bound att starta när datorn startas gör detta:
- öppna en terminal och skriv:
- sudo nano /home/pi/.config/autostart/bound.config

i filen skriv:

1. [Desktop Entry]
2. Encoding=UTF-8
3. Type=Application
4. Name=Bound service
5. Comment=
6. Exec= /usr/bin/python3 /home/pi/Desktop/BoundDevicePySplit/start.py
7. StartupNotify=false
8. Terminal=True
9. Hidden=false

Se till att start.py ligger i rätt katalog   dvs:  /home/pi/Desktop/BoundDevicePySplit/start.py
starta om datorn för att kolla ifall det funkar





Aktuellt:

Ifall det ligger flera meddelanden som tex "restartDevice", "online" osv kommer de att köras tills alla meddelanden är borta
