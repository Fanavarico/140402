"""
Created on Sun Aug 17 20:04:46 2025

@author: apm



ADV_L6 --> FUNCTIONS
ADV_L7 ---> CLASS

ADV_L8 ---> HALE MASAEL ( DORE EE, FUCNTIONS)


PROJECT_L1 ---> Project tadris , ya tek megdhari , 
dead line --> ersal konid
PROJECT_L2----> oon projat takmil konim , moshkel 




#---------------------------
ADV_L1 .... ADV_L7  

----------

HUMAN ------ PROGRAMMING LANGUAGE ---- MACHINE



---> zabna haye motefaveti
python
c++
c
fortran
javascript
html/css
java
GO
julia
pascal
......

farghesh --> tafavot haee --> mokhafaf sazi
application, karbordi

python --> backend , infrustructure --> zirsakht besazi
zirskaht --> ketabkhane [data process, simulation , engineering ,....
                         ketabkh hane motenave dar har hite ee kar konid]
AI --> hooshe masnooe --> python (ML , DATA PROCESSING, COMPUTER VISION, AUTOMATION)

FASTER PROCESS , computational expensive task --> C++ , Fortran
GUI --> Graphical user interface --> app , . --> javascript , html / GO [cross-platform]
Front --> backend --> Python


#---------------
python --------------

3 bakhshe asli
harchi benevisi --> python msihanse


1---python built in functions (print(),input(),open()...)
2---keywords --> manteghe code (if , if else, if elif , for , while ,....)
3--variables --> numbers (int, float, ), str , list, tuple, set , dictionary ,.... 

PYTHON BASIS , FOUNDATION --> yad grftim

kheyr--> ketabkhoone ha --> 
yekser mohti ha hastan


pip install ..... -->codash download 


from ketabkhone import jam

jam()


100 , 200 , 300 khat code 
yekseri code ha bshoma ejaze 

****mashin bekhay bsazi --> az aval nabayad charkh bsazi
shasi , platfrom , --> advanced tar
high-levelesh konid on teh top level





#------
artificial neural network --> shabake asabi masnooe
1960 ---> 1980 --> 1990 [hinton--> ]

1960 -- 1990 --> hinton --> perceptron --> zemeston ai
saal 2002 alexnet --> GPU run konan
alan --> hobabeshim --> 
AGI --> [] 


ANN --> shabake asabi masnoee --> algorithemi
Multi layer perceptron 

1960 --> 60 sal

yek neural network --> maghz kar mikone
proces pcihdiue ee --> az aval 
100 000 

sklearn , tensorflow --> zirsakht
tabe



from sklearn.neural_network import MLPRegressor

ANN=MLPRegressor(hidden_layer_size=(100,100,100))
ANN.fit(data)
ANN.predict(new_data)



functions --> b ch dard mikhord


codio download mirkdi
toosh khodet dasti taghir mdidi run

hamaro encapsule mikonan --> tabe
1000 khat 
estefade koni

1** unciton ch kari mikone ch komaki mikone

2--> nesbat b hoze eee --> ketabkhone hasho yad bgriid
documentation


numpy --> mohasebat
pandas--> kar ba excel , data manupulation
matplotlib --> rasm
sklearn --> Machine learning

Django --> backende website
fast-api --> AI tor , dataye sarii , crypto data





"""




'''

def name(vorodi,v,v,v):
    badane
    return khoroji



vorodi, khorohi nadashte abshe
vorodi Yes , khoroji NO
vodofi NO , kjhoroji yes
joftesho dashte



print != return



'''

