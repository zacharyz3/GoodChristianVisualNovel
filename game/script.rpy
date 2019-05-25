define m = Character("Me", color="#0051ff")
define z = Character("Zander", color="#990000")
define pm = Character("Pretzel Woman", color="#800080")
define mm = Character("Micah", color="#ff4c4c")
define rp = Character("Reporter", color="#00c5ff")
define t = Character("Thomas", color="#1a8b27")
define fdl = Character("Front Desk Lady", color="#800080")
default micaClout = 0
default pickMitchell = False
default pickSeiji = False
default pickMason = False
default pickWilliam = False

label start:
    
    stop music fadeout 1.0

    scene bg black

    "My Room | May 29th, 2018"

    scene bg myroom

    play sound "knock1.mp3"

    "*Knock* *Knock* *Knock*"

    m "zzz..."
    
    play sound "knock1.mp3"
    
    "*Knock* *Knock* *Knock*"    
    
    m "zzz..."
    
    play sound "door kick down.mp3"
    
    play music "funkorama.mp3" fadein 2.0

    show zander happy suit at left

    z "FBI OPEN UP!"
        
    show zach tired noshirt at right
    
    m "Let me sleeeeeeep Zander... I'm tired...."
    
    "Last night I stayed up until 3:30am watching youtube because I couldn't sleep."
    
    z "First of all, it's 1:40pm; Second of all, did you forget what today is????"
    
    m "Wednesday...??"
    
    z "Ha HA very funny, but do you seriously not remember??"
    
    m "Nope."
    
    z "Wow. You really are brain damaged, Micah's coming to Illinois today."
    
    m "Oh yeah, I have to pick him up right?"
    
    "Micah is my friend who lives in Canada that I met through William and Thomas, two more of my friends. I promised Micah that I would pick him up at the airport today for the party the Good Christian Discord was having at my house."
       
    z "Yes, you have to be at the airport by 2:30."
    
    m "OH YEAH, I guess there's no time to shower then..."
    
    z "Maybe you should have thought about that before you decided not to set an alarm to wake up earlier."
    
    m "SHADDUP YA BUCKET OF BOLTS!"
    
    stop music fadeout 2.0
    
    scene bg black
    with fade    
    
    $ renpy.movie_cutscene("car_airport_scene.webm")
    
    jump airport

label airport:
    
    scene bg airport
    with dissolve
    
    play music "blue_skies.mp3" fadein 2.0
    
    show zach normal orange
    
    "Hmm... Which flight was Micah on..? Ah, it doesn't matter I'll just look around and I'll find him eventually... probably..."
    
    show zach shocked orange
    
    "Wait I think I see some pretzels!! I HAVE to buy some or I'M GONNA DIE, it's the rules."
    
    show pretzelwoman normal stand:
        xalign .25 yalign 1.0
    
    show zach normal orange:
        xalign .75 yalign 1.0
    
    pm "Hello SIR, would you like to purchase 1 PREZEL."
    
    m "OH ABSOLUTELY, I would LOVE to CONSUME 1 Prezel."
       
    pm "That will be 265 ROBUX."
    
    m "Ok, here is my debit card."
    
    play sound "error noise.mp3"
    
    pm "OH NO!! It appears that your debit card has been declined!!"
    
    show zach nervious orange
    
    m "Oh frick, do you guys accept McDonalds Gift Cards?"
    
    pm "No, but I'll tell you what, if you give me your McDonalds Gift Card, I'll pay for your meal."
    
    m "Deal!"
    
    pm "Please enjoy your meal!!!!"
    
    "I look the prezel woman dead in the eyes and say,"
    
    show zach devious orange
    
    m "You Too."
    
    scene bg cafeteria_airport
    with dissolve
    
    show zach trash orange:
        xalign .75 yalign 1.0
    
    m "Where the hell is the garbage can in this terrible place??"
    
    scene bg starbucks
    with dissolve
    
    show zach trash orange:
        xalign .75 yalign 1.0
    
    show mica normal garbagecan:
        xalign .25 yalign 1.0
    
    m "Oh, there it is! In the Startbucks!"
    
    show mica surprise garbagecan:
        xalign .25 yalign 1.0
        
    show zach shocked orange:
        xalign .75 yalign 1.0
    
    mm "SURPRISE!!!"
    
    show mica normal casual
    
    show zach normal orange
    
    m "Hi Micah! Why were you in the trashcan?"
    
    mm "Zander told me to greet you like this."
    
    m "Hmm... Ok then."
    
    m "Alright, now that we have you, we just have to get Thomas, Seiji, Mason, and William."
    
    stop music fadeout 2.0
    
    mm "Sounds like a plan!"
    
