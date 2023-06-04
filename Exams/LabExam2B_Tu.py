'''
Grading Rubric: 25 points total
 0.5 pts: comment with EUID
   3 pts: function definition: syntax/name (1 pt), parameters (1 pt)
   2 pts: -- convert sentence string to list
   2 pts: -- generate random number between 2-4 (1 pt), assignment (1 pt)
 0.5 pts: -- print message indicating words with <= characters to be removed
   2 pts: -- convert string into list (1 pt), assignment (1 pt)
   2 pts: -- iterate through word list
   1 pt : -- -- if word length > min_length (discarded words are just ignored)
 1.5 pts: -- -- -- add words to list (many ways to do)
   2 pts: -- join list of strings as a single string
 0.5 pts: -- print modified sentence with words > min_length
   1 pt : prompt for (0.5 pts), read in sentence with punctuation (0.5 pts)
   2 pts: iterate through string (i.e., sentence)
   1 pt : -- if alphanumeric or space character
   1 pt : -- -- add character to new string
   1 pt : -- else (not alphanumeric or space character)
   1 pt : -- -- print message removing character
   1 pt : function call (0.5 pts), arguments (0.5 pts)
'''

#EUID
import random

def short_sentence(sentence):
    min_length = random.randint(2, 4)
    print('Words less than or equal to', min_length, 'characters will be removed.')
    word_list = sentence.split()
    new_list = []
    for word in word_list:
        if len(word) > min_length:
            new_list.append(word)
    mod_sent = ' '.join(new_list)
    print('Modified sentence:', mod_sent)

sentence = input('Enter a sentence: ')

new_sent = ''

for ch in sentence:
    if ch.isalnum() or ch.isspace():
        new_sent += ch
    else:
        print('Removing:', ch)

short_sentence(new_sent)
