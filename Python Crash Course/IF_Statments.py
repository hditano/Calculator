# If Statments on Lists

# Exercise 5.8

usernames = ['admin', 'hernan', 'sebastian', 'zoe', 'gimena']

# for username in usernames:
#     if username == 'admin':
#         print(f'Hello {username} you are clearly the boss right here. ')
#     else:
#         print(f'Hello {username} you are a generic ID')

#Exercise 5.9

# if usernames:
#    print('La lista tiene usernames')
# else:
#    print('La lista esta vacia')

#Exercise 5.10

# current_users = ['hernan', 'zoe', 'gimena', 'sebastian', 'marta']
# new_users = ['enrique', 'romina', 'sebastian', 'marta', 'run']

# for new_user in new_users:
#     if new_user in current_users:
#         print(f'[{new_user}] Name has been used')
#     else:
#         print(f'[{new_user}] Name is new')

#Exercise 5.11

ordinals = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for ordinal in ordinals:
    if ordinal == '2':
        print(f'{ordinal}nd')
    elif ordinal == '3':
        print(f'{ordinal}rd')
    else:
        print(f'{ordinal}th')


