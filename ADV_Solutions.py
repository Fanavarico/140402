
"""
In The Name of GOD


Created on Mon Oct 20 20:22:37 2025

@author: Ali Pilehvar Meibody


ADV_Solution





#------TOC -----------
---Review ??

---complete 


---DB , Log , .....

---GUI barash tarsim konim



"""

#=================
'''  REVIEW    '''
#=================



'''

Internet of Things --> IOT (intrnet ashya)

system control panel ---> connect b device , sensor ha --> control , manage mikone


Things ---> Device ( dastoor , turn on , turn off , lamp ,...) , Sensor (Read Data)

type --> Class --> object az oon class 




Device ---> class / sensor --> class
Control_panel --> Yek class kolie --> object --> har moshtarie ma mitone ye app dashte bashe


na backend -> code bzni bkhay ejra ?????
yani oon moshtarie code ? --> interface (Rabet) shekli
graphical user interface --> rabte karbarie graphici



focus --> backend (infrsuructure --> zirsakht)


Real Device , Real Sensor -->

def turn_on():
    status=on
    print()
    



** Vaghe ei anjam bde --> real project
api , yekchizi --> sherkate vaset --> vaslbseh b  oon device va oon device ro roshan kone



mock --> alaki dari 
devcie1  --> device1.turn_on() --> print() [+az computere-->ersal msihe b sherkat
                                            --> b device--> evice roshan mishe
                                            4 khat]

turn_on()








'''


class Device:
    
    #devcie haro baham mojaza koni
    def __init__(self,location,group,device_type,device_name):
        self.location=location
        self.group=group
        self.device_type=device_type
        self.device_name=device_name
        
        self.status='off'
        
        
    def turn_on(self):
        print('Done!!!')
        self.status='on'
        #-->inja mahali hast -_> oon coda neveshte --> b shekrate vaset vasl she az on bekhad
        #b devcie vasl she --> devcie ro turn on kone
        


    def turn_off(self):
        print('off')
        self.status='off'
        #-->inja mahali hast -_> oon coda neveshte --> b shekrate vaset vasl she az on bekhad
        #b devcie vasl she --> devcie ro turn off kone
        
        
    def get_status(self):
        '''
        On ya Off pas bde
        True , False
        
        
        '''
        if self.status=='on':
            return True
        else:
            return False
        



a1=Device('home','living_room','lamps','lamps1')
a1.turn_on()
a1.turn_off()
a1.get_status()

#a2=Device('home',)





import numpy as np
class Sensor:
    def __init__(self,location,group,sensor_type,sensor_name):
        self.location=location
        self.group=group
        self.sensor_name=sensor_name
        self.sensor_type=sensor_type
        #self.call=0
                
    #sensore  --> azash chizi mikahy?
    #data --> vasl b shekrate vasete -_> dta , ragahmo 
    #alan data in 
    def read_data(self):
       # if self.call==10:
       #     return 'error not connection'
        #self.call=self.call+1
        #return 25
        a=np.random.uniform(22,27)
        return a
    
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass



a1=Sensor('home', 'living_room', 'thermo', 'thermo108')
a1.read_data()




#----device
#----sensor

#-----Control panel-------

