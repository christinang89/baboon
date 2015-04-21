import datetime

class Animal():
    def __init__(self, arrtime, animaltype, id):
        self.arrtime = arrtime
        self.animaltype = animaltype
        self.id = id
    def __repr__(self):
        return str(self.arrtime) + " , " + self.animaltype + " , " + str(self.id)

class AnimalQueue():
    def __init__(self):
        self.catqueue = []
        self.dogqueue = []
    def enqueue(self, animal):
        if animal.animaltype == "cat":
            self.catqueue.append(animal)
        elif animal.animaltype == "dog":
            self.dogqueue.append(animal)
    def dequeueDog(self):
        if self.dogqueue == []:
            return "No dogs"
        else:
            return self.dogqueue.pop(0)
    def dequeueCat(self):
        if self.catqueue == []:
            return "No cats"
        else:
            return self.catqueue.pop(0)
    def dequeueAny(self):
        if self.dogqueue == [] and self.catqueue == []:
            return "No animals"
        elif self.dogqueue == []:
            return self.dequeueCat()
        elif self.catqueue == []:
            return self.dequeueDog()
        else:
            if self.dogqueue[0].arrtime > self.catqueue[0].arrtime:
                return self.dequeueCat()
            else:
                return self.dequeueDog()
    def __repr__(self):
        print "dog: "
        for i in self.dogqueue:
            print str(i.arrtime) + " , " + i.animaltype + " , " + str(i.id)
        print "cat: " 
        for i in self.catqueue:
            print str(i.arrtime) + " , " + i.animaltype + " , " + str(i.id)

dog1 = Animal(datetime.datetime(2015,1,1,15, 29, 43, 79060),"dog",1)
dog2 = Animal(datetime.datetime(2015,2,1,15, 29, 43, 79060),"dog",2)
cat1 = Animal(datetime.datetime(2015,1,1,15, 29, 53, 79060),"cat",1)
cat2 = Animal(datetime.datetime(2015,1,3,15, 29, 53, 79060),"cat",1)

q = AnimalQueue()
q.enqueue(dog1)
q.__repr__()
q.enqueue(dog2)
print q.dequeueDog()
print q.dequeueDog()
print q.dequeueDog()
q.enqueue(dog1)
print q.dequeueAny()

q.enqueue(dog2)
q.enqueue(cat1)
print "###"

q.__repr__()
print q.dequeueAny()
print q.dequeueDog()
print q.dequeueCat()
