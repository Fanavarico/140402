
"""
Created on Sat Sep 13 20:06:23 2025

@author: apm
"""


#====================================
#======Jalase 9 =====================
#====================================




#------soale1---------
#def calculator(....)


#calculator(1,2,231)

#a=calculator()

#a.add(x,y)

class calculator:
    
    #def __init__(self,)
    
    def add(self,x,y):
        result=x+y
        print('your result is :', result)
        return result
    
    
a=calculator()
    
    
a.add(4,5)
'''
your result is : 9
Out[3]: 9
'''

b=a.add(4,5)

print(b)
    

pow(4,3) #Out[7]: 64



def my_pow(x,y):
    return x*y*7


'''

BOX



Vorodi ---> BOX ---> khoroji



esm(vorodi1,vodori2,vorodi3)




def esm(vorodi1,vodori2,vorodi3)):
    
    voprodi1 * + - 
    if for else
    
    return result



khoroji =esm(10,20,30)


'''







    
class calculator:
    
    #def __init__(self,)
    
    def add(self,x,y):
        result=x+y
        print('your result is :', result)
        return result
    
    def subtract(self,x,y):
        result=x-y
        print('your result is :', result)
        return result
    
    def multiply(self,x,y):
        result=x*y
        print('your result is:',result)
        return result
    
    
    def divide(self,x,y):
        if y==0:
            print('your second numebr can not be 0')
            return None
        
            #return 'Infinit'
            
        result=x/y
        print('your result is:',result)
        return result
    


#a=Library(',marefat','karaj ...',4,['mardone,zanone,...])


class Library:
    
    def __init__(self,name,address,num_sections,section_names):
        
        self.name=name
        self.address=address
        self.num_sections=num_sections
        self.section_names=section_names
        
        
a=Library('marefat','karaj bagh fateh',4,['mrd','zan','masool','modirat'])
        
#object sakhtama z class


#a.displaye_info()


class Library:
    
    def __init__(self,name,address,num_sections,section_names,open_time,close_time):
        
        self.name=name
        self.address=address
        self.num_sections=num_sections
        self.section_names=section_names
        self.open_time=open_time
        self.close_time=close_time
        
    def display_info(self):
        
        text=f"""
        
        
        #======Be name khoda=====
        ketabkhaneye {self.name}
        
        saate kari : {self.open_time} ta {self.close_time}
        
        khoshal mishavim tashrif biavarid
        
        ma {self.num_sections} bakhsh darim besoorate:
            {self.section_names}
            
            
        ba sepas
        modiriate {self.name}
        
        address : {self.address}

        """
        
        print(text)
        
        
        
a=Library('marefat','karaj bagh fateh',4,['mrd','zan','masool','modirat'],8,18)
 
a.display_info()
'''
        #======Be name khoda=====
        ketabkhaneye marefat
        
        saate kari : 8 ta 18
        
        khoshal mishavim tashrif biavarid
        
        ma 4 bakhsh darim besoorate:
            ['mrd', 'zan', 'masool', 'modirat']
        
        
        ba sepas
        modiriate marefat
        
        address : karaj bagh fateh
        
        
'''



#a.is_open(18) --> True , False


class Library:
    
    def __init__(self,name,address,num_sections,section_names,open_time,close_time):
        
        self.name=name
        self.address=address
        self.num_sections=num_sections
        self.section_names=section_names
        self.open_time=open_time
        self.close_time=close_time
        
    def display_info(self):
        
        text=f"""
        
        
        #======Be name khoda=====
        ketabkhaneye {self.name}
        
        saate kari : {self.open_time} ta {self.close_time}
        
        khoshal mishavim tashrif biavarid
        
        ma {self.num_sections} bakhsh darim besoorate:
            {self.section_names}
            
            
        ba sepas
        modiriate {self.name}
        
        address : {self.address}

        """
        
        print(text)
        
        
    def is_open(self,time):
        
        if self.open_time<time and time < self.close_time:
            
            print('bale baz hast')
            return True
        
        else:
            print('kheyr ma baste hastim')
            return False
    
    
a=Library('marefat','karaj bagh fateh',4,['mrd','zan','masool','modirat'],8,18)

a.is_open(10)
'''
bale baz hast
Out[16]: True
'''

a.is_open(16)
'''
bale baz hast
Out[17]: True
'''

a.is_open(6)
'''
kheyr ma baste hastim
Out[18]: False
'''


a.is_open(22)

'''
kheyr ma baste hastim
Out[19]: False
'''
#====================================
#======Jalase 10 =====================
#====================================

#task(1,esm,status)

