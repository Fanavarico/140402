"""
Created on Sun Aug 31 20:05:07 2025

@author: apm



L8 : Hale tamrin


"""

#@-----------
#=======================
#------JALASE6---------
#=======================

#------1
D1 = {'a': 1, 'b': 3, 'c': 2}
D2 = {'a': 2, 'b': 3, 'c': 1}

#d1['a']
#d2['a']

#
D1.keys() # dict_keys(['a', 'b', 'c'])
D1.values() #dict_values([1, 3, 2])
D1.items() #dict_items([('a', 1), ('b', 3), ('c', 2)])

shared_keys= D1.keys() & D2.keys()


#shared_dict={key: D1[key] for key in shared_keys}

for key in shared_keys:
    print(key)

myvalue=[]
mykey=[]

final_dict={}


for key in shared_keys:
    if D1[key]==D2[key]:
        #myvalue.append(D1[key])
        #mykey.append(key)
        final_dict[key]=D1[key]







#2--------
sales = {
'Ali': {'Jan': 1200, 'Feb': 1300, 'Mar': 1000},
'Sara': {'Jan': 1500, 'Feb': 1600, 'Mar': 1700},
'Reza': {'Jan': 1100, 'Feb': 900, 'Mar': 950}
}

max_total=0
max_person=''

for saleperson , monthly_sales in sales.items():
    #print(saleperson)
    #print(monthly_sales)
    total=sum(monthly_sales.values())
    #$print(f'baraye {saleperson} totla has {total} ')
    if total>max_total:
        max_total=total
        max_person=saleperson
        
        
        
        
print(max_total) #4800
print(max_person) #Sara
    
        

#---3---
products = [
    ('laptop', 1200, 5),
    ('mouse', 20, 150),
    ('keyboard', 100, 70),
    ('monitor', 300, 20),
    ('printer', 200, 0)
]



for product in products:
    name, price, quantity = product
    if price > 1000 or quantity == 0:
        print(name)
        #mylist.append()
#laptop
#printer


#4---------
data = [
('Ali', 18),
('Sara', 19),
('Reza', 18),
('Niloofar', 20),
('Ali', 19)
]


#dict[key]: value

#kild-->key --> nomre
#meghdar --> values--> listi az danesh amoza

stores_dict={}

for d in data:
    print(type(d))
    print(d)


for student,score in data:
    print(student,score)


'''
Ali 18
Sara 19
Reza 18
Niloofar 20
Ali 19

'''
'''

dictsa={ 18 : []}

stores_dict={}

'''


data = [
('Ali', 18),
('Sara', 19),
('Reza', 18),
('Niloofar', 20),
('Ali', 19)
]

stores_dict={}

for student,score in data:
    if score not in stores_dict:
        stores_dict[score]=[]
    
    stores_dict[score].append(student)
    
        
    
print(stores_dict)

'''
{18: ['Ali', 'Reza'], 19: ['Sara', 'Ali'], 20: ['Niloofar']}

'''


#=======================
#------JALASE7---------
#=======================

#1-----------



def remove_even_indexed_chars(s):
    """
    Removes characters at even indices from a string.
    """
    kar=s[1::2]
    return kar

name='python'

edited_name=remove_even_indexed_chars(name)


print(edited_name)
#yhn

def remove_even_indexed_chars(s: str) -> str:
    """
    Removes characters at even indices from a string.
    """
    return s[1::2]




#2----
def remove_substring_by_range(s: str, start: int, end: int) -> str:
    """
    Removes a substring from a string within a specified range.
    """
    return s[:start] + s[end+1:]

# Example:
input_string = "python"
start = 1
end = 3
print(f"Original string: {input_string}")
print(f"Range to remove: {start} to {end}")
print(f"Result: {remove_substring_by_range(input_string, start, end)}")




#------

#ta abd anjam shavar taaaa.....
mylist=[]
while True:
    
    
    
    user_input=input('yechizi bede ezaf konm b listam')
    
    mylist.append(user_input)
    
    
#ta aabd trf hey inpiut hey append

mylist=[]

while True:
    
    
    
    user_input=input('yechizi bede ezaf konm b listam')
    
    if user_input.lower().strip()=='exit':
        break
    
    mylist.append(user_input)
    
    


