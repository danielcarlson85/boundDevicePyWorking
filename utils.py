from sense_hat import SenseHat
import start
import json
import os
import sys
import requests
import subprocess
import time


sense = SenseHat()

def setRedColor():
    sense.clear()
    sense.clear(255,0,0)

def setGreenColor():
    sense.clear()
    sense.clear(0,255,0)
    
def setBlackColor():
    sense.clear()

def showS():
    sense.clear()
    sense.show_letter("S")
    
def show0():
    sense.clear()
    sense.show_letter("0", text_colour= setgreentext())
    
def showLetter(letter):
    
    sense.clear()
    sense.show_letter(f"{letter}", text_colour= setgreentext())
 
def setgreentext():
    sense.clear()
    return [0, 255, 0]
  
def setredtext():
    sense.clear()
    return [255, 0, 0]
    
def setGreenDot():
    sense.clear()
    sense.set_pixel(0, 7, 0, 255, 1)
    
def setRedDot():
    sense.clear()
    sense.set_pixel(0, 7, 255, 0, 1)
    

def restart_bound_script():
    sendDebugTextToTablet("Restarting device...")
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
    
def restartRPI():
    print("RPI is restarting...")
    sense.show_letter("R", text_colour= setredtext())
    time.sleep(2)
    setBlackColor()
    subprocess.run(["sudo","reboot"])


def shutdownRPI():
    print("shutting down...")
    sense.show_letter("S", text_colour= setredtext())
    time.sleep(2)
    setBlackColor()
    subprocess.run(["sudo","poweroff"])
    
    
def reset_all():
    start.UserData.delaytime = 20
    start.UserData.reps = 0
    start.UserData.totalReps = 0
    start.UserData.moving = True
    start.UserData.previous = 0
    start.UserData.totalPause=0
    start.UserData.weight = 0
    start.UserData.data = None
    start.UserData.hasLoggedInOnDevice = False
    start.UserData.pauseSinceLastRep = 0
    setBlackColor()
    

def replace_empty_with_string(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            obj[key] = replace_empty_with_string(value)
        return obj
    elif isinstance(obj, list):
        return [replace_empty_with_string(item) for item in obj]
    else:
        return "Empty" if obj is None or obj == "" else obj
                    
def createNewUserDataObject():
    clean_object = '{"MachineName": "LocalChestMachine", "ObjectId": "Local6bc00f44-9a73-47da-a542-ee87d1e3981d", "Device": "Null"}'
    start.UserData.data = json.loads(clean_object)
    start.UserData.data["TrainingData"] = []


def sendException(exception):
    
    requests.get(f"https://boundhub.azurewebsites.net/send?debugText={exception}")


def sendTextToTablet(text):
    
    requests.get(f"https://boundhub.azurewebsites.net/send?name={text}")

def sendDebugTextToTablet(text):
    
    email = start.UserData.email
    machinename=start.UserData.machinename
    status = start.UserData.status
    reps = start.UserData.totalReps
    weight = start.UserData.weight

    requests.get(f"https://boundhub.azurewebsites.net/send?name={email}&reps={reps}&machinename={machinename}&weight={weight}&status=online&debugText={text}")
