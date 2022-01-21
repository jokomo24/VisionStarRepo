from time import sleep
import gpiozero
import constants as const

# Grid Layout Naming Convention
#         1      2     3
#      ____________________
#  1  |   A  |   B  |  C   |
#     |______|______|______|
#  2  |   D  |   E  |  F   |
#     |______|______|______|
#  3  |   G  |   H  |  I   |
#     |______|______|______|

# Initialize Vibrators - https://gpiozero.readthedocs.io/en/stable/api_output.html#pwmoutputdevice
active_high = True
initialVal = 0.0
freq = 100
pin_factory = None

vibrator_A = gpiozero.PWMOutputDevice(const.GPIO_A, active_high, initialVal, freq, pin_factory)
vibrator_B = gpiozero.PWMOutputDevice(const.GPIO_B, active_high, initialVal, freq, pin_factory)
vibrator_C = gpiozero.PWMOutputDevice(const.GPIO_C, active_high, initialVal, freq, pin_factory)
vibrator_D = gpiozero.PWMOutputDevice(const.GPIO_D, active_high, initialVal, freq, pin_factory)
vibrator_E = gpiozero.PWMOutputDevice(const.GPIO_E, active_high, initialVal, freq, pin_factory)
vibrator_F = gpiozero.PWMOutputDevice(const.GPIO_F, active_high, initialVal, freq, pin_factory)
vibrator_G = gpiozero.PWMOutputDevice(const.GPIO_G, active_high, initialVal, freq, pin_factory)
vibrator_H = gpiozero.PWMOutputDevice(const.GPIO_H, active_high, initialVal, freq, pin_factory)
vibrator_I = gpiozero.PWMOutputDevice(const.GPIO_I, active_high, initialVal, freq, pin_factory)

# |********************************************************************|
# | Here, we wish to define a set of Classes. Each Class will define a |
# | Haptic Signal Pattern. Each pattern will use 1 or more vibrators   |
# | with methods that define the style and feel of each particular     |
# | haptic message. Later, we will use these functions in our main app |
# | to interface with the camera and build logic to control the glove. |
# |********************************************************************|

# Define Classes for Column and Row patterns 

# fade_in_time = 0 
# fade_out_time = 0

# background defines whether a vibration request should, True, run in parallel as in vibrator A & B & C 
# or, False, run sequentially as in vibrator A then B then C
#background = False