mylist=[]
while True:

    
    user_input=input('yechizi bede ezaf konm b listam')
    
    if user_input.lower().strip()=='exit':
        break
    
    mylist.append(user_input)
    


max_len=0
winner=0

for element in mylist:
    len_element=len(element)
    
    if len_element>max_len:
        winner=element
        max_len=len_element
        
        
    
        


def append_search_find_max_len():
    mylist=[]
    
    while True:
        
        
        
        user_input=input('yechizi bede ezaf konm b listam:')
        
        if user_input.lower().strip()=='exit':
            break
        
        mylist.append(user_input)
        
        

    max_len=0
    winner=''

    for element in mylist:
        len_element=len(element)
        
        if len_element>max_len:
            winner=element
            max_len=len_element
        
    
    print(f'balatarin tool ro {winner} ba toole {max_len}')
    return winner

    

append_search_find_max_len()


'''
def list_str():
    x=[]
    y=''
    for i in range(4):
        m=input('enter value : ')
        x.append(m)
        y=input('enter value1 : ')
        count=0
        second=-1
        for i in range(len(x)):
            if y==x[i] :
                count+=1
                if count==2 :
                    second=i
                    break
                print(second)
                
                
                
list_str()
'''


#---5
a='23'




def convert_to_int(s):
    
    if s.isdigit():
        n=int(s)
        return n
        
    else:
        print(f'in yek name {s}')
        return s
    
    
convert_to_int('ali') #in yek name ali

convert_to_int('23')  # 23




    
def convert_to_int(s):
    
    try:
        integer=int(s)
        return integer
    except ValueError:
        print('in yek string hast na adad')




#----6------


def global_calculator():
    
    
    while True:
        value1=input('adade avaleto bede:')
        
        if value1=='exit':
            break
        
        value2=input('adade dovom bede:')
        amalgar=input('amalgareto bede:')
        
        
        
        if value1.isdigit() and value2.isdigit():
            value1=float(value1)
            value2=float(value2)
            
            if amalgar=='jam':
                result=jam(value1,value2)
                print(f'resulte shoma: {result}')
            
            elif amalgar=='tafrigh':
                result=tafrigh(value1,value2)
                print(f'resulte shoma: {result}')
                
            elif amalgar=='tavan':
                result=tavan(value1,value2)
                print(f'resulte shoma: {result}')
                
            elif amalgar=='taghsim':
                if value2==0:
                    print('bi nayahat')
                
                else:
                    result=taghsim(value1,value2)
                    print(f'resulte shoma: {result}')
  
            #lif..........
            
            else:
                #amlagar jam , tafrigh ,...
                print('amalgare mojaz ra entekhab nakardid , amalgarhaye mojood= [jam , tafrigh, taghsim ,.....')
            
  
        else:
            print('value1 vba value2 bayad adad bashad')





def jam(value1,value2):
    result=value1+value2
    return result

def tafrigh(value1,value2):
    result=value1-value2
    return result

def taghsim(value1,value2):
    result=value1/value2
    return result

def zarb(value1,value2):
    result=value1*value2
    return result

def tavan(value1,value2):
    result=value1**value2
    return result


#---soale kahar
std = [
    {'id': '5', 'm': '17', 'f': '19'},
    {'id': '14', 'm': '20', 'f': '17'}
]


for student in std:
    mianterm=student['m']
    final=student['f']
    
    average_score=(mianterm+final)/2
    #average_score=(mianterm + 2*final)/3
    #mianterm + final/2
    
    student['avg']=average_score
    
    
    
    
def calculation_of_average(std):
    for student in std:
        mianterm=float(student['m'])
        final=float(student['f'])
        
        average_score=(mianterm+final)/2
        #average_score=(mianterm + 2*final)/3
        #mianterm + final/2
        
        student['avg']=average_score
        
    return std
    
std = [
    {'id': '5', 'm': '17', 'f': '19'},
    {'id': '14', 'm': '20', 'f': '17'}
]

calculation_of_average(std)

'''
Out[43]: 
[{'id': '5', 'm': '17', 'f': '19', 'avg': 18.0},
 {'id': '14', 'm': '20', 'f': '17', 'avg': 18.5}]
'''

