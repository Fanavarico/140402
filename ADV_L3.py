"""
In The Name of GOD

Created on Sun Jun 29 18:30:36 2025

@author: Ali Pilehvar Meibody


ADV ----L3-------


Review------------------
python --> interface between human (english) / machine ( bianry 0,1)

In zaban --> 3 ta ghesmat dare 
har kalame ee



az bala ta peen az chap b rast mese ye ensan codeto
mikhone va ejra mikone

--------reserved---------
1---> python built in function --> print(), len() ,type() , input(), open(),....

2-->keywords--> if , else , for , while, elif , ....



-----unreversed----------
3--> variables ( moteghayer ha) ---> khdoeshon chand no hasan

3.1. Numbers ( int, float, complex) --> ** * / + - == > < !=
3.2. Boolean ( True , False)
3.3. Str --> string --> qutation '' harchi minevehstim reshte 
--> a='salam'
0 1 2 3 4 
a[2]  a[3] --. a , l 
str functions --> fght baraye str ha boodn / seda nmizdi()
roye varibale . esme function

a='salam' 
a.upper() ---> khrooji 

a --> taghir nmikrd
b=a.upper()
1--> kochik bozorg
a.upper()
a.lower()
a.title()
a.strip() --> space ro hazf
a.split() --> done done 

2--.adad mnidadan
name.count('a') ->2
name.find('a') --> indexe 0

3--> true False
name.islower()  ->True False


"""

a=10 #sahih 
print(type(a)) #<class 'int'>
a=10.2 #ashari
print(type(a)) #<class 'float'>

#riaziat --> danehsgah lisans --> Riazi1 
#--> yek mokhtasatye ajdid 
#adade jadid --> 

# do bakhsh skahte 4 + 2j
# a + bj
#3 + 8j
#7 + 9j

#i**2 = -1 
#mage mishe y adad agar b tavane 2 berse --> manfi 
#+ + = +
#- - = +
#**2 <0 nmishe

#dar in mokhgtase complex --> i , j 
#i**2=-1 --> dota javab ham dare
#i**4 = -1 --> 4 ta javb dare

#python --> adad ham support mikonm
a=3j
print(type(a)) #<class 'complex'>


A=-100
print(type(A)) #<class 'int'>
#- binahat -10 -9 ,....-1 0 1 2,...9,10 ,...binahayt

#ashari 

#import math
#math.sqrt(3) # 1.7320508075688772

#----------------
#-----VARIABLES-----
#1-numbers
#2-boolean
#3-str

#---Iterators , 
#ag man bkham chanta variable ro yeja bzaram chi?
#10 , 20 , 30 , 45 , .,...

#chnata moteghayer
#chanta megdhar dar yek zarf
#multiple variables inside one variable (iterator)

#----> LIST ---
#value , value , 
a=[10,20,30,40,50]
print(type(a)) #<class 'list'>

a=[10,10.445,3j,True,'SAalma']
print(type(a)) #<class 'list'>

print(len(a)) #5

#List --> Iterators
#dakhelesh --> ozvbash -_> element

#dastersi

#esme variable ro seda mzini [] --> too dleesh migi kodom element

#elemente 1 ro mikhay --> 10
#az 0 shoro mishavad

a[0] #10

a[1] #10.445

#az 1 ta 3
#[start:end+1]

a[1:4] #--> element 1 , 2 , 3
#a=[10,10.445,3j,True,'SAalma']
#--> 0 1      2   3     4
#[10.445, 3j, True]

#nbaraye taghir

a=[10,20,30,40,50,60,70]

mylen=len(a)
print(mylen) #7
#7 ta element
#0 1 2 3 4 5 6

 
a[6] # 70


#-----------
a[-1] #70

#yeki monde b akahro

a[-2] #60

a[-3] # 50


#element 2 --> 1000

#aval dastresi
#bad taghir

a[2]=1000


print(a)
#[10, 20, 1000, 40, 50, 60, 70]


#-------OPERATION-------

mylist=[10,20,30,40,50,60,70,80,90,100]
#> < == COMAPRISON --> KAR NMIKONE
mylist+2 #TypeError: can only concatenate list (not "int") to list
mylist**2 #,....


mylist * 2
'''
[10,
 20,
 30,
 40,
 50,
 60,
 70,
 80,
 90,
 100,
 10,
 20,
 30,
 40,
 50,
 60,
 70,
 80,
 90,
 100]

'''

#operation mikhay anjam bdi 
#ingahd sade nmitoni anjam bdi

#ma--> be donbale rah haee hastim k betonim
#adad bnvisim + - * 







