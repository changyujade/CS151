file = open("sample.txt", "r")

number_of_lines = 0
number_of_words = 0
number_of_characters = 0
number_of_paragraphs=0


for line in file:
    line = line.strip("\n")
    words = line.split()
    number_of_lines += 1
    number_of_words += len(words)
    number_of_characters += len(line)
    #number_of_sentences = line.count('.')+line.count('?')
    if line == (""):
        number_of_paragraphs += 1 
        

file.close()

print("number of sentences:", number_of_lines, "words:", number_of_words, "characters:", number_of_characters,'paragraphs:',number_of_paragraphs)





