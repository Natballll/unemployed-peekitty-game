# CHAPTER 1 IMPROV

label ch_01_improv:

    define f = Character("Finkle Pumm")

    default theatre1 = False
    default theatre2 = False

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

        "I can't hear you at all.":

            h "Strange. Given the only way you could have known I was asking you a question was through auditory stimuli, it sounds like you are lying to me."

            h "My question was more of a courtesy, really. My surgeons are the best in the land."

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

    show screen centraldisplay("central/ad_baby.png")

    h "It's why my children's book, Baby's First Networking Event, has done so well."

    h "Oh yes. I can pull up images like that. All part of the cranial implant package."

    hide screen centraldisplay

    h "It's time for us to get to work."

    show overlay scanning at top with dissolve

    h "Let's find you our first mark, shall we?"

    hide overlay scanning with dissolve

    h "I've got it. This fellow will be a great warmup for you."

    h "Do you see the fellow in the blazer, no tie, overpriced haircut, standing alone?"

    h "I'm CoachCasting his profile over to you, now."

    show screen topleftdisplay("lk/linkedin_improv.png")

    # show screen ding("Hey Reynard. Pleasure to connect.", "improv")

    h "Now, you're all ready to win this conversation."

    h "You know his area of expertise. You know the achievements he's the proudest of."

    menu:

        h "Use it to build a connection."

        "I'm ready.":

            h "Good lad. Soon this person will be dying to work with you."

        "I still have my doubts...":

            h "Just go with the flow. If the situation ever gets too delicate, I'll step in and tell you exactly what to say."

    menu:

        h "Let's start by introducing yourself."

        "(Action) Walk towards the man confidently.":

            h "Splendid, splendid, splendid. Chest out and decisive steps, that's what we like to see."

            h "Carry that energy into your voice and tone!"

        "(Action) Walk towards the man timidly.":

            h "Oh, dearie dearie dearie. We're going to have to work on that posture."

            h "You look like a lamb going to the slaughter."

        "(Action) Remain standing in your spot.":

            call ch_01_frozen

    show improv neutral with dissolve

    q "Hello."

    menu:

        q "Hello."

        "Hi! I'm [mcname]. Recently graduated, here to learn more about the Company.":

            q "Mmm. I'm Finkle Pumm, Software Engineer."

            f "Some party we've got over here, huh?"

        "Uhhhhhhhhh.":

            call ch_01_uh

    h "Good luck. You're in the driver's seat, now."
    
    while theatre1 == False:

        call ch_01_finkle1

    h "Excellent work finding an opening, my dear client."

    h "This is what it's all about. Find points of connection."

    h "Even if they don't exist."

    h "That's what I'm here for."
    
    h "More information on Mr Finkle is en route to you now."
    
    while theatre2 == False:

        call ch_01_finkle2

    h "I'm on the lookout for our next mark."

    return

label ch_01_frozen:

    "..."

    h "Hmm. It seems like your inexperience is worse than I had imagined."

    h "No matter. I pride myself on meeting my clients where they are."

    h "You see, you're not going to be able to introduce yourself by beaming thoughts into their mind from here."

    h "We're going to have to close the distance by walking up to them and using our words."

    h "Let's try it out, shall we?"

    menu:

        h "Let's try it out, shall we?"

        "(Action) Walk towards the man.":

            pass

    return

label ch_01_uh:

    q "Can I help you?"

    h "My goodness. Okay, repeat after me exactly."

    menu:

        "(Repeat after the Handler): I'm Reynard Gray. Sorry, my mind went blank there.":

            q "I guess we've all been there. I'm Finkle Pumm, Software Engineer."

            f "Some event we've got going on, huh?"

            pass

    return


label ch_01_finkle1:

    menu:

        "The LinkedIn Profile reads: \n Finkle Pumm, Software Engineer. Dedicated full-stack developer at the Company. Maintains patches to the Company's flagship software, The Software. \n Education: University of Unpobardo: B.S. in Computer Science. \n Past Activities: Coding for Good Club, Theatre Club"

        "So, Finkle, what brings you to this event today?":

            f "Well, it was a department requirement to have someone represented..."

            f "And the team volunteered me."

            f "The rest of the team is really busy..."

            f "After I accidentally deleted our production database last week."

            f "They're working hard to get it back up."

        "Finkle, do you like working here?":

            f "Of course! Of course."

            f "...Of course."

            f "..."

            f "They really shouldn't have sent me to represent the technology department."

            f "I guess it's a pretty forgiving working environment."

            f "After all, I'm still here."

        "What advice would you have for a fresh graduate looking for work?":

            f "I think you're doing a great job by just being here."

            f "I don't think I was out and about being as brave as you were..."

            f "But as you keep learning more information about jobs and companies..."

            f "Don't forget your passions, yeah?"

            f "They're what keep us creative..."

        "I'm very interested in software engineering. What should I do to nurture my passion?":

            f "Oh... that's nice..."

            f "I really love that for you."

            f "It's a wonderful thing... to be able to build something from scratch and push it out into the world."

            f "You could really change your community by making the right product..."

            f "Keep creating things... I think it's the best way to hone your skills."

            f "And maybe you'll make something special on your own... instead of maintaining code written by people you've never met decades ago..."

            f "..."

        "What are you proudest of regarding the software the Company releases?":

            f "Oh! That's a great question."

            f "We were currently working on upgrading a key feature of The Software..."

            f "What was it?"

            f "The Feature."

            f "We've been receiving some customer complaints, so I'll be happy when it's fixed."

            f "At least that way I have some impact on the world..."
        
        "(Lie) I'm in my university's theatre club.":

            "..."

            "Finkle's eyes widen."

            "Finkle's lips tremble."

            f "Could it be?"

            f "Another connoisseur of the arts??"

            f "We had so much trouble recruiting for my club in my final year before graduation..."

            f "I even had to funnel funding from my other student organisations to keep the theatre club open..."

            f "[mcname]! Let us discuss the state of the stage!"

            $ theatre1 = True

    return