'''


1---> psudocode --> script ta tah run bzne
automat, 


2---> function-based --> tavabe dakheel , seda zade
aksare API ,... --> backende website


-----------------
|     Login     |
|   user:       |
|   passsword:  |
|   button :    |
-------------------

Front --> jolo --> on ghesmat mibini 
zibaee ha [html / css /javascript]


user --> getplutus.solutions --> server [ computere yejaee , finalnd norway ]
--> server --> index.html [ html , css, javascript ] -->  mororgar browser (safari , google chrome )
engar in code ro miznan roo run --> website



esme --> user
password -->password
button --> click mikone


---> ooon posht?? mire ye jaygahi table username , password zakhrie shodan ( table of database)

user --> mire migrde beyen usernames --> ag nabashe nist ag bashe ham ...
user , password --> password == password --> ag are
--> redirect --> b ye safe html dg--> dashboard.html

backend etefgh miofte


front / backend 

backend --> python 


#----
html/css

<div ------
<div class=username , Username , entry>
   <div class=password , password, entry , type=* >
    <button class=login_button , colour = Yellow , login_button_function()
    
    
javascript

login_button_function():
    cons username = .get(username)
    cons password = .get(password)
    
    fetch (/login_handlling/):
        befres az front b backend
        
        
        

python------

@(/login-handling)
def login_handling(username,password):
    m,ire checkj mikone database
    
    agf username bodo 
    ag passowrd==
    if password==main_password:
        return True
        redirect (/dashbaord/)





ba fucntion --> nemishe anjam dad
--> class []

class --> moehem
C --> C++ 

c++ --> mohemtarin ---> support object oriented programming 
shey gera


3----> Object oriented programming (OOP )--> CLASS & OBJECT


'''
#dar kheyli kheyli application ha 
#Motasefane --> function

#----zirsakht baraye bank besazam-------

def welcome():
    print('salam moshtarie aziz khosh amadid')
    
    
#salam moshtarie aziz khosh amadid
welcome()



#-------3 ta tabeye asasio

#---> show_currency --> mojoodi
#---> deposition ---> variz
#_---> ATM ----> bardasht konim



def deposition(amount):
    global balance
    balance=0
    balance=balance + amount
    print(f'mojodie shoma hast {balance}')



welcome() #salam moshtarie aziz khosh amadid

deposition(1000) #mojodie shoma hast 1000



def show_balance():
    print(balance)
    
    
show_balance()
    

#global konam
#va inke moshkel ine
#man fght mitonm baray eyek user in karo anjam bdm

#100ta user, user ye balance dashte bashe???

'''

application --> karbord

niaz dahste bashid koli ajza
shey dahste abshi
aza 
afrad
user dahste


harkodom --> moshakahse khdoeshono dashte bashan

tavabe ee bashe k baraye hame yeksan kar kone bar asase
moshakahsateshonn


---> class ---> object besazid

object oriented programming (OOP)




'''
#def bank():
    
    
    
'''

class


attributes--> property --> moshakhast --> values

method --> functions ha hastam -> fucntion barashon



'''


#class---> besazi

class Bank:
    
    balance=100
    
    
#az class--> object

object1=Bank()

object1.balance #100


object2=Bank()

object2.balance #100
    

class Bank:
    
    balance=100
    
    start_date='farvardin'
    
    password='1234'
    
    def welcome():
        print('salam')



#aval yek object az class beeksh biron ( besaz)
object1=Bank()
    
#1---> attributes, property [moshakahs]
object1.balance #100
object1.password #'1234'
object1.start_date #'farvardin'

#2--->methods -->function ()
object1.welcome()



#-------------
#hezarta user besazi
#hamey user ha mahkooman k balance, start_date, password
#yeksan bashe

class Bank:
    
    balance=100
    
    start_date='farvardin'
    
    password='1234'
    
    def welcome():
        print('salam')


object1=Bank()

#--> baraye shoroe
#harchi 

#ma multilple user, property 

#az besazimshoj --> fsargho

#'az ebteda' yekseri moshakahse khas daran harki

#object1=Bank(name='ali pilehvar' , code_meli='00440044',password='1234',balance=2000)
#object2=Bank(name='vahid' , code_meli='43432423',password='423432',balance=10000000000)
#def bank(lllll)

#------
#class Bank(name ,.....)
#too delesh y tab edar eb name init
#initial---> az ebteda vaghty mikhay besazi chia ro bdi



#self, ejaze mide ke tabe ha be ham dg
#yekseri adad ro beresoonan


#amoutn
#share koni --> beyne tavabe , tabe ha


class Bank:
    
    #oon chzi hae k mikhay vaghty yeki object sakht
    #hatman bezane
    #yani benevise
    #a=Bank(vorodi1=... , vorodi2=...,...)
    
    def __init__(self,name,code_meli , password, initial_balance):
        pass
    
    

#khali bznio
obj1=Bank()
'''
TypeError: Bank.__init__() missing 4 
required positional arguments: 
    'name', 'code_meli', 'password', and
    'initial_balance'
'''


