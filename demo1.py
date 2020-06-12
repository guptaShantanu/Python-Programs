class Test:
    def __init__(self):
        self.variable='old'
        self.Change(self.variable)
    def Change(self,var):
        var='new'
ob=Test()
print(ob.variable)
