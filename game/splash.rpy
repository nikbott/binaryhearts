# Splash screen before main menu

label splashscreen:
    scene black
    with Pause(1)

    show text """
    Warning:

    This game contains sensitive content, including themes of trauma, mental health struggles, and emotional distress.

    Player discretion is advised.

    If at any point you feel uncomfortable or distressed, please take a break or seek support.
    """
    with Pause(5)

    hide text
    with Pause(1)

    play music "<from 11.6>hon_o_yomu.webm"

    show text """
    mov rax, 0x87
    mov rdi, 0xffffffff
    """
    with Pause(2)

    hide text
    with Pause(1)

    show text "syscall"
    with Pause(2)

    hide text
    with Pause(1)

    return
