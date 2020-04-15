class lru:
    def __init__ (self,capacity):
        super().__init__()
        self.capacity = capacity
        self.element = {}
        self.elements = {}

    def put(self,key,data):
        if key not in self.element and len(self.element)==self.capacity:
            old=min(self.elements.keys(),key=lambda k:self.elements[k])
            self.element.pop(old)
            self.elements.pop(old)
        self.element[key] = data
        self.elements[key]=1
        return "Entered"

    def get_cache(self):
        return self.element

    def get(self,key):
        if key in self.element:
            self.elements[key] += 1
            return self.element[key]
        else:
            print("not found in cache")
