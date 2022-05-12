# find the first recurring char in a given set of character.

def recurring_char(given_string):    
    char_list = {}
    for chars in given_string:
        if chars in char_list:
            return chars
        else:
            char_list[chars] = 1
    return None

print(recurring_char('DABCDBCD')) # returns 'D' being the first char and repetitive



# 