# PROLOGUE

label ch_prologue:

    scene bg email_inbox with fade
    show screen inbox
    
screen inbox:
    imagebutton auto "handleremail_%s.png" action Jump("email_1") focus_mask True
        
        

label email_1:
        
    h "Hey, it's me."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    h "Hey, it's me."

    mc "Who are you?"

    show email a

    h "You've got mail."

    return