'''
--------System Design-------------
Aval , God -> ajzahaye ebtedaee (Atoms) --> misazi
va real device ,things (khane ha ,..) --> Class (init--> tamayoz ,
                                                 attributes --> moshakhasati
                                                 methods-->function --> karhaee mitone anjam )

fahmidi baray ehame inkar ro anjam dadi

Level advanced [ tamame inharo ta jaee k mitoni subclass ye class Mother anjam]
devcie , sesnor --> Class Thing 
class Thing --<> felan 

ajzaye zirsakht sakhte shod


----- Up Design -----
Moshtari chikar kone??

ye chi dashte bashe , khoansh
koli dokme bashe


------------------------------------------------
 Otagh1|   Otagh2 |  service  |  ashpazkhoone     
------------------------------------------------
 parkjing|   parking2 | paziraee  |  hal     
------------------------------------------------
    |        |       |        |       |        |
------------------------------------------------



-->
------
lamps , doors , felan ha ....



lamps --> lamps 1 , lamps2



#------------
user --> GUI --> Graphical User interface

GUI --> html , react, python , c# , ...., GO , DART  [APP]


Graphical User interface <---- API ---> BACKEND (INfrustructure)


API_-> Application programming interface




class control_panel --> groups={}


groups={} --> group besaze
jahaye khoansho bsaze
har kodom devcie ,s ensor haro bsoorate list dakheelsh bzare

--> function haee besazam
fucntion turn on all device
type device turn on ()

...??

parkAnde --> Core (haste) vasate kari



GUI --> k b kodom functioneto seda bzane




------- 

HADAF --> grouos[] tike haye khoanto misazi
b hartike az khoant device haro mortabet , 

control konish

dictionary -->keys --> list --> element [class .method]


groups = {}



nesbat b khonat besazi group ha (ghesnmat az khonato)
KEYS         value

living_room  []    
parking     []
hal        []
...        []



#--devcie besazi ezafe koni
KEYS         value

living_room  [device1,devcie2,sensor1]    
parking     []
hal        []
...        []




groups -->dictionary

b harkodom az in lista dastresi peyuda konam


groups['living_room '] ---> [device1,devcie2,sensor1] 

a=groups['living_room ']



bkham b devcie 1 dastresi peyda konM

device_avalim=a[0]


a[1]




#object az yk class Device --> attributes .
device_avalim.location 
device_avalim.turn_on() --> kararo anjma


'''

#function ha az yeja bename GUI gahrare seda bokhoran

#user -_> button (dokme) -_>click --> seda zade mishe oon function az backend 




