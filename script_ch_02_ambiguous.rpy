# CHAPTER 2 AMBIGUOUS

label ch_02_ambiguous:

    define a = Character("Philly Pholop")

    default ambi1 = False
    default ambi2 = [False, False]
    default ambi3 = [False, False, False, False]
    default ambi4 = [False, False, False, False]

    scene bg event_room with fade

    h "That woman over there seems to be rather disengaged."

    call ch_02_ambi0     

    while ambi1 == False:

        call ch_02_ambi1

    h "Great work. Same drill as last time -- get her to warm up to you."
    
    h "Looks like it's going to be a little harder than pretending we've seen a play. Press on."

    h "Once we're confident that we've got her in our pocket, we can close the deal by asking for a referral or connection."

    while ambi2 != [True, True]:

        call ch_02_ambi2            

    a "I've said a lot about myself, [mcname]."

    h "And none of it particularly helpful."

    a "I'd love to find out more about you."

    h "After we've found out nothing about you??"

    call ch_02_ambi3

    call ch_02_ambi4

    call ch_02_ambi5

    call ch_02_ambi6

    return

label ch_02_ambi0:

    # show screen topleftdisplay("lk/linkedin_ambi")

    $ stacktopleft("lk/linkedin_ambi", True)

    "LinkedIn Profile for Philly Pholop: \n Public Relations Executive at the Company | Young Innovator Award | Two-Year Returning Intern at the Company's Global Internship Program | Outstanding Employee of the Year"

    h "How curious. It looks like this may be a particularly useful contact to procure."

    h "Don't be intimidated. Let's dive in and see whether she has anything for us."

    menu:

        h "Don't be intimidated. Let's dive in and see whether she has anything for us."

        "{i} Approach her.{/i}":

            pass

    show ambi neutral with dissolve

    q "Haven't seen you around before. Fresh grad?"

    menu:

        q "Haven't seen you around before. Fresh grad?"

        "I'm [mcname], and I'm really interested in working here.":

            q "I'm Philly."

            a "And we'll see about that."

        "I'm [mcname], and I'm exploring jobs.":

            q "Won't have time to explore forever, Reynard."

            q "Pick a target and stick to it."

            a "I'm Philly."

        "I'm [mcname], and I would like not to be homeless, please.":

            q "Don't we all."

            q "I'm Philly."

            a "Let's see if you can convince me to help you with that."

label ch_02_ambi1:

    default askwork = False
    default askbest = False

    menu:

        "What work do you do for the Company?":

            a "I'm in Public Relations."

            $ askwork = True
            
            a "..."

            h "Oh. That's it."

        "What's the best part about working here?":

            a "The pay and the job security."

            h "Hrm. Not much for chit-chat, this woman."

            $ askbest = True
        
        "Are you THE Philly Pholop? Of Young Innovation Award fame?" if askbest == True and askwork == True:

            a "You know this, but you don't know I work in Public Relations?"

            a "The Company appreciates attention to detail, you know."

            a "But I respect that you've done some research."

            a "What more would you like to know?"

            $ ambi1 = True
        
    return


label ch_02_ambi2:

    menu:

        "LinkedIn Profile for Philly Pholop: \n Public Relations Executive at the Company | Young Innovator Award | Two-Year Returning Intern at the Company's Global Internship Program | Outstanding Employee of the Year"

        # "What factors do you think contributed to your success?":

        #     a "Public Relations deals in people."

        #     a "Can you read people, [mcname]?"

        #     a "Anticipate the reactions of whole demographics to a new technology we release?"

        #     a "Or assess how bad the backlash will be when yet another crisis hits the news?"

        #     a "I've been told I can read people."

        #     a "It's served me well."

        #     a "..."

        #     a "Is what I would say to an interviewer who wants over-the-top quotes for their tabloid."

        #     a "But there's a grain of truth in it, anyway."

        #     h "Hmm."

        #     $ ambi2 += 1

        "I would love to have a job like yours.":

            a "I hate this job."

            a "We commodify language. Put a price tag on narratives and stories."

            a "We make empathy profitable. The better we are at, the more money we make."

            a "It goes against everything I believe in. Just not enough to overcome my desire to afford my rent."

            a "..."

            a "Is what I like to say to make people squirm."

            a "Occasionally, I use that spiel to convince people I'm not there to sell them something."

            h "Hmm. I'm uncertain how to respond."

            $ ambi2[0] = True
        
        "Do you enjoy your work?":

            a "I love my work."

            a "The engineers can design the best blueprints. The manufacturers can make the best products."

            a "But people have to believe in what we do."

            a "Or at least, be ambivalent to it."

            a "My work is necessary."

            a "..."

            a "Is what I would say to convince somebody to give me a promotion."

            a "Did I convince you?"

            h "What is up with this lady?"

            $ ambi2[1] = True
    
    return

