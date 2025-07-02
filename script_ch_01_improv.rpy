# CHAPTER 1 IMPROV

label ch_01_improv:

    define i = Character("Improv")

    scene bg event_room with fade

    h "Hello hello? Can you hear me?"

    menu:

        h "Hello hello? Can you hear me?"

        "Loud and clear.":

            h "Good thing we didn't skimp on that cranial implant quality, huh?"

            h "Wouldn't want your head to have been cut open for nothing."

        "Ahh! You're in my head!":

            h "Well, where else would I be?"

            h "It's a cranial implant. If I was in your appendix we'd both be clamoring for a refund."

    h "In any case, welcome to your first ever networking event!"

    h "How are we feeling today?"

    menu:

        h "How are we feeling today?"

        "Kinda nervous.":

            h "That's completely natural. There's a lot to learn, here."

        "I'm gonna crush it!":

            h "Time to tone down that overconfidence, buddy."

    h "This is an unstructured social event with no rules. We're in the Wild West, here."

    h "You're a little bit behind the curve. Most kids your age would have been doing this for years, now."

    show ad babybook with dissolve

    h "It's why my children's book, Baby's First Networking Event, has done so well."

    hide ad babybook with dissolve

    h "But don't fret, my promising client. We'll get you an interview yet."

    show overlay scanning with dissolve

    h "Let's find you our first mark, shall we?"

    hide overlay scanning with dissolve

    h "I've got it. This fellow will be a great warmup for you."

    h "Do you see the fellow in the blazer, no tie, overpriced haircut?"

    h "I'm CoachCasting his profile over to you, now."

    # "at linkedin" is the new position to show a 600x500px image at the top right corner. this will be where our linkedin/social media pngs show up
    show linkedin improv at linkedin with dissolve

    h "Try not to flinch next time. Never had your optical nerve hijacked before?"

    menu:

        h "Try not to flinch next time. Never had your optical nerve hijacked before?"

        "I have to say, it's my first time.":

            h "First of many, my dear client. First of many."

            h "Now, this profile is going to help you win this conversation."

        "What do I do with this information in front of me?":

            h "Win this conversation, that's what."

    h "You know his area of expertise. You know the achievements he's the proudest of."

    h "Just ask him about these things and he'll talk for ages."

    h "Sounds good? Let's try it out!"

    show improv neutral with dissolve

    h "He seems pretty lame."

    i "That's rude."

    h "Now Elijah removed the three lines and placed in this new line."

    return
