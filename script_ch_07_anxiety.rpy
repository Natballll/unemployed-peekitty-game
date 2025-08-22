# CHAP 5 IMPROV 2

label ch_07_anxiety:

    define x = Character("Part Tycholore")
    default good_route = False
    default referral = False

    scene bg event_room with fade

    h "There's about just enough time for us to court one last mark."

    $ stacktopleft("linkedin_anx", True)

    h "I've identified him for you. His name is Part Tycholore, Corporate Counter-Espionage Unit."

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

    # Tycholore knows
    call ch_07_anxiety3

    # Attempts to blackmail Tycholore
    call ch_07_anxiety4

    if good_route == False:
    
        call ch_07_anxiety5

    else:
    
        call ch_07_anxiety6

        if referral == True:

            call ch_07_anxiety_referral

        else:

            call ch_07_anxiety_panic

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

                $ confirm_chat = True
            
            "I worry we might need more time for our discussion. Could we extend it to 15 minutes?":

                x "Let me just double-check my calendar..."

                x "I can certainly block out 15 minutes."

                $ confirm_chat = True

            "I'm sorry. I'm not available during that time.":

                h "Are you stupid? Accept his invite!"

    h "I'd heard jokes about the eccentricities of this unit, but it's fascinating to see it in the flesh."

    x "My name is Part Tycholore. I work at the Company's Corporate Counter-Espionage Unit."

    x "It's good to connect. What agenda items do you have for me today?"
        
    return

label ch_07_anxiety2:

    default move_on = False
    default self_fin = False
    
    while move_on == False:

        menu:

            "What work do you do at the Counter-Espionage Unit?":
        
                $ stacktopleft("counter_website_aboutus")

                x "Fantastic question! Its name certainly evokes secrecy and mystery, but I assure you it's nothing as dazzling."

                x "The Company has many competitors seeking to get an edge over it. Sometimes, they resort to rather unscrupulous methods."

                x "They might pay a bribe to a current employee to extract company secrets, attempt to install a mole, or even steal important records or hard drives."

                x "My team works to get ahead of all of this. We design security policies and recommend best practices to ensure it never gets that far."

                x "And if it does, we perform the necessary actionables."

                x "If you'd like to learn more, we'd love to have you apply to join the team!"

            "Some people say your unit is one of the best departments to work for. Is that true?":
        
                $ stacktopleft("counter_website_ourpeople")

                x "Great question! It depends on your style and work ethic."

                x "We select the best of the best, so that we can entrust our representatives to work independently."

                x "You need to have a keen eye for detail. And things may become intense, so a calm demeanour in the face of rapidly changing circumstances is valuable."

                x "If you make the cut, there won't be a supervisor breathing down your neck."

                x "Your recommendations stand on their own. They are taken seriously, and each of us wield this responsibility gravely."

                x "And for our judgement, we are splendily compensated."

            "How does one join the Counter-Espionage Unit?":

                $ stacktopleft("counter_website_joinus")

                x "It's great to hear that query. There is a thorough selection process."

                x "It involves detailed background checks. If a representative in our department can be plausibly blackmailed, it would be a disaster."

                x "There are a litany of selection tests as well. Testing your pattern recognition and observation skills."

                x "Do not be surprised by the physical fitness tests as well. We look for zero liabilities."

                x "If you apply to us, [mcname], it is my duty to inform you to be as honest as possible in your application."

                x "Get caught during your application, and you will be barred from applying to any other opportunity at the Company ever again."

                x "Get caught after your application, when you are on active duty, and the consequences are far worse."

                x "You look like a young, upstanding, ambitious person. Feel free to arrange another chat with me if you'd like to go over your application together."

            "(Move On) Actually, I'd like to make a case for why I'd be a good fit for the Counter-Espionage team.":

                x "I'm glad to hear you be so forward!"

                x "Tell me more. And spare no details."

                $ move_on = True
    
    h "This is going suspiciously well. Either he's the world's best actor, or he actually wants to be here speaking to aspiring professionals."

    h "I have all the information on the Office at my fingertips here. Just don't say anything stupid, and I'll be able to back you up."

    menu:

        "I know that the Office is looking for people with a great attention to detail...":

            call ch_07_anx_attention

        "I know that the Office is looking for people who know how to make things disappear...":

            call ch_07_anx_disappear

        "I know that the Office is looking for me. Because I'm the best.":

            call ch_07_anx_best
        
    return

