def lexo(my_string):
    words = my_string.split()
    words.sort()
    for i in words:
        print( i )
if __name__=='__main__':
    my_string = " I am very Happy"\
    " Want to Drive"
lexo(my_string)
