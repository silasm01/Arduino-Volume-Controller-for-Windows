import yaml
import serial
import time
import serial.tools.list_ports
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
port = serial.Serial()
port.baudrate = 9600

def main():
    audioControlDict, port = loadSettings()
    last_second = 0
    serial_input = [0,0]
    while True:
        if int(last_second)+1 == int(time.strftime("%S")):
            audioControlDict, port = loadSettings()
        last_second = time.strftime("%S")

        serial_input = getPotValues(port, serial_input)

        setVolume(serial_input, audioControlDict)
        

def loadSettings():
    audioControlDict = []
    with open("settings.yaml") as f:
        data = yaml.load(f, Loader=yaml.BaseLoader)

        for key in data.get("controlApplications").keys():
            temp = []
            for i in data.get("controlApplications").get(key).split(" "):
                for session in AudioUtilities.GetAllSessions():
                    if session.Process and session.Process.name() == i:
                        temp.append(session._ctl.QueryInterface(ISimpleAudioVolume))
            audioControlDict.append(temp)

        if port.port != data.get("serialPort"):
            if data.get("serialPort") != "Auto":
                port.port = data.get("serialPort")
            else:
                for port1, _, _ in serial.tools.list_ports.comports():
                    if port1 != port.port:
                        port.port = port1
        if port.isOpen() == False:
                port.open()
                 
    return audioControlDict, port

def getPotValues(port, serial_input):
    try:
        serial_input = str(port.readline().strip()).replace("b","").replace("'","").split()
    except:
        for port1, _, _ in serial.tools.list_ports.comports():
            try:
                port.port = port1
            except:
                break
    return serial_input

def setVolume(serial_input, audioControlDict):
    for i in range(0,len(audioControlDict)):
        for u in range(0,len(audioControlDict[i])):
            try:
                audioControlDict[i][u].SetMasterVolume(float(serial_input[i])/100, None)
            except:
                return

if __name__ == "__main__":
    main()