label ch_07_anx_attention:

    "Bit about some famous Counter-Espionage bust that relied upon finding a literal needle in a haystack."

    return

label ch_07_anx_disappear:

    "Bit about some conspiracy theorist saying that the Company is disappearing people. Part takes it as a hilarious joke."

    return

label ch_07_anx_best:

    "Bit about the latest hire being some actual Nobel prize winning genius that Reynard's no match for"

    return

label ch_07_anxiety3:

    hide screen topleftdisplay
    hide screen topleft2

    x "Well, [mcname], I must say you've made an impression on me."

    x "I'd be happy to relay your name to the recruiters handling my division..."
    
    x "Of course, only if that's something that you would like."

    h "Congratulations, [mclast]. What a note to end your first networking event."

    menu:

        "Yes, I would love that.":

            x "Excellent."

        "No. I want to make sure I get in on my own merit on the open application, not because I got lucky speaking to you.":

            h "That is the most insane drivel I have ever heard."

            h "Take the bloody referral."

            x "Is that a nod I see? Excellent."
    
    x "There are just two things I need to move forward with that..."

    x "Firstly, can I confirm your name is [mcname] [mclast]?"

    menu:

        x "Firstly, can I confirm your name is [mcname] [mclast]?"

        "Yes.":

            pass
    
    x "Good, good. Secondly..."

    x "Could I remove the cranial implant in your head for inspection?"

    h "..."
    
    h "Hmm."

    menu:

        x "Could I remove the cranial implant in your head for inspection?"

        "Cranial implant? What cranial implant?":

            x "The one that's feeding you auditory and visual information."

            x "With someone else possibly speaking to you through the interface."

        "Cranial implant? Man, how did that get in my head?":

            x "Happens to the best of us. Trip and fall into an operating theatre, and suddenly you've got an implant."

            x "That feeds you auditory and visual information in a discreet fashion."

    x "They're an increasingly common tool for corporate espionage, you see."

    x "And we've needed to get better at spotting them on sight."

    x "Now, I don't think you're an agent from one of our competitors, [mcname]."

    x "Maybe you use it for convenience. Maybe you're bad with directions or conversation."

    x "But I need to do my job and make sure equipment of this sort that finds itself on Company grounds is thoroughly inspected."

    x "And I'm still willing to share your name with my colleagues handling recruitment."

    x "Please consent to my inspection."

    x "Or do you need time to confer with whoever's on the other side of that interface?"

    x "I'll give you a moment."

    h "..."

    menu:

        "What should I do?":

            h "Wait, wait, wait, wait, wait..."

            h "I'm thinking. I'm thinking!"

        "I'm going to consent.":

            h "Wait. WAIT!"

            h "You really are stupid. Think of what he's going to see!"

        "I'm not going to consent.":

            h "Wait, wait, we have to think about how we're going to do this!"

            h "I have no idea what's about to happen if you declare your intent not to consent."

    h "If there's any chance that he gets a record of what we've done here today, you and I are ruined."

    h "We've wilfully manipulated an employee into resigning and poisoned another."

    h "And worse still, it shows you aren't the well-researched applicant I've fought so hard to make you out to be!"

    h "And if you don't get hired as a result of this..."

    h "People are going to find other handlers. Other career coaches with better records."
    
    h "And I will be out of a job!"

    h "Do you know how terrifying that is? In this job market??"

    menu:

        "As a matter of fact, I do. Somebody made that abundantly clear to me.":

            h "Bah. Don't get sarcastic with me now."

        "I'm sure it can't be that bad.":

            h "Do I need to haul you into the bathroom again??"
        
    h "Here's what we do. We stall."

    menu:

        h "Here's what we do. We stall."

        "How?":

            h "For once this afternoon can you just do something without explicit step by step instruction?"

        "I'll do my best.":

            h "Our careers depend on it."

    h "I just need to find something. Anything. That will force this fellow to turn a blind eye."

    x "Just so you know, whatever you guys are discussing is probably traceable in your implant and therefore subject to inspection."

    h "Stall. Stall!"

    menu:

        "Before I give my answer on inspection, could I ask a few questions?":

            x "Of course. Happy to clarify anything."

    default ask_happen = False
    default ask_invasive = False
    
    while ask_happen == False or ask_invasive == False:

        menu:

            "What were to happen if I were to decline to be inspected?":

                x "Then I'd ask security to activate the implant detectors at the building's exits when you attempt to leave the building."

                x "We often leave them off, to save power to reach our sustainability goals."

                x "If something were to be detected, you would be detained."

                x "If nothing were to be detected, I would offer you a sincere apology and submit a report to my supervisors about this incident."

                x "You would of course, be within your rights to file a formal complaint."

                x "If you do have an implant on you, however, ..."

                x "Consenting to be inspected gives you the opportunity to clear your name sooner rather than later."

                h "... Give me something... anything..."

                $ ask_happen = True

            "Is the inspection procedure invasive?":

                x "Oh, hardly."

                x "In the past, we would actually have to sedate the individual and extract the hardware from the skull."

                x "That could get ugly, and we'd prefer not to have to do that."

                x "So now we've developed the technology to make a synthetic copy of the implant's memory without needing to make a single incision."

                x "If that is your concern, I can assure you that it is in your best interests to consent to an inspection swiftly."

                h "... Is this enough? Could this work...?"

                $ ask_invasive = True

    h "I have it!"

    return