#----
def calculation_of_average(std):
    
    new_std_list=[]
    
    for student in std:
        new_student_dict={}
        
        mianterm=float(student['m'])
        final=float(student['f'])
        
        average_score=(mianterm+final)/2
        #average_score=(mianterm + 2*final)/3
        #mianterm + final/2
        
        #student['avg']=average_score
        new_student_dict['id']=student['id']
        new_student_dict['avg']=average_score
        
        
        new_std_list.append(new_student_dict)
        
          
    return new_std_list
    


    
std = [
    {'id': '5', 'm': '17', 'f': '19'},
    {'id': '14', 'm': '20', 'f': '17'}
]

calculation_of_average(std)

'''
Out[45]: [{'id': '5', 'avg': 18.0}, {'id': '14', 'avg': 18.5}]

'''








'''
parantez
tavan
zarg taghsim
jam tafrigh
'''



#=======================
#------JALASE8---------
#=======================

#1----


def div(value1,value2):
    
    result=value1/value2
    return result


div(10,5)


div('ali','mohsen')

'''
TypeError: unsupported operand type(s) for /: 'str' and 'str'
'''



div(10,0)

#ZeroDivisionError: division by zero




def div(value1,value2):
    try:
    
        result=value1/value2
        return result
    
    #nhar erori
    except Exception as e:
        print(f'error in division: {e}')




def div(value1,value2):
    try:
    
        result=value1/value2
        return result
    
    except ValueError:
        print('invalid input')
        #bejaye adad , horofi 
        
    except ZeroDivisionError:
        print('0 gozashet tooye makhraj')






#---2

file_content=['yes','no','no','yes','yes']

with open('mytext.txt','w') as file:
    for item in file_content:
        #file.write(item) #yesnoyesnononoyesyes
        file.write(item + '\n')
        #ye
        #no
        #ye
        #no
        
        
        
def count_yes_no(file_name):
    
    counts={'yes':0 , 'no':0}
    
    try:
        with open(file_name,'r') as file:
            for line in file:
                word=line.strip()
                if word in counts:
                    counts[word] +=1
                    
    except FileNotFoundError:
        print(f'Error: the file {file_name} was not found')
        return None
                    
    return counts



#====================
'''
jam bandi


Function --> bOX


voroodi --> BOX --> khoroji mdie [print]

vorodi --> input , vborodie tabe


def name (vorodi1,vorodi2)




***
agar o ama --> sharti besanji
if


agh dorahi --> if else

ag chandrahi --> [ jam , tavan , zarb , tafrigh] if elif elif elif else


***
mikhasi beri toye yek list , dictioanry ya harchi

for item in ....

list[ tuple , tuple, tuple]

for item in list:
    for ... in tuple
    
    
list[(itm1,itm2)  , (itm1,itm2)]


for tuple in list:
    for item1,item2 in tuple:
        
        
        
MAX--> max==0
if hesaab>max:
    max=hesabb *update
    winner=esm
    
    

ta abad yekario konee-- >whiel
while true --> abad ye exit

if ...input=='exit':
    breake
    
    
    
    


with open('esme file',mode) as file:
    ....
    ...
    .
    .
    
    
    
mode='w' --> file.write()

mode='r' --> for . in file
---> file.read() file.readlines() file.readline()




try:
    
except:
    
    
    
code---> ejra mishe --> ag error bokhgroe , motafsfena barnam kolesho ghat

k kole codo berizi too ye badane try

except-->

except Exception as e:
    print(e)
    print('error : e')
    
    send_telegram(...(e))
    
    
    
except Valueerror:
    ......
    
exept ZeroDivision...:
    .....
    print(.....)
    
    

'''




'''
review



yesri kar ha ba function ha nmishe anjam dad


--> class


obejct orineted programming (OOP )--> shey gara--> asan ye raveshe zendgeie


class koili --> properties ( variabke) , methdo (function)

object besazi az har class


class bank --> hesab bsazi
bashgah --> heab 

app --> safe besazi



app --> profile



hesab --> hesab ebanki


tasks --> task

patements--> paymenet


'''


#=======================
#------JALASE9---------
#=======================
#harmoghe khasi clas -> chijori estefade mishe


