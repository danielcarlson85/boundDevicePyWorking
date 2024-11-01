from sense_hat import SenseHat
import iothubManager
from azure.iot.device import IoTHubDeviceClient, exceptions, Message
import start
import subprocess
import utils
import time
import json
import excersiceAlgorithms

sense = SenseHat()
timestart =0
timeend = 0
def stopped(accelerator_value):
    return abs(accelerator_value) < 0.17

def checkForDeviceMovements():
    utils.sendDebugTextToTablet("[checkForDeviceMovements] CheckForDeviceMovements method started")
    utils.show0()
    
    if start.UserData.data == None:
        utils.createNewUserDataObject()

    while True:
        acceleration = sense.get_accelerometer_raw()
        accelerator_value = acceleration['z'] - 1.0
        short_accelerator_value = float(str(accelerator_value)[:5])
        start.UserData.totalSecUntilRestartExcersise += 1
        
        if start.UserData.totalSecUntilRestartExcersise >= 10000:    
            start.UserData.totalSecUntilRestartExcersise=0
            utils.restart_bound_script_with_logging()
        
        if short_accelerator_value >0.4:
            start.UserData.startExcersice=True
            break
    startExercise()
            
def startExercise():
    utils.sendDebugTextToTablet("[startExercise] StartExcersice method started")
    timestart=int(time.time())
    timeend=0
    while start.UserData.startExcersice:
        if start.UserData.reps == 10:
            start.UserData.reps = 0
            
        time.sleep(start.UserData.delaytime / 1000)
        acceleration = sense.get_accelerometer_raw()
        accelerator_value = acceleration['z'] - 1.0
        
        if start.UserData.reps >= 0 and start.UserData.reps < 10:
            utils.showLetter(start.UserData.reps)
        if start.UserData.moving:
            if stopped(accelerator_value):
                start.UserData.deviceSensitivity += 1
                if start.UserData.deviceSensitivity >= 15:
                    if start.UserData.direction =="up":
                        start.UserData.reps += 1
                        start.UserData.totalReps += 1
                    start.UserData.deviceSensitivity = 0
                    start.UserData.moving = False
            else:
                start.UserData.deviceSensitivity += 1
                start.UserData.direction="up"
        else:
            if not stopped(accelerator_value):
                start.UserData.deviceSensitivity += 1
                if start.UserData.deviceSensitivity >= 15:
                    start.UserData.direction="up"
                    start.UserData.deviceSensitivity = 0
                    start.UserData.moving = True
            else:
                start.UserData.deviceSensitivity += 1
                start.UserData.direction = "down"
            
        if start.UserData.reps >-1:
            timeend=int(time.time())
            timeTotal = (timeend-timestart) - 5
            start.UserData.data['TrainingData'].append({'Reps': start.UserData.totalReps, 'Weight': start.UserData.weight, 'Time': timeTotal})
            
        short_accelerator_value = float(str(accelerator_value)[:5])

        lowerLimit = -0.07
        upperLimit = -0.02
        
        if lowerLimit <= short_accelerator_value <= upperLimit:
            start.UserData.totalPause = start.UserData.totalPause +1
            print("Checking pause")
            print(short_accelerator_value)
            if start.UserData.totalPause == 100:
                start.UserData.totalPause = 0
                start.UserData.data['TotalReps'] = start.UserData.totalReps
                training_data = json.dumps(utils.replace_empty_with_string(start.UserData.data))                
                iothubManager.Program.send_data_to_iothub(training_data)
                start.UserData.totalReps=0
                start.UserData.reps=0
                start.UserData.weight=0
                utils.setBlackColor()
                start.UserData.startExcersice=False
                checkForDeviceMovements()
                break

        else:
            start.UserData.totalPause = 0
