# CHAPTER 2 AMBIGUOUS

label ch_02_ambiguous:

    define a = Character("Philly Pholop")

    default ambi1 = False
    default ambi2 = 0
    default ambi5 = 0

    scene bg event_room with fade

    h "That woman over there seems to be rather disengaged."

    show screen topleftdisplay("lk/linkedin_ambi")

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

            a "Tell me, [mcname]. Why should the Company help with that?"        

    while ambi1 == False:

        call ch_02_ambi1

    h "Great work. Same drill as last time -- get her to warm up to you."
    
    h "Looks like it's going to be a little harder than pretending we've seen a play. Press on."

    h "Once we're confident that we've got her in our pocket, we can close the deal by asking for a referral or connection."


    while ambi2 < 2:

        call ch_02_ambi2            

    a "I've said a lot about myself, [mcname]."

    h "And none of it particularly helpful."

    a "I'd love to find out more about you."

    h "Tread carefully. We've got to say the right things, and she hasn't given us much to work with."

    h "Stay alert. More information is on the way."

    call ch_02_ambi3

    call ch_02_ambi4

    call ch_02_ambi5

    call ch_02_ambi6

    return

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

            h "This is not giving us very much to work upon."

            $ ambi2 += 1
        
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

            $ ambi2 += 1
    
    return

label ch_02_ambi3:

    default ambi3 = 0

    a "I know some people have opinions on how the Company treats its staff."
    
    show screen topleftdisplay("linkedin_ambi_1")

    menu:
        

        a "What views do you have on that?"
        
        "I like it.":

            $ ambi3 += 1

            pass

        "I don't like it.":

            $ ambi3 -= 1

            pass

    show screen topleftdisplay("linkedin_ambi_2")

    menu:

        a "Really! I'm surprised!"

        "Don't be surprised. I've thought about this long and hard.":

            if ambi3 > 0:

                $ ambi3 += 1
            
            else:

                $ ambi3 -= 1

            a "Wow. You seem really firm on this."
            
        "Haha, I'm only joking! Of course I'm being sarcastic.":

            if ambi3 < 0:

                $ ambi3 += 1
            
            else:

                $ ambi3 -= 1

            a "Oh. I'm not sure if this is something to be sarcastic about."

    show screen topleftdisplay("linkedin_ambi_3")

    if ambi3 > 0:

        menu:

            a "So you really believe in the staff welfare initiatives that the Company has implemented?"

            "I absolutely do! Who doesn't love their staff benefits?":

                show screen topleftdisplay("linkedin_ambi_4")

                a "If you say so."
            
            "Well, I wouldn't say I 'really believe'...":

                show screen topleftdisplay("linkedin_ambi_4")

                a "Let's can discuss something else. Hopefully something you're more settled on."

                $ ambi5 += 1
     
    if ambi3 < 0:

        menu:

            a "So you really oppose how the Company has gone about developing its staff welfare initiatives?"

            "I absolutely do. What the Company is doing is wrong.":

                show screen topleftdisplay("linkedin_ambi_4")

                a "Those are strong words."

            "Oppose is a strong word... I do like my staff benefits.":

                show screen topleftdisplay("linkedin_ambi_4")

                a "Looks like you haven't made up your mind just yet."

                $ ambi5 += 1

    if ambi3 == 0:

        menu:

            a "So tell me what you really think. What's your stance on recent initiatives by the Company for staff?"

            "I think the Company is doing nothing wrong.":

                show screen topleftdisplay("linkedin_ambi_4")

                a "Fascinating position to take."

            "I think the Company is guilty of terrible things.":

                show screen topleftdisplay("linkedin_ambi_4")

                a "Interesting stance on this issue."

    hide screen topleftdisplay
    
    return

