"""
Created on Sun Aug  3 20:09:48 2025

@author: apm


ADV L6

"""

#---------
#TEKRAR ANJUAM BDIM
# for , while

#loop --> HALGHE

for i in [1,2,3,4,5]:
    print('dastooor')
    print('dastoor haro anjam mide')
    
    
'''
i=1 --> dastoor, dastoroha
i=2 
i=3
i=4
i=5 
'''



#for i in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
for i in range(0,20):
    print('salam')

#20 bar salam


#iteration
a=[10,20,30,40,50]
a=['ali','hamid']
a='alipilehvar'

for i in a:
    print(i)
    

#for --> if estefade mikoni
for i in a:
    if i=='b':
        print(i)
        
        
#---beshmori
count=0
for i in a:
    if i>10:
        count=count+1
    

print(count)


#---varesh dari

mylist=[]
for i in a:
    if i>10:
        mylist.append(i)
        
        
    
    
    
    
#-------FOR--------------
# -->shomarande -->i
#--->start , end 
#--->step
#--->dastooor

start=0
end=100 #100-1 = 99
step=2 #default 1

for i in range(start,end,step):
    print('dastoor')    #tekrar
    print(i) #--> dastoroet motefavete
    #if --> count , .append()
    
    
#instead of range ---> List
#for i in mylist
#for i in mystring
#iteration

#start , end , step beynesh
#-------------------------------


#---------while

'''
start ---> end 
step step yekario anjam bdi
\for??



endam bnejaye inke biayt
begi be ezaye har i i k darone yek range hast (start, step dare)




shomarande--> 0 , 1 ,2 ,3 


boro too ye loop , halghe

shart --> ta zamani k oon shart True has inkaro hey tekrar kon

va vaghty tamom shod
bia biroon



bejaye inke specify moshakahs koni end ro 
ba shart end ro moshakahs mikoni

'''

#shomarande
i=0 #i , j , k  / 0 , 1 ,2 ,3 

#while shart:

#** shart --> True , False --> > < == , str functions

#sharte payane halghe
while i<10:
    print('dastoor')
    print('dastoorat....')
    i=i+1
        
#hamvare i kochik tar az 0 
#hey miad check mikoen shart --> true
#ta ab

#endless loop

 
    
    
'''

for i in range(start,end,step):
    dastooorat
    
    
    

i=start
while i<end:
    dastoorat
    i=i+step
    
    
'''





#----------ESHTEBAHATE RAYEJ--------------------
i=0


while i<10:
    print('salam')
    
    i=i+1
    
    
for i in range(0,10,1):
    print('salam')
'''
i-->
0 1 2 3 4 5 6 7 8 9




'''



#--------------------
i=4

while i<10:
    print('salam')  
    i=i+1
    
'''
salam
salam
salam
salam
salam
salam
'''

#--------------------
i=4 
while i<3:
    print('salam')
    i = i+1
    
#start = 4
#ta zmaani i<3 --> True ejhra kon

#4<3 --> False --> varede halghe nemishe

#varede halgeh nemishe
#sharti k mziari , initial value (start) --> baham co nflicty nadashte bashe


#--------------------
i=0
while i<10:
    print('salam')

#ednless loop
#halgehye bi payan

#i=0 i<10 --> slasam
#i=0 i<10 --> salam
#i=0 i<10



#print('salam')
#i=i+1 ---> k betone shart --> False--> az halgeh biron biad va kahrej bshe




#--------------------
i=0
while i<10:
    print('salam')
    i=i+2
    
    
'''
i=0  i<10 --> 0<10 ->True ->varewdded halgeh -_> print(salam) --> i=0+2 =2

i=2 i<10 --> 2 <10 -->True -_> halgeh edame ->print(salam) -->i=2+2=4
i=4
i=6
i=8 i<10 --> 8<10 -->True -->: hyalgeh edame --> print(slaam) --> i=8+2 =10
i=10 i<10 --> 10<10 --> False --> az halghe kharej mishe

salam
salam
salam
salam
salam

'''



'''

for shomarande in (start,end ,step):
    dastoor1
    dastooor2
    dastoor3
    ......
    
    
    


shoamrande=start
while shoamrande<end:
    dastoor1
    dastoor3
    dastoor3
    ...
    shoamrande = shomarande + step



'''
#--------------------

#while ( javabe --> True , False)

#while i<10:
    
    #

while False:
    print('salam')





while True:
    print('salam')



#kheyli jaha niaz has
#yekario tra abaad anjam bshe


#hey y adad begir berzi too list


