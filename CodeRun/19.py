import sys


def main():
    s = '(' + input() + ')'
    while not (s == '1' or s == '0'):
        if ')' in s:
            left_br = s.rfind('(', 0, s.find(')'))
            right_br = s.find(')')
            before = s[:left_br]
            after = s[right_br+1:]
            s = before + brackets(s[left_br+1:right_br]) + after
    print(s)

def brackets(s: str):
    while not (s == '1' or s == '0'):
        if '!' in s:
            before = s[:s.find('!')]
            after = s[s.find('!') + 2:]
            s = before + str(int(not int(s[s.find('!')+1]))) + after
        elif '&' in s:
            before = s[:s.find('&') - 1]
            after = s[s.find('&') + 2:]
            s = before + str(int(s[s.find('&')-1]) & int(s[s.find('&')+1])) + after
        elif s[1] == '|':
            after = s[3:]
            s = str(int(s[0]) | int(s[2])) + after
        else:
            after = s[3:]
            s = str(int(s[0]) ^ int(s[2])) + after
    return s


if __name__ == '__main__':
    main()