class parent():
    
    def __init__(self):
        self.name="fam1"
    
    def intro(self):
        print(self.name)
        
        
class child(parent):
    
    def __init__(self):
        self.number="234"
        self.name="fam2"
        
    def childdetail(self):
        print("fam: ",self.name)
        print("child.detail:", self.number)
c=child()
c.intro()
c.childdetail()