label ch_02_ambi3:

    a "I'm curious where you stand on the Company's recent staff welfare initiatives."

    a "Tell me about that."

    h "Finally, an explicit lead! I'm sending you everything I have, as fast as I get find it."
    
    $ stacktopleft("linkedin_ambi_1", True)

    h "Don't just stand there! Start saying something!"

    menu:
        
        "I love it! Who could possibly have a problem with a huge resort for staff?":

            $ ambi3[0] = True

        "You're referring to the resort. I think it's disgusting...":

            $ ambi3[0] = False

    $ stacktopleft("linkedin_ambi_2")

    menu:

        "Except, of course, the grave plights of the people who had to leave their homes forever... very sad..." if ambi3[0] == True:

            $ ambi3[1] = False

        "Unless they've heard the accusations about forced displacement, then they're just way too sensitive..." if ambi3[0] == True:

            $ ambi3[1] = True

        "Disgusting on account of the terrible human rights violations that have gone on..." if ambi3[0] == False:

            $ ambi3[1] = False

        "Disgustingly fantastic! I can't wait for my beach vacation..." if ambi3[0] == False:

            $ ambi3[1] = True

    $ stacktopleft("linkedin_ambi_3")

    if ambi3[0] == True:

        menu:

            "Because those accusations are outrageous! The Company would never do such a thing." if ambi3[1] == True:

                a "So you don't think anyone could possibly oppose the resort-building, you don't care about the forced displacement accusations, because you don't believe them because the Company would never do such a thing."
                
                $ stacktopleft("linkedin_ambi_4")

                a "..."

                a "That's a very committed stance you've got there."

                $ ambi3[2] = True

                $ ambi3[3] = True

            "I joke, of course. We all know the Company is capable of much worse." if ambi3[1] == True:

                a "So you don't think anyone could possibly oppose the resort-building, you don't care about the forced displacement accusations, but actually you were joking all along because the Company's capable of evil."
                
                $ stacktopleft("linkedin_ambi_4")

                a "..."
                
                a "Not sure if this is something to joking about."

                $ ambi3[2] = False
                $ ambi3[3] = False

            "Or it would be, if it wasn't all just made up! The Company would never do such a thing." if ambi3[1] == False:

                a "So you don't think anyone could possibly oppose the resort-building, except for people who could be forcibly displaced, but fortunately none of them exist."
                
                $ stacktopleft("linkedin_ambi_4")

                a "..."

                a "It's a very... interesting way how you've structured your response."

                $ ambi3[2] = True
                $ ambi3[3] = False

            "Very sad, indeed. The whole thing's an utter tragedy, that's what this is!" if ambi3[1] == False:

                a "So you don't think anyone could possibly oppose the resort-building, except for people who could be forcibly displaced, and you think that's a tragedy."
                
                $ stacktopleft("linkedin_ambi_4")

                a "..."

                a "I've got to say, that opening line's a bit misleading."

                $ ambi3[2] = False
                $ ambi3[3] = False

    if ambi3[0] == False:

        menu:

            "But I'm so relieved that the Company was absolved of all wrongdoing! Never doubted it for a second." if ambi3[1] == False:

                a "So you think the resort's disgusting, because of the human rights violations, but you never doubted that the Company was completely innocent."
                
                $ stacktopleft("linkedin_ambi_4")

                a "..."

                a "It feels like not all parts of that sentence can be true at the same time."

                $ ambi3[2] = True
                $ ambi3[3] = False

            "There's more to unpack here, I know it. The Company has blood on its hands." if ambi3[1] == False:

                a "So you think the resort's disgusting, because of the human rights violations, and you're determined that the Company is guilty of something."

                $ stacktopleft("linkedin_ambi_4")

                a "..."

                a "That's a very committed stance you've got there."    
                
                $ ambi3[2] = False
                $ ambi3[3] = True

            "So I can soak in the ocean, enjoy the local produce and embrace pristine nature." if ambi3[1] == True:

                a "So you think the resort's disgusting, but disgustingly fantastic, and you're looking forward to reconnecting with pristine nature."
                
                $ stacktopleft("linkedin_ambi_4")

                a "..."

                a "I'm afraid you're in for some disappointment."

                $ ambi3[2] = True
                $ ambi3[3] = False
                
            "So I can get there myself and conduct my own independent investigation. The Company's hiding something, I know it." if ambi3[1] == True:

                a "So you think the resort's disgusting, but disgustingly fantastic, because it gives you a chance to go there and conduct your own investigation."

                $ stacktopleft("linkedin_ambi_4")

                a "..."

                a "I think 'fantastic' probably isn't the right word here."

                $ ambi3[2] = False
                $ ambi3[3] = False
    
    if ambi3[3] == False:

        h "Observe closely the look on her face."

        h "That's derision. It means she doesn't like you very much."

        h "I'm sensing a chance of some frustration towards me here. \n Let the record show I got you everything as fast as I could and therefore this is not my fault."

    if ambi3[3] == True:

        h "Observe closely the look on her face."

        h "I do believe I sense the slightest tinge of respect in her eyes."              
    
    return

