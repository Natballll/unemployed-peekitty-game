# CHAP 5 IMPROV 2

label ch_07_anxiety:

    define x = Character("Part Tycholore")

    scene bg event_room with fade

    h "There's about just enough time for us to court one last mark."

    h "I've identified him for you. His name is Park Tycholore, Corporate Counter-Espionage Unit."

    menu:

        h "It's a well-paying field known for rapid career progression. It may do you good to get to know someone in the industry."

        "I trust you.":

            h "Thank you. Hopefully, we won't need to do anything as unpleasant as before."

            h "But we leave nothing off the table."

        "Whatever it takes.":

            h "Let's start with our pleasantries."

            h "Things don't need to get ugly if they don't need to be."

            h "And of course, if they need to be, I'll make sure you come out looking spectacular."    
            
    h "And [mcname] [mclast], I appreciate that you've been following my instructions. I'm glad you've come to see the nature of the situation."

    h "I will fulfil my end of the contract."

    h "Let's finish today strong."

    # Introduction to Part Tycholore
    call ch_07_anxiety1

    # Asking Tycholore Basic Questions, Bonding and Good Vibes
    call ch_07_anxiety2

    return

label ch_07_anxiety1:

    show anxiety neutral with dissolve

    x "Good afternoon! How's it going?"

    menu:

        "I'm good! I'm [mcname], and I'm looking to connect with folks from the Company.":

            x "Well, [mcname], thanks for reaching out. I'd be happy to find a time to chat."

        "Terrible. I'm [mcname], and I've been struggling to find a job.":

            x "I've received your concern [mcname]. Shall we block out some time to shine a spotlight on this?"

    x "How does a 10-minute chat, today, 10 seconds from now sound?"

    default confirm_chat = False

    while confirm_chat == False:

        menu:

            "Uh, sure.":

                x "Excellent."

                confirm_chat = True
            
            "I worry we might need more time for our discussion. Could we extend it to 15 minutes?":

                x "Let me just double-check my calendar..."

                x "I can certainly block out 15 minutes."

                confirm_chat = True

            "I'm sorry. I'm not available during that time.":

                h "Are you stupid? Accept his invite!"

    h "I'd heard jokes about the eccentricities of this unit, but it's fascinating to see it in the flesh."

    x "My name is Part Tycholore. I work at the Company's Corporate Counter-Espionage Unit."

    x "It's good to connect. What agenda items do you have for me today?"

label ch_07_anxiety2:

    default move_on = False
    
    while move_on == False:

        "What work do you do at the Counter-Espionage Unit?":

            x "Fantastic question! Its name certainly evokes secrecy and mystery, but I assure you it's nothing as dazzling."

            x "The Company has many competitors seeking to get an edge over it. Sometimes, they resort to rather unscrupulous methods."

            x "They might pay a bribe to a current employee to extract company secrets, attempt to install a mole, or even steal important records or hard drives."

            x "My team works to get ahead of all of this. We design security policies and recommend best practices to ensure it never gets that far."

            x "And if it does, we perform the necessary actionables."

            x "If you'd like to learn more, we'd love to have you apply to join the team!"

        "Some people say your unit is one of the best departments to work for. Is that true?":

            x "Great question! It depends on your style and work ethic."

            x "We select the best of the best, so that we can entrust our representatives to work independently."

            x "You need to have a keen eye for detail. And things may become intense, so a calm demeanour in the face of rapidly changing circumstances is valuable."

            x "If you make the cut, there won't be a supervisor breathing down your neck."

            x "Your recommendations stand on their own. They are taken seriously, and each of us wield this responsibility gravely."

            x "And for our judgement, we are splendily compensated."

        "How does one join the Counter-Espionage Unit?"

            x "It's great to hear that query. There is a thorough selection process."

            x "It involves detailed background checks. If a representative in our department can be plausibly blackmailed, it would be a disaster."

            x "There are a litany of selection tests as well. Testing your pattern recognition and observation skills."

            x "Do not be surprised by the physical fitness tests as well. We look for zero liabilities."

            x "If you apply to us, [mcname], it is my duty to inform you to be as honest as possible in your application."

            x "Get caught during your application, and you will be barred from applying to any other opportunity at the Company ever again."

            x "Get caught after your application, when you are on active duty, and the consequences are far worse."

            x "You look like a young, upstanding, ambitious person. Feel free to arrange another chat with me if you'd like to go over your application together."

        