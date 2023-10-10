def ninetynine():
    print("We are going to play a game.I want you to pick a number then do a series\n of calculations.I bet I know what the result of those calculations will be!")
    print("\n\n")
    me_answer=int(input("*You* This will be the answer.Select a number 10-49:"))
    factor=99-me_answer
    player_answer=int(input("*Player* Pick any number 50-99:"))
    the_factor=factor+player_answer
    remove=int(str(the_factor)[1:3])+int(str(the_factor)[0])
    sub=player_answer-remove
    print(f"I said the answer was {me_answer} and the calculation result is {sub}")

ninetynine()
