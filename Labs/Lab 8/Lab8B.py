def add_to_dict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist, wordfreq)))

wordstring = input('Enter a sentence: ')

wordlist = wordstring.split()

wordfreq = []

for word in wordlist:
    wordfreq.append(wordlist.count(word))

print('Word list:', wordlist)
print('Word freq:', wordfreq)

worddict = {}

worddict = add_to_dict(wordlist)

for key, value in worddict.items():
    print('{:9}: {}'.format(key, value))
