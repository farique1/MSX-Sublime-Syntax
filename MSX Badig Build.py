"""

MSX Badig Build
v1.0
A build system to run MSX Basic Dignified source or tradicional
MSX Basic code on openMSX straight from Sublime Text 3.

Copyright (C) 2019 - Fred Rique (farique)
https://github.com/farique1/MSX-Sublime-Syntax/
"""

import subprocess
import argparse
import ConfigParser

openmsx_filepath = ""
savestate_filepath = ""
msxbadig_filepath = ""
export_file = ""
export_path = ""
throttle = True
classic_basic = False

# Read command line arguments
parser = argparse.ArgumentParser(description='Convert MSX Basic Dignified source and run on openMSX')
parser.add_argument("file_path", help='The oppened file to converted')
parser.add_argument("file_name", help='The path to the oppened file to converted')
args = parser.parse_args()


# Read ini file
config = ConfigParser.ConfigParser()
config.sections()
try:
    config.read(args.file_path + '/MSX Badig Build.ini')
except IOError:
    print '.ini file not found.'
    raise SystemExit(0)
finally:
    openmsx_filepath = config.get('DEFAULT', 'openmsx_filepath')
    savestate_filepath = config.get('DEFAULT', 'savestate_filepath')
    msxbadig_filepath = config.get('DEFAULT', 'msxbadig_filepath')
    export_path = config.get('DEFAULT', 'export_path')
    export_file = config.get('DEFAULT', 'export_file')
    throttle = config.getboolean('DEFAULT', 'throttle')
    classic_basic = config.getboolean('DEFAULT', 'classic_basic')

# print args.file_path
# print args.file_name
# print openmsx_filepath
# print savestate_filepath
# print msxbadig_filepath
# print export_path
# print export_file

if not classic_basic:
    print 'MSX Basic Dignified'
    print 'Converting ' + args.file_path + '/' + args.file_name
    print 'To ' + export_path + export_file

    chama = ['python', msxbadig_filepath, args.file_path + '/' + args.file_name, export_path + export_file]
    # print chama
    print subprocess.check_output(chama)
else:
    export_path = args.file_path
    export_file = args.file_name

throttle_display = "With throttle" if throttle else "Without throttle"
print 'openMSX'
print 'Opeening ' + export_path + export_file
print throttle_display
print

# openMSX <command>s like their spaces escaped
export_path = export_path.replace(' ', '\ ')
export_file = export_file.replace(' ', '\ ')

cmd = (openmsx_filepath + '/contents/macos/openmsx -control stdio -savestate ' + savestate_filepath)
# print cmd
proc = subprocess.Popen([cmd], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

proc.stdin.write('<command>set renderer SDL</command>')
proc.stdin.flush()
print proc.stdout.readline()

proc.stdin.write('<command>diska eject</command>')
proc.stdin.flush()
print proc.stdout.readline()

proc.stdin.write('<command>diska insert ' + export_path + '</command>')
proc.stdin.flush()
print proc.stdout.readline()

if throttle:
    proc.stdin.write('<command>set throttle off</command>')
    proc.stdin.flush()
    print proc.stdout.readline()

proc.stdin.write('<command>type_via_keybuf run"' + export_file + '\\r</command>')
proc.stdin.flush()
print proc.stdout.readline()
