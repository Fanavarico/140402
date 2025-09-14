
"""

In The Name of GOD

Created on Sun Jun  8 18:34:39 2025

@author: Ali Pilehvar Meibody




ADV_L2



"""


'''


human -----interface(python programming language)--- machine (0,1 binary)



#---------
3 daste


---------------reserved words----------------------
1- python built in function --> () yek kari mikone
print()  input() len()  type()
narenji


2-keywords --> manteghi , if , else, for , while , def , class ,....
--> banafsh


-------------unreserved words---------------------
sefidesh---> esme yek zarfg bashan

zarf --> variable (moetghayer)----> megdhar (value) --> assign 


esme zarf - mohtaviate zarf

esm --> ghanooon  * 2 reserved  --> Name name _

=


---------------values for variables------------
1--->numbers (int, float , complex (i j )) --> ** * / + - 
2--->bool (True , False) --> == != > < >= <=
3--->str --> string --> reshte ee az character harchi bashe
4--->



'''



a=10
b=30

#a+b = c

c= a+b


#_----
a=10

a=40

#a khali mikone 40 ro toosh mriize


#----
a=10
b=40

a=b




#jofteshon 10 ya jofteshon 40?
#hamishe chapie ro ya misaze , ag vojod dare khali mikone
#a=0
#a=40
#b=40


#--------
a=10 #dastoor --> a=10

a==10 #ppresh aya a barabar hats ba 10 -> True False


#--------------------------
a='salam'

print(type(a))
#<class 'str'>
#strin reshte--> ye adad

#resht --> harf , chjaracter, kalame, jomkle

a='salam b hameye azzan khosh oomadid'



'''
mohasbati
+ * - / **


a+b 


a=10



'''


'''
moghhayese ee

==
!=
>
<

soalie

aya mosavi hast?


'''


a=10
b=30
a==b #False


a=10
b=10
a==b




a=10
b=30
a=b





#------------
a=2  #adade 2 -->
print(type(a)) #<class 'int'>

a/10 #0.2

#qoutation --> str
#keyworde 23 
b='2'
print(type(b)) #<class 'str'>

b/10 #TypeError: unsupported operand type(s) for /: 'str' and 'int'


n='ali'
n='salam'
n='@'
n='2'



print(a==b)
#False

print(a) #2


a=10000
print(a) #10000



a=10
b=40

a=b


#========================
#========================
#========================
#========================
#========================
#========================

name='ali'

#print(ali)

'''

zarf esmesh name toosh chi rikhtm ali
'''

print(name) #ali



print(ali)
#NameError: name 'ali' is not defined

print('ali')

#harfi hrchizi k gheyr az zabane pythn
#berizi tooye zarf (esm)

#tooye quoit


#==========================================
#===========================================

name='ali'
last_name='pilehvar'

print(name)
print(last_name)

'''
ali
pilehvar
'''



print(name,last_name)
#ali pilehvar

#print()

#print( , , , , , , , , )


print(name,last_name , 100)

#ali pilehvar 100




print(ghad)
#NameError: name 'ghad' is not defined




#andaze


name='alipilehvarmeibody'
 
len(name) #18


type(name) #str


name1='ali'

name2='ali '


print(name1==name2)



print(len(name1)) #3
#a l i

print(len(name2)) #4

a='2'

a=' '

a='23723987398273@#!#Ihjuhjesklu1dhy13271d312s7ym'


#False



#-----------------
#-----------------
#1-assignment 
#esme zarf = ' ' 

#2-ndazasho?

#print(len(esme zarf))


#3-type esh chie
#print(type(esme zarf))


#4-chijori dastresi peyda konm??
#reshte ? ---> reshte ee az horod
#reshte ee az charactewr 

#ali --> a l i

#b yekodom az in element (joz)


#masalan esme shoam felane
#Mikham bbinm 5 omin harfe esmet chie???

name='alipilehvar'

#too barname nevsii hamehci az 0 shoro mishe

#a l i p i l
#0 1 2 3 4 5 --> index

#chandomie --> index 

#index---> 0 shor mishan

name='alipilehvar'

#b 5omin harfe esmam

#b indexe chande esmam???

# a l i p i l e h v a r
# 0 1 2 3 4 5 6 7 8 9 10

#i

#5omin harf --> indexe 4

#mikhay elemente indexe 4 e yek zarfio bekeshi biuron
#nayad aval esem zarfo biari 