label carSceneOne:
    
    scene bg car
    with dissolve
    
    play music "go_to_church2.mp3" fadein 2.0
    
    show mica normal casual:
        xalign .75 yalign 1.0
        
    show zach normal orange:
        xalign .25 yalign 1.0
    
    mm "Who should we find next, Zach?"
    
menu:
    
    "William":
        $pickWilliam = True
        jump choseWilliam
    "Seiji":
        $pickSeiji = True
        jump choseSeiji
    "Mitchell":
        $pickMitchell = True
        jump choseThomas
    "Mason":
        $pickMason = True
        jump choseMason
        
label choseWilliam:
    
    m "Let's go find William next."
    
    mm "TO WILLIAM'S HOUSE!!"
    
    mm "Hey Zach?"
    
    m "Yeah?"
    
    mm "Can we stop for some food? I haven't eaten in 2 days."
    
    m "MICAH YOU NEED TO EAT YA GOOMBA"
    
    mm "Who are you, NOAH? I wasn't hungry."
    
    m "Ok, we'll go to..."
    
    jump restaurantChoice
        
label choseSeiji:
    
    return ##placeholder
    
label choseThomas:
    
    return ##placeholder
    
label choseMason:
    
    return ##placeholder
    
label restaurantChoice:
    
menu:
    
    "Papa John's":
        
        $micaClout = micaClout + 1
        
        m "How about we go to PAPA JOHNNNS"
        
        mm "Zach, I HATE pizza"
        
        m "But... Papa Johns is COOL"
        
        mm "Fine...."
        
        jump scenePapaJohns
        
    "Subway":
        
        $micaClout = micaClout - 1
        
        m "How about we go to Subway?"
        
        mm "You know... I don't really wanna order anything at Subway"
        
        m "Alright, suit yourself buddy"
        
        return ##placeholder
        
    "Burger King":
        
        $micaClout = micaClout + 1
        
        m "How about we go to Burger King?"
        
        mm "Great idea Zach, pure GENIUS."
        
        return ##placerholder
    
