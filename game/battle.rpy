screen battle_screen(fighter, enemy):
    frame:
        xalign 0.5
        yalign 0.5
        add "glitch" # Replace with your background image

        # Display player and enemy with health bars
        vbox:
            xalign 0.1
            yalign 0.1
            text "[fighter]"
            hbox:
                image "[fighter] battle"  # Show player's sprite
                text "Health: [player_health]"  # Display player's health dynamically

        vbox:
            xalign 1.0
            yalign 0.1
            text "[enemy]"
            hbox:
                image "[enemy] battle"  # Show enemy's sprite
                text "Health: [enemy_health]"  # Display enemy's health dynamically

label start_battle(fighter, enemy):
    play music "nightmares.webm" fadein 0.5
    show screen battle_screen(fighter, enemy)
    $ player_health = 100
    $ enemy_health = 80

    while player_health > 0 and enemy_health > 0:
        menu:
            "Attack":
                $ player_health -= 10  # Simulated player attack
                $ enemy_health -= 10   # Simulated enemy attack

    if player_health <= 0:
        "You've been defeated."
    else:
        "You defeated the enemy!"

    stop music
    hide screen battle_screen

    return
