
"""
Created on Mon Jul 21 19:32:35 2025

@author: apm



-----ADV 5 -----------


"""

'''
---------REVIEW--------------


Huma ------python ------machine

1-->python builtin function --> print() , len(),type()
2-->keywords-->manteghe ejraye code ro taghir mdiadan

3---> sefid--> variable (moteghayer dr nazar migrf)
3.1.numebrs (int, float, complex ,..) [** * + - / ] [== != > < >= <=]
3.2. Boolean ( True , False)
3.3. Str --> kalame , character, jomle , esm ,..
reshte ee az chaarcter ha --> 'harchi miokahsi minvshti'
esm='value'
esm[index] -->
index 1--> 
esm[1]-->a
esm[1:4] 
str fucntions --> tavabe e baraye str ha bod
variable.lower()
.upper()
.isdigit()
.isupper() --> True , False
.strip() --> fasedle space 
.split(',') -->list
.coutn('a')--.4
.find('a')--> indexe

taghir emal nmikonan , yechize jadid (khroji) --> avriable jadid savesh koni


3.4.Multiple variables --> iterables 

3.4.1. List --> [ozv1,ozv2,ozv3]
mylist=[10,20,30,40]
mylist[index]
mylist[index]=100000
list fucntions--> fucntion fght baraye list 
taghir ijad mikoen (khrooji nmide)

a=[10,20,30]
a.append(40) --->
a=[10,20,30,40]
a.remove(40)  value hazf koni
a.pop(2) indexe 2
ordered, changable , allow duplicated



3.4.2. Tuples --> (10,20,30,40)
unchangable
a=(10,20,30,40)
a[2]=200 XXXXXXXX
a-->list -->taghiur --> tuple
taghir napazir bodnsho--> data base ha estefade


3.4.3. Set --> {10,20,30,40}
unordered , unchangable , duplicated XXXX
a={10,20,30,40}
print(a)
20 30 10 40
a[index]-->gahele dastresi

a={10,20,20,20,30}
---> a={10,20}
-> duiplicated haro hazf konan estefade mikonan

3.4.4.--> dictionary

list -->
index   value
0        10
1        20

list[0] ---> 10


properties --> moshakahsat -->dictionary

dictionary = { keys : values , .....}

mydict={'vazn':100 ,'ghad':180}

keys  value
vazn    100
ghad   180

mydict['vazn'] -->100




#---------
-------PYTHON--------3 BAKHSH
1---> built i9n functionsd 
2--->keywords
3-->variables



======keywords=====================

mantegeh codeto beham bzn


mantegh ---> pythoin mesle yek ensan
az bala b paeen
az chap b rast --> code ro mikhoen ejra mikone


man mikham in mantegh ro taghir bdm,





------> IF Ha sharti ha---------
yek khat code (chan khat) -->hamishe ejra nshe
ghablesh y shart check bshe






1.Only if


if shart:
    dastoooor
    
    
shart--> True False (== > < ,isdigiti())
dastoor--> print()  a=a+2
dastoor->dastor ha bashe -_< chanta


shart -->
shart1 and shart2 --> joftesh true bashe
shart1 or shart2 --> hadedeghaal yekish true bashe



if sen>20:
    print('salam')
    
    
az beyen tamame sen ha fght onae k bala 20 hastan
sen>20 --> True , fALSE --> True
print('salam')


onae zire 20 --> False ->ejra
onae k sharto nmitonan --> bikhial bema che





2-- If else
mige bebin dorahi doro skon

shart -->sen>20
agar True -> yekaor kon
agar false -->(nemigi bikhial)--> oonkaro kon



if shart:
    dastoor1
else:
    dastoor2
    
    
dorahie ejra code


if shart:
    dastoorate1
    dastporate1
    dastoorat2
else:
    dastoorate2
    dastoorate
    2datsoorate2
    

3- if else elif

doprahi mzsaszi
bad troo dorahi oane k shart false--> dorahi bsazi

ag sen >20 --> True / False

onae k zire 20 --> age beyne 18 ta 20 / 0 ta 18 



if shart:
    dastoor1
else if shart2:
    dastooor
else:
    dasoooor
    
    
    
if sen>20:
    print('senet bala 20 e')  
elif sen>18:
    print(senet beyen 18 ta 20 e)
else:
    print('senet zire 18 ast')


inam az 3 ta sharti ki ma darim

'''