name[4]
#indexe 4-->
#Out[39]: 'i'


my_elemnt=name[4]

#slicing yad bgirim

#chanta ro mikhay 

#5 ominta 8omi 

# a l i p i l e h v a r
# 0 1 2 3 4 5 6 7 8 9 10


#i l e h

# 5 ta 8
#4     7 

#4 ta 7 

#: ta 
#bahse rnage
#start end

#end ro cover nmikoen end -1


name[4:8]

#4 5 6 7 XXX8XXXX

#Out[41]: 'ileh'


name='alipilehvar'


#ali ro bekeshid biron
#chi minevisidi
#indexe 0 ta 2


name[0:3]
#Out[42]: 'ali'



#--------------------
#assignemnmt
#len
#tyep
#access
#sclicing yad grftim

#str methods
#str functions

#توابع مختص رشته ها

#yekseri tabe hastan k fghtr mokhtase 
#mokhtase str ha hastan


#TABE??
#python built in function-0-
#print()
#input()
#...()
#len()
#type()



print(10)
print(10.545)
print(True)
print('ali')

#mokhtas , baray ehame



#tabe hae estefade konim fght mokhtase str h hast

'''
baraye str HA sakhte shode

upper()

kalame e behesh bdi --> bozorgesh mikone

ali ----> ALI
salam --> SALAM



upper()
lower()
islower()
count()
find()
split()
strip()

.....




'''


len('ali') # 3

#upper ---> ()    ('ali) --> ALI

#upper('ali')
#NameError: name 'upper' is not defined

#inja k drm harf miznmm python buil in function 

#str functions --> function fght baraye str 

name='ali'

#esme_zarf.esme_tabe()


#upper(name) XXXXXXXXXXX

name.upper() #'ALI'

new_zarf=name.upper()

print(new_zarf) #ALI

#kochjkesh kon

#lower()

#ALI --> ali

#lower(new_zarf)


print(name) #ali

new_zarf.lower()


#-------------------
#-------------------
name='ali'

zarf=name.upper()

#ALI --> zarf

#In The Name


print(zarf) #ALI

print(name) #ali



#emal nemishe, balke khoroji mide

#tavabe haye TYPI
#str function
#list function 
#x function

#2 no

#emal mishan --> ghablie emal mishe , naiz b zarfe jadid ndri

#khoroji midan --> (emal nmiushe) --> zarfe jadid biari jolosh , ghablie avaz nmishe


a=100

a.upper()
#AttributeError: 'int' object has no attribute 'upper'


'''

-----STR FUNCTIONS------

vase str hast
esme_zarf.esme_tabe()

***
khoroji mide, emal nmishe
yani roo on zarfi k dot mizni. -> taghiri emal nmishe
ama bayad yek zarfe jadid jholosh bezari


esme tab           karkard

capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values from a dictionary in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Converts the elements of an iterable into a string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning





------3 ghesmat------




'''




#_______> 1--> khorojish , khdoe hamono taghir mdin 


name='ali'

#zarf=name.upper()
name.upper() #ALI

name.lower()

name.capitalize() # 'Ali'

name='in the name of god'

name.title() #'In The Name Of God'

name.capitalize() #'In the name of god'

#tavabe STR ---> str khoroji midan


#----> 2 --> ina str migirn , khroji adqd mide??

name='ali'

#count

#horofi ro bnvism bhm mige chanta vojod dare too on chizi dot


name.count('a') # 1

#miagrde k too name chnata a 


name='alipilehvarmeibody'

name.count('i') #3


#--------


#name.find()


name='ali'

#ag l ro mikhasam
#name[1]


name.find('l')  #adad

#peyda kon? --> bego kodom indexe

#shoamre indexo paas mide behm
#1



#------3----> str mgiir e, True false
#is

name='ali'


name.islower() #True


name='ALI'

name.isupper()

#@isdigit
#is....

#=======-============
#mororodi

#-----reserved-----
#1----pyuthon buyilt in function
#2----keywrpodss

#3---unreseerved--> variable
#3.1.numebrs( int, float, complex) | = + - ** * | == > < 
#3.2. bool (True , False)
#3.3. str ( reshte)


#assignment --> a=''
#andaze len()
#type()
#access (index)
#slice [index : index+1]
#methods----> str function

#zarf.function()
#funciton ha emal nmishan khoroji midn pas zarf bzar joloshj
#-------noe 1-----

