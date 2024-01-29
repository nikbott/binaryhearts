﻿# The script of the game goes in this file.

init python:
    import datetime

define a = Character("Aya (あや)")
define e = Character("Eriko (えり子)", color="#c072e8")
define h = Character("Hiroshi (ひろし)", color="#c7e84f")
define k = Character("Kaito (かいと)", color="#e85643")

label start:

    call intro from _call_intro

    call cafe1 from _call_cafe1

    call city1 from _call_city1

    call vending_machine1 from _call_vending_machine1

    return
