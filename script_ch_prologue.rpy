# PROLOGUE

label ch_prologue:

    scene bg email_inbox with fade
    show screen inbox
    
screen inbox:
    imagebutton:
        auto "handleremail_%s.png" 
        action Jump("email_1") 
        focus_mask True
        

label email_1:

    window hide

    show screen centraldisplay("event_room_placeholder.png") with dissolve

    pause

    window show
    
    h "Hey, it's me."

    hide screen centraldisplay with dissolve

    mc "Who are you?"

    h "You've got mail."

    hide screen inbox

    return