name=input('name mahsooleto begoo')
code=input('code mahsooleto begoo:')
price=float(input('gheymate mahsooleto begoo:'))

text=f"""

%%%%%%%%%PLUTUS%%%%%%%%%%%%%%

Name : {name}

Product Code : {code}


    Total : {price}

"""

print(text)

answer=input('do you confirm these informations?')

#agar taraf nevesht yes --> taeed shod
'''
aya man do rahi daram? ya ye rahi?


y rahie --> only if

do rahie --> if else / if elif .... (range)

yedone--> fght onae k nvshtn yes
baghei ro bikhail


if shart:
    dastooor
    
    
dastoor--> print('taaed shod')

shart --> True , False

==
!=
>
<
..

answer=='yes' nesbat b answer --> false , true


'''




name=input('name mahsooleto begoo')
code=input('code mahsooleto begoo:')
price=float(input('gheymate mahsooleto begoo:'))

text=f"""

%%%%%%%%%PLUTUS%%%%%%%%%%%%%%

Name : {name}

Product Code : {code}


    Total : {price}

"""

print(text)

answer=input('do you confirm these informations?')
#print('taeed shod') -->hamishe nemikham ejra she


if answer=='yes':
    print('taeed shod')

'''
ag yes bshe -->  taeed shod
ag na , kheyli kojae , ...--> rad mikoen mrie
'''

#----------------------------


name=input('name mahsooleto begoo')
code=input('code mahsooleto begoo:')
price=float(input('gheymate mahsooleto begoo:'))

text=f"""

%%%%%%%%%PLUTUS%%%%%%%%%%%%%%

Name : {name}

Product Code : {code}


    Total : {price}

"""

print(text)

answer=input('do you confirm these informations?')
#print('taeed shod') -->hamishe nemikham ejra she


if answer=='yes':
    print('taeed shod')
else:
    print('taeed nashod')

'''
ag yesd --> taedf
ag no --> ateed nashod

'''


'''

ag yes --> taeed shod
ag harchi joz yes nsvht --> taeed nashod

'''



name=input('name mahsooleto begoo')
code=input('code mahsooleto begoo:')
price=float(input('gheymate mahsooleto begoo:'))

text=f"""

%%%%%%%%%PLUTUS%%%%%%%%%%%%%%

Name : {name}

Product Code : {code}


    Total : {price}

"""

print(text)

answer=input('do you confirm these informations?')
#print('taeed shod') -->hamishe nemikham ejra she

#bhehtarine
if answer=='yes':
    print('taeed shod')
elif answer=='no':
    print('taeed nashod')
else:
    print('gozineye mojod nadare')





#--------
#--------------
#------------------

name=input('name mahsooleto begoo')
code=input('code mahsooleto begoo:')
price=float(input('gheymate mahsooleto begoo:'))
text=f"""

%%%%%%%%%PLUTUS%%%%%%%%%%%%%%

Name : {name}

Product Code : {code}


    Total : {price}

"""
print(text)
answer=input('do you confirm these informations?:')

if answer=='yes':
    print('taaeed shod')
else:
    print('taaed nashod')


#do you confirm these informations?:Yes


answer='Yes'
answer='yeS'
print(answer=='yes')
#False
#False




if answer=='yes' or answer=='Yes':
    print('taaeed shod')
else:
    print('taaed nashod')

#yEs
#yeS
#YEs
#yES


answer=input('do you confirm these informations?:')

