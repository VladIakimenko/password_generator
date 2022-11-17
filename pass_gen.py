from random import choice

def pass_gen(length, inclusions_list, exclude=False):
    possible_inclusions = {
        'digits': '0123456789',
        'lowercase_letters': 'abcdefghijklmnopqrstuvwxyz',
        'uppercase_letters': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'punctuation': '!#$%&*+-=?@^_.',
                          }
    exclusion = 'IilL1o0O'

    raw_pass_char = ''
    for item in inclusions_list:
        raw_pass_char += possible_inclusions[item]

    if exclude:
        excluded_raw_pass_char = ''
        for c in raw_pass_char:
            excluded_raw_pass_char += c if c not in exclusion else ''
        raw_pass_char = excluded_raw_pass_char

    password = ''
    for _ in range(length):
        password += choice(raw_pass_char)

    return password

def main():
    inclusions_list = []
    reply = ''
    cmd = ''
    exclude = False

    print('Welcome to safe password generator!\n')

    while reply not in ('y', 'n', 'yes', 'no'):
        reply = input('Include digits? "y" or "n"\t').strip().lower()
        if reply in ('y', 'yes'):
            inclusions_list.append('digits')
    else:
        reply = ''

    while reply not in ('y', 'n', 'yes', 'no'):
        reply = input('Include capitals? "y" or "n"\t').strip().lower()
        if reply in ('y', 'yes'):
            inclusions_list.append('uppercase_letters')
    else:
        reply = ''

    while reply not in ('y', 'n', 'yes', 'no'):
        reply = input('Include lowercase? "y" or "n"\t').strip().lower()
        if reply in ('y', 'yes'):
            inclusions_list.append('lowercase_letters')
    else:
        reply = ''

    while reply not in ('y', 'n', 'yes', 'no'):
        reply = input('Include symbols? "y" or "n"\t').strip().lower()
        if reply in ('y', 'yes'):
            inclusions_list.append('punctuation')
    else:
        reply = ''

    while reply not in ('y', 'n', 'yes', 'no'):
        reply = input('Do you want similar-looking chars '
                      '(like "IilL1o0O") to be used? "y" or "n"\t')
        reply = reply.strip().lower()
        if reply in ('n', 'no'):
            exclude = True

    while not reply.isdigit():
        reply = input('Choose password length:\t').strip()
    else:
        length = int(reply)

    print("""
            Keep pressing enter to generate a password...
            Type "back" or "b" to customise options again.
          """)

    while cmd not in ('b', 'back'):
        cmd = input(pass_gen(length, inclusions_list, exclude))
    else:
        print('\n\n\n')

while True:
    main()