mylist=[]
while True:
    adad=input('adaddee jadid bede:')
    if adad=='exit':
        break
    mylist.append(adad)
    

#while True -->? yekartio ta abad anjam mishe
#too dele khode while true -_> 
#sharte khoroj


#--------
#pass
#continiue
#break

#Halghe ha
#taghir mdie ravanda



for i in range(0,10):
    print(i)
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
    pass

    
    
def salam(a):
    pass



#------

for i in range(0,10):
    print(i)


for i in range(0,10):
    if i==8:
        continue
    print(i)

'''
0 1 2 3 4 5 6 7 9 10

i==8 -->True --> edame ro bor badi print(I) ejra nmishe
    

'''


for i in range(0,10):
    if i==8:
        break
    print(i)
    
    
'''
0 1 2 3 4 5 6 7 

if i==8 --> 8==8 -->True -> Break -->biron az halghe

'''

#------------------------------------------------------
#-------------------------------------------------------
#------------------------------------------------------
#-------------------------------------------------------
#------------------------------------------------------
#-------------------------------------------------------
name=input('name mahsool:')
code=input('code mahsool:')
price=input('gheymate mahsool:')

'''
ta zamani k taraf price ro adad nazade ejaze nade edame baibe kharido forosh
'''

#while

'''


while shart:
    yekari kon....
    
    
'''

#price.isdigit()
#not price.isdigit()



while not price.isdigit():
    print('adad vared kon !!!!')
    price=input('gheymate mahsool:')
    




price=float(price)


text=f"""
---------PLUTUS----------

Name : {name}
Code : {code}

    total: {price*0.8}
    

"""

print(text)

answer=input('do you confirm your order?:')

if answer.lower().strip()=='yes':
    print('congradulation')
    
elif answer.lower().strip()=='no':
    print('try again')
    
else:
    print('only you can answer with yes/no')
    



#--------------------------------------

name=input('name mahsool:')
code=input('code mahsool:')

while True:
    price=input('gheymate mahsool:')
    if price.isdigit():
        price=float(price)
        break
    print('adad vared kon!!!!!')
    

text=f"""
---------PLUTUS----------

Name : {name}
Code : {code}

    total: {price*0.8}
    

"""

print(text)

answer=input('do you confirm your order?:')


if answer.lower().strip()=='yes':
    print('congradulation')
    
elif answer.lower().strip()=='no':
    print('try again')
    
else:
    print('only you can answer with yes/no')
    

while True:
    answer=input('do you confirm your order?:')
    if answer.lower().strip()=='yes':
        print('agah tabrik migam')
        break
    elif answer.lower().strip()=='no':
        
        name=input('name mahsool:')
        code=input('code mahsool:')
        while True:
            price=input('gheymate mahsool:')
            if price.isdigit():
                price=float(price)
                break
            print('adad vared kon!!!!!')
        text=f"""
        ---------PLUTUS----------
        
        Name : {name}
        Code : {code}
        
            total: {price*0.8}
            
        
        """
        print(text)
    else:
        print('you must inser yes or no , nothing else....')
        



#========================
#======================
#=======================
name=input('name mahsool:')
code=input('code mahsool:')
while True:
    price=input('gheymate mahsool:')
    if price.isdigit():
        price=float(price)
        break
    print('adad vared kon!!!!!')

text=f"""
---------PLUTUS----------

Name : {name}
Code : {code}

    total: {price*0.8}
    

"""
print(text)


while True:
    answer=input('do you confirm your order?(yes/no):')
    
    if answer.lower().strip()=='yes':
        print('agah tabrik migam')
        break
    elif answer.lower().strip()=='no':
        print('so try again')
        name=input('name mahsool:')
        code=input('code mahsool:')
        while True:
            price=input('gheymate mahsool:')
            if price.isdigit():
                price=float(price)
                break
            print('adad vared kon!!!!!')
        text=f"""
        ---------PLUTUS----------
        
        Name : {name}
        Code : {code}
        
            total: {price*0.8}
            
        
        """
        print(text)
    else:
        print('you must insert yes or no , nothing else....')
        







#========================
'''       FINAL    '''
#=======================


name=input('name mahsool:')
code=input('code mahsool:')
while True:
    price=input('gheymate mahsool:')
    if price.isdigit():
        price=float(price)
        break
    print('adad vared kon!!!!!')

text=f"""
---------PLUTUS----------

Name : {name}
Code : {code}

    total: {price*0.8}
    

"""
print(text)