final_answer=answer.lower()

if final_answer=='yes':
    print('taaeed shod')
else:
    print('taaed nashod')


final_answer=answer.upper()

if final_answer=='YES':
    print('taaeed shod')
else:
    print('taaed nashod')

#------


answer=input('do you confirm these informations?:')
if answer.lower()=='yes':
    print('taaeed shod')
else:
    print('taaed nashod')

'''
yes --> yes --> True
Yes --> yes --> True
YES 
yeS


y + e + s --> yes --> True

'''


answer=input('do you confirm these informations?:')
if answer.lower()=='yes':
    print('taaeed shod')
else:
    print('taaed nashod')



#do you confirm these informations?: yes


#taaed nashod

print(answer) # yes


print(len(answer)) #4

# yes

a='yes'
b=' yes'

print(a==b) #False
'''
answer=' yes'
answer.lower=' yes'
if ' yes'=='yes' --> False -->Taeed nashod:
    
'''



answer=input('do you confirm these informations?:')

final_answer=answer.lower()

final_answer2=final_answer.strip()


if final_answer2=='yes':
    print('taaeed shod')
else:
    print('taaed nashod')


'''

30 no --> yes
Yes
yEs
 yes
yes 
YES 
 Yes



'''

answer=input('do you confirm these informations?:')

if answer.lower().strip()=='yes':
    print('taaeed shod')
else:
    print('taaed nashod')
    
#XXXXX-->Yadet bashe ke
#answe inja taghir nkrde

#if answer=
    


password=input('passworde morede nazar ro vared konid:')

#check kone 8 ragham abshe
#bozorgtar
#character bashe
#bege amne (safe)
#bege na amne


#===================================
#===================================
#===================================
'''
Sharte if --->

shart ro chizi bzari k javaesh True,False


adad ha kar dari --> == > < >= <=
str --> ==  !=  answer=='yes' 

str function --> .isupper() .islower()
.isdigit()

custom function --> 



'''






name=input('name mahsooleto begoo')
code=input('code mahsooleto begoo:')
price=input('gheymate mahsooleto begoo:')

#print(type(price)) #<class 'str'>

##float('10')
#float('10.45')
#float(10)

#float('salam')
#ValueError: could not convert string to float: 'salam'





new_price=price*0.8

text=f"""

%%%%%%%%%PLUTUS%%%%%%%%%%%%%%

Name : {name}

Product Code : {code}

    Total with discount: {new_price}

"""
print(text)
answer=input('do you confirm these informations?:')

if answer=='yes':
    print('taaeed shod')
else:
    print('taaed nashod')


#--------------------


name=input('name mahsooleto begoo')
code=input('code mahsooleto begoo:')
price=input('gheymate mahsooleto begoo:')

if price.isdigit():
    new_price=float(price)*0.8

    text=f"""
    
    %%%%%%%%%PLUTUS%%%%%%%%%%%%%%
    
    Name : {name}
    
    Product Code : {code}
    
        Total with discount: {new_price}
    
    """
    print(text)
    answer=input('do you confirm these informations?:')
    
    if answer=='yes':
        print('taaeed shod')
    else:
        print('taaed nashod')

else:
    print('lotfan adad vared konid')




#--------------------------
#reverse development




name=input('name mahsooleto begoo')
code=input('code mahsooleto begoo:')
price=input('gheymate mahsooleto begoo:')

if not price.isdigit():
    print('lotfan adad vared konid')
    
else:

    new_price=float(price)*0.8

    text=f"""
    
    %%%%%%%%%PLUTUS%%%%%%%%%%%%%%
    
    Name : {name}
    
    Product Code : {code}
    
        Total with discount: {new_price}
    
    """
    print(text)
    answer=input('do you confirm these informations?:')
    
    if answer=='yes':
        password=input('baraye takmil password ra vared namaeed:')
        #.....
        
    else:
        print('taaed nashod')




