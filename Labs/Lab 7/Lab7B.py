import Lab7A # must also add if __name__ == '__main__': statement to Lab7A.py

def replace_word(sentence, target, replace):
    list1 = sentence.split()
    for index in range(len(list1)):
        if list1[index] == target:
            list1[index] = replace
    return ' '.join(list1)

sentence = input('Enter a sentence: ')
target   = input('Enter a word in sentence to replace: ')
replace  = input('Enter a replacement word: ')

new_str = replace_word(sentence, target, replace)

if sentence != new_str:
    print('Here is the new sentence:', new_str)
else:
    print('No changes were made to the original sentence')

# use Lab7A remove_letter() function
letter   = input('Enter letter to remove from sentence: ')

mod_sent = Lab7A.remove_letter(new_str, letter)

print('New sentence with letter', letter, 'removed:', mod_sent)
