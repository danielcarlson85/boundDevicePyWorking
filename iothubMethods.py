import start
import utils
import json
import excersiceAlgorithms
    
def startnow(usertext):
    utils.sendDebugTextToTablet(f"[startnow] Method started startnow")
    user = json.loads(usertext)        
    start.UserData.email = user["Email"]
    start.UserData.machinename=user["DeviceData"]["MachineName"]
    start.UserData.firstname = user["FirstName"]
    start.UserData.lastname = user["LastName"]
    start.UserData.status = user["Device"]["AzureIoTHubDevice"]["connectionState"]
    start.UserData.weight = user["DeviceData"]["Weight"]
    clean_object = json.dumps(utils.replace_empty_with_string(user["DeviceData"]))
    start.UserData.data = json.loads(clean_object)
    start.UserData.data['TrainingData'] = []
    excersiceAlgorithms.checkForDeviceMovements()