#----
password=input('baraye takmil password ra vared namaeed:')


'''

avalish --> ishtar az 8 joz
fdovmish -> ham kochik ham bozorg
sevomish -->adad dashte bashe
XXXX --> charomish--> character dashte bashe

'''



if len(password)>=8:
    if password.isalpha():
        print('character nadare')
    else:
        print('taaede')
else:
    print('passworde shoam 8 ragham nadarad')


'''
FOR

a='salam'
b='SALAM'
c='Salam'

print(a.isupper())
print(b.isupper())
print(c.isupper())
done fonr horofo begarde

'''




#------------------------
#--------------------------
#----------------------------------
'''

-----2.keywords-------
------2.1. If
-------2.1.1. only if
-------2.1.2. if else
-------2.1.3. if elif else


-----2.2. Loop
-----2.2.1. For
------2.2.2. while


'''


print('salam')



a=10
b=a+10



'''
repeat(10):
    print('salam')

    

man niaz daram
b ychizi bname y zarf banem hsomarande

asaye dast emane


man mikham y kar konm



zarf bdi --> variable 
bad ye shoro bedi ye enteha , chanta chnata



1 ta 10 yeki yeki


1 2 3 4 5 6 7 8 9 


har dafe oon khat codi k tab zadi ejra mikonam



for shoamrane in mahdode(start,end):
    in dastoramo ejra kon



'''

for i in [1,2,3,4,5]:
    print('salam')
    
    
'''
be ezaye har i i k dar in [1,2,3,4,5] hast print kon salam


i=1  ---> dastooro ejra mikoen --> 
i=2 

i=5 --> dastooro ejra mikone


eameye code




'''

for i in [1,2,3,4,5]:
    print('salam')
    
    
'''
i=1 --> print('salam') --.salam
i=2 -->print('salam') --> salam
i=3 -->print(salam)p-0sakan
i=4 -->salam
i=5 -->salam

5 bar 

tekrar

'''   
    
    


for i in [1,2,3,4,5]:
    print(i)
    
    
'''
b ezaye har i i k dar [1,2,3,4,5] hast code zir ro ejr kon (print(i))

yek kar tekrari--> i

i=1 --> print(I)-->print(1) --> 1
i=2 -->print(i)-->print(2)-->2
i=3 -->print(i)-->print(3)-->3
i=4 -->print(i)-->print(4)-->4
i=5 -->print(i)-->print(5)-->5


'''


#1 ta 100

#for i in [1,2,3,4,5,6,7,8,9,9,....]



#tabe ye dakheli --> built in function 
#--> narenji

#range(start,end,step)

#[start , start+step , ....... , end-1]


#range(1,100,1)
#[1,2,3,4,......99]



#range(1,100,2)
#[1,3,5,...,99]

#range(1,100)
#[1,2,3,4,5,6,7./..9]

'''
a='ali'
a[0:3]

range---->

(start,end,step)

step --> 1 --> to mitoni taghgir


end --> end-1  khode end shaml nis


range(end)
-->0


range(start,end)

---> [1,2,3,4,]

i --> hey bsh eoon
dastoro ejra kone


'''


for i in range(0,5):
    print('salam')
    
    
'''
be ezaye har i k in toooe

range(0,5,1)-->
[0,1,2,3,4]


i=0 --> porintslama --.salam
1
2
3
4


5--> salam

salam
salam
salam
salam
salam


'''



for i in range(0,5):
    print(i)


'''

i=0 -0->print(i)-->print(0)-->0

i=1
i=2
i=3
i=4 

0
1
2
3
4

'''


#-----> FOR


#-----1----> yek kario tekrar anjam bdi

for i in range(0,10):
    print('salam')
    
    



#----2----> mihay varresi koni

for i in [1,2,3,4,5]:
    print(i)


mylist=[1,2,3,4,5]
for i in mylist:
    print(i)