label scenePapaJohns:
    
    play music "Go_To_Church.wav" fadein 2.0

    scene bg papa_johns
    with dissolve
    
    show mica normal casual:
        xalign .25 yalign 1.0

    show zach happy orange:
        xalign .75 yalign 1.0
    
    m "Hmm... Mica how about we get a medium 2 topping pizza, I choose 1 topping, you choose the other."
    
    show mica sad casual
    
    mm "But Zaaaaach..."
    
    mm "I don't like pizza... The sauce is disgusting."
    
    show zach sad orange
    
    m "Fine, fine, let's get some buffalo wings, my zodiac says that the buffalo is my 3rd luckiest animal anyways."
    
    show zach normal orange
    
    show mica normal casual
    
    mm "Ok, I like wings."
    
    "We enjoyed our wings when something on the TV caught our eyes"
    
    scene bg tv
    
    play music "alien covenant.mp3" fadein 2.0
    
    rp "Fox 87 News coming at you live from Illinois"
    
    rp "All throughout Illinois, strange puppet figures have been appearing in restaurants."
    
    rp "Nobody knows where they come from, they seem to appear out of thin air!"
    
    rp "In other news, there have been 18 new missing person reports have came up in the past hour..."
    
    m "Hey Micah, doesn't that puppet look... Familiar to you?"
    
    mm "Is that...? No it's impossible... There's no way-"
    
    m "So it looks like Thomas to you too, huh?"
    
    mm "Yeah, but there's-"
    
    m "Micah, we need to go fast or we might be too late, let's get out of here"
    
    mm "Hold on, let's see if we can get any more information before we leave"
    
    m "Ok... Whatever you say..."
    
    rp " ...And now we will read off a list of the known missing persons:"
    
    rp "Greg Heffley, age 24, last known location, Arby's near Lake Zurich"
    
    rp "Stan Loonster, age 19, last known location, Burger King in Chicago"
    
    rp "Nowi Johnman, age 45, last known location, Domino's Pizza in Arlington Heights"
    
    rp "Winston Wang, age 17, last known location, Subway in Arlington Heights"
    
    rp "Joshua Manalanson, age 17, last known location, Burger King in Schaumburg"
    
    rp "Thomas H-"

    play sound "TV Static Turn Off Effect.mp3"

    "..."
    
    "The TV turns off by itself"
    
    m "NO!"
    
    mm "I... I can't believe it..."
    
    mm "The Good Christians might be..."
    
    m "DON'T SAY THAT!"
    
    m "C'mon Micah, let's go get William to help us look for Thom-"
    
    scene bg papa_johns
    
    play music "Jason Derulo - Whatcha Say.mp3"
    
    show thomas normal casual
    
    t "YO WHAT'S POPPING GAAAAAAAAAAMERS!"
    
    mm "Thomas! I'm so glad you're okay!"
    
    m "Thomas, how are you even here? You live in California!"
    
    t "Yeaaah BRUDES, I droove here for the PPPARRRTYY!"
    
    "Thomas takes a puff of his blunt."
    
    m "Thomas... There's a sign right there that says \"no smoking\""
    
    t "Oh shit, my bad brude."
    
    mm "Anyways, how's it going Thomas, have you noticed anything odd lately?"
    
    t "Yeah.. I met up with Seiji before this and he said he was gonna stop at McDonalds before we went to your house, but he hasn't texted me since."
    
    m "Hmm... This isn't good. Let's go to DePaul to see if he's there."
    
    jump sceneDePaulSeijiMeetUp
    
label sceneDePaulSeijiMeetUp:

    stop music

    scene bg depaul
    with dissolve

    show zach normal orange:
        xalign .25 yalign 1.0
    
    show mica normal casual:
        xalign .75 yalign 1.0
    
    m "Let's ask the front desk person if they know where Seiji is!"
    
    mm "As long as you're the one asking"
    
    hide mica normal casual
    
    show thomas normal casual:
        xalign .75 yalign 1.0
    
    t "Zach, that doesn't make any sense! Why would the front desk person know anything about Seiji's whereabouts?"
    
    m "Thomas, that's not a growth mindset, trust me, it will work!"
    
    scene bg depaul_front_desk
    with hpunch
    
    play music "Crowd_Talking.wav"
    
    show zach normal orange:
        xalign .1 yalign 1.0
        
    show frontdeskwoman normal stand:
        xalign .85 yalign 1.0
        
    show mica normal casual:
        xalign .5 yalign 1.0
    
    fdl "Hello! Welcome to DePaul University, how can I help you?"
    
    m "TELL ME WHERE MR. HAMADA IS"
    
    fdl "Ok. That will be 18 Robucks!"
    
    m "Uhh.... Do you accept McDonalds Gift Cards??"
    
    fdl "No, sorry, we only accept Robucks and Murder Miners Steam Keys"
    
    hide mica normal casual
    
    show thomas normal casual:
        xalign .5 yalign 1.0
    
    t "Don't worry guys, I've got this"
    
    "Thomas hands the front desk lady 18 Murder Miners Steam Keys"
    
    fdl "Thank you, have a nice day!"
    
    "The front desk lady hands Thomas Seiji's exact coordinates on google maps"
    
    show thomas normal casual: 
        xalign .85 yalign 1.0
    
    show mica normal casual:
        xalign .5 yalign 1.0
    
    m "Thank god you bought the Murder Miners 50 Friend pack Thomas!"
    
    mm "An absolute mastermind at work"
    
    t "Don't mention it guys, I got you!"
    
    m "Hmm... It looks as if Seiji is still at the McDonalds you were talking about, Thomas"
    
    mm "Maybe he's in the PlayPlace™!!"
    
    m "MICAH YOU'RE A GENIUS!"
    
    m "Ok guys, we know he's at the PlayPlace™ so let's just go find William"
    
    t "What?? That doesn't make any sense, we don't know that!!"
    
    m "No one cares Thomas, we're finding William now!!"
    
return