label ch_07_anxiety4:

    h "Take a look, [mclast]. I've never had to do this deep a dive on the Company before, but I can't say I'm surprised."

    $ stacktopleft("counter_perfreport", True)

    h "No single organisation gets this powerful without breaking a few eggs."

    h "I know what you are, Part Tycholore."

    h "Let's let him know that we know, [mclast]."

    $ stacktopleft("counter_contents")

    menu:

        "You won't be inspecting anything...":

            x "Is there a reason why?"

    $ stacktopleft("counter_incident1")

    menu:

        "Because you don't want the world to know that the Counter-Espionage Office has stolen its competitors' secrets!":

            x "..."

    $ stacktopleft("counter_incident2")

    menu:

        "And has blackmailed people into joining the Company and not your competitors!":

            x "..."

    $ stacktopleft("counter_incident3")
    
    menu:

        "And is guilty of kidnapping, assassination, and even inciting insurrections!":

            x "..."
    
    x "If you believe the Company is guilty of any crimes, you are well within your rights to submit your suspicions to the local authorities."

    x "But please, I am just here to do my job at this event."

    x "Please consent to the inspection."

    h "Hmm. I suppose that was kind of an open secret, anyway."

    h "But let's see how he reacts when it gets personal, [mclast]."

    $ stacktopleft("july8_1")

    menu:

        "Well, what if I told you that I knew where you were on the night of July 8th this year?":

            x "..."

    $ stacktopleft("july8_2")

    menu:

        "And I knew the person you were meeting?":

            x "..."

    $ stacktopleft("july8_3")

    menu:
        
        "And what became of him?":

            x "..."

    x "Once again, if you have reason to believe that myself or any of my colleagues have broken the law, you are welcome to report it to the authorities."

    x "Of course, the Company will retain its right to provide a robust legal defence."

    x "Just as it reserves the right to prosecute any defamatory rumours unsubstantiated by court or arbitration proceedings."

    h "Not even a peep."

    h "Everyone has an angle. And you, have a family."

    $ stacktopleft("part_family_1")

    menu:

        "Are we going to kill his family?":

            x "Pardon?"

            h "Shut up! You just saw images of him vanishing someone and your first instinct is to threaten his family?"

            h "We can't touch his family, but maybe we can touch how his family sees him."

            h "Maybe it's not the authorities we should be leaking these images to."

    x "Have we come to a decision?"

    $ stacktopleft("part_family_2")

    menu:

        "Well, would you like what I know about July 8th to be shared with your loved ones?":

            x "..."

    $ stacktopleft("part_family_3")

    menu:

        "I know you have a son and a daughter...":

            x "..."

    $ stacktopleft("part_family_4")

    menu:

        "And I know they look up to you.":

            x "..."

    x "If you know their names, look them up."

    h "Oh."

    $ stacktopleft("part_family_5")

    h "I may have miscalculated."

    $ stacktopleft("part_family_6")

    x "Having attachments is an occupational hazard in my line of work. But the appearance of having a family can make one appear less threatening."

    x "As I said, the Company prepares you well to excel in this role."

    x "Now, I'm afraid that if you continue to delay giving an answer to my request for an inspection, I will accept it as a refusal."

    x "And the subsequent protocols will take place."

    hide screen topleftdisplay
    hide screen topleft2

    h "I don't think so."

    h "I signed a contract with you, [mclast]. I'm getting you out of this."

    h "As long as he's a hired hand of the Counter-Espionage Office, we can't touch him..."

    h "So maybe we need to find something about him he doesn't want the Counter-Espionage Office to know."

    h "It has to be somewhere here! Find it!"

    show screen topleftdisplay("sea_messy")

    menu:

        "I'll tell the Company about July 8th.":

            x "Whatever you think happened on July 8th, it was just routine business."

            x "Indeed, my supervisors are well aware of my activities day-to-day."
            
            pass

        "I'll tell the Company about your criminal record.":

            x "Whatever you think I've done, the Company hires with thorough background checks."

            x "I'm sure you'll find that whatever you're thinking of sharing has long since been known to them."

            pass

        "I'll tell the Company about your workplace romance.":

            x "Whatever encounter you think you've seen, it was most certainly for the mission."

            x "But you are welcome to develop your fantasies."

            pass

        "I'll tell the Company about your embezzlement.":

            x "As I said, we are well-compensated for our work."

            pass

        "I'll tell the Company about your psychological record.":

            $ good_route = True

            x "The Company would never dismiss an employee on the sole basis of a mental health condition."

            x "It is embarrassing to hear you think the Company would be that medieval."

        "I'll tell the Company you've been stealing office supplies.":

            x "Seriously?"
            
            pass

    hide screen topleftdisplay

    return

