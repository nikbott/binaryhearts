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
    hide eriko

    show clouds

    k "wow! it's actually not that bad!"

    hide clouds

    show eriko happy

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

    e "HI, HIROSHI!! how did you know we were here?"

    e "it's so nice we're all together in a totally random manner! hehe~"

    hide eriko

    show aya cringe

    a "h-hi... hiroshi senpai!"

    a "i-i was just leaving, i have to go to the library!!"

    hide aya

    show hiroshi neutral

    h "oh, i see. i'll see you later, then"

    h "she's being a bit weird recently, isn't she?"

    hide hiroshi

    show eriko happy

    e "yeah, i think she's just a bit shy~"

    e "she's also been working a lot on her simulation project"

    hide eriko

    show hiroshi neutral

    h "i guess so"

    h "well, the reason i came here is because i wanted to ask you something, Kaito"

    k "what is it?"

    h "i'm having a bit of trouble with my code, and i was wondering if you could help me"

    k "sure, i'll be glad to help"

    h "it's about that thing, functional programming"

    h "...again"

    k "yea, i'm worried if i'm gonna be able to learn it, i'm not that good at math"

    k "but we can try, i guess"

    h "thanks, i really appreciate it"

    h "those lambda calculus concepts are really confusing"

    k "i know, right? i'm still trying to understand it"

    k "but what exactly is the problem?"

    h "well, i'm trying to implement a function that processes IO operations without side effects"

    h "but i'm not sure how to do it"

    hide hiroshi

    show eriko shocked

    e "lamda calculus? IO operations? side effects?"

    e "what are you two talking about? i don't understand a thing!"

    k "it's a bit complicated, Eriko"

    k "but i can explain it to you later, if you want"

    e "really? that would be great!"

    e "i'm sure i'll understand it if you explain it to me, Kaito"

    k "don't be silly, Eriko. you're not that smart"

    hide eriko

    show eriko moody

    e "what did you say?????"

    e "i'm gonna call you ugly names if you keep saying that, Kaito!"

    k "i'm just kidding, Eriko. you're smart, i know that"

    e "you better be"

    e "hmph!"

    hide eriko

    show hiroshi neutral

    h "well, i'll be going now. the AI test is in 2 days and i haven't studied yet. i'll see you later, Kaito"

    k "you'll ace it like always, don't worry! see you later, Hiroshi"

    hide hiroshi

    show eriko happy

    e "you know what, Kaito? i think you're really smart too!"

    e "you're the smartest person i know!"

    e "we should also totally get something to drink, i'm thirsty~"

    k "but you literally just had a boba tea!"

    e "i know, but i'm still thirsty!"

    e "i'd like something from a vending machine i guess"

    k "fine then, let's go"

    e "yay!!"

    hide eriko

    stop music fadeout 1.0

    scene black with fade

    # senpai has a code problem, aya solves and sends "magically" to his pc

    return
