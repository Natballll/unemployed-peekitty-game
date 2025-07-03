# PROLOGUE


init python:
    def name_func(newstring):
        store.mcname = newstring

        
    def lastname_func(newstring):
        store.mclast = newstring

# screens

screen inbox:
    imagebutton auto "prl/handleremail_%s.png" action Jump("email_1") focus_mask True
        
screen email_1:
    imagebutton auto "prl/pdf_%s.png" action Jump("LiabilityPDF") focus_mask True
    imagebutton auto "prl/reply_%s.png" action Show("reply_menu") focus_mask True

screen reply_menu:
    add "prl/sugreplies.png"
    imagebutton auto "prl/mvng_%s.png" action Jump("reply_moving") focus_mask True
    imagebutton auto "prl/pymnt_%s.png" action Jump("reply_payment") focus_mask True

screen reply_mvng:
    imagebutton auto "prl/email1_%s.png" action Jump("email_1") focus_mask True
    imagebutton auto "prl/reply_%s.png" action Show("reply_mvng_menu") focus_mask True

screen reply_mvng_menu:
    add "prl/sugreplies.png"
    imagebutton auto "prl/pymnt2_%s.png" action Jump("reply_payment") focus_mask True

screen reply_pymnt:
    imagebutton auto "prl/email1_%s.png" action Jump("email_1") focus_mask True
    imagebutton auto "prl/reply_%s.png" action Show("reply_pymnt_menu") focus_mask True

screen reply_pymnt_menu:
    add "prl/sugreplies.png"
    imagebutton auto "prl/mvng2_%s.png" action Jump("reply_moving") focus_mask True

# events

label ch_prologue:

    scene bg email_inbox with fade
    show screen inbox
    pause 

label email_1:
    hide screen reply_mvng
    hide screen reply_mvng_menu
    hide screen reply_pymnt
    hide screen reply_pymnt_menu
    hide screen reply_menu
    hide screen LiabilityPDF
    hide screen inbox
    scene bg email_1
    show screen email_1
    pause

label LiabilityPDF:
    hide screen reply_menu
    hide screen email_1
    show screen LiabilityPDF
    pause

label reply_moving:
    hide screen reply_mvng
    hide screen reply_mvng_menu
    hide screen reply_pymnt
    hide screen reply_pymnt_menu
    hide screen reply_menu
    hide screen LiabilityPDF
    hide screen email_1
    scene bg reply_mvng
    show screen reply_mvng
    pause


label reply_payment:
    hide screen reply_mvng
    hide screen reply_mvng_menu
    hide screen reply_pymnt
    hide screen reply_pymnt_menu
    hide screen reply_menu
    hide screen LiabilityPDF
    hide screen email_1
    scene bg reply_pymnt
    show screen reply_pymnt
    pause


label prologue_end:
    hide screen reply_mvng
    hide screen reply_mvng_menu
    hide screen reply_pymnt
    hide screen reply_pymnt_menu
    hide screen reply_menu
    hide screen LiabilityPDF
    hide screen email_1
    h "It's a pleasure to meet you, [mcname] [mclast]."    

