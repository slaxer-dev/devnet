import math as ma
import calendar as cal


class Router:
    def __init__(self,model, swversion, ip_add):
        '''initialize value'''
        '''print(self.model)
                print(self.swversion)
                print(self.ip_add)'''
        self.model = model
        self.swversion = swversion
        self.ip_add = ip_add


    def getdesc(self):
        '''return your instance's desc'''
        desc = f'Hello\n'\
               f'your Router\' model is : {self.model}\n'\
               f'your swversion\' is : {self.swversion}\n'\
               f'your ip\' is : {self.ip_add}'
        return desc



class Switch(Router):
    def getdesc(self):
        desc = (f'Hello\n' \
               f'your switch\' model is : {self.model}\n' \
               f'your swversion\' is : {self.swversion}\n' \
               f'your ip\' is : {self.ip_add}')
        return desc

