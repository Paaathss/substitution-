# substitution method
newline = re.sub("programming", "high", line1)
print(newline)
line1 = "python is simple. python is powerful python is great"
newline1 = re.sub("python", "C", line1, count=2)
print(newline1)
line2 = "4253243432 5324 python is 3423324 programming language python is a high level language"

# All numerical characters are selected.

new1line2 = re.sub("\d", "X", line2)
print(new1line2)

# All characters except numerical characters are selected.
new2line2 = re.sub("\D", "X", line2)
print(new2line2)

# All spaces are selected.
new3line2 = re.sub("\s", "X", line2)
print(new3line2)

# All characters except spaces are selected.
new4line2 = re.sub("\S", "X", line2)
print(new4line2)

#Excluded substitution

import re

line = '66788 ## $$ python  is  67890 @ # programming $$$ language python'

x = re.sub('[^a-z,A-Z,0-9,\s]',' ',line)

print(x)

# split method

import re

line1 = 'language python is high level language'

x = re.split("\s",line1)

print(x)

# max split

import re

line = 'Language python is high level language, haai'

x =re.split("\s",line1,1)

print(x)


#findall

import re

line1 = 'python is an a1234567 language 34567890 is high level 09876543 lang 677 9876'

x = re.findall('\d',line1)

print(x)
#/d+

import re
line1 = 'python is an a1234567 language 34567890 is high level 2345'
x = re.findall('[0-9]+',line1)

print(x)



import re
line1 = 'python +9234567 language +34567890 is high level +09876543'
x = re.findall('[+]\d+',line1)
print(x)

#getting python only


import re
line1 = 'python +9234567 language +34567890 is high level +09876543'
x = re.findall('[p]\w+[n]',line1)
print(x)


import re

line1 = 'python language fathimanasrinek@gmail.com  +09876543'

x = re.findall('[a-z,A-Z,0-9]+[@][a-z]+[.][a-z]+',line1)
print(x)

#pwd validity using re


# 6 - 16 digits
#atleast one in a-z
#atleast one in A-Z
#0-9
#special character

import re

pwd = input('enter the password') #8921113513

if len(pwd)>16 or len(pwd)<6:
    print('length not satisfied')

elif not re.search('[a-z]',pwd):
    print('No small letter')

elif not re.search('[A-Z]', pwd):
    print('No upper case letter')

elif not re.search('[0-9]',pwd):
    print('there is no number')

elif not re.search('[^a-z,A-Z,0-9,\s]', pwd):
    print('there is no special character')

else:
    print('thaats a valid passwoord')