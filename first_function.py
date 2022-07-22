def check_guess(guess, word):
    answer = ''
    for i in range(len(word)):
        if guess[i] == word[i]:
            answer += guess[i]
        elif guess[i] in word:
            answer += guess[i].upper()
        else:
            answer += '*'
    return answer

print(check_guess('benny','denna'))