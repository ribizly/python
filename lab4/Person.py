import weakref

class Person(object):

    __slots__=('__weakref__','_name','_gender','age')
    persons=[]

    def __init__(self,name,gender,age=0):
        self._name=name
        self._gender=gender
        self.age=age
        Person.persons.append(weakref.ref(self,Person.__on_delete))

    def __del__(self):
        '''Do nothing'''
        print("Destructor is called for %s" % self)

    @staticmethod
    def __on_delete(weakrf):
        '''This one is called by weakref when the referred object is about to finalize'''
        if (Person): Person.persons.remove(weakrf)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if (str.upper(name) == str.upper(self._name)):
            self._name=name
        else:
            raise AttributeError("Changing name is not allowed!")

    def __str__(self):
        attrs=[ str(self.__getattribute__(attr)) for attr in ('name','_gender','age') ]
        return ('/'.join(attrs))

    def __cmp__(self,other):
        return cmp(self.name,other.name)

    def __add__(self,other):
        self.age+=other
        return self

    @staticmethod
    def printAll():
        for p in Person.persons:
            print p()

p=Person('Bela','Male',99)
p.printAll()