class Task:
    
    def __init__(self,task_id,title,status='undone'):
        self.task_id=task_id
        self.title=title
        self.status=status
        
        
    
        

a=Task(1,'noon kharidan')

a.task_id #1
a.title #'noon kharidan'
a.status #'undone''undone'





#tick bznm
#ion doen shod
#oon done nshod
#oon felan on 
#a.mark_as_done()

class Task:
    
    def __init__(self,task_id,title,status='undone'):
        self.task_id=task_id
        self.title=title
        self.status=status
        
        
        
    def mark_as_done(self):
        self.status='done'
        print(f'task named {self.title} has updated to Done status')
        

    def mark_as_undone(self):
        self.status='undone'
        print(f'Task named {self.title} has updated to Undone Status')
        

a=Task(1,'noon kharidan')

a.status #Out[27]: 'undone'


a.mark_as_done()
#task named noon kharidan has updated to Done status

a.status #Out[29]: 'done'

a.mark_as_undone()


#modirate
#koli taskj has

#a=todolist()

#a.addd_task(nopon kharidan)


class Todolist:
    def __init__(self):
        self.tasks={}
        self.id=1
        
    
    def add_task(self,title):
        
        new_task=Task(self.id,title)
        
        
        self.tasks[self.id] = new_task
        
        '''
        
        tasks={ 1  : Task  ,  2 : task  , 3 : task}
        '''
        self.id = self.id + 1
        
        print(f'new task with title {title} is added to task manager app')
        
        
    
    def delete_task(self,task_id):
        if task_id in self.tasks : 
            deleted_task = self.tasks.pop(task_id)
            
            print(f'the task with id {task_id} is deleted')
        
        
        
    def displaye_tasks(self):
        
        if not self.tasks:
            print('your tasks are empty')
            return
        
        print('=========================')
        print('TASK LIST \n')
        for task_id , task in self.tasks.items():
            print(f'ID : {task.task_id} | Title : {task.title} | status : {task.status}')
            
            print('-------------------')
        print('=========================')
        
        
    def update_tasks(self,task_id,new_status):
        if task_id in self.tasks:
            if new_status=='done':
                self.tasks[task_id].mark_as_done()
                
                
            elif new_status=='undone':
                self.tasks[task_id].mark_as_undone()
                
                
            else:
                print('you must chsoe status from tehse two option (done or undone)')
                
            
        else:
            print(f'the task with this id {task_id} not found')
            return None
        
    
    
a=Todolist()

a.tasks #{}
a.id #1


a.add_task('noon kharidan')
#new task with title noon kharidan is added to task manager app

a.tasks
# {1: <__main__.Task at 0x16fa7bbe0>}

b=a.tasks

a.add_task('namaz')
a.add_task('barname nevisi')


b=a.tasks
a.tasks[1].title #'noon kharidan'
        
    
    
a.delete_task(3)
    
a.displaye_tasks()
    
'''
=========================
TASK LIST 

ID : 1 | Title : noon kharidan | status : undone
-------------------
ID : 2 | Title : namaz | status : undone
-------------------
=========================
'''

a.update_tasks(2, 'done')

a.displaye_tasks()

'''
=========================
TASK LIST 

ID : 1 | Title : noon kharidan | status : undone
-------------------
ID : 2 | Title : namaz | status : done
-------------------
=========================

'''