#list --> list functions

#functions --> ()  --> khoroji mide aksaran --> amalkard


#----> built in fucntions --> barayte hamas --> anrenji
print()
len()
type()
open()
input()
enumerate()
zip()



#---STR frunctions--------
#funciton fghht baraye str ha hastan 
#dot . esmo 
#taghir nmdie khoroji mide

name='ali'

new_name=name.upper()

print(name) #ali

print(new_name) #ALI



#---LIST functions------
#function haee fght baraye List ha hast
#variable dot. emsesho bnvisi
#taghir mide, khoroji nemide

mylist=[10,20,30,40,50,60,70,80,90,100]


#change--->
mylist[2]=10000
print(mylist)
#[10, 20, 10000, 40, 50, 60, 70, 80, 90, 100]



#yehi onja jash konam

#30 hazf konm, , yechizi inaj ja konm

#tabe e --> insert()
#insert()
mylist=[10,20,30,40,50,60,70,80,90,100]

mylist.insert(2,10000)

print(mylist)

#[10, 20, 10000, 30, 40, 50, 60, 70, 80, 90, 100]


new_list=mylist.insert(2,10000)

#esme_list.insert(index,adad)
#too kodom index, ch adddi ja kone


print(new_list) #None

#taghir mdie, khrooji nmide--> yani niaz b zarf ndre



mylist=[10,20,30,40,50,60,70,80,90,100]


#b tahe listy ezafe konm
#chiakr konm?
#append kardan --> 

mylist.append(2000)

#esme_list.append(adad) --> kodom adado b tahe list ezafe kone


print(mylist)
#[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 2000]



#2 ta tabe dg 

#pop

#rmeove


#remove()


a=[10,20,30,40]


a.remove(30)

print(a) #[10, 20, 40]


#pop ham hamon rmeove, value , 
#kodom adado mikhay remove, kodom index

a=[10,20,30,40]

a.pop(2)


print(a) #[10, 20, 40]


a=[10,20,30,40,50,30]

a.remove(30)
print(a) #[10, 20, 40, 50, 30]

#hamishe --> manteghe python

name='salam'

name.find('a') #1



a=[10,20,30,40,50,30]

a.remove(30)
print(a)
#[10, 20, 40, 50, 30]

a.remove(30)
print(a)
#[10, 20, 40, 50]


#-----------------------
#delete , clear

#delete --> hamishe hazxf she 

a=[10,20,30,40]

del a

print(a) #NameError: name 'a' is not defined

#kole zarfo ba jash hazf krde


#--------------

a=[10,20,30,40]

a.clear()

#zarfe has --> ama toosh khalie
#toosho clear krdim

print(a) #[]

b=[]

#-------------------

#-------Iterables --> 
#--> chiz haere , chanta vakue dakheelsh mitoni bzari
#1---> LIst
#2--> tuple
#3--> set
#4-->dictionary





#------list-----------
a=[10,20,30,40,50,60]
a=list((10,20,30,40,50,60))

#--> ordered (index) , changable , allow duplicated

a[3]
#40


a[3]=400000
print(a)
#[10, 20, 30, 400000, 50, 60]


a=[10,20,20,20,20,20,20,20]






#------tuple-----------
b=(10,20,30,40,50,60)
b=tuple((10,20,30,40,50,60))
#chANge nmishe --> data base ha , dataharo tuple behet pas midan


#--> ordered , unchangable , allow duplicated

b[3] #40 

b[3]=1000
#TypeError: 'tuple' object does not support item assignment


#tuple-->list taghir midm list --> tuple

b2=list(b)

b2[3]=1000

b=tuple(b2)

print(b)
#(10, 20, 30, 1000, 50, 60)




#------set-----------
c={10,20,30,40,50,60}
c=set((10,20,30,40,50,60))

#--> unordered , unchangable , doesn allow duplicated


#index
c[2]
#TypeError: 'set' object is not subscriptable

print(c)
#{40, 10, 50, 20, 60, 30}


#c[2]--> 

#duplicated (tekrari ) oonaro hazf

c={10,20,20,20,30}

print(c)

#{10, 20, 30}

#--> aksaran --> majmoe ha hast
#tekrario hazf koni
#ejtejma , eshterak bgiri 
#






a=[10,20,30,40]
b=(10,20,30,40)
c={10,20,30,40}


#------dict-----------

#ye ensani

a=[30,10000,'bmw','black']

#range cheshe
a[3]

a[0]

#bejaye index
#esm dashtam

#a['ghad']
#a['sen']
#a['hesba;]