label ch_01_finkle2:

    "The University of Unpobardo Theatre Club Past Productions: \n The Woman with a Block of Cheese \n Mcbeth"

    menu:

        "I personally love the play Macbeth! It was a great introduction to Shakespeare.":

            f "Then you would have loved the production my team and I put on!"

            f "It's Macbeth... except the noblemen are fighting over rule over a vast fast food empire."

        "It's a little esoteric, but have you ever seen The Woman with a Block of Cheese?":

            f "..."

            f "I can't believe it."

            f "I wrote that play!"

            f "How... we only had 9 people in the audience... could it be that other troupes have taken on my script?"

            f "Thank goodness I kept it in the public domain! Art should be free!"

            f "We must discuss this further. What were your thoughts? How did you find it?"

            call ch_01_cheese

    return

label ch_01_cheese:

    h "He's right. He uploaded the entire PDF online."

    h "It's 847 pages and there's no summary. I'm going to need to find a workaround."

    h "I'm feeding the pages into a program that will highlight the most common nouns and verbs it detects. Try to use that for now."

    menu:

        "Pages 1-50: 1st) Kill 2nd) Dairy 3rd) Intolerance"

        "I couldn't believe it when the murder was revealed!":

            f "Really? But that all took place within the first minute of the play."

        "It was a great study of the cross-cultural importance of milk products.":

            f "Oh... I really wasn't thinking about that all that much..."
            
            f "I was hoping people would be more focused on the commentary on colonialism..."

        "I loved the message about the need for inclusivity and unity.":

            f "I'm surprised that stuck with you... given that the character who advocates for that dies in the first scene..."

    f "Hmm."

    menu:

        "Page 50-400: 1st) God 2nd) Key 3rd) Arms"

        "I also admired the serious treatment of the concept of the divine.":

            f "Really? Someone got offended by all the swearing I wrote into the play."

            f "A little excessive, I must admit."

        "I enjoyed how you built the suspense in the search for the key.":

            f "Key? What key?"

            f "One of my favourite adjectives, though. I must say."

        "It was great commentary on the ethics of wielding weapons and proportionate response.":

            f "That's a very interesting interpretation..."

            f "Though I understand how the scene with the amputee could be contrived as such..."

    menu:

        "Page 400-847 1st) First 2nd) Second 3rd) Third"

        "Ending the play with reciting the step by step instructions for the cheese was poignant.":

            pass

        "Concluding the rest of the play with the reading of the itemised will was a stroke of genius.":

            pass
        
        "Finishing the play by reading out the results of every Olympic event in the year 2000 was bold, and I liked it.":

            pass

    f "..."

    f "I'm starting to think you may have watched a different play."

    f "Which means that... someone has put on a new work with my title... it took me years to come up with..."

    menu:

        f "Which means that... someone has stolen my title... it took me years to come up with..."

        "Years to come up with 'A Woman with a Block of Cheese'?":

            f "..."

            f "I suppose..."

            f "But the play you watched... from what you've described..."

            f "Is absolute genius!"

            f "I could never have written something better if I tried!"

            f "I guess it is clear now. Some are blessed with the power of the quill and others are not."

            f "..."

            f "It was nice talking to you. I hope you get to see more plays."

            f "And good luck for your job search."

            hide improv neutral with dissolve

            "..."

            h "Well, sometimes that's how it goes."

            h "But remember, time is money. And time wasted reading 847 pages of a play about the vikings is money lost forever."

            h "It is, actually, about the vikings. I read pretty fast."

            h "Let's keep our chin up, and move on."

        "No, no! I am known for my very quirky interpretations. I'm sure it was written by you.":

            f "You're... sure?"

            f "So you already knew that I was the playwright... before speaking to me?"

            f "I am in the presence of... a fan??"

            f "We will do great things together, you and I!"

            f "We will unite our technological and creative prowess, and change the world!"

            f "All while... making sure our paychecks are still coming in, of course..."

            f "If you ever are interested... in joining our technological division... please let me know..."

            f "I'll be happy to carry this conversation further..."

            hide improv neutral with dissolve

            "..."

            show screen ding("Finkle has requested to connect with you.", "improv")

            h "Great work."

            h "Not sure what we're going to do with that connection given that you've never wrote a single line of code or screenplay in your life,"

            h "But you never know what might be that connection that lands you that interview."
            
    $ theatre2 = True        

    return
