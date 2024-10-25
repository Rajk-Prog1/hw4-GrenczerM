def minion_game(s: str) -> str:
    vowels = ["A", "E", "I", "O", "U"]

# Stuart: must start with constonents
    player1_score = 0
    
#Kevin: most start with vowels
    player2_score = 0
    
#create all possible iterations (substrings) of original string
    all_substr = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

#with this line we define all possible substring by starting from the first letter, then creating subtrings for all possible existing lengths by letter, and doing so by gradually strating from each letter of the original string
#source: https://www.geeksforgeeks.org/python-get-all-substrings-of-given-string/


    #number of points for player1
    player1_score = sum(1 for i in all_substr if i[0] == any(vowels))

#source: https://stackoverflow.com/questions/15375093/get-number-of-items-from-list-or-other-iterable-with-certain-condition

    #number of points for player2
    player2_score = sum(1 for i in all_substr if i[0] == (not any(vowels))) 
        
    
    if player1_score == player2_score:
        result = "Draw"

    elif player1_score > player2_score:
        result = ("Stuart " + {player1_score}) 

    elif player1_score < player2_score:
        result = ("Kevin " +{player2_score})

    return result
    pass
