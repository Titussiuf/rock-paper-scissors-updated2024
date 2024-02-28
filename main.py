hand = 0

def on_button_pressed_a():
    global hand
    hand = randint(1, 3)
    if hand == 1:
        basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            """)
        music.play(music.create_sound_expression(WaveShape.NOISE,
                54,
                54,
                255,
                0,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.UNTIL_DONE)
    elif hand == 2:
        basic.show_leds("""
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            """)
        music.play(music.create_sound_expression(WaveShape.SINE,
                928,
                302,
                255,
                255,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.UNTIL_DONE)
    else:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        music.play(music.create_sound_expression(WaveShape.SAWTOOTH,
                5000,
                5000,
                255,
                255,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global hand
    hand = randint(1, 3)
    if hand == 1:
        basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            """)
        music.play(music.create_sound_expression(WaveShape.NOISE,
                54,
                54,
                255,
                0,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.UNTIL_DONE)
    elif hand == 2:
        basic.show_leds("""
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            """)
        music.play(music.create_sound_expression(WaveShape.SINE,
                928,
                302,
                255,
                255,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.UNTIL_DONE)
    else:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        music.play(music.create_sound_expression(WaveShape.SAWTOOTH,
                5000,
                5000,
                255,
                255,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)
