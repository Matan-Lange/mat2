def revowrd(word: str) -> str:
    return word.lower()[::-1]


def countword() -> int:
    file = open('text.txt', 'r')
    words = file.read().split()

    word = words[0]
    file.seek(0)
    text_list = file.readlines()[1:]
    file.close()

    file = open('text.txt', 'w')
    file.write(word + '\n')

    counter = 1

    for line in text_list:
        newline = line.rstrip('\n')

        for w in newline.split():
            if revowrd(w) == word.lower():
                counter += 1
            file.write(revowrd(w) + " ")
        file.write('\n')

    file.close()
    return counter
print(countword())