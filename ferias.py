PERGUNTA = (
    "Quais são as suas férias ideais?\n"
    "  - PRAIA\n"
    "  - NEVE\n"
    "  - FAZENDA\n"
    "Digite sua escolha: "
)

ARTES = {
    'PRAIA': r"""
          |
        \ _ /
      -= (_) =-
        /   \         _\/_
          |           //o\  _\/_
   _____ _ __ __ ____ _ | __/o\\ _
 =-=-_-__=_-= _=_=-=_,-'|"'""-|-,_
  =- _=-=- -_=-=_,-"          |
    =- =- -=.--"
        Sol, mar e coco gelado!
""",
    'NEVE': r"""
   .  *   .   *   .  *   .   *   .  *
                  __
   _[___]_     -=(o '.
    (o o)         '.-.\
  --( : )--       /|  \\      (o_ (o_
   (  :  )        '|  ||      //\ (/)_
    `---'          _\_):,_    V_/_
 * . * . * . * . * . * . * . * . * . *
        Chocolate quente e neve!
""",
    'FAZENDA': r"""
          /\
         /  \          ^__^
        /____\         (oo)\_______
        | [] |         (__)\       )\/\       ,~.
        |____|             ||----w |         <(o )_
                           ||     ||            (__/
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              Ar puro e leite fresquinho!
""",
}


def montar_resposta(escolha):
    escolha = escolha.strip().upper()
    if escolha in ARTES:
        return f"Suas férias ideais: {escolha}\n{ARTES[escolha]}"
    return "Opção inválida. Escolha entre PRAIA, NEVE ou FAZENDA."