obj1=Bank('ali pm','1020939287238','1234',20000)

obj1.name 
#AttributeError: 'Bank' object has no attribute 'name'


#def __init__(self,name,....)
#name y zarfe movagaht k esmo vaghty frd shey misaze
#Begire hamin


#----> self 
#---> self. --> ghafase behesh ezafe 



class Bank:
    
    #oon chzi hae k mikhay vaghty yeki object sakht
    #hatman bezane
    #yani benevise
    #a=Bank(vorodi1=... , vorodi2=...,...)
    
    def __init__(self,name,code_meli , password, initial_balance):
        
        self.name  = name
        self.code_meli = code_meli
        self.password = password
        self.initial_balance= initial_balance
    
    
obj1=Bank('ali pm','1020939287238','1234',20000)


obj1.name #'ali pm'
obj1.code_meli #'1020939287238'
obj1.password #'1234'





class Bank:
    
    #oon chzi hae k mikhay vaghty yeki object sakht
    #hatman bezane
    #yani benevise
    #a=Bank(vorodi1=... , vorodi2=...,...)
    
    def __init__(self,nam,code_meli , ramze_oboor, mojodi_avalie):
        self.name  = nam
        self.code= code_meli
        self.password= ramze_oboor
        self.initial_balance= mojodi_avalie




obj1=Bank('apm','328773928','1234',10000)

obj1.nam #AttributeError: 'Bank' object has no attribute 'nam'

obj1.code_meli #AttributeError: 'Bank' object has no attribute 'code_meli'
obj1.ramze_oboor


obj1.name #'apm'
obj1.password


#=======================


class Bank:
    
    def __init__(self,name,meli_code,password,initial_balance):
        
        self.name=name
        
        self.meli_code=meli_code
        self.password=password
        self.initial_balance=initial_balance
        
        
        
#obj1=Bank('','','',13223)
#obj2=Bank('','','',13223)
#obj3=Bank('','','',13223)
#obj4=Bank('','','',13223)
        
#obj1.name
#obj2.name
#obj3.name
#obj4.name

#properties ro mikesham biron





class Bank:
    
    def __init__(self,name,meli_code,password,initial_balance):
        
        self.name=name
        
        self.meli_code=meli_code
        self.password=password
        self.initial_balance=initial_balance
        
        
        
    def welcome(self):
        print('سلام مشتری عزیز خوش آمدید')
        


obj1=Bank('apm','328773928','1234',10000)
        
#property 
obj1.name
        
        
#functions
obj1.welcome() #function
#سلام مشتری عزیز خوش آمدید

class Bank:
    
    def __init__(self,name,meli_code,password,initial_balance):
        
        self.name=name
        
        self.meli_code=meli_code
        self.password=password
        self.initial_balance=initial_balance
        
        
        
    def welcome(self):
        print('salam moshtarie aziz khosh amadid')
        
obj1=Bank('ali','328773928','1234',10000)
obj2=Bank('vahid','323292810987021','44334',20000)


obj1.name #'ali'
obj2.name #'vahid'

obj1.welcome()
#salam moshtarie aziz khosh amadid

obj2.welcome()
#salam moshtarie aziz khosh amadid

class Bank:
    
    def __init__(self,name,meli_code,password,initial_balance):
        
        self.name=name
        
        self.meli_code=meli_code
        self.password=password
        self.initial_balance=initial_balance
        
        
        
    def welcome(self):
        
        text='salam ' + self.name + 'e aziz khosh amadid'
        #undefined name?????
        print(text)
        
        
        
obj1=Bank('ali','328773928','1234',10000)
obj2=Bank('vahid','323292810987021','44334',20000)


obj1.name #'ali'
obj2.name #'vahid'

obj1.welcome()
#salam alie aziz khosh amadid


obj2.welcome()
#salam vahide aziz khosh amadid
        
        
'''


show_balance---> balance esho trf bebine


deposition --> variz


atm --> bardare  (withdraw)





'''  



class Bank:
    
    def __init__(self,name,meli_code,password,initial_balance):
        
        self.name=name 
        self.meli_code=meli_code
        self.password=password
        #******
        self.balance=initial_balance
        #mojodiii
        #self.balance

    def welcome(self):   
        print(f'salam {self.name} e aziz khosh amadid')


    def show_balance(self):
        print(f'mojodie shoam hast : {self.balance}')
     