label ch_02_ambi4:

    default ambi4 = 0

    a "But are you comfortable working for an organisation that has a reputation like the Company's?"

    a "Some people take a look at us and all they see is greed."

    show screen topleftdisplay("linkedin_ambi_5")

    menu:

        a "Where do you lie on that?"

        "I need to be honest. The Company's record is shameful.":

            a "Is that so? You're making us sound like villains."

            $ ambi4 += 1

        "I think those people are wrong. I'm proud of what the Company does to give back.":

            a "Is that so? You're making us sound like heroes."

            $ ambi4 -= 1
    
    show screen topleftdisplay("linkedin_ambi_6")
        
    menu:

        a "In light of recent events, it's interesting to find someone with your stand."

        "Well, I guess I'm not as impressed by your CEO's generosity as you would like." if ambi4 > 0:

            pass

        "Of course I'm supportive of RECENT actions. I just think there's more to be done." if ambi4 > 0:

            $ ambi4 -= 2

        "Well, anyone who has done their homework on the Company's CEO would be inspired by his generosity." if ambi4 < 0:

            pass

        "I've heard of what your CEO did. Actually, I have my doubts about it." if ambi4 < 0:

            $ ambi4 += 2

    a "I'm glad to hear that you're up to date on current affairs."        

    show screen topleftdisplay("linkedin_ambi_7")

    menu:

        a "There was intense disagreement from many sides over his final decision to carve up his wealth."

        "He stuck to his guns. He did the right thing." if ambi4 < 0:

            a "Really? I think I would have enjoyed just receiving that handout."

            show screen topleftdisplay("linkedin_ambi_8")

            a "Your opinions are truly intriguing, [mcname]."

            pass

        "The Company's an overall good for society. But this recent decision? I just can't stand it." if ambi4 < 0:

            a "..."

            a "Didn't you just say you were supportive of his recent actions?"

            a "Either I'm having a stroke, or you're not making much sense."

            a "But I don't blame you."

            show screen topleftdisplay("linkedin_ambi_8")

            a "The whole thing defies imagination."

            $ ambi5 += 1
            
        "The Company's overall record still needs work. But your CEO got this one thing right." if ambi4 > 0:

            a "..."

            a "Didn't you just say that you were unsupportive of that?"

            a "Either there's a hallucinogen in the snacks, or you're not being very coherent."

            a "But I don't blame you."

            show screen topleftdisplay("linkedin_ambi_8")

            a "It was a whole mess."

            $ ambi5 += 1

        "Well deserved. Your CEO made a grave mistake." if ambi4 > 0:

            a "It was the only way we could keep everyone happy."
            
            show screen topleftdisplay("linkedin_ambi_8")

            a "Your opinions are truly intriguing, [mcname]."

    return

label ch_02_ambi5:

    hide screen topleftdisplay

    if ambi5 >= 2:

        a "Well, it's been nice talking to you."

        a "I'd offer to keep in touch, but I wouldn't really want you on my team."

        a "You haven't even joined it yet..."

        a "And you're already saying things you don't believe."

        a "Have a great day."
    
    if ambi5 == 1:

        a "Well, it's been nice talking to you."

        a "Reach out to me if you're ever thinking about joining this field."

        a "No promises, of course."

        a "Have a great day."

    if ambi5 == 0:

        a "Well, it's been nice talking to you."

        a "You're opinionated. You've got guts."

        a "Maybe not the right fit for a team like mine..."

        a "I'll let you know if I know anyone who might need that trait."

        a "Have a great day."

        hide ambi with dissolve

label ch_02_ambi6:

    if ambi5 < 2:

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

    if ambi5 >= 2:

        h "That seemed to go poorly."

        menu:

            h "You need to sharpen your instinct for this."

            "It wasn't my fault. Your information came kind of slowly, didn't it?":

                h "Slowly?"

                h "Are you seriously suggesting that this is... my fault?"

                h "..."

                h "How amusing."

                h "Come. Many connections to form."

            "I'll do better.":

                h "Of course you will. You have me on your side."

                h "And with me, you WILL embark on the path to gainful employment."

                h "You have my word."

                h "Come. Many connections to form."

    return