#dictonary maninja

#cxxxhanagble , duplciated , ...
#index --> keys (kilidvazhe dsare)
a=[30,10000,'bmw','black']

d={ 'sen' : 30 ,  'pool' : 10000 , 'mashin' : 'bmw' , 'rang': 'black' }


#behet in ejazer ro mide k kilidvazhe ro seda bzni


d['sen'] #30

d['pool']


d['mashin']

#moshakahsat darin va mikhayd behehs dastresi epyda konid


d={'devices': ['d1','d2','d3','d4']}



d={'devices': [[10,20,30],[50,60,70]]}


#==================================
#==================================
#==================================
#==================================
#==================================
#==================================
#==================================

product_code=input('code mahsooleton ro begid:')
product_name=input('name mahsooleton ro begid:')
product_price=float(input('gheymate mahsoooleton ro begid:'))

text=f'''

-------PLUTUS--------

Product name : {product_name}
Product Code : {product_code}

     Total price: {product_price}
     

aya shoam etelaate baal ro taaed mikonid:
'''


print(text)



#-------------------
product_code=input('code mahsooleton ro begid:')
product_name=input('name mahsooleton ro begid:')
product_price=float(input('gheymate mahsoooleton ro begid:'))
discount=float(input('darsad takhfif begid:'))




text=f'''

-------PLUTUS--------

Product name : {product_name}
Product Code : {product_code}

     Total price: {product_price* ( 1 - discount/100)}
     

aya shoam etelaate baal ro taaed mikonid:
'''


print(text)


'''
-------PLUTUS--------

Product name : nvidia
Product Code : l100
     
     Total price: 800.0


aya shoam etelaate baal ro taaed mikonid:
    
'''







#========================================
#========================================
#========================================
#========================================

#--> hamaro begire berize toye ye list 
#badesh az tooye list element haro bekeshe biron dakhele text
#berize


product_code=input('code mahsooleton ro begid:')
product_name=input('name mahsooleton ro begid:')
product_price=float(input('gheymate mahsoooleton ro begid:'))

mylist=[product_code,product_name,product_price]


print(mylist)
#['l100', 'nvidia', 1000.0]



text=f'''

-------PLUTUS--------

Product name : {mylist[1]}
Product Code : {mylist[0]}

     Total price: {mylist[2]}
     

aya shoam etelaate baal ro taaed mikonid:
'''


print(text)

'''
-------PLUTUS--------

Product name : nvidia
Product Code : l100
     
     Total price: 1000.0


aya shoam etelaate baal ro taaed mikonid:
    
'''



#=================
mylist=[]


product_code=input('code mahsooleton ro begid:')
mylist.append(product_code)


product_name=input('name mahsooleton ro begid:')
mylist.append(product_name)


product_price=float(input('gheymate mahsoooleton ro begid:'))
mylist.append(product_price)


print(mylist)
#['l100', 'nvidia', 1000.0]




text=f'''

-------PLUTUS--------

Product name : {mylist[1]}
Product Code : {mylist[0]}

     Total price: {mylist[2]}
     

aya shoam etelaate baal ro taaed mikonid:
'''


print(text)



#===============
#===============
#================


product_code=input('code mahsooleton ro begid:')
product_name=input('name mahsooleton ro begid:')
product_price=float(input('gheymate mahsoooleton ro begid:'))



mydict={ 'code' :product_code,
        'name' : product_name,
        'price': product_price}


print(mydict)
#{'code': 'l100', 'name': 'nvdiia', 'price': 1000.0}



print(mydict['code']) #l100
print(mydict['name']) #nvdiia
print(mydict['price']) #1000.0



text=f'''

-------PLUTUS--------

Product name : {mydict['name']}
Product Code : {mydict['code']}

     Total price: {mydict['price']}
     

aya shoam etelaate baal ro taaed mikonid:
'''


print(text)


'''

-------PLUTUS--------

Product name : nvdiia
Product Code : l100
     
     Total price: 1000.0


aya shoam etelaate baal ro taaed mikonid:

'''




'''

TASK1--->
code , nmame , price ro begire berize too list
badesh behesh bege yek chizi benevis ta hazf konm
price --> price ro hazf kone
code --> code hazf kone
name --> name ro hazf kone



TASK2--->
inaro begrie berize trooye tuple 
va badesh az tuple bekeshe biron tooye text neshon bde







'''









#==================================
#==================================
#==================================
#==================================
#==================================
#==================================
#==================================