label ch_07_anxiety5:

    h "He's unfazed. He knows we have nothing."

    x "I'm afraid our time together is up."

    x "[mcname] [mclast], I have activated security to escort you off the floor to be examined."

    x "The results of their investigation will yield what they yield."

    x "Which may or may not have consequences for your future access to the premises of the Company..."

    x "And your future employment prospects."

    x "Have a wonderful day, and it was good to speak with you."

    call ch_07_anxiety_bad_end

    return

label ch_07_anxiety_bad_end:

    h "Well."

    h "Chin up, old chap, you win some, and you lose some."

    h "In this case, you might have lost quite a bit, considering how many other corporations are subsidaries of the Company"

    h "So your falling out with the Company might have some... fallout."

    h "Any case, my young fellow, this is where we part ways."

    h "I was forced to be multitasking, you see. This script I'm about to run ought to remove any trace of me from your implant."

    h "I can't say what other consequences it might have for the rest of your neurons, however."

    h "But you understand. I've got a career to take care of."

    h "Now, now, don't pout."

    h "It was all in the fine print."

    h "Pleasure working with you, [mcname] [mclast]."

    h "And all the best with your job search."

    return

label ch_07_anxiety6:

    h "He's unfazed. He knows we have nothing."

    x "I'm afraid our time together is up."

    x "[mcname] [mclast], I have activated security to escort you off the floor to be examined."

    h "Wait a minute."

    x "The results of their investigation will yield what they yield."

    h "That's a..."

    x "Which may or may not have consequences for your future access to the premises of the Company..."

    h "Single drop of sweat."

    x "And your future employment prospects."

    menu:

        "{i} Comply. {/i}":

            call ch_07_anxiety_bad_end

            return

        "I think I would be more concerned about your future employment prospects.":

            pass

    x "I'm afraid I don't know what you mean."

    x "As I said earlier, the Company's far too progressive to compromise any employee's future over a past record of mental health hurdles."

    menu:

        "But the sheer severity of your condition would make any organisation worried, wouldn't it?":

            x "..."

            x "I would not presume to know what it is you think that I have."

            x "But many employees are more than capable of performing their roles whilst managing their conditions responsibly."

            x "And I'm afraid I must, in good conscience, report the attitudes you are sharing to our recruiting team as well."

            x "The security team is here. They will take you away for further inspection."

            x "Once again, have a great day ahead."

            call ch_07_anxiety_bad_end

            return
        
        "But whether the Company is aware of your condition is a different matter, isn't it?":

            x "..."

            pass

        "But what if I had evidence it has materially affected your ability to do your job?":

            x "..."

            x "Then you would be bluffing."

            x "As I suspect you have been doing all evening."

            x "I am a professional, and I am proud of the work I have done for this organisation."

            x "The security team is here. They will take you away for further inspection."

            x "Once again, have a great day ahead."

            call ch_07_anxiety_bad_end

    show screen topleftdisplay("sea_revealed")

    menu:

        "You did not declare your condition when you first made your application.":

            pass

    menu:

        "And that would mean grounds for your immediate suspension.":

            pass

    menu:

        "Including all the protections that the Company affords to you by virtue of your contract.":

            pass

    h "..."

    x "..."

    x "Look at that. My next meeting's been cancelled, so we can have a little more time to chat."

    hide screen topleftdisplay

    x "Upon a second re-assessment of the situation, I've decided the security team won't be necessary."

    x "You've impressed me with your critical thinking and analytical skills, and you may well be a valuable asset to the Company."

    x "What say we put this conversation on the backburner?"

    x "We can circle back to it another time... or not."

    x "And in the meantime, I can put in a compelling word for you to join one of our departments."

    h "Oh my."

    h "You found it. Well done, [mclast]. Well done, indeed!"

    h "I must say, this perhaps warrants a sizable discount for my services. You've pulled your own weight today!"

    h "What say, 0.5 percent?"

    h "Never mind. We can settle contigencies later. Let's secure this connection and be done with this!"

    x "So? How does that sound for my action-item?"

    menu:

        "No objections from me.":

            $ referral = True

        "I also know about the April Incident.":

            pass

    return

