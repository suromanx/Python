def create_tuple(user_text):
    original_tuple = tuple(user_text)
    return original_tuple

def the_new_tuple(original_tuple, step):
    new_tuple = original_tuple[::step]
    return  new_tuple

def main():
    user_text = input('Input number')
    step = int(input('Input step'))

    original_tuple = create_tuple(user_text)
    new_tuple = the_new_tuple(original_tuple,step)


    print('The original tuple:', original_tuple)
    print('New tuple:', new_tuple)


if __name__ == '__main__':
    main()
