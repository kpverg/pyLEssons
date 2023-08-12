jabber = open('/home/thedoctor/Documents/pyLEssons/files/Jabberwocky.txt', 'r')

for line in jabber:
    #print(line.rstrip())
   # print(line,end='')
    print(line.strip())
jabber.close()
with open('/home/thedoctor/Documents/pyLEssons/files/Jabberwocky.txt', 'r') as jabber:
    
    for line in jabber:
        print(line.rstrip())
    
#readline

    lines=jabber.readlines() #readlines creating a list with each line
print(lines)

for line in reversed (lines):
    print(line)
    
with open('/home/thedoctor/Documents/pyLEssons/files/Jabberwocky.txt') as jabber:  #creating a string  if you dont specify 'r' => default setting:'r'
    text=jabber.read()

print(text)

for char in reversed(text):
    print(char, end="")
print()    
print('*'*80)
with open('/home/thedoctor/Documents/pyLEssons/files/Jabberwocky.txt') as jabber:
    while True:
        line=jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break
print('*'*80)
with open('/home/thedoctor/Documents/pyLEssons/files/Jabberwocky.txt') as jabber:
    for line in jabber:
        print(line.rstrip())
        if 'jubjub' in line.casefold():
            break