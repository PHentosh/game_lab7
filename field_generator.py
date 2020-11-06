def field(ulam_numbers: list, lucky_numbers: list, even_numbers: list)-> list:
    """
    This function takes three lists of Ulam, lucky and even numbers and returns a game field as a list
    """
    import random
    field = []
    heigh = 6
    length = 6
    list_of_nubers = []
    for i in range(int((heigh * length)/3)):
        random_number = random.randrange(0, len(ulam_numbers))
        list_of_nubers.append(ulam_numbers[random_number])

        random_number = random.randrange(0, len(lucky_numbers))
        list_of_nubers.append(lucky_numbers[random_number])

        random_number = random.randrange(0, len(even_numbers))
        list_of_nubers.append(even_numbers[random_number])

    indexs_used = []
    for i in range(heigh * length):
        random_position = random.randrange(0, len(list_of_nubers))
        while random_position in indexs_used:
            random_position = random.randrange(0, len(list_of_nubers))
        field.append(list_of_nubers[random_position])
        indexs_used.append(random_position)
    return field

def print_field(field: list):
    """
    This function takes list of lists and print each list in new line
    """
    import math

    length = len(field)

    for i in range(int(math.sqrt(length))):
        print('|', end = '')
        
        for j in range(int(math.sqrt(length))):

            spaces = 0

            if len(str(field[0])) != 3:
                spaces = 3 - len(str(field[0]))

            print(field.pop(0), ' ' * spaces, '|', sep = '', end = '')

        print()
