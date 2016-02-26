class Env:
    def __init__(self):
        self.outer = None
        self.data = {}

    def set(self,key,val):
        self.data[key] = val

    def find(self,key):
        if key in self.data:
            return self
        elif key not in self.data and self.outer!=None:
            return self.outer.find(key)
        else:
            return None

    def get(self,key):
        env = self.find(key)
        if env == None:
            raise "not find: "+str(key)
        else:
            return env.data[key]
