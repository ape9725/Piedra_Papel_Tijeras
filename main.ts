let x = 0
function image () {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        # # . # #
        # # . # #
        `)
    music.playTone(262, music.beat(BeatFraction.Whole))
    basic.showLeds(`
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        `)
    music.playTone(262, music.beat(BeatFraction.Whole))
    basic.showLeds(`
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        `)
    music.playTone(262, music.beat(BeatFraction.Whole))
    basic.clearScreen()
}
function Juega (x: number) {
    if (x == 1) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            # # . # #
            # # . # #
            `)
    }
    if (x == 2) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
    }
    if (x == 3) {
        basic.showLeds(`
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            `)
    }
    TobbieII.dance(10)
    music.startMelody(music.builtInMelody(Melodies.PowerDown), MelodyOptions.Once)
    basic.pause(2000)
}
basic.forever(function () {
    if (TobbieII.LBlock(700)) {
        image()
        x = 1 + randint(0, 2)
        TobbieII.rightward()
        basic.pause(2900)
        TobbieII.stopturn()
        Juega(x)
    } else {
        if (TobbieII.RBlock(700)) {
            image()
            x = 1 + randint(0, 2)
            TobbieII.leftward()
            basic.pause(2900)
            TobbieII.stopturn()
            Juega(x)
        }
    }
})