'''

------reserved-----
1-python built in functions
2-keywords -----> banafsh --> 
3-variables ( numebrs, bool , str , iterables 
             (list, tuple , set , dict))





********
2-keywords -----> banafsh --->

ina miad manteghe code ro avaz mikone
function -> amalkardi
variable--. chzii toosh miriz


dastooore --> miad manteghe code ro avaz mikone


PYHTON AGHA
harjaro shoam run koni


script (edit) --. mese safe chate telergame
ta send ro nzni ( ejra ro nzni) -->
chizi run nmishe

vaghty run mizni

ya --> kolesho run bzni 
ya I kochik --> yek ghesmati ro selecty koni



harjaro k run kardi --> Python mofaser

miad az bala ta paeen
az chap b rast
mese ye ensan k code mikhone 
code ro ejra mikone



'''




print('salam')


print('chanta mikhay?')

print('khodafez')

'''
az bala miad mirese b kjhatye 867 
badesh 868 -> p r i n t (
    print()--> harchi tozh bashe ro man tooye
    console namayesh midm
    \
        tosh neveshte shode slam
        
        toye concole --> salam
        
    az chap b rast
    az bala b paeen

869 khalie
p r i n t ()
chanta mikhaty


'''




#yani mikhay 3 bodu koniu

#yek khat code ro 
#yek khat code ro ya bakhshi az codto
#mese hamsihe ejra nshe

#balke b sharti ** ejra bshe
#---> keyword-->manteghe khodnan epythono beham mzini


#---> IF

#if

'''

ghable oon kahti k mikhay 
mese hamishe ejra nshe

hamishegi nabashe

if shart:
    .........


'''


#dar harsoorati har chizi in ejra bshe
print('salam')

#ama ino ghablesh ychziio chekc kone
#fght baraye yeseri shroot ejra she , yesri shorot jer nshe
print('chanta mikhay')
#a+2 
#s.append()


#dar harsoorati har chizi in ejra bshe
print('khodafez')




#dar harsoorati har chizi in ejra bshe
print('salam')


if shart:
    print('chanta mikhay')


#dar harsoorati har chizi in ejra bshe
print('khodafez')


'''

shart?????
if hsart

shart --> gzoare ee bashe
k behet javab --> True False


True --> on khate ejra mishe 
False--> ejra nmishe


shart ?

condition comaprison operators
==
!=
>
<



2-> str function
.islower()
.isupper(()
         
         

'''



sen=10


print('salam')


print('chanta mikhay?')


print('khodafez')


'''
salam
chanta mikhay?
khodafez
'''

#magar inke afrade balaye 18 sal --> 
#shart 



sen=10


print('salam')

#poshte in if bezanam --> oon khate codi k
#miikham shartish kjonm
print('chanta mikhay?')


print('khodafez')




#-----

sen=10


print('salam')


if shart:
    print('chanta mikhay?')


print('khodafez')


#sen>18 --> True , False

#sen--> zzire 18 --> False
#balaye 18 --> True -->ejra mishe





#-----

sen=10

print('salam')


if sen>18:
    print('chanta mikhay?')


print('khodafez')



'''
salam
khodafez
'''



sen=20
print(sen>18) #True


print('salam')


if sen>18:
    print('chanta mikhay?')


print('khodafez')



'''
salam
chanta mikhay?
khodafez

'''



#-----------------------
#---------------------
#-------------------------

#body -->

#abdaneye sharft


sen=10


if sen>18:
    print('chanta mikhay')
    print('che marki mikhay?')
    print('gheymat ,...')
    a=10
    a+100
    


print('khodafez')




#khodafez






sen=20


if sen>18:
    print('chanta mikhay')
    print('che marki mikhay?')
    print('gheymat ,...')
    a=10
    a+100
    


print('khodafez')



'''
chanta mikhay
che marki mikhay?
gheymat ,...
khodafez

'''


'''


HARMOGEH DIDI --> codet mikhay az halate manteghi (logic)
bniad biroon--> keywords


bahse inmmishe yek khat code ya chan khat code ro
mikhay hamshegi ejra nshe-p-> shart

dastoorate sharti estefade koni


1-if

2-if else




3-if elif

'''




#if---->yek rah zan bedoonesh


#maid az beyen hjame kaht coda k ejra mishe

#done donashono ye rahzane mikeshe kenar
#mibien kia bala 18 

#ooane k bala 18 hastan --> khosh omadi ro ejra mikone

#onae k nisan chi???
#hichi asan hichji ejra nmikone


sen=20

if sen>18:
    print('khosh amaadi')


#khosh amaadi


sen=12

if sen>18:
    print('khosh amaadi')

