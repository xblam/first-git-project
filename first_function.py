from random_word import get_random_word as get_word

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

word_list = ['ben','dan','bench','danch','eating','lunch']

word = get_word(word_list)

user_guess = (input(f'guess what the {len(word)} word is! '))

print(check_guess(user_guess, word))