mylist=['reza','vahid','hamid','ali']
for i in mylist:
    print(i)


'''

i in too [rezz,vhid,hami,ali]

i=reza --> ejra --> print(i)-->print(reza)
i=vahid --> jerra-->print(i)-print(vahid)



reza
vahid
hamid
ali

'''

mylist='salam'
#mylist=['s','a','l','a','m']
for i in mylist:
    print(i)

'''
i k dar salam 

salam --> listi az character ha hessab shod

i=s --> print(i)-->print(s)-->s
a
l
a
m

'''


password='aliali1000'
for i in password:
    print(i)
    
    
    
    
    
password='aliali1000'
for i in password:
    if i.isupper():
        print('bozorg')
    else:
        print('koochik')
    
    
    
#-------------3 ta ravehs darim-------


mylist=[10,20,30,40,50,60,70,80]



#adad haye balaye 50

for i in mylist:
    print(i)



for i in mylist:
    if i>=50:
        #flean karo kon
        #1-->printesh kon
        print(i)


'''
iteration

50
60
70
80

'''
    
'''
i--> 10,20,30,40,5

i=10 --> if i>50 -> if 10>50 -->if false 
i=20 --> if i>50 ->if 20>50 -->if false
...
i=50 --> if i>=50 --> if 50?=50 --> if True -->print(i) -->print(50)-->50
60,70,80,90,100



'''




#------3 ta halat dare iteration

#1------->namayesh
#-->yek sharti cehck koni vba print koni


for i in mylist:
    if i>=50:
        #flean karo kon
        #1-->printesh kon
        print(i)



#2-----> jam avarie
#boro azin list, adadaye balaye 50 ro briz to ye liste dg 
#bekeshesh biroon
mylist=[10,20,30,40,50,60,70,80]

new_list=[] #yadeshon mire bznn


for i in mylist:
    if i>=50:
        #print(i)
        new_list.append(i)
        


print(new_list)
#[50, 60, 70, 80]


#-----

mylist=[10,20,30,40,50,60,70,80]

new_list=[] #yadeshon mire bznn
nist_list=[]

for i in mylist:
    if i>=50:
        #print(i)
        new_list.append(i)
    else:
        nist_list.append(i)
        


print(new_list)
#[50, 60, 70, 80]

print(nist_list)
#[10,20,30,40]


#-----

'''
mylist=[10,20,30,40,50,60,70,80]

for i in mylist:
    if i>=50:
        mylist.remove(i)



print(mylist)

'''



#3----->beshmorish

mylist=[10,20,30,40,50,60,70,80]

count=0

for i in mylist:
    if i>=50:
        #print(i)
        #new_list.append(i)
        count=count+1
        
        
         
print(count) #4




#=========================
#=========================
#=========================

asami=['ali','vahid','hamid','amir']


#koli esm dare
#boto toosh begard
#beshmor onae k avale esmeshon ba a shoro mishe


#yek list drm bayad bekesham brion--> varresi--> For
#done doen keshidm --> harfe avale beksham biron
#if agar a bood 
#-->beshmoram


for i in asami:
    if i[0]=='a':
        print(i)



count=0
for i in asami:
    if i[0]=='a':
        count=count+1


print(count) #2



#ag a shro shod
#bejaye oon ozv benesvis --> DOROS

#[dorost, hamid, reza , dorost]


asami=['ali','vahid','hamid','amir']

for i in asami:
    if i[0]=='a':
        i='dorost'


print(asami)
#['ali', 'vahid', 'hamid', 'amir']


#--------

asami=['ali','vahid','hamid','amir']

#len(asami)=4

#b ezaye i in range (0,1,2,3)
#for i in asami
for i in range(0,len(asami)):
    #if i[0]=='a'
    if asami[i][0]=='a':
        #i='dorost
        asami[i]='dorost'
    
    
print(asami)
#['dorost', 'vahid', 'hamid', 'dorost']





    
