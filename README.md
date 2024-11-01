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
  
installera Azure-
- pip install azure-iot-device --break-system-packages

- sudo apt-get install sense-hat
- sudo apt install python3-dev python3-pip libjpeg-dev libtiff5-dev libfreetype6-dev libopenjp2-7 libjpeg62-turbo-dev zlib1g-dev


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
