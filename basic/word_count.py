
sample_string = "To be or not to be"
occurrences = {}
for word in sample_string.lower().split():
    occurrences[word] = occurrences.get(word, 0) + 1

for word in occurrences:
    print("The word", word, "occurs", occurrences[word], "times in the string")

infile = open('word_count.tst')
lines = infile.read().split("\n")

line_count = len(lines)
word_count = 0
char_count = 0

for line in lines:
    words = line.split()
    word_count += len(words)
    char_count += len(line)

print("File has {0} lines, {1} words, {2} characters".format(line_count, word_count, char_count))

