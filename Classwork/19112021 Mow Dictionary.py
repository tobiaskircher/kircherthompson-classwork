#Classwork 19-11-2021

mow = {'one':6,'man':6,'went':16,'to':17,'mow':17,'a':12,'meadow':12,
       'and':5,'his':5,'dog':5,'two':5,'three':4,'four':3,'five':2,'men':14}

if 'cat' in mow:
  print('dog')

print(mow['one'])
mow['cat'] = 0
print(mow)

del(mow['cat']) #or mow.pop("cat")

if 'cat' in mow:
    print("Yes")
else:
    print("No")
