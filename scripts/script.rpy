# The characters names and images of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Voz")
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

    $ p = renpy.input("Meu nome é...")
    $ p = p.strip()
    if p == "":
     $ p = "Jeniffer"

    "O passado foi esquecido e a única preocupação é o presente."
    "A humanidade, há muito, já superou os deuses e a adoração, as raízes da vida estão fracas."

    show Charia with dissolve

    c "Os deuses estão fracos."
    c "Essa é a hora perfeita para atacar de novo."

    hide Charia with dissolve

    p "Aff… {w}Por que a vida adulta é difícil assim?"

    "{i}Você tem uma nova mensagem"

    menu:
     "Ler":
      "Não esqueça suas raízes."

      p "Minhas raízes? {w}Que tipo de trote é esse?"
      p "Eu tenho mais o que fazer."

      "{i}Você tem uma nova mensagem"
      p "Se for um dos meus amigos de novo, eu juro que vou…"
      "{i}Você tem um novo arquivo. Abrir?"
      image JBody = "JBody.png"
      #flags
      $ warrior = False
      $ healer = False
      $ mage = False
      menu:
       "Sim":
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

        "Nós convocamos você por nosso contrato espiritual."

        show TBody
        with dissolve
        pause 0.1
        hide TBody
        with dissolve

        "É chegada a hora de se levantar novamente, shaman."
        jump route
    return

label route:
    menu:
     "Quem está te chamando?"
     "O guerreiro":
      $warrior = True
      $n = "Tupã"
      jump calling
     "A curandeira":
      $healer = True
      $n = "Jaci"
      jump calling
     "O mago":
      $mage = True
      $n = "Guaraci"
      jump calling

label calling:
 if warrior == True:
  show  TBody
  with dissolve

  n "Saudações, humano."
  p "Quem… é você?"
  n "Você sabe a resposta, pequeno shaman. Não teste a minha paciência."
  p "Não pode ser…"
  n "Ah não pode? Tem certeza?"
  p "Minha desculpas… Lord Tupã."
  n "[Otimo. {w}Nos tempos atuais, a humanidade não liga mais para os deuses"
  n "Mas você, quem carrega o sangue médium, jamais deve esquecer."
  p "O que… é isso tudo?"
  n "Pelo sagrado eu! Você não sabe?"
  n "Não me admira que minhas crianças estão tão fracas."
  n "Você carrega o sangue da linhagem shamanica."
  n "Está {i}beeem{/i} dissovida, mas posso sentir."
  n "Nossa conexão com a Terra depende da crença da humanidade. Quanto mais forte ela for, mais forte seremos."
  n "Hoje em dia, as artes místicas quase não existem. Sabe o que isso significa?"
  menu:
   "Você está morrendo?":
    n "Ha! {w}ser tolo. Claro que não"
    p "Você está."
    n "Como é?!"
    jump lore
   "Poderia ser…?":
    p "Ah, não… Isso é terrível."
    n "Meu ponto, precisamente."
    p "Esse é o fim dos doramas?"
    n "Sim, o fim dos-"
    n "O fim dos doramas?"
    n "Você acha que eu viria até aqui por causa de uma coisa boba como dorama?"
    p "Não são o mais fino exemplo de arte?"
    n "Você tem coisa mais importante para se preocupar."
    p "Tipo…?"
    n "Tipo uma onça pintada gigante tentando acabar com o seu mundo."
    p "ah… {p}AH!"
    jump lore
   "O fim do mundo?":
    n "Ah! Vejo que você tem uma intuição forte. Vai te fazer bem nessa jornada."
    p "Calma! Alto lá! Eu estava brincando."
    n "Bem… Eu não."
    hide TBody
    with dissolve
    jump lore
 elif healer == True:
  show JBody
  with dissolve

  n "Ah, você veio."
  p "Que bonita…"
  n "Oh, obrigada, pequeno shaman. Sou a Jaci, prazer em te conhecer."
  p "Pequeno shaman? Você está falando de mim?"
  n "Está vendo mais alguém?"
  p "Justo. {w}mas eu não me lembro de ser um shaman."
  n "Não precisa lembrar. {w}Sua alma já o faz."
  n "Vê?"

  hide JBody
  with dissolve
  jump lore

 elif mage == True:
  show Gbody
  with dissolve

  n "Já era hora. {w}Estou tentando falar com você de hoje."
  p "E você é…?"
  n "Ha! O grande Guaraci! Sinta-se em honra por eu precisar da sua ajuda, shaman esquecido."
  p "Guaraci? Como o deus do Sol?"
  n "Quem mais eu seria?"
  p "Um lunático?"
  n "Um lu-! {w}Perdeu a cabeça?"
  p "É isso que estou tentado te perguntar…"
  n "Humanos…"
  n "Veja bem, esqueça as introduções. {w}Tem uma coisa que você precisa saber…"

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
  n "Quando eu criei os humanos originais…"
  pass
 else:
  n "Quando Tupã criou os humanos originais…"
  pass
 n "Haviam três irmãos."
 n "O primeiro deles era Tumé Arandú, o grande profeta."
 n "Depois, veio Marangatú, um liver generoso e benevolente."
 n "O terceiro filho foi Japeusá, considerado um mentiroso desde o nascimento, um ladrão e enganador."
 n "Você, [p], é o último descendente de Tumé Arandú. Você é o profeta nascido para salvar os humanos."
 p "Um profeta...?"
 n "Sim. O único tipo permitido a ter contato direto conosco, deuses."

 if warrior == True:
  p "Tá… {w} mas e sobre aquela onça pintada que você me disse mais cedo?"
  n "Vou chegar lá. Não seja impaciente."
  pass
 else:
  pass
 p "O que quer de mim?"
 n "O poder dos deuses vem da crença de vocês."
 n "O mundo místico está deixando de existir."
 n "Isso significa que estamos predendo a influência na Terra."
 n "Por outro lado, Charía, a onça celestial, fica mais forte com o tempo."
 n "Se as coisas continuarem assim, Charía terá força o suficiente para capturar o deus do Sol e a duesa da Lua…"
 n "… E a Terra vai cair em uma escuridão sufocante até deixar de existir."
 n "This cannot happen."

 if warrior == True:
  n "Pegue isso. Use a Taquara como uma arma para derrotar Charía."
  hide TBody
  with dissolve
  jump minigame
 elif healer == True:
  n "Pegue isso. Use a Taquara como um instrumento para encantar Charía."
  hide JBody
  with dissolve
  jump minigame
 elif mage == True:
  n "Pegue isso. Use a Taquara como um recipiente para selar Charía."
  hide Gbody
  with dissolve
  jump minigame

label minigame:
 show Charia with dissolve

 if warrior == True:
  menu:
   "Aqui vai ter um minijogo depois."
   "Atacar":
    "Você usou a Taquara Como uma arma para salvar o mundo."
    "Parabéns, estamos em paz agora."
    "Fim do jogo"
    hide Charia
    return
 elif healer == True:
  menu:
   "Aqui vai ter um minijogo depois."
   "Cantar":
    "Você usou a Taquara como um instrumento para acalmar Charía."
    "Parabéns, estamos em paz agora"
    "Fim do jogo"
    hide Charia
    return
 elif mage == True:
  menu:
   "Aqui vai ter um minijogo depois."
   "Lançar feitiço":
    "Você usou a Taquara como um recipiente para selá-la"
    "Parabéns, estamos em paz agora"
    "Fim do jogo"
    hide Charia
    return

    