from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse
import start
import utils
import iothubMethods
import time
import sys
import json

class Program:
    def on_message_received(message):
        message = message.data.decode("utf-8")
        utils.sendDebugTextToTablet("Incomming message: " +message)
        result = message.split("****")
        
        if result[0] == "login":
            utils.setGreenColor()
            utils.sendDebugTextToTablet("[login] User is logged in")
            
        elif result[0] == "restartRPI":
                utils.restartRPI()
                
        elif result[0] == "shutdownRPI":
                utils.shutdownRPI()

        elif result[0] == "restartDevice":
                utils.restart_bound_script_with_logging()
        elif result[0] == "saveData":
                data=utils.replace_empty_with_string(start.UserData.data)
                start.UserData.startExcersice = False
                start.UserData.hasDeviceBeenMoved = False
                training_data = json.dumps(data)
                Program.send_data_to_iothub(training_data)
        elif result[0] == "start":
                utils.sendDebugTextToTablet("[login] Startng excersise")
                iothubMethods.startnow(result[1])

    @staticmethod
    def send_data_to_iothub(data_to_send):
        utils.sendDebugTextToTablet("[send_data_to_iothub] Sending data to IoTHub...")
        start.UserData.startExcersice = True
        start.UserData.hasDeviceBeenMoved = False
        message = Message(data_to_send)
        Program.client.send_message(message)
        utils.showS()
        time.sleep(2)
        utils.setGreenColor()
        time.sleep(1)
        print(data_to_send)
        utils.sendDebugTextToTablet("[send_data_to_iothub] DONE, data sent to IoTHub.")
        return
        
    @staticmethod
    def setup(conn_str):
        print(conn_str)
        Program.client = IoTHubDeviceClient.create_from_connection_string(conn_str)
        Program.client.on_message_received = Program.on_message_received
        Program.client.connect()
        utils.sendDebugTextToTablet("[setup] Device is up and running")
