# The characters names and images of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Random Voice")
define c = Character("Charía")
$ p = "",

# Declare image used for each character

image Gbody = "Gbody.png"
image TBody = "TBody.png"
image BG = "BG.png"
image Charia = "charia.png"

# The game starts here.

label start:
    play music "audio/608630__shadydave__jungle-loop.mp3"
    show BG

    $ p = renpy.input("My name is...")
    $ p = p.strip()
    if p == "":
     $ p = "Jeniffer"

    "The past is forgotten, and the only concern is the present."
    "Humanity has long moved past gods and worship, the roots of life are weak."

    show Charia with dissolve

    c "The gods are weak."
    c "Perfect timing to strike once more."

    hide Charia with dissolve

    p "Crap… {w}Why adult life has to be that way?"

    "{i}You got a new message"

    menu:
     "pick phone":
      "Don’t forget your roots."

      p "My roots? {w}What kind of prank is that?"
      p "I have better things to do."

      "{i}You got a new message"
      p "If this is one of my friends I swear that I…"
      "{i}You got a new file. Open it?"
      image JBody = "JBody.png"
      #flags
      $ warrior = False
      $ healer = False
      $ mage = False
      menu:
       "yes":
        show JBody
        with dissolve
        pause 0.1
        hide JBody
        with dissolve

        "[p]."

        show Gbody
        with dissolve
        hide Gbody
        with dissolve

        "We summon you by your soul contract."

        show TBody
        with dissolve
        pause 0.1
        hide TBody
        with dissolve

        "It is time to rise once again, shaman."
        jump route
    return

label route:
    menu:
     "Who is calling you?"
     "The Warrior":
      $warrior = True
      $n = "Tupã"
      jump calling
     "The Healer":
      $healer = True
      $n = "Jaci"
      jump calling
     "The Mage":
      $mage = True
      $n = "Guaraci"
      jump calling

label calling:
 if warrior == True:
  show  TBody
  with dissolve

  n "Greetings, human."
  p "Who… Are you?"
  n "You know the answer, little shaman. Don’t test my patience."
  p "It can’t be…"
  n "Oh, It can’t? Are you sure?"
  p "My apologies… Lord Tupã."
  n "Good. {w}In this age, gods are long forgotten by humanity"
  n "But you, who carries the blood of our medium receptacle, shall never forget."
  p "What… is this about?"
  n "Great me! You don’t know?"
  n "No wonder my children are so weak."
  n "You carry the blood of a shamanic lineage."
  n "It is faint, but I can still feel it."
  n "Our connection to the Earth depends on humanity\'s beliefs. The stronger they are, the greater we get."
  n "Nowadays, the mystical arts are close to nonexistent. Do you know what that means?"
  menu:
   "Are you dying?":
    n "Ha! {w}foolish being. Of course not"
    p "You are."
    n "Excuse me?!"
    jump lore
   "Could it be…?":
    p "Oh, no… That’s terrible."
    n "Exactly my point."
    p "Is this the end of soap operas?"
    n "Yes, the end of-"
    n "The end of soap operas?"
    n "Do you think I would come here for some foolish soap opera?"
    p "Aren’t they the best example of art?"
    n "You have more important things to worry about."
    p "Such as…?"
    n "Such as a giant jaguar trying to destroy your so beloved world."
    p "oh… {p}OH!"
    jump lore
   "The end of the world?":
    n "Ah! I see that you have a sharp intuition."
    p "Wait! Hold up! I was just kidding."
    n "Well… I’m not."
    hide TBody
    with dissolve
    jump lore
 elif healer == True:
  show JBody
  with dissolve

  n "Ah, you came."
  p "So pretty…"
  n "Well, thank you, little shaman. I’m Jaci, pleased to meet you."
  p "Little shaman? Are you talking about me?"
  n "Are you seeing someone else?"
  p "Fair point. {w}but I don’t remember being a shaman."
  n "You don’t need to. {w}Your body does."
  n "See?"

  hide JBody
  with dissolve
  jump lore

 elif mage == True:
  show Gbody
  with dissolve

  n "It’s about time. {w}I’ve been trying to talk to you for ages."
  p "And you are…?"
  n "Ha! The great Guaraci! Feel honored that I need your help, forgotten shaman."
  p "Guaraci? Like in the god of the Sun?"
  n "Who else would I be?"
  p "A freak?"
  n "A fre-! {w}Have you lost your mind?"
  p "That’s what I’ve been trying to ask you…"
  n "Humans…"
  n "Look, forget about introductions. {w}There’s something that you need to know…"

  hide Gbody
  with dissolve
  jump lore

label lore:
 if warrior == True:
  show TBody
  with dissolve
  pass

 if healer == True:
  show JBody
  with dissolve
  pass

 if mage == True:
  show Gbody
  with dissolve
  pass

 if warrior == True:
  n "When I created the original humans…"
  pass
 else:
  n "When Tupã created the original humans…"
  pass
 n "They had three sons."
 n "The first of their sons was Tumé Arandú, the great prophet."
 n "Second, was Marangatú, a benevolent and generous leader of his people."
 n "Their third son was Japeusá, who was from birth considered a liar, a thief, and a trickster."
 n "you, [p], are the last descendant of Tumé Arandú. You are the prophet birthed to serve us."
 p "A prophet you say?"
 n "Yes. The only humans allowed to have direct contact with gods."

 if warrior == True:
  p "okay… {w} but what about that jaguar you told me earlier?"
  n "I’ll get there. Don’t be impatient."
  pass
 else:
  pass
 p "What do you want from me?"
 n "The gods' power comes from the beliefs of humans."
 n "The mythic world ceased to exist almost entirely."
 n "That means that we are losing our soberany over Earth."
 n "On the other hand, Charía, the celestial Jaguar, gets stronger over time."
 n "If things continue this way, they will be strong enough to kill both the god of the Sun and the goddess of the Moon…"
 n "… And Earth will fall into a suffocating darkness until it no longer exists."
 n "This cannot happen."

 if warrior == True:
  n "Take this. Use the Taquara as a weapon to defeat Charía."
  hide TBody
  with dissolve
  jump minigame
 elif healer == True:
  n "Take this. Use the Taquara as an instrument to enchant Charía."
  hide JBody
  with dissolve
  jump minigame
 elif mage == True:
  n "Take this. Use the Taquara as a recipient to seal Charía."
  hide Gbody
  with dissolve
  jump minigame

label minigame:
 show Charia with dissolve

 if warrior == True:
  menu:
   "This will be a minigame later on."
   "Attack":
    "You used the Taquara as a weapon to save the world."
    "Congratulations, we are in peace now."
    "End game."
    hide Charia
    return
 elif healer == True:
  menu:
   "This will be a minigame later on."
   "Sing":
    "You used the Taquara as an instrument to calm Charia down."
    "Congratulations, we are in peace now."
    "End game"
    hide Charia
    return
 elif mage == True:
  menu:
   "This will be a minigame later on."
   "Chant":
    "You used the Taquara as an recipient to seal it down"
    "Congratulations, we are in peace now."
    "End game"
    hide Charia
    return

    