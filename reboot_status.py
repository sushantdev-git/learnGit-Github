#!usr/bin/env python  
#this is a shabang line

import os
import sys
def checkReboot():
    #returns true if the computer has a pending reboot.
    return os.path.exist("/run/reboot-required")

def main():
    "some changes added here"
    if checkReboot():
        print("Pending reboot")
        sys.exit(1)
    print("no pending reboot")
    sys.exit(0)

main()