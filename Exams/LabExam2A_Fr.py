'''
Grading Rubric: 25 points total
 0.5 pts: comment with EUID
   3 pts: function definition: syntax/name (2 pts), parameters (1 pt)
   2 pts: -- iterate over word list
   1 pt : -- -- if word length = avg_length
 1.5 pts: -- -- -- add words to list (many ways to do)
   1 pt : -- -- else (not avg_length)
 0.5 pts: -- -- -- print message word discarded
   2 pts: -- join list of strings as a single string
   2 pts: -- return new string
   1 pt : prompt for (0.5 pts), read in phrase (0.5 pts)
   1 pt : initialize sum and number of words to 0 (0.5 pts each)
   2 pts: convert string into list (1 pt), assignment (1 pt)
   2 pts: iterate over word list 
   1 pt : -- add word length to sum
   1 pt : -- increment word counter
   1 pt : compute average length of words in phrase
 1.5 pts: function call (0.5 pts), arguments (0.5 pts), assignment (0.5 pts)
   1 pt : print message with average word length and new string
'''

#EUID

def find_fixed(word_list, avg_length):
    new_list = []
    for word in word_list:
        if len(word) == avg_length:
            new_list.append(word)
        else:
            print('Discarded word:', word)
    new_str = ' '.join(new_list)
    return new_str


phrase = input('Enter a phrase: ')

my_sum = 0
num_words = 0
word_list = phrase.split()
for word in word_list:
    my_sum += len(word)
    num_words += 1

avg_length = my_sum // num_words

new_str = find_fixed(word_list, avg_length)

print('Average', avg_length, 'letter word string:', new_str)



