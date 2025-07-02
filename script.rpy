# MASTER SCRIPT
# owo

define mc = Character("Main Character")
define h = Character("Handler")

$ bad_route = True

label start:

    call ch_prologue
    call ch_01_improv
    call ch_02_ambiguous
    call ch_03_pet
    call ch_04_dead

    if bad_route == True:
        call ch_05_improv2
        call ch_06_gut
        call ch_07_anxiety

    if bad_route == False:
        call ch_08_crashout
        call ch_09_waiter
        call ch_10_maintenance
        call ch_11_security

    return
