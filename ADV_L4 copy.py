#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 18:37:02 2025

@author: apm


ADV - L4 ( HALE MASALE)






HUMAN ------ Python ----- Interface


python---------

1-built in functions ( print(),input(),len(),type(),;.....)
2-keywords()




3-- variables
numebrs ( int , float , complex , ** * + - , compartison (== , != , > <))
Boolean ( True ,False)
string ( str '' )--> zarf[index 0 ] , str functions --> zarf.function()  .lower()
ina taghri ijad nmikrd --> zarf_jadid = zarf.function()

tedadi az variables --> iterables
list --> changable , allow duplicated , ordered
a=[]  zarf[index]=new_value , list functions --> emal mishodn
zarf.append() zarf.insert()

tuple --> () --> unchangable ,.....
set -> {} ---> unchanghable , ordered nabod (index) ,. duplicated
dictionary --> {keys : values} --> bejaye zarf[index]  zarf[key]

"""


#------keywords-------------------
'''

python az bala b paeen mesle yek ensan az chap b rast
code shoamro mikhoen va ejra mikone
yani harchiu bnvisi
kodet eja mishe
gahi mikhay in mantegh ro in raveshe ejr ro beham bzni
yekarte jadid koni --> KEYWORDS


KEYWRODS---> if  , else , elif, for , while ,... --> banafsh 



'''


print('salam')

print('chanta mikhay')


#hamishe in dot aprint mishan

#yek khat az codee ro nmikham ejra bshe


#in kaht az code --> print()Z
a=10
b=a+20


#hamishegi?? --> shart

#--> if




'''



if shart:
    codet 
    
    
shartet Trye --., code ejra mishe
ag False--> ejra nmishe



shart --> True , false


comparison

if a>10:
    
    
if sen>20



if message=='bale':
    
    
    
    


'''
#hamishe
   
sen=10
sen=20
sen=340890794823179837
print('khosh omadid')



#-----------
#sen>20 --> True , False
#be sen 

#ag taraf senesh zire 20 

print(10>20) #False
print(30>20) #True


sen=10


if sen>20:
    print('khosh omadid')
    
    
    
#----------------------

sen=20
print('khosh omadid')
    
#sen=10 , 20 , 309 ,
#khati k print('')ejr am,ishe





if sen>10:
    print('khosh omadid')
    
'''


age in sharti k shoma gzoashjtri true bashe javabesh --> Body  khosh amadi



'''
    

sen=5
#print(sen)
#print('sen>10')
print(sen>10)

'''
comparison operators
alaeme moghayese
==
!=
>
<
>=
<=

soalie-->

False



'''
sen=20
#print(sen)
#print('sen>10')
print(sen>10)
#True


#------
sen=10
print(sen>10)
#False




print('salam')

a=10



'''

if shart:
    print('salam')
    
    
shart --> True , False


==
!=
>
<



'''
#sen=5
#sen>10 --> False

#sen=20
#sen>10 --> True

if sen>10:
    print('salam')



sen=5
if sen>10:
    print('salam')




sen=20
if sen>10:
    print('salam')



#-----


sen=20
if sen>10:
    print('salam')
    print('khobu')
    a=20
    b=a+300
    c=b*3
    print(c)
    
'''
salam
khobu
960
'''



#-----

sen=20
if sen>10:
    print('salam')
    print('khobu')
    a=20
    b=a+300
    c=b*3
    print(c)
    
    
print('khodafez')

'''
salam
khobu
960
khodafez
'''


#------
#only IF

#Just if


#ye sharti ro check mikone ag true bod --> inkaro kon
#ag nabod --> bikhial bman che




#----dorahi doros koni

#age true bood --> inakro kon
#age false (nmikhay bgi bikhian) -->kare dg

#if else


'''

shart --> True , false

True --> kare 1
False--> kare 2

dorahi



if shart:
    kare1
    
else:
    kare2
    




'''


sen=10



if sen>10:
    print('salam')
    
else:
    print('shoam senet ghjanoni nist')
    
    
    
    
'''

code rad mishe


vase har seni -->

har kodom k sen>10 --> sen>>>10 --> True -->   print('salam')

baghie? else --> sen<=10 --> False --> print('shoam senet ghjanoni nist')

'''

if sen>10:
    print('salam')
    print('khobi')
    a=100
    b=a*2
    print(b)
    
else:
    print('shoam senet ghjanoni nist')
    a=1000000000
    b=a/100
    print(b)
    
'''

farsi ( idea, issues, project ,...) --> python



agar ---> If ( 1-just if 2-if else 3-elif)


agare fght baraye yek shart mikhay yk kar koni --> just if


age mikhay dorahi doros koni --> if else


'''
    



'''

-------------if else-------------
           true----> kare1
-------> if 
           false---> kare 2
           
     
           
     
        
           true----> kare1
-------> if        --->kare2
           if shart 
                  --->kare3
                  
                  
    chanta dorahi --> 
    elsia khdoeshon chan dastan--> if elif
    
           
           
'''
#sen >18 --> ghanonie
#18> sen >16 -->agha dosal sab kon
#sen<16 --> ghanoni nisi
  

#----------just if-----------  
sen=input('senet cheghadre')

if sen>18:
    print('salam)
    
    
#sen>18 ----> sene shoam gahnonie
#sen <18 -->hcihi nminevise



#------if , else-----------

sen=input('senet cheghadre')

if sen>18:
    print('salam')
else:
    print('gheyre ghanoni')


#sene >18 ---> sene shoam ghanoni
#sene 18 > 16 --> False--> gheyre ghanoni
#>16 --> false-->gheyre ghanoni



if sen>18:
    print('salam')

else if sen>16:
    print('dosal sab kon')




#----------------------------------------
# if elif 



sen=20 #salam

sen=17 #dosal sab kon

sen=10 #gheyre ghjanoni hasti



if sen>18:
    print('salam')

elif sen>16:
    print('dosal sab kon')
    
else:
    print('gheyre ghjanoni hasti')
    



print('dfsdsfsfdsfdfs')
#------





'''



if shart:
    dastoor
    



if shart:
    dastoor1
    dastoor2
    dastoor3
    .......
    
    

if shart1 and/or shart2:
    dastoor1
    dastoor2
    dstoor3
    
    

shart1  --> True , False
shart2  --> True False


fght y shart sharte1 doros

if shart1:
    fdfdssfds
    
    
    
dota 

2 ta halat

yamikhay bgi har dotash bayad True bashe , 
sharte 1 va sharte 2 true bashe in karo kon


if shart1 and shart2:
    print(dsdfsadsadsadas)


if sen>10 and jensiat=='mard':
    dsijdslsd
else:
    
    
    
    
#---
hadeagal yeki az shart ha true bashe

ya

ya sharte1 ya sharte 2
ya -> or

if sen>10 or jensiat=='zan':
    
    
ya sen>10
ya sjensiat=10



#-----------------------



code sade ro .....


code


shartish kon


1-if 

2-if else


3- if elif else


#---------


'''




print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')






print('salam')

a=100+8000

b=[10,20,30]

b.append(100)


#har kaht codi
#ey kash msihdo chanbar ejhrash karddd




'''

python --> Halghe

logic ya manteghe halghe --> 


halgeh --> mikhay biay ye codet chanbar benevsiish
amna khob nmikhay copy paste

halghe --> va 

print built in fucntion
keywords
variable??



mage nmikhay dobare mantegh va skahrtare kdo beham brizi?


keywords---> halghe



For 
while



FOR....
          
          
          
          
'''

for :
    print('salam')



for :
    print('salam')
    print('khobi')

'''

baraye tekrar pyuthon tooey code sourcesh


b ychizi niaz dare
--> shomarande




20 bar coddo ejra kon

repeat 10:
    print('salam')


#---------------------------


niaz darma b ychi bname shoamrande

b y range niaz drm

(start , end)



i , j , k, l  , sh ,, s

i 







'''

for i in range(0,10):

#b ezaye har i ee k dar [0,1,2,3,4,5,6,7,8,9]
#boro done done i ro bzar  , code paeen ro anjam bde




for i in range(0,10):
    print('salam')




'''
i ---> zarf

i=0 --> print('salam') ----> salam 
i=1 --> print('salam,') ---> salam
i=2 --> prinmt('sal')
i=3
i=4
i=5
i=6
i=7
i=8
i=9 --> print('salam') --> salam
i=10 -tamam 

edam e b code



'''



'''
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam

'''




for i in range(0,10):
    a=10

'''
shoamrnade --> i 

i [ 0 , 1, 2,3 ,....,9]


i=0 --> a=10 --> X
i=1 --> a=10
i=2 --> a=10

.
.
.
.
.
.
i=9 --> a=10 --> X
i=10







'''



for i in range(0,10):
    print('salam')

'''

shoamrande i 
rnage [ start , end]

az start i=start 
i=
i=


i=0 -- > print(salam)-->slaam
i=2
i=4
i=6
i=8





'''


#range (start,end+1 , step)




for i in range(0,10):
    print('salam')


for i in range(0,10,1):
    print('salam')


for i in range(0,10,2):
    print('salam')

'''
i --> [0 , 2 , 4, 6, 8]

i-->0 ---> print(salam) -->salam
i-->2 --> print(salam) -->salam
i-->4 -->print(salam)-->salam
i--6 ->print(slaam) -->salam
i-->8 pirnt(salam)---> salam
'''


#--------------------------

for i in range(0,10):
    print('salam')
    
    
    
    
for i in range(0,10):
    print(i)
    
        
        
        
        
        
'''
i=0 --> print(i) --> print(0) -->0
i=1 --> print(i) -->print(1) -->1
i=2 -->
i=9 --> prtint(i) -->print(9)-->9

'''

'''
0
1
2
3
4
5
6
7
8
9
'''



for i in range(0,10):
    print(i)



#range --> []




numbers=[0,1,2,3,4,5,6,7,8,9]
for i in numbers:
    print(i)

'''
b ezaye har i i k dar [0,]

i=0 --> dastor
i=1 dastoor
i


'''

#---> Iteration --> Varresiii


a='salam'
for i in a:
    print(i)


'''
i--> shjoamrande ma nist?
a--> s a l a m

b ezaye i k dakehle a (salam)


i='s' --> print(i) --> print(s) --_>s
i='a' -->print(i) -->print(a) -->a

i=m  --->print(i) -->print(m) -->m

s
a
l
a
m

'''


a='ali'
for i in a:
    print('salam')

'''
i-->shoamrandfe
a -_>listy --> [a l i]


i='a' -->code ejra kon -->print(salam) -->salam
i='l' -->coee ejra --> print(salam) --.salam
i='i' --> cxode ejra kon-->print(salam) --.salam


'''




for i in range(0,5):
    print('salam')
    
'''

i-->shoamrande
range(0,5) --> [0,1,2,3,4]

i-->0 ejraye code
i--.1 ejraye code
i-->2 ejraye
i-->3
i-->4 ejraye code


'''



#----------------------------------
#----------------------------------
#----------------------------------
#----------------------------------
#----------------------------------
#----------------------------------
#----------------------------------
#----------------------------------




print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')


'''
repeat 10:
    print('salam')

#SyntaxError: invalid syntax

'''


'''

for shomarande (range):
    dastoooor
    
range --> [0,1,2,3,4,5]

shoamrande (i)

i=0 -->dastoooor
i=1 -->dastoor
...
i=5 --> dastooor






    
    
'''



for i in [0,1,2,3,4,5]:
    print('salam')
    
'''
salam
salam
salam
salam
salam
salam
'''



'''

range(start,end,step)


start , +step , +step , end -1

[......]

[0,1,2,3,4,5]


range(0,6)

[0 1 2 3 4 5]

'''

    


for i in range(0,6):
    print('salam')
    
    
    
'''

i=0 --> dastoor --> print(salam)
i=1 --> dastoor --> print(salam)
i=2 --> dastoor --> print(salam)
i=3 --> dastoor --> print(salam)
i=4 --> dastoor --> print(salam)
i=5 --> dastoor --> print(salam)


i=6-->


'''

my_zarf=['ali','vahid','reza','hamid']


for i in my_zarf:
    print('salam')
    
'''


i=ali --- >print('salam') -->salam
i=vahid --.print('salam') -->
i=reza-->print('salam') -->
i=hamid -->print('salam') -->



salam
salam
salam
salam


'''
    
name='ali'
#name = [ a , l , i]

  

for i in name:
    print('salam')


'''
i=a --> print(slaam)
i=l
i=i
'''



name='ali'
#name = [ a , l , i]

for i in name:
    print(i)

'''
i='a'--> print(i) --> print(a) ---> a
i='l' -->print(i) --> print(l)[-->]l
i='i' -->print(i) -->print(i) -->i



a
l
i

'''

for i in range(0,5):
    print('salam')
  
    
name='alipi'

for i in name:
    print('salam')

    
mylist=[0,1,2,3,4]
for i in mylist:
    print('salam')




#_-----

matrix=[ [1,2,3] ,[4,5,6] ,[7,8,9] ]



matrix[1] #[4, 5, 6]


index1=matrix[1]

print(index1) #[4, 5, 6]

index1[::-1] # [6, 5, 4]



#------------

matrix=[ [1,2,3] ,[4,5,6] ,[7,8,9] ]

matrix[1][::-1] #[6, 5, 4]


a=[10,20,30]

a[-1] #30
a[-2] #20
a[::-1] #[30, 20, 10]


#---------------


'''

Yek chzi efarsi ---> pythonish kon


ye barname ee benevsiid k norme ra az danesh amoz dareyaft konad
va bar asaseajdval ......


daryaft ---> input()




'''

nomre=float(input('danesh amoze aziz , nomrat chand shode?'))


'''

check kone 
age =18 ta 20 --> A
16 ta 18 --> B
ag 14 ta 16 --> C
af 10 ta 14 --> D
ag zire 10 -->F



age --> if


if elif 

'''



nomre=float(input('danesh amoze aziz , nomrat chand shode?'))


if nomre>=18:
    print('A')
    #print('nomrewye shoam shode A')
    #grade='A'
elif nomre>=16:
    print('B')
    
elif nomre>=14:
    print('C')
    
elif nomre>=10:
    print('D')

else:
    print('F')
    
    
    




#---------------------
nomre=float(input('danesh amoze aziz , nomrat chand shode?'))
if nomre>=18:
    grade='A'

elif nomre>=16:
    grade='B'
elif nomre>=14:
    grade='C'

elif nomre>=10:
    grade='D'
else:
    grade='F'


print(f'Daneshjoye aziz nomre shoma shod : {grade}')
    

#--------------------------
nomre=float(input('danesh amoze aziz , nomrat chand shode?'))

if nomre<10:
    print('F')
elif nomre<14:
    print('D')
    
elif nomre<16:
    print('C')

elif nomre<18:
    print('B')
    
elif nomre<=20:
    print('A')

else:
    print('normaton ro eshtebah zadid')











'''
danesh amoze aziz , nomrat chand shode?20
Daneshjoye aziz nomre shoma shod : A
'''


ghad=float(input('gahdeto begooo:'))
vazn=float(input('vaznetoo begooo'))
#bmi=w/(h**2)

bmi=vazn/(ghad**2)



if bmi>35:
    print('kheyli chagh')
    
elif bmi>30:
    print('chagh')
    
elif bmi>25:
    print('ezafe vazn')
    
elif bmi>18.5:
    print('normal')
    
elif bmi>16:
    print('laghar')
    
elif bmi>15:
    print('kheyli laghar')
    
else:
    print('sooe taghzie')
    
    
    
#----------------------

#dota vorodi 
#dota shart


sen=float(input('senetoon cheghadre:'))
jensiat=input('jensiateton?:')


#ag fard zan bashe va senesdh ta 40 bashe
#print(dokhtar)

if sen<40 and jensiat=='zan':
    print('dokhtar')




#--------------

if jensiat=='zan':
    if sen >65:
        print('madarbozog')
    elif sen >40:
        print('madar')
    else:
        print('dokhtar')
#mard
else:
    if sen >65:
        print('pedarbozog')
    elif sen >40:
        print('pedar')
    else:
        print('pesar')
    
    


#------------
#Zan

jensiat='Zan'
jensiat=='zan' # False


sen=float(input('senetoon cheghadre:'))
jensiat=input('jensiateton?:')



if jensiat.lower().strip()=='zan':
    if sen >65:
        print('madarbozog')
    elif sen >40:
        print('madar')
    else:
        print('dokhtar')
#mard
elif jensiat.lower().strip()=='mard':
    if sen >65:
        print('pedarbozog')
    elif sen >40:
        print('pedar')
    else:
        print('pesar')
else:
    print('ma fght baarye mard va zan misanjim')
    
    
#-------------

    

esm=input('esmei begooo:')



'''

esm='khiaban'

miraftam done done too

done done bere toosh
bgrde aieuo

beshmore




'''


esm='khiaban'

for i in esm:
    print('salam')

'''
i=k --> salam
i=h --> saalam

..
i=



'''




esm='khiaban'

for i in esm:
    print(i)

'''
k
h
i
a
b
a
n

'''
#----->
#if else



    
esm='khiaban'

for i in esm:
    if i in ['a','u','i','o','e']:
        print(i)

'''

i=k ,  falase badi
i=h --> false badi
i=i -->print(i) -->print(i) -- i
i=a --> print(a)--> a
i=b
i=a ---> a
i=n

i a a 
'''

'''
i
a
a
'''


esm='khiaban'


count=0

for i in esm:
    if i in ['a','u','i','o','e']:
        #print(i)
        count=count+1


'''

i=k , h , ...
i= a --> count= 0 +1 =1


'''

print(count) #3




#------------------------

esm=input('esmei begooo:')

for i in esm.lower():
    if i in ['a','u','i','o','e']:
        #print(i)
        count=count+1


#------------




a=0
b=1

for _ in range(10):
    print(a)
    a=b
    b=a+b


a, b = 0, 1
for _ in range(10):
    print(a)
    a, b = b, a + b









