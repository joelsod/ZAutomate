from Tkinter import *


LIBRARY_PREFIX = '/media/ZAL/' 	## '/media/DATA_NEW/ZAL/'
PLATFORM_DELIMITER = '/' 		### should be \ on win32, / on *nix

### turn this to True to automatically log tracks played
# TODO: disable automatic logging during development
AUTOLOG = False

### define which sound backend to use
### current options: "madao", "vlc" -- "snack" used to work
PLAYER_CLASS = "madao"
PLAYER_DRIVER = "alsa"

## how big do you want the cart machine?
CARTS_ROWS = 8
CARTS_COLS = 6

##CARTMACHINE_DIMENSIONS = (1280, 960)
LIBRARY_DIMENSIONS = (1050, 788)


### these three apply only to automation
SizeX = 800
SizeY = 600
WinGeometry = (str)(SizeX)+"x"+(str)(SizeY)+"+0+0" #SIZEXxSIZEY+XOFFSET+YOFFSET

### Automation will add to its playlist when there are this many or fewer tracks to go
PlistGenThreshold = 10
### How many prior carts to keep in the queue
PlistHistThreshold = 3

### all modules use this
Root = Tk()


CART_WIDTH = 200
CART_MARGIN = 10
CART_HEIGHT = 75

METER_INTERVAL = .25
METER_WIDTH = 1250