obj1=Bank('ali','328773928','1234',10000)
obj2=Bank('vahid','323292810987021','44334',20000)


obj1.name
obj1.initial_balance #AttributeError: 'Bank' object has no attribute 'initial_balance'

obj1.balance # 10000


obj1.welcome() #salam ali e aziz khosh amadid

obj1.show_balance()
#mojodie shoam hast : 10000

 
#---------------------------

#baraye sakhtane tabeye deposit -->

#obj1=.....
#obj1.deposit(meghdar 4-00)

#tabe ee k dar dele class-->
#def deposition(amount)







class Bank:
    
    def __init__(self,name,meli_code,password,initial_balance):
        
        self.name=name 
        self.meli_code=meli_code
        self.password=password
        #******
        self.balance=initial_balance
        #mojodiii
        #self.balance

    def welcome(self):   
        print(f'salam {self.name} e aziz khosh amadid')


    def show_balance(self):
        print(f'mojodie shoam hast : {self.balance} toman')
     
        
     
    def deposition(self,amount):
        
        #amount --> + baalnce
        
        self.balance= self.balance + amount
        
        print(f'Moshtarie aziz variz b mablaghe {amount} ba moafaghiat anjam shod')
        
        print(f'Mojodie shoma: {self.balance}')
    
    
obj1=Bank('ali','328773928','1234',10000)
obj2=Bank('vahid','323292810987021','44334',20000)



obj1.show_balance()
#mojodie shoam hast : 10000 toman

obj1.balance #10000

obj1.deposition(5000)
'''
Moshtarie aziz variz b mablaghe 5000 ba moafaghiat anjam shod
Mojodie shoma: 15000
'''


obj2.name #'vahid'
obj2.show_balance()  # 'vahid'

obj2.deposition(100000)

'''
Moshtarie aziz variz b mablaghe 100000 ba moafaghiat anjam shod
Mojodie shoma: 120000

'''





#-------



#obj1=.....

#obj1.show_balance() --_>< balance 


#obj1.ATM(amount)



class Bank:
    
    def __init__(self,name,meli_code,password,initial_balance):
        
        self.name=name 
        self.meli_code=meli_code
        self.password=password
        #******
        self.balance=initial_balance
        #mojodiii
        #self.balance

    def welcome(self):   
        print(f'salam {self.name} e aziz khosh amadid')


    def show_balance(self):
        print(f'mojodie shoam hast : {self.balance} toman')
     
        
     
    def deposition(self,amount):
        
        #amount --> + baalnce
        
        self.balance= self.balance + amount
        
        print(f'Moshtarie aziz variz b mablaghe {amount} ba moafaghiat anjam shod')
        
        print(f'Mojodie shoma: {self.balance}')
    
    
    
    def ATM(self,amount):
        
        self.balance= self.balance - amount
        
        print(f'moshtarie aziz , bardahst b mablaghe {amount} ba moafaghiat anjham shod')
        
        print(f'Mojodie shoma : {self.balance}')





obj1=Bank('ali pilehvar','322321',1234,1000)
        
#----properties------
obj1.name #'ali pilehvar'
obj1.meli_code #'322321'


#----methods-----
obj1.welcome()
#salam ali pilehvar e aziz khosh amadid


obj1.show_balance()
#mojodie shoam hast : 1000 toman


obj1.deposition(19000)

'''
Moshtarie aziz variz b mablaghe 19000 ba moafaghiat anjam shod
Mojodie shoma: 20000

'''


obj1.show_balance()
#mojodie shoam hast : 20000 toman



obj1.ATM(15000)
'''
moshtarie aziz , bardahst b mablaghe 15000 ba moafaghiat anjham shod
Mojodie shoma : 5000
'''

obj1.show_balance()
#mojodie shoam hast : 5000 toman


obj1.ATM(10000)
'''
moshtarie aziz , bardahst b mablaghe 10000 ba moafaghiat anjham shod
Mojodie shoma : -5000

'''
#mojodii kafi nis??

obj1.show_balance()

#mojodie shoam hast : -5000 toman





