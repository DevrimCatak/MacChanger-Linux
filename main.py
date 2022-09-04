import subprocess
import optparse
import re


def getInput():
    parseObject = optparse.OptionParser()
    parseObject.add_option("-i", "--interface", dest="interface", help="interface to change!")
    parseObject.add_option("-m", "--mac", dest="macAddress", help="new mac address!")
    return parseObject.parse_args()


def changeMac(interface, macAddress):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", macAddress])
    subprocess.call(["ifconfig", interface, "up"])


def controlChangeMac(interface, macAddress):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    newMacAddress = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))

    if newMacAddress:
        if newMacAddress.group(0) == macAddress:
            print("The MAC address has been successfully changed.")
        else:
            print("An error was encountered while changing the MAC address.")
    else:
        print("An error was encountered while changing the MAC address.")


if __name__ == '__main__':
    (userInputs, args) = getInput()
    interface = userInputs.interface
    macAddress = userInputs.macAddress
    changeMac(interface, macAddress)
    controlChangeMac(interface, macAddress)
