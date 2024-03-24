# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

# and
# or
# not



# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


###


condition = 'Test'

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


###
# and   # Both should be right 
# or    # one should be right
# not   

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
   print('Admin Page')
else: 
    print('Bad Creds')

###
user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
   print('Admin Page')
else: 
    print('Bad Cred')

###

user = 'Admin'
logged_in = False

if not logged_in:
   print('Admin Page')
else: 
    print('Bad Cred')


###
user = 'Admin'
logged_in = False

if not logged_in:
   print('Please Log In')
else: 
    print('Welcome')