class control_panel:
    
    def __init__(self):
        '''
        shoroe sakhte control_panel
        
        
        a=control_panel()
        '''
        self.groups={}
        
        
        
    
    #yadet abshe chijori estefade mishe?
    def create_group(self,group_name):
        '''
        vaghty user mikhad yek bakhsh az khonashio tarif (Define) kone
        masalan bege man living_room
        
        a.create_group('living_room')
        
        
        --------
        KEYS         Value
        living_room   [] --> badan behesh device ezaf konim
        
        
        
        '''
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'groups {group_name} created !!')
            
        else:
            print('your group name is duplicated')
        
    
    
    
    
    

    
    def add_device_to_group(self,group_name,device):
        '''
        Device misaze a=Device('home','felan','lamps','lamps123')
        
        group --> [device]
        
        self.groups= {     }
        
        self.groups['keys'] ---> [az device]
        
        
        .append --> device [a]
        
        
        'living_room'  [a]
        
        'living_room'  [a,b,c,d,e,f,g]
        
        
        '''
        if group_name in self.groups:
            
        
            self.groups[group_name].append(device)
            # groups['living_room'] -->[]
            print(f'your devic is added to {group_name}')
        else:
            print('you group is not exist....')
        
        
        
        
    def create_device(self,group_name,device_type,device_name):
        
        '''
        farghesh ine ke dg bniazi nadari aval device besazi
        device ro bedio b in fucntion abd append kone b liste dvice ha
        
        
        --> mostaghim agha msoahkahaset devcie , group-->
        
        
        
        
        
        
        '''
        
        if group_name in self.groups:
            location='home'
            new_device=Device(location,group_name,device_type,device_name)
            
            self.groups[group_name].append(new_device)
            print('///////bamofghtia')
            
        else:
            print('agha in esm vojod ndre') #...
        
    #natije --> create_device ba add_device_to_group yekian
    #fght add_device aval bayad devic ebsazi ta brizish too grpup ad
    #create_device --> hamon lahze khdoesh devcie misaze o add mikone -> rahat tare
        
    
    #tooye living_room , lamps , 40
    
    def create_multiple_device(self,group_name,device_type,device_number):
        '''
        
        yekbar seda zadane in tabe
        living_room [] b oon liste 40 , 100 , 100000 devcie mitoni ezafe koni
        '''
        
        if group_name in self.groups:
            
            for i in range(1,device_number+1):
                dv_name=f'{device_type}_{i}'
                self.create_device(group_name,device_type,dv_name)

            print(f'{device_number} devices created!!')
            
        else:
            
            print('....')
            
            
    
            
    #ino badan bekhon     
    #living room --> []
    '''
    
    groups= dictioanry
    keys              values
    Living_room  [d1,d2,d3,...]
    
    
    
    devices -->
    
    groups['living_room']
    
    
    
    
    
    '''
    
    
    def get_devices(self,group_name):
        devices=self.groups[group_name]
        return devices
        
        
        
    #group_name 
    '''
    
    GUI --> living__rom [button]  [khamosh kardane devcie ha]
    
    
    trun_on_in_group(living_room)
    
    '''
    def trun_on_in_group(self,group_name):
        
        if group_name in self.groups:
            
            #devices=self.groups[group_name]
            devices=self.get_devices(group_name)
            #[d1,d2,d3,d4] --> living_room (group_name)
            '''
            
            living_room [device1,device2,sensor1,sensor2,device1]
            
            '''

            #device -_> object haee boodan ma sakhtim
            #device21=Device(;.....)
            #device
            for device in devices:
                device.turn_on()
                print(f'device {device.device_name} is on ')
            
        else:
            print('....') 
            
    
    #turn_off device hast toye yek group
    #group_name
            
    def turn_off_in_group(self,group_name):
        '''
        biad dakhele oon group_name doone doone ro
        khamoosh kone 
        
        
        '''
        
        if group_name in self.groups:
            
            devices=self.get_devices(group_name)
            for device in  devices:
                device.turn_off()
                print(f'device {device.device_name} is off ')
            
  
        else:
            print('sorry we dont have this one')
    
    
    
    
    def get_all_devices(self):
        
        all_devices=[]
        for group_name in self.groups.keys():
            device_list=self.get_devices(group_name)
            #all_device.extend(device_list)
            for device in device_list:
                all_devices.append(device)
                
        return all_devices
            
            
        
    
    def turn_on_all(self):
        '''
        tamame device haro roshan kone
        
        '''
        
        all_devices=self.get_all_devices()
        
        for device in all_devices:
            device.turn_on()
            print(f'device {device.device_name} is turned on!!')
    
    
    def turn_off_all(self):
        '''
        hamaro khamoosh kone
        '''
        
        
        all_devices=self.get_all_devices()
        
        for device in all_devices:
            device.turn_off()
            print(f'device {device.device_name} is turned off!!')
    
    
    #group_name --> statuse doone dooen devuice haro behet bede
    def old_get_status_in_group(self,group_name):
        
        if group_name in self.groups:
            
            #self.groups[group_name]
            
            devices=self.get_devices(group_name)
            for device in devices:
                print(f'device {device.device_name} is {device.status}')
                
                
            
        else:
            print(f'sorry this {group_name}is not in our groups')
        
        
    def get_status_in_group(self,group_name):
        
        if group_name in self.groups:
            
            status_results={}
            
            #self.groups[group_name]
            
            devices=self.get_devices(group_name)
            for device in devices:
                status_results[device.device_name]=device.get_status()
                
                
            return status_results
                
        
            
        else:
            print(f'sorry this {group_name}is not in our groups')
        
        
    '''
    
    {
        
    'device101' : True
    'device102' : False
        
        }
    
    
    
    
    '''
        
    
    #living
    #harja k device type --> lamp 
    #lamp khoen , parking, hal ,.....
    
    def get_status_in_device_type(self,dvice_type):
        
        #hameye device haro mikham
        
        '''
        all_devices=[]
        for group_name in self.groups.keys():
            devices=self.groups[group_name]
            for device in devices:
                all_devices.append(device)
                
        '''
        
        all_devices=self.get_all_devices()
        status_results={}
        
        for device in all_devices:
            #dar soorsati k tyopesh lamp
            #age type oon device hae k too all_device
            #tamame device haye khoant, trypoeshon
            #device_tyope to moshakahs
            if device.device_type == dvice_type:
                device.get_status()
                status_results[device.device_name]=device.get_status()
               # print(f'device {device.device_name} is {device.status}')
                
        return status_results
    
    
    '''
    
    
    
    lamps101  Truye
    lamps9332  False
    Lamps 
    
    
    '''
    
    def turn_on_in_device_type(self,dvice_type):
        

        all_devices=self.get_all_devices()
        
        for device in all_devices:
            if device.device_type == dvice_type:
                device.turn_on()
                
                
    def turn_off_in_device_type(self,dvice_type):
        

        all_devices=self.get_all_devices()
        
        for device in all_devices:
            if device.device_type == dvice_type:
                device.turn_off()
                

    #tabe ee bename create_device???
    '''
    
    
    ye sensor besaze barat va bezare too ye goroh ()
    
    '''
    
    
    
    
    def create_sensor(self,group_name,sensor_type,sensor_name):
        if group_name in self.groups:
            
            new_sensor=Sensor('home',group_name,sensor_type,sensor_name)
            #oinja devcie besazi --> sensor besazi va addesh koni b list
            
            self.groups[group_name].append(new_sensor)
        
        else:
            print('injae naskahte , create-Groups')

    '''
    
    groups
    
    living_room  [device11,device2, ..... sensor1 , sensor2 , sensor3]
    '''
    
    
    
    def check_group_availability(self,group_name):
        if group_name in self.groups:
            return True
        else:
            print('your group is not in groups , first buil with function crate_group')
            return False
    
    def create_multiple_sensor(self,group_name,sensor_type,sensor_number):
        
        if self.check_group_availability(group_name):
            
            for i in range(1,sensor_number+1):
                sensor_name=f'{sensor_type}_{i}'
                
                #new_sensor=
                #ba in esm new sensor besazam bad add konm??
                self.create_sensor(group_name, sensor_type, sensor_name)
                