class Todolist:
    def __init__(self):
        self.tasks={}
        self.id=1
        
    
    def add_task(self,title):
        
        new_task=Task(self.id,title)
        
        
        self.tasks[self.id] = new_task
        
        '''
        
        tasks={ 1  : Task  ,  2 : task  , 3 : task}
        '''
        self.id = self.id + 1
        
        print(f'new task with title {title} is added to task manager app')
        
        
    
    def delete_task(self,task_id):
        if task_id in self.tasks : 
            deleted_task = self.tasks.pop(task_id)
            
            print(f'the task with id {task_id} is deleted')
        
    #a.edit)task()
    def edit_task(self,task_id,new_title=None,new_status=None):
        
        if task_id in self.tasks:
            
            task=self.tasks[task_id]
            
            if new_title:
                
                task.title=new_title
            if new_status:
                if new_status=='done':
                    task.mark_as_done()
                    
                elif new_status=='undone':
                    task.mark_as_undone()
                else:
                    print('fght dota akr mitoni (done , undone')
                    
                    
            print('all edit successfuly ')
            
            
            
        else:
            print('nist')
        
        
        
 
    def displaye_tasks(self):
        
        if not self.tasks:
            print('your tasks are empty')
            return
        
        print('=========================')
        print('TASK LIST \n')
        for task_id , task in self.tasks.items():
            print(f'ID : {task.task_id} | Title : {task.title} | status : {task.status}')
            
            print('-------------------')
        print('=========================')
        
        
    def update_tasks(self,task_id,new_status):
        if task_id in self.tasks:
            if new_status=='done':
                self.tasks[task_id].mark_as_done()
                
                
            elif new_status=='undone':
                self.tasks[task_id].mark_as_undone()
                
                
            else:
                print('you must chsoe status from tehse two option (done or undone)')
                
            
        else:
            print(f'the task with this id {task_id} not found')
            return None
        
        
    def search_by_name(self,query):
        for task in self.tasks.values():
            if query.lower() in task.title.lowe():
                
                print(f'i find it Task ID : {task.task_id} | title : {task.title} | status : {task.status}')
                return task
            
            
    def search_by_id(self,task_id):
        
        if task_id in self.tasks:
            founded=self.tasks[task_id]
            
            
            print(f' i found ID : {founded.task_id} .....')
            
            return self.tasks[task_id]
            
        else:
            print('nikst')
        
    
    
    def filter_tasks(self,status):
        
        if status not in ['done','undone']:
            print('bayad ya done begi ya undone')
            
            
        wanted_tasks=[]
        
            
        for task in self.tasks.values():
            if task.status==status:
                wanted_tasks.append(task)
                
        
        for task in wanted_tasks:
            print('ID : {task.task_id} | title : {task.title} | status : {task.status}')



            
#======================
       


#def Book:
#    def __init__(self,)

    #self.books={}
#moshakhasaatt
#
'''
. id_b شناسه کتاب
b
. title عنوان کتاب
c
. author نویسنده
d
. copies تعداد نسخه موجود
'''


'''
LibraryManager
'''

#add_book

#def add_bok(self,title):
    #self.books[self.id]=title



#--->tamrine khobie


#====================================
#======Jalase 11 =====================
#====================================


class List:
    
    def append(self,item):
        #item mriize to list
        pass
    
    
    #def extend:
        
        
    #def isnert



a=[10,20,30]


a=list([10,20,30])
    
a.append(40) #yedone ro b tah ezafe mikone
a.extend([100,200]) #yek liste jadid b tah ezafe mikone

a.isnsert(2,2000) #indexe felan, felan chizo ezad kon


#mylist --> list
#hame tabe haee k list hnamashono dare

#appendesh frghesh a khdo append
#aval chjeck mikone bayad fght str ezafe koni



class mylist(list):
    
    def append(self,item):
        if isinstance(item, str):
            super().append(item)        
        else:
            print('your item must be string')
            
    def insert(self,index,item):
        if isinstance(item, str):
            super().insert(index,item)
            
        else:
            print('your item must be string')
            
            
    def extend(self,iterable):
        if all(isinstance(item,str) for item in iterable):
            super().extend(iterable)
            
        else:
            print('bayad bashe')
            
            
    #----
    def extend(self,iterable):
        all_results=[]
        
        for item in iterable:
            res=isinstance(item, str)
            all_results.append(res)
            
            
        #all_results=[true,true,false,false]
        count=0
        for result in all_results:
            if result==True:
                count=count+1
            
        if count==len(iterable):
            super().extend(iterable)
            
        else:
            print('migam shoam bayad hameye listeton str bashand')
            
            

    
a=list([10,20,30])
a.append(40)

a.append('ali')
print(a)

#[10, 20, 30, 40, 'ali']



b=mylist([10,20,30])

print(type(b)) #<class '__main__.mylist'>

b.append('ali')

print(b)
#[10, 20, 30, 'ali']

b.append(40)
#your item must be string
print(b)
#[10, 20, 30, 'ali']



#======2========
#classe valed
class product:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category
        
        
    def discount(self,percentage):
        discount_amount=self.price * ( percentage/100)
        
        final_price=self.price - discount_amount
        
        
        #self.price= final_price
        return final_price

#a=product(...)
#a.discount -->


#---electronic product --> farzand

#brand

#init
#vorodi ha yeksan bashe init dgf tarif nmikonim

#ama ag vorodi jadid bkhaym


class elecdtronicproduct(product):
    def __init__(self,name,price,category,brand):
        super().__init__(name,price,category)
        self.brand=brand
        
        
#b=electroncidevcie()...

#b.discount()
 
    
class Book(product):
    def __init__(self,name,price,category,author,pages):
        super().__init__(name,price,category)
        self.author=author
        self.pages=pages
        
        
smartphone=elecdtronicproduct('iphpon13', 1000000, 'mobile','apple')


    







