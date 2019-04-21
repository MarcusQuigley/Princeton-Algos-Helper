import math

class MaxHeap(object):
    def __init__(self):
        self._count = 0
        self._minindex = 0
        self._maxindex = 0
        self._heap_array = [None]
    
    @property
    def count(self):
        return self._count   

    def insert(self, value):
        self._maxindex += 1
        self._heap_array.append(value)
        if self.count == 0:
            self._minindex += 1
        else:
            #self._heap_array[self._maxindex] = value
            tempidx = self._maxindex
            parentidx = math.floor(tempidx/2)
            while self._heap_array[parentidx] < self._heap_array[tempidx]:
                temp = self._heap_array[parentidx]
                self._heap_array[parentidx] = self._heap_array[tempidx]
                self._heap_array[tempidx] = temp
                tempidx = parentidx
                parentidx = math.floor(parentidx/2)
                if parentidx < self._minindex: break
        self._count += 1
    

    def remove(self):
        value = self._heap_array[self._minindex]
        self._heap_array[self._minindex] = self._heap_array[self._maxindex] 
        self._heap_array.pop()#[self._maxindex])
        self._maxindex -= 1
        self._count -= 1
        child_left = math.floor(self._minindex * 2) 
        child_right = math.floor(self._minindex * 2) + 1
        child_idx = 0
        temp_index = self._minindex
        while self._heap_array[temp_index] < (self._heap_array[child_left] or self._heap_array[child_right] ):
            child_idx = child_right if self._heap_array[child_right] > self._heap_array[child_left]  else child_left
            temp = self._heap_array[temp_index]
            self._heap_array[temp_index] = self._heap_array[child_idx]
            self._heap_array[child_idx] = temp
            temp_index = child_idx
            child_left = math.floor(temp_index * 2) 
            child_right = math.floor(temp_index * 2) + 1
            if child_right > self._maxindex: break
        
        return value