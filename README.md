open a terminal and write:

- sudo apt-get update
- sudo apt-get upgrade
- sudo apt-get install sense-hat
- sudo apt install python3-dev python3-pip libjpeg-dev libtiff5-dev libfreetype6-dev libopenjp2-7 libjpeg62-turbo-dev zlib1g-dev
- pip3 install --no-cache-dir pillow
- pip3 install sense-hat
- pip3 install azure-iot-device
- pip3 install requests
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
