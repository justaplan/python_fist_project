# Convert elevator floors
inp = input('Europe Floor')
usf = int(inp) + 1
print('US floor', usf)

# Conditional Step
x = 5
if x < 10:
    print('smaller')
if x > 20:
    print('bigger')
if x == 5:
    print('equal!')
if x !=6:
    print('not equal to 6')


#Example increase/ manitan after it or for , decrease to indicate end of the block
x=5
if x > 2 :
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2')

for i in range (6) :
    print(i)
    if i > 2 :
        print('Bigger than 2')
    print('Done with i', i)
print('All Done')

# Example Nested Decision
x = 101
if x > 1 :
    print('X more than 1')
    if x < 100:
        print('X less than 100')
print('All Done!')

# Example Two way Decision
x = 50
if x > 1 :
    print('X greater than 1')
else :
    print('X less than 1')
print('All done!')

# Example multi way - only pick one answer route
x = 0
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('Large')
print('All Done')


# Q & A
x = 2
if x < 2 :
    print('Below 2')
elif x < 20:
    print('Below 20')
elif x < 10 :
    print('Below 10')
else :
    print('Something else')

# More conditional try and except
astr = 'Hello Bob'
try :
    istr = int(astr)
except :
    istr = -1
print('First', istr)

astr = '123'
try :
    istr = int(astr)
except :
    istr = -1
print('Second', istr)

# Example Conditional
x = input('Enter your age: ')
y = int(x)
if y < 21:
    print("your age must be more or equal to 21 to enter the website")
elif y < 40:
    print("You are permitted to enter the website")
else:
    print("your are too old for ths shit")

# Practice
x = input("X: ")
z = int(x)
y = input("Y: ")
u = int(y)
zr = z * u
print("Amount" ,zr)