class Bank:
    
    def __init__(self,name,meli_code,password,initial_balance):
        
        self.name=name 
        self.meli_code=meli_code
        self.password=password
        #******
        self.balance=initial_balance
        #mojodiii
        #self.balance

    def welcome(self):   
        print(f'salam {self.name} e aziz khosh amadid')


    def show_balance(self):
        print(f'mojodie shoam hast : {self.balance} toman')
     
        
     
    def deposition(self,amount):
        
        #amount --> + baalnce
        
        self.balance= self.balance + amount
        
        print(f'Moshtarie aziz variz b mablaghe {amount} ba moafaghiat anjam shod')
        
        print(f'Mojodie shoma: {self.balance}')
    
    
    
    def ATM(self,amount):
        
        if amount<=self.balance:
        
            self.balance= self.balance - amount
            
            print(f'moshtarie aziz , bardahst b mablaghe {amount} ba moafaghiat anjham shod')
            
            print(f'Mojodie shoma : {self.balance}')
            
        else:
            print('mojodie shoma kafi nist')


obj1=Bank('ali pilehvar','322321',1234,1000)
obj1.show_balance() #mojodie shoam hast : 1000 toman
obj1.ATM(2000) #mojodie shoma kafi nist
obj1.ATM(500)

'''
moshtarie aziz , bardahst b mablaghe 500 ba moafaghiat anjham shod
Mojodie shoma : 500

'''



#============




class Bank:
    
    def __init__(self,name,meli_code,password,initial_balance):
        
        self.name=name 
        self.meli_code=meli_code
        self.password=password
        #******
        self.balance=initial_balance
        #mojodiii
        #self.balance
        
        self.base=10000

    def welcome(self):   
        print(f'salam {self.name} e aziz khosh amadid')


    def show_balance(self):
        if self.balance>500:
            self.balance= self.balance - 500
            print(f'mojodie shoam hast : {self.balance} toman')
        else:
            print('shoma mojodie moshahede mojodi nadare')
            
        
     
    def deposition(self,amount):
        
        #amount --> + baalnce
        
        
        darsad=(1/100) * amount  
        
        if self.balance + amount > darsad:
        
            self.balance= self.balance + amount  - darsad
            
            print(f'Moshtarie aziz variz b mablaghe {amount} ba moafaghiat anjam shod')
            
            print(f'Mojodie shoma: {self.balance}')
        else:
            print('mojodi nadari k variz koni')
    
    
    
    def ATM(self,amount):
        
        darsad=(1/100) * amount
        
        if amount + darsad<=self.balance:
            
            if self.balance - amount - darsad >= self.base:
        
                self.balance= self.balance - amount - darsad
                
                print(f'moshtarie aziz , bardahst b mablaghe {amount} ba moafaghiat anjham shod')
                
                print(f'Mojodie shoma : {self.balance}')
            else:
                print('shom a bayad hatman 10000 dar hesabetan bemanad')
            
        else:
            print('mojodie shoma kafi nist')




#============================
#password mikhan





class Bank:
    
    def __init__(self,name,meli_code,password,initial_balance):
        
        self.name=name 
        self.meli_code=meli_code
        self.password=password
        #******
        self.balance=initial_balance
        #mojodiii
        #self.balance
        
        self.base=10000

    def welcome(self):   
        print(f'salam {self.name} e aziz khosh amadid')


    def show_balance(self):
        
        input_password=input('passwordeton ro bezanid:')
        
        if input_password==self.password:
        
        
            if self.balance>500:
                self.balance= self.balance - 500
                print(f'mojodie shoam hast : {self.balance} toman')
            else:
                print('shoma mojodie moshahede mojodi nadare')
                
        else:
            print('passworde shoma doros nist')
        
     
    def deposition(self,amount):
        
        #amount --> + baalnce
        
        
        darsad=(1/100) * amount  
        
        if self.balance + amount > darsad:
        
            self.balance= self.balance + amount  - darsad
            
            print(f'Moshtarie aziz variz b mablaghe {amount} ba moafaghiat anjam shod')
            
            print(f'Mojodie shoma: {self.balance}')
        else:
            print('mojodi nadari k variz koni')
    
    
    
    def ATM(self,amount):
        
        darsad=(1/100) * amount
        
        if amount + darsad<=self.balance:
            
            if self.balance - amount - darsad >= self.base:
        
                self.balance= self.balance - amount - darsad
                
                print(f'moshtarie aziz , bardahst b mablaghe {amount} ba moafaghiat anjham shod')
                
                print(f'Mojodie shoma : {self.balance}')
            else:
                print('shom a bayad hatman 10000 dar hesabetan bemanad')
            
        else:
            print('mojodie shoma kafi nist')