label ch_02_ambi4:

    a "There's more I am curious about."

    a "Are you comfortable working for an organisation that has a reputation like the Company's?"

    a "Some people take a look at us and all they see is greed."

    a "Where do you lie on that?"

    h "Stay focused, watch the displays. Start talking!"

    $ stacktopleft("linkedin_ambi_5")

    menu:
        
        "I think those people are wrong. I'm proud of what the Company does to give back...":

            $ ambi4[0] = True

        "The Company's record is shameful. But hey, I'm here to make money, not give it away...":

            $ ambi4[0] = False

    $ stacktopleft("linkedin_ambi_6")

    menu:

        "Like the CEO's recent decision to give up his wealth, which surely everyone knows. What a shining role model to us all!" if ambi4[0] == True:
            
            $ ambi4[1] = True

        "Except the CEO's recent decision to give up his wealth. I have some reservations about that." if ambi4[0] == True:

            $ ambi4[1] = False

        "Till I make enough money to make a huge difference! So I can follow in the footsteps of your CEO!..." if ambi4[0] == False:

            $ ambi4[1] = True

        "And I'd never want to give any of it away. We should stop pretending that's all it takes to solve long-standing systemic issues..." if ambi4[0] == False:

            $ ambi4[1] = False

    $ stacktopleft("linkedin_ambi_7")

    if ambi4[0] == True:

        menu:

            "I'm glad he stuck to his guns despite some criticisms. One day, I hope to follow in his footsteps" if ambi4[1] == True:

                a "So you're proud of the Company's record, you think our CEO is a role model, and you're glad he stuck to his final decision."
                
                $ stacktopleft("linkedin_ambi_8")

                a "..."

                a "Fascinating. You are nothing if not consistent."

                $ ambi4[2] = True
                $ ambi4[3] = True

            "Of course, maybe there should have been a longer conversation of where that wealth actually went..." if ambi4[1] == True:

                a "So you're proud of the Company's record, you think our CEO is a role model, but just maybe more thought should have gone into where the money went."
                
                $ stacktopleft("linkedin_ambi_4")

                a "..."
                
                a "I think maybe is a horrifying understatement."

                $ ambi4[2] = False
                $ ambi4[3] = False

            "But not too serious. People are dragging the CEO's good name through the mud when all he wanted to do was to do the right thing!" if ambi4[1] == False:

                a "So you're proud of the Company's record, with the exception of our CEO's latest actions, but you think people opposing him are overreacting."

                $ stacktopleft("linkedin_ambi_4")

                a "..."

                a "I think those people have a right to be a little miffed, no?"

                $ ambi4[2] = True
                $ ambi4[3] = False

            "I think the subsequent criticism was justified. Maybe there could have been better uses for that money." if ambi4[1] == False:

                a "So you're proud of the Company's record, with the exception of our CEO's latest actions, and you think the subsequent criticism was justified."
                
                $ stacktopleft("linkedin_ambi_4")

                a "..."

                a "And you still claim to be proud of the Company's record?"

                $ ambi4[2] = False
                $ ambi4[3] = False

    if ambi4[0] == False:

        menu:

            "He's a real role model for all wealthy people around the world. We should all be inspired by him!" if ambi4[1] == True:

                a "So you think the Company's record is shameful, but our CEO is amazing, and we should all be inspired by him."
                
                $ stacktopleft("linkedin_ambi_8")

                a "..."

                a "I'd say his actions have more than overshadowed what little record the Company had."

                $ ambi4[2] = True
                $ ambi4[3] = False

            "But not all of his footsteps, of course. Just handing out money like that isn't going to solve anything." if ambi4[1] == True:

                a "So you think the Company's record is shameful, but our CEO is amazing, except for the part where he gave up his wealth."

                $ stacktopleft("linkedin_ambi_8")

                a "..."

                a "It's not clear to me why at all you find our CEO amazing."    
                
                $ ambi4[2] = False
                $ ambi4[3] = False

            "The Company hides behind these one-off performative donations while there's a complex ecosystem of factors that makes it difficult for people to rise up on their own two feet. There needs to be an honest discussion on what we expect from corporations and workers, and the Company has actively avoided these conversations in favour of short-term grandstanding." if ambi4[1] == False:

                a "So you think the Company's record is shameful, giving away money is useless, and blah, blah, blah..."
                
                $ stacktopleft("linkedin_ambi_8")

                a "..."

                a "I feel like there were bigger problems with that whole episode."

                $ ambi4[2] = True
                $ ambi4[3] = False
                
            "Because most poor people deserve to be poor, those lazy parasites!" if ambi4[1] == False:

                a "So you think the Company's record is shameful, giving away money is useless, because you hate poor people."

                $ stacktopleft("linkedin_ambi_8")

                a "..."

                a "Sounds like you'll fit right in here."

                $ ambi4[2] = False
                $ ambi4[3] = True
    
    if ambi4[3] == False:

        h "Examine intently the furrow of her eyebrows."

        h "We call that a frown. It's not a good sign."

        h "Perhaps I need to re-evaluate my strategies. This one doesn't seem to be working for you."

    if ambi4[3] == True:

        h "Examine intently the arc of her eyebrows."

        h "You may see, as I do, the slightest note of interest in her expression."  

    return