#c=calculator()

#c.add(.. ,..)
#c.



#----1---
class ClassCalculator:
    def add(self, x, y):
        """Returns the sum of two numbers."""
        return x + y

    def subtract(self, x, y):
        """Returns the difference between two numbers."""
        return x - y

    def multiply(self, x, y):
        """Returns the product of two numbers."""
        return x * y

    def divide(self, x, y):
        """
        Returns the quotient of two numbers.
        Handles division by zero.
        """
        if y == 0:
            return "Error: Cannot divide by zero."
        return x / y
   
    
   
o1=ClassCalculator()
    
res=o1.add(10,20)
    
    
    
    
    
#----

#c1=ClassCalculator(value1,value2)


#c1.add()
#c1.divide()

#c1.change()

#c1.add()

class ClassCalculator:
    def __init__(self,value1,value2):
        self.value1=value1
        
        self.value2=value2
        
        
    def add(self):
        """Returns the sum of two numbers."""
        return self.value1 + self.value2

    def subtract(self):
        """Returns the difference between two numbers."""
        return self.value1 - self.value2

    def multiply(self):
        """Returns the product of two numbers."""
        return self.value1 * self.value2

    def divide(self):
        """
        Returns the quotient of two numbers.
        Handles division by zero.
        """
        if self.value2==0:
            return "Error: Cannot divide by zero."
        
        return self.value1/self.value2
    
    
    def change(self):
        
        x=self.value1
        y=self.value2
        
        self.value1=y
        self.value2=x
        
        print('it is changed')
   

o1=ClassCalculator(10,20)
o1.add()

o1.multiply()
    

o1.divide() #0.5


o1.change() #it is changed

o1.divide()
#Out[59]: 2.0



'''


OOP

Vzihegi , proeprty , attributes ---> oon variablkes haee k zkhire self. 


function . method ----> oon tab ehaee k tarif mikoniud




'''
#----2-----

#o1=library(id,.....,)
class Library:
    
    def __init__(self,name,address,num_sections,sections_name ,open_time,close_time):
        
        
        self.name=name
        self.address=address
        self.num_sections=num_sections
        self.sections_name=sections_name
        
        if len(sections_name)!=int(num_sections):
            raise Exception('your section numbers are not equal to section names which you provided')
            
        
        if open_time>close_time:
            raise Exception('Error : close time can not be less than open time')
        
        if open_time>24 or close_time>24:
            raise Exception('Tiem can not be mroe than 24')
            
        if open_time<0 or close_time<0:
            raise Exception('time can not be negative')
            
            
        self.open_time=open_time
        self.close_time=close_time
        
        
        

    def displaye_info(self):
        
        text=f'''
        
        =============================
        &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        
              be ketabkhaneye {self.name} khosh omadid
              
         ketabkhaneye ma {self.num_sections} section darad
         
         
         ma az saate {self.open_time} ta {self.close_time} dar khedmate shoma hastim
         
         
         
         ya hagh..


     #==========
     #&&&&&&&&&&&
     address = {self.address}        
        
        '''
        
        print(text)
        
        
    def is_open(self,time):
        
        if time>self.open_time and time<self.close_time:
            print('bale ma bazim')
            return True
        else:
            print('na ma baste em')
            return False




o1=Library('marefat','baghe fateh',3,['khanoma','aghayan','herasat'],7,18)


o1.displaye_info()

o1.is_open(6)
'''
na ma baste em
Out[69]: False

'''



o1.is_open(14)


o1.is_open(22)

'''

taghiri dar clas dadid
dobare bayad azash object besaziiiid
yeho funcitonoi seedda

'''


o1=Library('marefat','baghe fateh',3,['khanoma','aghayan','herasat'],22,18)
'''
Exception: Error : close time can not be less than open time

'''


k_list=[10,20,30,40,50,60,70,80,90]

new_list=[]
for k in k_list:
    new=k+10
    new_list.append(new)
    
    

ne_listtttttt=[ k+10 for k in k_list]



new_dict={ f'number_{k}':k for k in k_list}




new_dict={  f'id_{i}':k   for i,k in enumerate(k_list)}





#=======================
#------JALASE10---------
#=======================





#=======================
#------JALASE11---------
#=======================


