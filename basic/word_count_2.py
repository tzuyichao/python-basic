def preprocessing(line):
    return line.lower().replace(".", "").replace(",", "")

with open('word_count.tst') as infile:
    text = infile.readlines()
    line_count = len(text)
    word_count = 0
    char_count = 0
    for line in text:
        line = preprocessing(line)
        terms = line.split()
        word_count += len(terms)
        char_count += len(line)
    print("File has {0} lines, {1} words, {2} characters".format(line_count, word_count, char_count))