import glove_signal_lib as gsl
from time import sleep
import sys;print(sys.version);print(sys.executable)

pulse_on_time = .5
pulse_off_time = .005
blink_on_time = .25
blink_off_time = .005
blink_fade_in_time = 0.0
blink_fade_out_time = 0.0
n = 1 # number of blinks
sleep_time = 1
# background defines whether a vibration request should, True, run in parallel as in vibrator A & B & C 
# or, False, run sequentially as in vibrator A then B then C
background = True

while True:

# Test Row and Column Signal Methods

    # gsl.Row1.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Row2.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Row3.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)

    # gsl.Row1.pulse(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Row2.pulse(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Row3.pulse(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Column1.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Column2.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Column3.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)

    # gsl.Column1.pulse(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Column2.pulse(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Column3.pulse(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # Directional
    # gsl.Row1.blink_rightward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Row1.blink_leftward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)

    # gsl.Row1.pulse_rightward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Row1.pulse_leftward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Row1.pulse_inward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Row1.pulse_outward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Row2.blink_rightward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Row2.blink_leftward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)

    # gsl.Row2.pulse_rightward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Row2.pulse_leftward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Row2.pulse_inward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Row2.pulse_outward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Row3.blink_rightward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Row3.blink_leftward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)

    # gsl.Row3.pulse_rightward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Row3.pulse_leftward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Row3.pulse_inward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Row3.pulse_outward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Column1.blink_upward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Column1.blink_downward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)

    # gsl.Column1.pulse_upward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Column1.pulse_downward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Column1.pulse_inward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Column1.pulse_outward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Column2.blink_upward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Column2.blink_downward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)

    # gsl.Column2.pulse_upward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Column2.pulse_downward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Column2.pulse_inward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Column2.pulse_outward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Column3.blink_upward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Column3.blink_downward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)

    # gsl.Column3.pulse_upward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Column3.pulse_downward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Column3.pulse_inward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Column3.pulse_outward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

# Test Arrow Signal Methods
    # Sequential
    # gsl.Arrow.upward_left(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Arrow.downward_right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Arrow.upward_right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Arrow.downward_left(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Arrow.upward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Arrow.downward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Arrow.leftward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Arrow.rightward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    
#     # Parallel
#     blink_on_time = .5
#     blink_off_time = .5
#     sleep_time = 1
    # gsl.Arrow.out_left(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Arrow.in_right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
#     gsl.Arrow.out_right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
#     sleep(sleep_time)
#     gsl.Arrow.in_left(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
#     sleep(sleep_time)
#     gsl.Arrow.up(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
#     sleep(sleep_time)
#     gsl.Arrow.down(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
#     sleep(sleep_time)
#     gsl.Arrow.left(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
#     sleep(sleep_time)
#     gsl.Arrow.right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
#     sleep(sleep_time)

# Test Triangle Signal Methods
    # gsl.Triangle.up(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.down(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.left(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.upper_left(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.upper_right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.lower_left(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.lower_right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    
    # # # Sequential
    # gsl.Triangle.upward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.downward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.leftward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.rightward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.upper_leftward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.upper_rightward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.lower_leftward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.lower_rightward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)

# Test Diagnal Signal Methods

# Test Box Signal Methods

# Test Urgency Signal Methods
    gsl.Acknowledge.Row(1)
    sleep(sleep_time)
    gsl.Attention.Row(2)
    sleep(sleep_time)
    gsl.Alert.Row(3)