label ch_07_anxiety_referral:

    x "Wonderful!"

    x "I'm sure it goes without saying, but..."

    x "I would truly appreciate your discretion regarding our conversations today."

    x "It would not be good for either of us if they were shared with management..."

    x "Or with our hiring team."

    x "Indeed, it would bode rather poorly for our continued future at this organisation."

    x "Be in touch soon, and I hope you receive an offer from us!"

    x "Looks like we can end our chat here for today, and I can give you back 7 minutes of your time."

    x "Have a great day ahead."

    return

label ch_07_anxiety_panic:

    h "[mclast]? What are we doing?"

    x "I'm not sure what you're implying."

    menu:

        "I know all about the April Incident. And I'll share it with your management, unless you offer me something more.":

            pass

    h "[mclast], we've already been offered a referral! There's nothing more under his purview that he can do for us!"

    x "Once again, I can't possibly comment on the existence of any such incident, ..."

    x "But now I know you're lying to me."

    h "You think I didn't try to pull this thread, [mclast]? I see what you're trying to do."

    h "But there's nothing on any hard drive or in the Cloud about this incident."

    h "Whatever it is, it's like it never happened."

    x "It also appears to me that we are no longer having this conversation in good faith."

    x "You would never have known what such an incident would have been..."

    x "Unless it was just by sheer dumb luck."

    menu:

        "Do you really want me to tell them what happened to your daughter?":

            call ch_07_anxiety_panic_averted

        "Do you really want me to tell them what happened to your dog?":

            call ch_07_anxiety_panic_averted

        "Do you really want me to tell them what happened to your past employer?":

            call ch_07_anxiety_panic_active

        "Do you really want me to tell them what happened to your parents?":

            call ch_07_anxiety_panic_averted

        "Do you really want me to tell them what happened at your high school?":

            call ch_07_anxiety_panic_averted

    return

label ch_07_anxiety_panic_averted:

    x "Wrong."

    x "You really are an impostor."

    x "The security team will see you on your way out."

    call ch_07_anxiety_bad_end

    return

label ch_07_anxiety_panic_active:

    x "... Impossible."

    x "But how?"

    menu:

        "I don't pretend to know things I don't.":

            pass

    menu:

        "Now tell me what more you can do for me, if this really concerns you so much.":

            pass

    x "No."

    x "You cheated. You got lucky."

    menu:

        "Tell me what more you can do, or every person in my network, and in their network, will know what you did.":

            pass

    menu:

        "And after you're fired, I'm not sure if anyone will ever hire you again.":

            pass

    show anxiety hyperventilating

    h "I don't know what magic you pulled, [mclast]..."

    h "But I think you may have made this connection less useful that it could have been."

    show anxiety breakdown

    h "You need to put some distance between yourself and him."

    h "Start walking away, now. Before he starts attracting more attention."

    show anxiety breakdown small

    h "Let others call for medical attention."

    h "..."

    h "What happened there?"

    hide anxiety

    h "Why take such a reckless risk claiming to know something you didn't?"

    menu:

        "I thought we could get even more out of him.":

            h "What were you expecting? That a connection would just offer you a job after ten minutes of speaking to them?"

            h "You're not just inexperienced, you've been living under a rock!"

        "I was curious to see what would happen.":

            h "... Curious?"

            h "..."

    h "I'm not sure if I'm comfortable with sustaining you as a client, [mclast]."

    h "I'd like to suspend our correspondence till I can propose a new contract."

    h "Something that protects my liabilities a little more."

    h "Go home. Whatever fruits come out of the past two hours of networking, you're free to follow up as you please."

    h "This has been Handler Career Coaching Services."

    "Connection lost."