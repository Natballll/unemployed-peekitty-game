# CHAP 4 DEAD FRIEND

label ch_04_dead:

    define d = Character("Dead Friend Guy")

    scene bg event_room with fade

    mc "I'm meeting the Guy With a Dead Friend now."

    h "Isn't it great how you know that in advance?."

    show dead neutral with dissolve

    d "I love my friend. Shame they died."

    menu:
        "I'll be your new dead friend.":

            d "Wow. It's like you're just like my dead friend."

            $ bad_route = True

        "I'd rather not emotionally manipulate this person, please.":

            h "Let's head into the bathroom, shall we?"    

            $ bad_route = False

    return