label ch_02_ambi5:

    hide screen topleftdisplay
    hide screen topleft2

    if ambi3[3] == False and ambi4[3] == False:

        a "Well, it's been nice talking to you."

        a "I'd offer to keep in touch, but I wouldn't really want you on my team."

        a "You haven't even joined it yet..."

        a "But you're already saying things you don't believe."

        a "Have a great day."
    
    if (ambi3[3] == False and ambi4[3] == True) or (ambi3[3] == True and ambi4[3] == False):

        a "Well, it's been nice talking to you."

        a "Reach out to me if you're ever thinking about joining this field."

        a "No promises, of course."

        a "Have a great day."

    if ambi3[3] == True and ambi4[3] == True:

        a "Well, it's been nice talking to you."

        a "You're opinionated. You've got guts."

        a "Maybe not the right fit for a team like mine..."

        a "I'll let you know if I know anyone who might need that trait."

        a "Have a great day."

    hide ambi neutral with dissolve

    return

label ch_02_ambi6:

    if ambi3[3] == False and ambi4[3] == False:

        h "That seemed to go poorly."

        menu:

            h "You need to sharpen your instinct for this."

            "It wasn't my fault. Your information came kind of slowly, didn't it?":

                h "Slowly?"

                h "Are you seriously suggesting that this is... my fault?"

                h "..."

                h "I am never one to shy away from feedback. Perhaps we shall diversify our tactics."

                h "Come. Many connections to form."

            "I'll do better.":

                h "Of course you will. You have me on your side."

                h "And with me, you WILL embark on the path to gainful employment."

                h "You have my word."

                h "Come. Many connections to form."

    else:
        
        h "Fantastic work!"

        h "At this rate, we'll be swimming in interview offers."

        menu:

            h "No need to thank me for the just-in-time information to seal the deal."

            "It was hardly just in time. Everything came just too late.":

                h "Well, that's just nonsense. Or else, how did you land that connection?"

                h "Be more appreciative next time."

                h "Come. Many more connections to form."

            "Thank you.":

                h "Well, you're very welcome."

                h "What would you do without me?"

                h "Come. Many more connections to form."

    return