while True:
    answer=input('do you confirm your order?(yes/no):')
    
    if answer.lower().strip()=='yes':
        print('agah tabrik migam')
        break
    
    elif answer.lower().strip()=='no':
        print('so try again')
        name=input('name mahsool:')
        code=input('code mahsool:')
        while True:
            price=input('gheymate mahsool:')
            if price.isdigit():
                price=float(price)
                break
            print('adad vared kon!!!!!')
        text=f"""
        ---------PLUTUS----------
        
        Name : {name}
        Code : {code}
        
            total: {price*0.8}
            
        
        """
        print(text)
    
    elif answer.lower().strip()=='cancel':
        code=''
        name=''
        price=''
        print('ezafe kardane mahsole shoam ba moafaghiat cancle shod')
        break
    
    else:
        print('you must insert yes or no , nothing else....')
        


'''
raveshe code 3 zani:
    
    
1-Psudo-code --> raveshie


2- Function-based

3- Object oriented programming (OOP) ---> class and objects


ghesmat haee az codee ro mziri tooye yek BOX --> esm mziri
1--> atr tamizmikone code / ha rbakhsh joda ,debugging

yekseri kar ha -> sad bar too code 

500 khate
50 khati --> hey sedash konam

tabe -->


'''

'''


FUNCTIONS--> Clear, encapsulation, avoid repetition , efficient




1--> Definition --> besaz

2--> Call (sedash koni) --> ba y khat cod , 100 khat run bshe



aval besazi, badesh sedash bzni


'''





'''

def name(vorodi):
    
    badane
    
    khoroji
    
    
  
    
**esm --> tabe esme varibale
adad avalesh bzni , tabe hae vojod drn print , ...
character vasatesh
fasele --> _ 


'''


#1---> tae ee k vorodi dare , khoroji nadaare


def jam(a,b):
    c=a+b
    print(c)


#tafrigh(10,20) #NameError: name 'tafrigh' is not defined

jam(10) #TypeError: jam() missing 1 required positional argument: 'b'
jam(10,20,30) #TypeError: jam() takes 2 positional arguments but 3 were given

jam(10,20)

#a=10
#b=20



d=jam(10,20)

#30 -->print
print(d) #None



#2---> ham vorodi dare ham khoroji

def jam(a,b):
    c=a+b
    return c


jam(10,20)

d=jam(10,20)

print(d) #30





'''
def jam(a,b):
    c=a+b
    print(c)

jam(10,20) ---> print--->30
d=jam(10,20) --> d-->None


def jam(a,b):
    c=a+b
    return c
jam(10,20)-->< out=30
d=jam(10,20) ---> d-->30



'''


def jam(a,b):
    c=a+b
    print(c)
    return c


d=jam(10,20)



'''
808 ta 811 --> jam = yechizie hamin chzii ejra nnmiseh

814 --> d= --> ye zarf (variable) misaze bename d =

jam( --> parnatez --> tabas
    mrie bala check mikone
    mibine tarifesh krdi --> ag nakarde bodi -_> error mide
    


jam(a,b) --> 2 ta vorodi 

jam(10,20) --> 2ta vroodi ddi oke (1 --> miss , 3 --> were given )
jam(10,20) --> a=10 , b=20

Body ro ejras moikone

c=a+b --> Mchjashm c=30
print(c)--_> too console 30
return 30 --> oonaje k sedassh zadi

d=jam(10,20)
d=30


--> d=30



'''


def jam(a,b):
    c=a+b
    print(c)
    return c




def jam(a,b):
    c=a+b
    return c
    print(c)


d=jam(10,20)





def calculator(a,b,amalgar):
    
    if amalgar=='jam':
        c=a+b
        return c
        #print()
    
    elif amalgar=='tafrigh':
        c=a-b
        return c
    
    
    
    




#---tabe e vorodi nadare , khoroji dare


#adade

def pi():
    #amaliat ......
    #result pass 
    return 3.14



a=pi()

print(a)
    


pi=3.14

a=pi
    
    
    
#tabe ee drim na khoroji dre na voorodi

def welcome():
    print('salam khosh omadid')
    
    
    
    
welcome()






#-----------------------------------
# f= m * a

#jesmi jerme m , acceleration--> a ---> f= m*a


def newton(m,a):
    
    f=m*a
    print(f)
    #return f


newton(20,5)  #20 * 5 -->100
newton(10)

def gravity(m):
    #f=m*a
    #a=9.8
    f=m*9.8
    print(f)
    
gravity(20) #196.0
gravity(20,5)

#ag frd m --> zarorie

#age a dad ---> f= m* a --> javab print

#age a ro ndad --> f=m*9.8 pish farz

#gahan dakheel tavabe mikham pishfarz bezaram


