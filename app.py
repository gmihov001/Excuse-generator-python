import random
import math

# your code here

who = ['My cat ', 'My grandma ', 'My boss ', 'The neighbor ']
what = ['chewed my shoes ', 'wrecked my car ', 'peed in my bed ', 'knocked on the door ']
when = ['when I was trying to leave.', 'yesterday.', 'when you called.', 'when I was driving.']

excuse = who[random.randint(0,len(who)-1)] + what[random.randint(0,len(who)-1)] + when[random.randint(0,len(who)-1)]

print(excuse)