#Read a text file and count the number of lines, words , and characters.
# Counting lines, words, and characters in a text file
def count_text_file(file_path):
    with open(file_path,'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines) 
    return line_count,word_count,char_count

file_path = 'example.txt'
lines,words,characters = count_text_file(file_path)
print(f'Lines: {lines}, Words: {words}, Characters: {characters}')