class Row1:
# Define vibration pattern/behavior with Class methods
    # TODO rename these methods based on the signal we decide they represent 
    def blink(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_rightward(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_leftward(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    
    def pulse(on_time, off_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_A.pulse(on_time, off_time, n, background)
        vibrator_B.pulse(on_time, off_time, n, background)
        vibrator_C.pulse(on_time, off_time, n, background)
    def pulse_rightward(on_time, off_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_A.pulse(on_time, off_time, n, background)
        vibrator_B.pulse(on_time, off_time, n, background)
        vibrator_C.pulse(on_time, off_time, n, background)
    def pulse_leftward(on_time, off_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_C.pulse(on_time, off_time, n, background)
        vibrator_B.pulse(on_time, off_time, n, background)
        vibrator_A.pulse(on_time, off_time, n, background)
    def pulse_inward(on_time, off_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_A.pulse(on_time, off_time, n, background)
        vibrator_C.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_B.pulse(on_time, off_time, n, background)
    def pulse_outward(on_time, off_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_B.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_A.pulse(on_time, off_time, n, background)
        vibrator_C.pulse(on_time, off_time, n, background)

    # Constant On/Off methods
    def on():
        vibrator_A.on()
        vibrator_B.on()
        vibrator_C.on()
    def off():
        vibrator_A.off()
        vibrator_B.off()
        vibrator_C.off()

class Row2:
    def blink(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_rightward(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_leftward(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    
    def pulse(on_time, off_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_D.pulse(on_time, off_time, n, background)
        vibrator_E.pulse(on_time, off_time, n, background)
        vibrator_F.pulse(on_time, off_time, n, background)
    def pulse_rightward(on_time, off_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_D.pulse(on_time, off_time, n, background)
        vibrator_E.pulse(on_time, off_time, n, background)
        vibrator_F.pulse(on_time, off_time, n, background)
    def pulse_leftward(on_time, off_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_F.pulse(on_time, off_time, n, background)
        vibrator_E.pulse(on_time, off_time, n, background)
        vibrator_D.pulse(on_time, off_time, n, background)
    def pulse_inward(on_time, off_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_D.pulse(on_time, off_time, n, background)
        vibrator_F.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_E.pulse(on_time, off_time, n, background)
    def pulse_outward(on_time, off_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_E.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_D.pulse(on_time, off_time, n, background)
        vibrator_F.pulse(on_time, off_time, n, background)

    # Constant On/Off methods
    def on():
        vibrator_D.on()
        vibrator_E.on()
        vibrator_F.on()
    def off():
        vibrator_D.off()
        vibrator_E.off()
        vibrator_F.off()

class Row3:
    def blink(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_rightward(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_leftward(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def pulse(on_time, off_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_G.pulse(on_time, off_time, n, background)
        vibrator_H.pulse(on_time, off_time, n, background)
        vibrator_I.pulse(on_time, off_time, n, background)
    def pulse_rightward(on_time, off_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_G.pulse(on_time, off_time, n, background)
        vibrator_H.pulse(on_time, off_time, n, background)
        vibrator_I.pulse(on_time, off_time, n, background)
    def pulse_leftward(on_time, off_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_I.pulse(on_time, off_time, n, background)
        vibrator_H.pulse(on_time, off_time, n, background)
        vibrator_G.pulse(on_time, off_time, n, background)
    def pulse_inward(on_time, off_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_G.pulse(on_time, off_time, n, background)
        vibrator_I.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_H.pulse(on_time, off_time, n, background)
    def pulse_outward(on_time, off_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_H.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_G.pulse(on_time, off_time, n, background)
        vibrator_I.pulse(on_time, off_time, n, background)

    # Constant On/Off methods
    def on():
        vibrator_G.on()
        vibrator_H.on()
        vibrator_I.on()
    def off():
        vibrator_G.off()
        vibrator_H.off()
        vibrator_I.off()

class Column1:
    def blink(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_upward(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_downward(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def pulse(on_time, off_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_A.pulse(on_time, off_time, n, background)
        vibrator_D.pulse(on_time, off_time, n, background)
        vibrator_G.pulse(on_time, off_time, n, background)
    def pulse_upward(on_time, off_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_G.pulse(on_time, off_time, n, background)
        vibrator_D.pulse(on_time, off_time, n, background)
        vibrator_A.pulse(on_time, off_time, n, background)
    def pulse_downward(on_time, off_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_A.pulse(on_time, off_time, n, background)
        vibrator_D.pulse(on_time, off_time, n, background)
        vibrator_G.pulse(on_time, off_time, n, background)
    def pulse_inward(on_time, off_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_A.pulse(on_time, off_time, n, background)
        vibrator_G.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_D.pulse(on_time, off_time, n, background)
    def pulse_outward(on_time, off_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_D.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_A.pulse(on_time, off_time, n, background)
        vibrator_G.pulse(on_time, off_time, n, background)

    # Constant On/Off methods
    def on():
        vibrator_A.on()
        vibrator_D.on()
        vibrator_G.on()
    def off():
        vibrator_A.off()
        vibrator_D.off()
        vibrator_G.off()

class Column2:
    def blink(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_upward(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_downward(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def pulse(on_time, off_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_B.pulse(on_time, off_time, n, background)
        vibrator_E.pulse(on_time, off_time, n, background)
        vibrator_H.pulse(on_time, off_time, n, background)
    def pulse_upward(on_time, off_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_H.pulse(on_time, off_time, n, background)
        vibrator_E.pulse(on_time, off_time, n, background)
        vibrator_B.pulse(on_time, off_time, n, background)
    def pulse_downward(on_time, off_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_B.pulse(on_time, off_time, n, background)
        vibrator_E.pulse(on_time, off_time, n, background)
        vibrator_H.pulse(on_time, off_time, n, background)
    def pulse_inward(on_time, off_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_B.pulse(on_time, off_time, n, background)
        vibrator_H.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_E.pulse(on_time, off_time, n, background)
    def pulse_outward(on_time, off_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_E.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_B.pulse(on_time, off_time, n, background)
        vibrator_H.pulse(on_time, off_time, n, background)

    # Constant On/Off methods
    def on():
        vibrator_B.on()
        vibrator_E.on()
        vibrator_H.on()
    def off():
        vibrator_B.off()
        vibrator_E.off()
        vibrator_H.off()

class Column3:
    def blink(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_upward(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_downward(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def pulse(on_time, off_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_C.pulse(on_time, off_time, n, background)
        vibrator_F.pulse(on_time, off_time, n, background)
        vibrator_I.pulse(on_time, off_time, n, background)
    def pulse_upward(on_time, off_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_I.pulse(on_time, off_time, n, background)
        vibrator_F.pulse(on_time, off_time, n, background)
        vibrator_C.pulse(on_time, off_time, n, background)
    def pulse_downward(on_time, off_time):
        n = 1 # execute only once
        background = False # execute sequentially
        vibrator_C.pulse(on_time, off_time, n, background)
        vibrator_F.pulse(on_time, off_time, n, background)
        vibrator_I.pulse(on_time, off_time, n, background)
    def pulse_inward(on_time, off_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_C.pulse(on_time, off_time, n, background)
        vibrator_I.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_F.pulse(on_time, off_time, n, background)
    def pulse_outward(on_time, off_time):
        n = 1 # execute only once
        background = True # execute in parallel
        vibrator_F.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_C.pulse(on_time, off_time, n, background)
        vibrator_I.pulse(on_time, off_time, n, background)

    # Constant On/Off methods
    def on():
        vibrator_C.on()
        vibrator_F.on()
        vibrator_I.on()
    def off():
        vibrator_C.off()
        vibrator_F.off()
        vibrator_I.off()

class arrow:
    # Define Arrow Pattern methods
    # Sequential
    def upward_left(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = False # execute arrow body sequentially
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        background = True # execute arrow wings in parallel
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def upward_right(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = False # execute arrow body sequentially
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        background = True # execute arrow wings in parallel
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def downward_right(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = False # execute arrow body sequentially
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        background = True # execute arrow wings in parallel
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def downward_left(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = False # execute arrow body sequentially
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        background = True # execute arrow wings in parallel
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def upward(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = False # execute arrow body sequentially
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        background = True # execute arrow wings in parallel
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def downward(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = False # execute arrow body sequentially
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        background = True # execute arrow wings in parallel
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def leftward(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = False # execute arrow body sequentially
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        background = True # execute arrow wings in parallel
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def rightward(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = False # execute arrow body sequentially
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        background = True # execute arrow wings in parallel
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    # Parallel
    def out_left(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = True # execute arrow body in parallel
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        sleep(off_time)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def out_right(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = True # execute arrow body in parallel
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        sleep(off_time)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def in_right(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = True # execute arrow body in parallel
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        sleep(off_time)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def in_left(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = True # execute arrow body in parallel
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        sleep(off_time)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def up(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = True # execute arrow body in parallel
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        sleep(off_time)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def down(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = True # execute arrow body in parallel
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        sleep(off_time)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def left(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = True # execute arrow body in parallel
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        sleep(off_time)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def right(on_time, off_time, fade_in_time, fade_out_time):
        n = 1 # execute only once
        background = True # execute arrow body in parallel
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        sleep(off_time)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)