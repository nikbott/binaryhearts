label vending_machine1:
    scene bg vending machine
    $ renpy.music.set_volume(0.25, 1, "music")
    play sound "vending_machine_hmm.webm" fadein 1.0 loop

    k "wow! there's so many drinks to choose from!"
    e "i know, right?"
    e "actually, i'm not sure what to get..."
    k "i'll get something for you"
    e "really?"
    e "do you know what i like?"

    $coffee = False
    $snk = False
    $ttt = False

    label machine:
        menu:
            "red dragon super spicy energy drink!!":
                jump red_dragon
            "neon purple cosmic goo energy drink!!":
                jump cosmic_goo
            "plain coffee" if not coffee:
                $coffee = True
                jump eww
            "no way, i'm not drinking that" if coffee:
                jump machine
    
    label red_dragon:
        $snk = True
        e "red dragon super spicy energy drink!! (赤いドラゴン 超辛いエナジードリンク！！)"
        "Eriko loves this stuff."
        jump buy

    label cosmic_goo:
        $ttt = True
        e "neon purple cosmic goo energy drink!! (ネオンパープル コズミックグー エナジードリンク！！)"
        "Eriko loves this stuff."
        jump buy
    
    label eww:
        e "eww, coffee? (コーヒー？)"
        "Eriko despises coffee."
        jump machine
    
    label buy:
        menu:
            "buy":
                pause(1.0)
                play sound "vending_machine_buy.webm"
                pause(5.0)
                k "..."
                k "it's not working"
                e "why?"
                k "i think it's broken"
                play sound "vending_machine_buy.webm"
                pause(5.0)
                k "oh, come on!"
                e "..."
                e "k-kaito"
                k "why can't i just want to buy a drink?"
                e "..."
                e "kaito, what's that on the screen?"
                k "huh?"

                scene black
                stop music
                pause(0.2)
                play sound "glitch.webm"
                $ renpy.movie_cutscene("movies/glitch.webm", 0.5)
                pause(3)

                if snk:
                    jump snake
                if ttt:
                    jump tic_tac_toe

            "actually, i don't want this":
                jump machine
    
    label snake:
        python:
            import snake_game
            snake_game.main()
        jump end

    label tic_tac_toe:
        python:
            import tic_tac_toe_game
            tic_tac_toe_game.main()
        jump end
    
    label end:
        
    
    return
