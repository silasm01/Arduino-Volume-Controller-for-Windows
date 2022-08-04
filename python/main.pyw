import yaml
import serial
import time
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
port=serial.Serial("COM4", baudrate=9600)

def main():
    audioControlDict = loadSettings()
    first = True
    last_second = 0
    while True:
        if int(last_second)+1 == int(time.strftime("%S")):
            audioControlDict = loadSettings()
        last_second = time.strftime("%S")

        serial_input = getPotValues()

        setVolume(serial_input, audioControlDict)

def loadSettings():
    audioControlDict = []
    with open("settings.yaml") as f:
        data = yaml.load(f, Loader=yaml.BaseLoader)
        controlApplicationDict = data.get("controlApplications")
        for key in controlApplicationDict.keys():
            temp = []
            for i in controlApplicationDict.get(key).split(" "):
                sessions = AudioUtilities.GetAllSessions()
                for session in sessions:
                    if session.Process and session.Process.name() == i:
                        temp.append(session._ctl.QueryInterface(ISimpleAudioVolume))
            audioControlDict.append(temp)
    return audioControlDict
            
def getPotValues():
    serial_input = str(port.readline().strip()).replace("b","").replace("'","").split()
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