#str migrftn str pas middn

#name.upper()
#name.lower()
#name.title()


#---noe2----
#str migrftn adad middn
#name.count('a') ---> 3 ta a hast
#name.find('a') --> #indexe 1 om has

#--noe3
#str migrf true false pas mdiad
#name.islower() ---> True False
#.....


#==========================
#==========================
#==========================
#==========================
#==========================
#==========================
#==========================

'''

man mikham yehcizi bashe ke
be sahebe kasbo kar bege lotfan code mahsoleto benevis 
oon venevise --> #zakhriahs konm
bad begam agha in xcocd, esme mahsolo benvisi
oonbenevsie --> #zkahirash konm
bad begam agha gheyamet mahsolo begoo -->
on bbenvsise

hamasho har 23 taro baham 
#dobare az taraf beporsam 
#in moshakhast .  .. . . . taeede 
behesh namayesh midim




html , ...


input()



'''

#yek zarf skahim
#jolosh yek tabeye dkaheli input 

#input(........) khoroji mide zarf bzar jolosh

#******* input --> hameye khoroji haro bsorat STR zakhire mikone


product_code=input('shomare code mahsooleton ro begid:')

print(product_code) #c100
print(type(product_code)) #<class 'str'>



#--------------
'''
@(digicala/)
@post
def (product_code):
'''    
    

product_code=input('shomare code mahsooleton ro begid:')
product_name=input('name mahsool chie?:')
product_price=input('gheymate mahsool chande?:')

'''
shomare code mahsooleton ro begid:l10  enter
name mahsool chie?:nvidia  enter
gheymate mahsool chande?:10000  enter

'''




#+++++++++++++++++++++++++++++++++++++++

product_code=input('shomare code mahsooleton ro begid:')
product_name=input('name mahsool chie?:')
product_price=input('gheymate mahsool chande?:')

text='''
PLUTUS FACTOR---------

Your product name : 
    
    Product code:
        
    Total price:
        
        ^^^^^^^^^^^^
do you confirm these informations?

'''

print(text)


#--khrojie console---
'''
shomare code mahsooleton ro begid:l10
name mahsool chie?:nvidia
gheymate mahsool chande?:1000000

PLUTUS FACTOR---------

Your product name : 
    
    Product code:
    
    Total price:
        
        ^^^^^^^^^^^^
do you confirm these informations?

'''






#==================================

product_code=input('shomare code mahsooleton ro begid:')
product_name=input('name mahsool chie?:')
product_price=input('gheymate mahsool chande?:')

text='''
PLUTUS FACTOR---------

Your product name :  product_code
    
    Product code: product_name
        
    Total price: product_price
        
        ^^^^^^^^^^^^
do you confirm these informations?

'''

print(text)


'''
PLUTUS FACTOR---------

Your product name :  product_code
    
    Product code: product_name
    
    Total price: product_price
        
        ^^^^^^^^^^^^
do you confirm these informations?
'''



ghad=100

print(ghad) #100

print('salam ghad e man 200 e ')
#salam ghad e man 200 e 


#-----------
#@hamroghe kahsi chizi az biron az zarfi berizi tooye yek matni
#f string estefade


ghad=100
print('ghad e man hast : ghad')


#ghadame aval --> f poshtesh bzar

print(f'ghad e man hast : ghad')
#ghad e man hast : ghad


#ghadame dovom

print(f'ghad e man hast : {ghad}')
#ghad e man hast : 100





name='ali pilehvar'

price=200000000


print(f'salam gheymate mashien {name} hast {price}')

#salam gheymate mashien ali pilehvar hast 200000000


#+++++++++++++++

product_code=input('shomare code mahsooleton ro begid:')
product_name=input('name mahsool chie?:')
product_price=input('gheymate mahsool chande?:')

text=f'''
PLUTUS FACTOR---------

Your product name :  {product_name}
    
    Product code: {product_code}
        
    Total price: {product_price}
        
        ^^^^^^^^^^^^
do you confirm these informations?

'''

print(text)


'''
shomare code mahsooleton ro begid:l100
name mahsool chie?:nvidiia
gheymate mahsool chande?:10000

PLUTUS FACTOR---------

Your product name :  nvidiia
    
    Product code: l100
    
    Total price: 10000
        
        ^^^^^^^^^^^^
do you confirm these informations?

'''


#============================================
#10%
#bayad takhfif emal kone rooye price-------


