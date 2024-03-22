

class IEvent():
    def __init__(self, id :str,title :str,categories :str,sources :str,description :str=None):  
        self.id :str = id
        self.title :str = title
        self.description :str = description
        self.categories :str = categories
        self.sources :str = sources
    

    def create(self):
        return self
    
    def get(self):
        return {k.replace("_","",1):v for k,v in self.__dict__.items()}
    
    
    def __repr__(self) -> str:
        return str(self.__dict__)
    
    def set_object(self, data):
        for k, v in data.items():
            self.__setattr__(k, v)
        return self



    
