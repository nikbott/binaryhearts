label cafe1:
    scene bg cafe

    play music "moe_jazz_dreamer_instrumental.webm"

    "later that day..."

    e "thank you, Aya. i'm so happy that you liked it! i hope he also does~"

    k "you mean me?"

    show eriko shocked 

    e "eeeeeehh???"

    e "how did you know i was here?? you creep!"

    k "how can you not be at the Code Café, Eriko?"

    show eriko happy

    e "you're right. the boba tea here is sooo good~"

    e "also, HAPPY BITHDAY!!!"

    k "it's {i}not{/i} my birthday, Eriko..."

    $ today = datetime.date.today().strftime('%B %d')

    e "of course it is, today is [today] !"

    k "i refuse to argue"

    e "but hey, at least you'll get a present, huh"

    e "take a look"

    # insert painting

    k "wow! it's actually not that bad!"

    e "yaaaay~ i knew you'd like it!"

    e "see, Aya, we were right"

    hide eriko

    show aya neutral

    a "cool. how are you doing on your not-birthday, Kaito?"

    k "pretty well. just a bit sleepy because of something"

    hide aya

    show eriko cringe

    e "eeeh~"

    k "and what are you doing here today, Aya? did you both agree on meeting?"

    hide eriko

    show aya neutral

    a "no, i actually just came to pick up a coffee and found ms. sunshine here begging for boba XD"

    a "but i need to go now, i have to implement that new class for my simulati-"

    e "AYA LOOK WHO IS HERE!!"

    hide aya

    show hiroshi neutral

    h "well, hi there"

    hide hiroshi

    show eriko happy

    e "HI, HIROSHI-KUN!! how did you know we were here?"

    e "it's so nice we're all together in a totally random manner! hehe~"

    hide eriko

    show aya cringe

    a "h-hi... hiroshi senpai!"

    # senpai has a code problem, aya solves and sends "magically" to his pc

    return