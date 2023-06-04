def remove_letter(sentence, letter):
    new_str = ""
    for ch in sentence:
        if ch != letter:
            new_str += ch
    return new_str

if __name__ == '__main__':
    sentence = input('Enter a sentence: ')
    letter   = input('Enter letter to remove from sentence: ')

    mod_sent = remove_letter(sentence, letter)

    if sentence == mod_sent:
        print('No letter', letter, 'removed from:', mod_sent)
    else:
        print('New sentence with letter', letter, 'removed:', mod_sent)