obj1=Bank('ali pilehvar','322321','1234',1000)
            
    
obj1.show_balance()
#passwordeton ro bezanid:238273
#passworde shoma doros nist


obj1.show_balance()
#mojodie shoam hast : 500 toman



#================================
#=================================

class Bank:
    
    def __init__(self,name,meli_code,password,initial_balance):
        
        self.name=name 
        self.meli_code=meli_code
        self.password=password
        #******
        self.balance=initial_balance
        #mojodiii
        #self.balance
        
        self.base=10000

    def welcome(self):   
        print(f'salam {self.name} e aziz khosh amadid')


    def show_balance(self):
        
        result=self.get_password()
        if result:
        
            if self.balance>500:
                self.balance= self.balance - 500
                print(f'mojodie shoam hast : {self.balance} toman')
            else:
                print('shoma mojodie moshahede mojodi nadare')
        
    
     
    def deposition(self,amount):
        
        #amount --> + baalnce
        result=self.get_password()
        if result:
            darsad=(1/100) * amount  
            
            if self.balance + amount > darsad:
            
                self.balance= self.balance + amount  - darsad
                
                print(f'Moshtarie aziz variz b mablaghe {amount} ba moafaghiat anjam shod')
                
                print(f'Mojodie shoma: {self.balance}')
            else:
                print('mojodi nadari k variz koni')
    
    
    
    def ATM(self,amount):
        result=self.get_password()
        if result:
        
            darsad=(1/100) * amount
            
            if amount + darsad<=self.balance:
                
                if self.balance - amount - darsad >= self.base:
            
                    self.balance= self.balance - amount - darsad
                    
                    print(f'moshtarie aziz , bardahst b mablaghe {amount} ba moafaghiat anjham shod')
                    
                    print(f'Mojodie shoma : {self.balance}')
                else:
                    print('shom a bayad hatman 10000 dar hesabetan bemanad')
                
            else:
                print('mojodie shoma kafi nist')


    #hucihi migire
    #True
    #false
    
    def get_password(self):
        input_password=input('passwordet ro bezan:')
        
        if input_password==self.password:
            return True
        
        else:
            print('Ramze obore shoam doros nemibashad')
            return False




obj1=Bank('ali pilehvar','0222222222','1234',10000)


#------proeprties------
obj1.name #'ali pilehvar'
obj1.meli_code


obj1.welcome()
#salam ali pilehvar e aziz khosh amadid

obj1.show_balance()
#mojodie shoam hast : 9500 toman

obj2=Bank('vahid mosavi','32892373287','4444',20000)

obj2.meli_code #'32892373287'

obj2.welcome() #salam vahid mosavi e aziz khosh amadid

obj2.show_balance()
'''
passwordet ro bezan:1234
Ramze obore shoam doros nemibashad

'''

obj2.show_balance()
'''
passwordet ro bezan:4444
mojodie shoam hast : 19500 toman

'''


obj2.deposition(20000)

'''
Moshtarie aziz variz b mablaghe 20000 ba moafaghiat anjam shod
Mojodie shoma: 39300.0

'''


#39000 --> 29000

obj2.deposition(30000)

'''
Moshtarie aziz variz b mablaghe 30000 ba moafaghiat anjam shod
Mojodie shoma: 69000.0

'''

#59000
#na 60000

obj2.ATM(60000)

'''
passwordet ro bezan:4444
shom a bayad hatman 10000 dar hesabetan bemanad

'''


'''

> 3 bar ramz zade shod -> block

admin_panle --> unblock

hsitory_transection --> =[]

+ --> .append
- --> .append

transection --> gardesh 

motefavet besazid


#-----advanced------

class dolari roosh bsazid

ghesmate dollari dare

class Currency_Bank:
    def __init___(self,name, code_meli, password, ....)
    super().--->
    versata
    
    
currency_bank() dolaari <----> rialii


'''



        