'''
INJA ---> project
#-------REAL ------------




Note1 --> ta jae k mitonid , abd az etamme kar , bad bin bashid
yani say konid khata peyda konid 

erroro peyda kon

note2-->#---> Trye except --> error khord , try except 



note3--> sari naro halesh kon , sari das b code

bhtarijn rah
ta jaee k mitoni, kari kon k nari too kole code khat b khat taghir bdi





note 4---> databasd , logg

rune --> Memory rune khamosh bshe hame dchi mipare

--> Data base -->

data abse --> Hard 
tak take in emal ha k mikhore

turn_on()

turn_off() device

tabe e ezafe 




tabel LOG

id     date     device_name  action



dalilesh -_> hame ye ina zakhire shode 
barname roo rune -_> ram --> khamosh bshe, barghe hame chi mipare data 
--> data base zakhire bshe

logg--> actigity akhir ro bbini , error felan shod ,...


--> feature ha vizhegi hay ejadid estefade krd





'''
            
            
        
class Device:
    
    #devcie haro baham mojaza koni
    def __init__(self,location,group,device_type,device_name):
        self.location=location
        self.group=group
        self.device_type=device_type
        self.device_name=device_name
        
        self.status='off'
        
        
    def turn_on(self):
        print('Done!!!')
        self.status='on'
        #-->inja mahali hast -_> oon coda neveshte --> b shekrate vaset vasl she az on bekhad
        #b devcie vasl she --> devcie ro turn on kone
        
        logg(self.device_name,'ON')
        


    def turn_off(self):
        print('off')
        self.status='off'
        #-->inja mahali hast -_> oon coda neveshte --> b shekrate vaset vasl she az on bekhad
        #b devcie vasl she --> devcie ro turn off kone
        logg(self.device_name,'OFF')
        
    def get_status(self):
        '''
        On ya Off pas bde
        True , False
        
        
        '''
        if self.status=='on':
            return True
        else:
            return False
    
    
def logg(device_name,action):
    
    '''
    time = time  -->
    ddvice_name self.device_name
    actiuon--> 'ON'
    action-->'OFF'
    
    sql , ....
    
    
    time, device_name,action ---> database logg
    
    
    '''
        





#-------------------------------------------
#-------------------------------------------
#-------------------------------------------
#-------------------------------------------
#-------------------------------------------
#-------------------------------------------
#-------------------------------------------
#-------------------------------------------
#-------------------------------------------
#-------------------------------------------
#-------------------------------------------
#-------------------------------------------

'''

Nimsaate , ....


GUI

-----
dokme
groups


.....








'''































