class lru:
      pass
    

    def put(self,key,data):
          pass
        

    def get_cache(self):
        return self.element

    def get(self,key):
        if key in self.element:
            self.elements[key] += 1
            return self.element[key]
        else:
            print("not found in cache")
