from io import StringIO 

def word_count(string_io):
    current_char = string_io.read(1)
    last_char = ' '
    word_count = 0
    while current_char != '':
        if not current_char.isspace() and last_char.isspace():
            word_count += 1
        last_char = current_char
        current_char = string_io.read(1)
    # if last_char != ' ':
    #     word_count += 1
    return word_count


text = 'aaaaaa\tb'
string_io = StringIO(text)



print(word_count(string_io))
# print('hello world')