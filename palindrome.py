### Write a function that returns a boolean stating whether or not
### a given sentence is a palindrome. This function should ignore spaces and casing.
### eg 'racecar' => True
###    'RaCeCar' => True
###    'Do geese see God' => True

def palindrome(sentence):
    sentence = sentence.replace(" ", "").lower()
    rev_sentence = sentence[::-1]

    for i in range(len(sentence)):
        if sentence[i] != rev_sentence[i]:
            return False

    return True


def main():
    print(palindrome('Do geese see God'))
    print(palindrome('rokjhuiir'))


if __name__ == '__main__':
    main()