product_code=input('shomare code mahsooleton ro begid:')
product_name=input('name mahsool chie?:')
product_price=input('gheymate mahsool chande?:')

text=f'''
PLUTUS FACTOR---------

Your product name :  {product_name}
    
    Product code: {product_code}
        
    Total price: {product_price}
        
        ^^^^^^^^^^^^
do you confirm these informations?

'''

print(text)



#==================================
#==================================
#==================================
#==================================
#==================================
#==================================
#==================================
#==================================
#==================================
#==================================
product_price=220000


product_price * (10/100)

product_price * (1/10)

product_price * 0.1

product_price - product_price * 0.1

#90% 0.9

final_price=0.9 * product_price

print(final_price) #198000.0







#+++++++
product_code=input('shomare code mahsooleton ro begid:')
product_name=input('name mahsool chie?:')
product_price=float(input('gheymate mahsool chande?:'))

print(type(product_price)) #<class 'str'>

#100000
#'100000'

float('1000') # 1000.0
int(135.500) # 135



final_price=product_price * 0.9


text=f'''
PLUTUS FACTOR---------

Your product name :  {product_name}
    
    Product code: {product_code}
        
    Total price: {final_price}
        
        ^^^^^^^^^^^^
do you confirm these informations?

'''

print(text)


#TypeError: can't multiply sequence by non-int of type 'float'






product_code=input('shomare code mahsooleton ro begid:')
product_name=input('name mahsool chie?:')
product_price=float(input('gheymate mahsool chande?:'))
final_price=product_price * 0.9
text=f'''
PLUTUS FACTOR---------

Your product name :  {product_name}
    
    Product code: {product_code}
        
    Total price: {final_price}
        
        ^^^^^^^^^^^^
do you confirm these informations?

'''

print(text)



'''

PLUTUS FACTOR---------

Your product name :  nvidiia
    
    Product code: l100
    
    Total price: 9000.0
        
        ^^^^^^^^^^^^
do you confirm these informations?


'''




#===========================================
product_code=input('shomare code mahsooleton ro begid:')
product_name=input('name mahsool chie?:')
product_price=float(input('gheymate mahsool chande?:'))

text=f'''
PLUTUS FACTOR---------

Your product name :  {product_name}
    
    Product code: {product_code}
        
    Total price: {product_price*0.9}
        
        ^^^^^^^^^^^^
do you confirm these informations?

'''

print(text)




#========================================
#========================================
#========================================
#========================================
#========================================
#========================================
#========================================
#========================================
#========================================
#========================================
#========================================
#========================================
#========================================


#upper()
#lower()
#title()
#count()
#find()
a='ali'

a="ali"


text='
bename khoda
'

text='''

bename khdoa ,......


'''


text= """

bename khoda...


"""




#-----------------------
a='ali'

b='ali '

print(a==b)




#tabe  hast k miad faseleye samte chapo raste yek kalame ro
#hazf mikone
#strip()


b.strip() #'ali'


c=b.strip()

print(len(a)) #3

print(len(b)) #4
print(len(c)) #3


print(a==c) #TRUE


#strip()


name='     ali pilehvar  '

name.strip() #'ali pilehvar'



#------------------
#split()

text='salam arz shod, khedmate hamegi, man ali , hastam'

#vorodi --> str
#khrooji --> LIST


mylist=text.split(',')



#salam arz shod
# khedmate hamegi
# man ali 
# hastam
#[salam arz shod  ,  khedmate hamegi  , man ali   , hastma]
#4 ta joz

#bar asase , 
#str split --> joda jdoa tyike tikash konam baram beriz too lis
mylist=text.split(' ')


text='user/desktop/apm/nvdiia.xlsx'


mylist=text.split('/')



'''


#1-----> hamin mesal ro berid bejaye 10 % 
# az khode fard dsarsade takhfif begirid





#2---->
dar entehash azash beporsid aya confirm mikone ya na
age trf neveshte yes --> begid sabt shod
ag taraf nevesht na --> begdi sabt nashod



'''

product_code=input('shomare code mahsooleton ro begid:')
product_name=input('name mahsool chie?:')
product_price=float(input('gheymate mahsool chande?:'))

text=f'''
PLUTUS FACTOR---------

Your product name :  {product_name}
    
    Product code: {product_code}
        
    Total price: {product_price*0.9}
        
        ^^^^^^^^^^^^
do you confirm these informations?

'''

print(text)









