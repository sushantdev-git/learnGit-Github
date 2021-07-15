#!usr/bin/env python  
#this is a shabang line

import os

def checkReboot():
    #returns true if the computer has a pending reboot.
    return os.path.exist("/run/reboot-required")

def main():
    "some changes added here"

main()