#khali

#mieg oonae k sharteshon False
#beman che

#-->if --> shoam yek gehshri ro mikhay y kari barahson kohni
#codto dfght baraye yek bakshh mijkhay run konish

#--> rahzanas

'''
has shoam do rahi doros koni


2--->IF else


'''

#1- if --> ag shart True shod k inkaro kon
#ag nashod bikhial rad sho boro


#21--> dorahi baz koni

#ag shart True shod --> kare 1
#age nashod bikhial na --> kare 2


#rah nadare rad shui ---> sade 
#do rahi



'''

if shart:
    kare1
    ....
    ...
    ......
else:
    kare2
    ....
    
    

if shart:
    kare1
else:
    kare2
    
    
ag shart True --> code 1
age shart Flase shod --> code2



if shart:
    code1
    code101
    codee102
    code103
    ....
else:
    code2
    code202
    code2002
    code200002

'''

#----> 1 - if

sen=10


if sen>18:
    print('khosh omadid')
    
    
#gardane afardi k bala 18 hyastan ro migiri
#va emal mikoni--> code--> kjhosh omadid

#age paen 18 -> beman che
    

#----2 if else

#ya 1 ya 2 

#zhart tyru , false

#ya khosh omdid
#senme hsoma ghanoni

#dorahi sakhtam

if sen>18:
    print('khosh oomadid')
    
else:
    print('sene shoma ghanoni nist')

#chanta kaht 


if sen>18:
    print('khosh oomadid')
    print('chanta sigar mikhayt>')
    print('kodom mark')
    
else:
    print('sene shoma ghanoni nist')
    print('esrar koni znag mizanam b valedein')
    print('khodafez')




#=========================
#=========================
#=========================
#=========================
#=========================
#=========================
#=========================




product_code=input('code mahsooleton ro begid:')
product_name=input('name mahsooleton ro begid:')
product_price=float(input('gheymate mahsoooleton ro begid:'))



text=f'''

-------PLUTUS--------

Product name : {product_name}
Product Code : {product_code}

     Total price: {product_price}
     
'''

print(text)

#print('aya etelaate balaro taeed mikoni ya na')
#aya etelaate balaro taeed mikoni ya na?

#mikhamchizi begiram

answer=input('aya etelaate balaro taed mikoni ya na?(yes/no):')

print('sabt shod')
#in code dar hame soorat
#dare ejra mishe

#mikham fght kasanei k answer==yes hast ro
#barashon benevisam sabt shod

#aval yk tgahiri  -> keywords

#sharti --> if , if els,e elif 

#mese ye rahzan
#fght oonae k answer yes has ro barashon sabt shod



#-----------
product_code=input('code mahsooleton ro begid:')
product_name=input('name mahsooleton ro begid:')
product_price=float(input('gheymate mahsoooleton ro begid:'))
text=f'''

-------PLUTUS--------
Product name : {product_name}
Product Code : {product_code}
     Total price: {product_price} 
'''
print(text)
answer=input('aya etelaate balaro taed mikoni ya na?(yes/no):')

#if shart:
#    print('sabt shod')


if answer=='yes':
    print('sabt shod')
    

#yes --> in kar krd


#if-->
#sabt shod hamishe print nmishe
#fght dar soorati k answere==yes bashe pritn mishe




#yes --> sabt shod
#no --> motasefane sabt nashod

#------------
product_code=input('code mahsooleton ro begid:')
product_name=input('name mahsooleton ro begid:')
product_price=float(input('gheymate mahsoooleton ro begid:'))
text=f'''

-------PLUTUS--------
Product name : {product_name}
Product Code : {product_code}
     Total price: {product_price} 
'''
print(text)
answer=input('aya etelaate balaro taed mikoni ya na?(yes/no):')

#agar yes --> sabrt shod
#age harchi dg nevesht (yes nanevesht) -p-> motasefane sabrt nashod

#dorahi misazi

#age neveshte --. yes ---> ye karo (kare1)
#age harchi dg nevesht --> kare 2


if answer=='yes':
    print('sabt shod')
else:
    print('motasefgane sabt nashod')


#motasefgane sabt nashod





'''
1--> task3-->

inja shoma benevisi Yes --> motasefane minveis
sabt anshod

_---> dorostesh konid
k ag ye nafar nevesht Yes --> sabt shod



task4-->
ag taraf nvsht fasele yes --> 
bayad benevise sabt shod





#---------
ADV -- L4----

if 
else

if elif --> (3)

--> chanta mesal -> hal mikonim


for , while



'''
