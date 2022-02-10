x = 0
def image():
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                # # . # #
                # # . # #
    """)
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    basic.show_leds("""
        . . . . .
                . # # # .
                . # # # .
                . # # # .
                . . . . .
    """)
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    basic.show_leds("""
        # # # # #
                # . . . #
                # . . . #
                # . . . #
                # # # # #
    """)
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    basic.clear_screen()
def Juega(x2: number):
    if x2 == 1:
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        # # . # #
                        # # . # #
        """)
    if x2 == 2:
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        """)
    if x2 == 3:
        basic.show_leds("""
            # # # # #
                        # . . . #
                        # . . . #
                        # . . . #
                        # # # # #
        """)
    TobbieII.dance(10)
    music.start_melody(music.built_in_melody(Melodies.POWER_DOWN),
        MelodyOptions.ONCE)
    basic.pause(2000)

def on_forever():
    global x
    if TobbieII.lblock(700):
        image()
        x = 1 + randint(0, 2)
        TobbieII.rightward()
        basic.pause(2900)
        TobbieII.stopturn()
        Juega(x)
    else:
        if TobbieII.rblock(700):
            image()
            x = 1 + randint(0, 2)
            TobbieII.leftward()
            basic.pause(2900)
            TobbieII.stopturn()
            Juega(x)
basic.forever(on_forever)