#general(5,20) --->  5* 20 = 100
#geenral(5)---> 5 * 9.8 = 48


def general(m,a=9.8):
    f=m*a
    print(f)
    
    
general(5,20) #---> m=5 , a=20 --> f=5 * 20 = 100 , 100

general(5)  # --> m=5 , a=9.8 --> f= 5 * 9.8 = 49.0

#range(1,10,)


'''

def range(start,end,step=1):
    dsdsasdaas
    


range(0,10)



range(0,10,1)


range(0,10,2)



'''



def jam(a,b):
    c=a+b
    return c


jam(10,20) #30

jam(a=10,b=20) #30

#argument ro 



#--------
#ag bgi na argument niazi nis fght bayad taraf adad bzne

def jam(a,b,/):
    c=a+b 
    return c




jam(10,20)

jam(a=10,b=20) #TypeError: jam() got some positional-only arguments passed as keyword arguments: 'a, b'






#-------------
def jam(*,a,b):
    c=a+b
    return c


jam(10,20) #TypeError: jam() takes 0 positional arguments but 2 were given

jam(a=10,b=20) 



#a , b , c , d 

#a , b --> adad nazad
#c , d --> hatmam adad bzne

def tarkibi(a,b,/,*,c,d):
    f=a+b+c+d
    print(f)
    
    
tarkibi(10,20,c=30,d=40)





def jam(a,b):
    c=a+b
    return c



f=jam(10,20)

print(c)

#NameError: name 'c' is not defined


'''
1060 ta 1062 --> jam yek tabe ast k a, b vorodie , c khorojie , body


1066 --> f --> zarf skahte =

jam(  -->tabe --> tarif krdi

jam(a,b)--> a , b
hargoone esme zarf ( hargoen variables, dar inpuyt , output , bvadane)
tabe -->hamashon zarf haee hasan k movaghatan 

a=10 , b=20
c=a+b = 10 + 20 = 30
return c --> 30 

f=30


local variables

global (sarasari)


'''


#-------------------------------------------
#--------------------------------------------


def jam(a,b):
    global c
    c=a+b
    return c



f=jam(10,20)

print(c)

#--------------------------------------------


#calulato


#1---psudocode


adade_aval=float(input('adade avaleto begooo:'))
adade_dovom=float(input('adade dovometpo begoo:'))
amalgar=input('amalgareto begoo(jam,tafrigh,zarb,taghsim):')

if amalgar=='jam':
    answer=adade_aval+adade_dovom
    print(answer)
    
elif amalgar=='tafrigh':
    answer=adade_aval+adade_dovom
    print(answer)
    
    
elif amalgar=='taghsim':
    answer=adade_aval/adade_dovom
    print(answer)
    
elif amalgar=='zarb':
    answer=adade_aval*adade_dovom
    print(answer)
    
else:
    print('eshetabh neveshti')






def calculator(adade_aval,adade_dovom,amalgar):
    if amalgar=='jam':
        answer=adade_aval+adade_dovom
        return answer
        
    elif amalgar=='tafrigh':
        answer=adade_aval+adade_dovom
        return answer
        
        
    elif amalgar=='taghsim':
        answer=adade_aval/adade_dovom
        return answer
        
    elif amalgar=='zarb':
        answer=adade_aval*adade_dovom
        return answer
        
    else:
        print('eshetabh neveshti')   
        return None
    

myvariable=calculator(10, 20, 'jam')






#---------------------------------
#---------------------------------
#---------------------------------


def calculator(adade_aval,adade_dovom,amalgar):
    '''
    Parameters
    ----------
    adade_aval : float
        adade avali k mikhahid bedahid
    adade_dovom : float
        adade dovomi k mikhahid bedahid.
    amalgar : str
        jam / tafrigh / zarb / taghsim.

    Returns
    -------
    answer : float
        in tabe miad adade aval o dovom ro migire
        mesle yek mashin hesab behet javab ro pas mide.

    note**: mroagheb bashid k agar dar taghsim adade dovom
    ro 0 bzarid in tabe crash mikone
    
    '''
    

    if amalgar=='jam':
        answer=adade_aval+adade_dovom
        return answer
        
    elif amalgar=='tafrigh':
        answer=adade_aval+adade_dovom
        return answer
        
        
    elif amalgar=='taghsim':
        answer=adade_aval/adade_dovom
        return answer
        
    elif amalgar=='zarb':
        answer=adade_aval*adade_dovom
        return answer
        
    else:
        print('eshetabh neveshti')   
        return None
    

myvariable=calculator()








    
    
    