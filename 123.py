def create_tuple(text):
    original_tuple = tuple(text)
    return original_tuple

def create_new_tuple(original_tuple,step):
    new_tuple = original_tuple[::step]
    return new_tuple

def main():
     user_text = input('Input the text:')
     step = int(input('Input step:'))

     original_tuple = create_tuple(user_text)
     new_tuple = create_new_tuple(original_tuple,step)


     print('Original tuple:',original_tuple)
     print('New tuple:', new_tuple)

if __name__ == '__main__':
    main()