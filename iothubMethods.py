import start
import subprocess
import utils
import time
import json
import excersiceAlgorithms
    
def startnow(usertext):
    print(f"Method started startnow")
    print(usertext)
            
            
    user = json.loads(usertext)        
    
    print(user["Email"])
    
    start.UserData.email = user["Email"]
    start.UserData.machinename=user["DeviceData"]["MachineName"]
    start.UserData.firstname = user["FirstName"]
    start.UserData.lastname = user["LastName"]
    start.UserData.status = user["Device"]["AzureIoTHubDevice"]["connectionState"]
    
    weight = (user["DeviceData"]["Weight"])
    start.UserData.weight = weight
    
    clean_object = json.dumps(utils.replace_empty_with_string(user["DeviceData"]))
    start.UserData.data = json.loads(clean_object)
    start.UserData.data['TrainingData'] = []
                    
    excersiceAlgorithms.checkForDeviceMovements()
    
    print("Startnow method exited")
    
    
#    except Exception as e:
#        print("Wrong json format" + e)
#    finally:
#        utils.restart_bound_script()
#        return-1
