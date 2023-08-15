 
# find mean,mode,modal for 10 random numbers

import random

class Stats:
    def __init__(self,nums_array,sum,number_of_values):
        self.sum = sum
        self.nums_array = nums_array
        self.number_of_values = number_of_values 

    def find_mean(self):
        for i in range(self.number_of_values):
            self.nums_array.append(random.randint(1,5))
            self.sum += self.nums_array[i]
        print("Generated list:\n",self.nums_array)
        return round(self.sum/self.number_of_values,1)

    def find_mode(self):
        modes = []
        for value in self.nums_array:
            if self.nums_array.count(value) > 1:
                if (value in modes) == False:
                    modes.append(value)
        return modes
    
    def find_modal(self):
        count = 0
        modal = []
        for value in self.nums_array:
            if(self.nums_array.count(value) >1):
                if(count < self.nums_array.count(value)):
                    count = self.nums_array.count(value)
                    modal.append(value)
        return modal    


stat = Stats([],0,10)
print("Mean: ",stat.find_mean())
print("Mode: ",stat.find_mode())
print("Modal: ",stat.find_modal())










