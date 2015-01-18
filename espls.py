#-- Copyright 2015 David Lyon. All rights reserved.
#-- 
#-- Redistribution and use in source and binary forms, with or without modification, are
#-- permitted provided that the following conditions are met:
#-- 
#--    1. Redistributions of source code must retain the above copyright notice, this list of
#--       conditions and the following disclaimer.
#-- 
#--    2. Redistributions in binary form must reproduce the above copyright notice, this list
#--       of conditions and the following disclaimer in the documentation and/or other materials
#--       provided with the distribution.
#-- 
#-- THIS SOFTWARE IS PROVIDED BY DAVID LYON ''AS IS'' AND ANY EXPRESS OR IMPLIED
#-- WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
#-- FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL BART VAN STRIEN OR
#-- CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#-- CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#-- SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
#-- ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#-- NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
#-- ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#-- 
#-- The views and conclusions contained in the software and documentation are those of the
#-- authors and should not be interpreted as representing official policies, either expressed
#-- or implied, of David Lyon.
#--
#-- The above license is known as the Simplified BSD license.

import sys
import serial
from time import sleep
import argparse

version="0.1.0"

lscommand = """c = 0
l = file.list();
for k,v in pairs(l) do
   print("name:"..k..", size:"..v)
   c = c + 1
end
print("Files:"..c)
"""

def send_line(port, textline):

    port.write(textline)
    port.write('\n')
    
    rcv = port.readline()

    #print("Sent    >>" + repr(textline))
    if not rcv.startswith('>'):
        print("Received<<" + repr(rcv))
    #print
    
    return rcv
   
if __name__ == '__main__':

    # parse arguments or use defaults
    parser = argparse.ArgumentParser(description='ESP8266 Lua script uploader.')
    parser.add_argument('-p', '--port',    default='/dev/ttyUSB0', help='Device name, default /dev/ttyUSB0')
    parser.add_argument('-b', '--baud',    default=9600,           help='Baudrate, default 9600')
    parser.add_argument('-f', '--src',     default='main.lua',     help='Source file on computer, default main.lua')
    parser.add_argument('-t', '--dest',    default='main.lua',     help='Destination file on MCU, default main.lua')
    parser.add_argument('-r', '--restart', action='store_true',    help='Restart MCU after upload')
    parser.add_argument('-d', '--dofile',  action='store_true',    help='Run the Lua script after upload')
    parser.add_argument('-v', '--verbose', action='store_true',    help="Show progress messages.")
    args = parser.parse_args()

    # open serial port
    try:
        port = serial.Serial(args.port, args.baud)
    except:
        sys.stderr.write("Could not open port %s\n" % (args.port))
        sys.exit(1)

    # clear the line
    send_line(port,'')
    
    for l in lscommand.split('\n'):

        send_line(port,l)
        
    rcv = port.readline().strip()
    while not rcv.startswith("Files:"):
        
        if (len(rcv) != 0) and (not rcv.startswith('>')):

            print("Received<<" + repr(rcv))

            # print rcv
            
        rcv = port.readline().strip()

    print rcv
