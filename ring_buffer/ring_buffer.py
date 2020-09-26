class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.oldest = None

    def append(self, item):
        if len(self.data) < self.capacity:
            if len(self.data) == 0:
                self.oldest = item
            self.data.append(item)
        else:
            oldest_index = 0
            for i, value in enumerate(self.data):
                if value == self.oldest:
                    self.data[i] = item
                    if i == self.capacity - 1:
                        oldest_index = 0
                    else:
                        oldest_index = i + 1
            self.oldest = self.data[oldest_index]
            


                
            

    def get(self):
        no_none = []
        for item in self.data:
            if item != None:
                no_none.append(item)
        
        return no_none