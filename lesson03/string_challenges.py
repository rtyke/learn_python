# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв а в слове
word = 'Архангельск'
print(len(word))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 'аоиеёэыуюя'
vowels_in_word = [char for char in word.lower() if char in vowels]
print(len(vowels_in_word))
# vowels_in_word = sum([word.lower().count(vowel) for vowel in vowels])
# print(vowels_in_word)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(' ')))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split(' '):
    print(word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
words = sentence.split(' ')
words_length = [len(word) for word in words]
average_word_length = sum(words_length)/len(words_length)
print(average_word_length)



