import glove_signal_lib as gsl
from time import sleep

pulse_on_time = .5
pulse_off_time = .5
blink_on_time = .05
blink_off_time = .05
blink_fade_in_time = 0.0
blink_fade_out_time = 0.0
n = 1
sleep_time = .5
# background defines whether a vibration request should, True, run in parallel as in vibrator A & B & C 
# or, False, run sequentially as in vibrator A then B then C
background = True

while True:

# Test Row and Column Signal Methods

    gsl.Row1.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.Row2.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.Row3.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)

    gsl.Row1.pulse(pulse_on_time, pulse_off_time)
    sleep(sleep_time)
    gsl.Row2.pulse(pulse_on_time, pulse_off_time)
    sleep(sleep_time)
    gsl.Row3.pulse(pulse_on_time, pulse_off_time)
    sleep(sleep_time)

    gsl.Column1.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.Column2.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.Column3.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)

    gsl.Column1.pulse(pulse_on_time, pulse_off_time)
    sleep(sleep_time)
    gsl.Column2.pulse(pulse_on_time, pulse_off_time)
    sleep(sleep_time)
    gsl.Column3.pulse(pulse_on_time, pulse_off_time)
    sleep(sleep_time)

    # Directional
    gsl.Row1.blink_rightward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.Row1.blink_leftward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)

    gsl.Row1.pulse_rightward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)
    gsl.Row1.pulse_leftward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)

    gsl.Row1.pulse_inward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)
    gsl.Row1.pulse_outward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)

    gsl.Row2.blink_rightward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.Row2.blink_leftward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)

    gsl.Row2.pulse_rightward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)
    gsl.Row2.pulse_leftward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)

    gsl.Row2.pulse_inward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)
    gsl.Row2.pulse_outward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)

    gsl.Row3.blink_rightward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.Row3.blink_leftward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)

    gsl.Row3.pulse_rightward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)
    gsl.Row3.pulse_leftward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)

    gsl.Row3.pulse_inward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)
    gsl.Row3.pulse_outward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)

    gsl.Column1.blink_upward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.Column1.blink_downward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)

    gsl.Column1.pulse_upward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)
    gsl.Column1.pulse_downward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)

    gsl.Column1.pulse_inward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)
    gsl.Column1.pulse_outward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)

    gsl.Column2.blink_upward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.Column2.blink_downward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)

    gsl.Column2.pulse_upward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)
    gsl.Column2.pulse_downward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)

    gsl.Column2.pulse_inward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)
    gsl.Column2.pulse_outward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)

    gsl.Column3.blink_upward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.Column3.blink_downward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)

    gsl.Column3.pulse_upward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)
    gsl.Column3.pulse_downward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)

    gsl.Column3.pulse_inward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)
    gsl.Column3.pulse_outward(pulse_on_time, pulse_off_time)
    sleep(sleep_time)

# Test Arrow Signal Methods
    # Sequential
    gsl.arrow.upward_left(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.arrow.downward_right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.arrow.upward_right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.arrow.downward_left(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.arrow.upward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.arrow.downward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.arrow.leftward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.arrow.rightward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    
    # Parallel
    blink_on_time = .5
    blink_off_time = .5
    sleep_time = 1
    gsl.arrow.out_left(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.arrow.in_right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.arrow.out_right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.arrow.in_left(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.arrow.up(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.arrow.down(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.arrow.left(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)
    gsl.arrow.right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time)
    sleep(sleep_time)