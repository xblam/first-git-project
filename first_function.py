def check_guess(guess, word):
    answer = ''
    for i in range(len(word)):
        if guess[i] == word[i]:
            answer += word[i]
        else:
            answer += '*'
    return answer

print(check_guess('benny','denns'))