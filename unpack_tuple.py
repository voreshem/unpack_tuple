#!/usr/bin/env python3

def unpack_paren(ntup_list):
    '''
    Takes list of numbers `[1,2,3,4,5]`,
        or list of str `['a','b','c','d','e']`,
        and returns formatted str.
    '''
    if len(ntup_list)==1:
        return f"({''.join(str(e) for e in ntup_list)})"

    elif len(ntup_list)==2:
        return f"{(len(ntup_list)-1)*'('}{', '.join(str(e) for e in ntup_list)})"

    else:
        return f"{(len(ntup_list)-1)*'('}" + f"{', '.join(str(e) for e in ntup_list[:2])}), " + f'{"), ".join(str(e) for e in ntup_list[2:])}' + ")"

def unpack_curly(ntup_list):
    if len(ntup_list) <= 1:
        ans = 'Expression undefined...'
    elif len(ntup_list) == 2:
        ans = '{' + '{' + str(ntup_list[0]) + '}' + ',' + '{' + str(ntup_list[0]) + ',' + str(ntup_list[1]) + '}' + '}'
    else:
        ans = '{' + str(unpack_curly(ntup_list[:len(ntup_list)-1])) + ',' + '{' + str(unpack_curly(ntup_list[:len(ntup_list)-1])) + ',' + str(ntup_list[len(ntup_list)-1:][0]) + '}' + '}'
    return ans


if __name__ == "__main__":
    ntup_list = input("\n\nEnter the n-tuple in the following format:\n(x₁,x₂,...,xn)\nWITH parentheses & NO spaces!\n\n")[1:-1].split(',')

    print("\n")
    print(unpack_paren(ntup_list))
    print("\n")

    '''
    if ntup_list[0] == ntup_list[1]:
        ntup_list[:2] = list(set(ntup_list[:2]))
    '''

    print(unpack_curly(ntup_list))
    print("\n")
