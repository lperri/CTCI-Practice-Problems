# animal shelter: fifo, must adopt either the oldest (based on arrival time) of all the animals in the shelter
# or they can select if they prefer dog or cat and will receive the oldest animal of that type
# they cannot select which specific animal they would like
# operations: enqueue, dequeueAny, dequeueDog, dequeueCat
from implementation_stack_queue import Queue


class AnimalShelter(Queue):

    def __init__(self):
         self.cat_queue = Queue()
         self.dog_queue = Queue()
         self.full_queue = [self.cat_queue, self.dog_queue]

    def enqueue(self, animal):
        if animal["is_cat"]:
            self.cat_queue.enqueue(animal)

    def dequeueAny(self):
        if (not self.cat_queue.is_empty()) and (not self.dog_queue.is_empty()):
            return max(self.cat_queue.peek()["number"], self.dog_queue.peek()["number"]).dequeue()
        elif (self.cat_queue.is_empty()) and (not self.dog_queue.is_empty()):
            return self.dequeueDog()
        elif (not self.cat_queue.is_empty()) and (self.dog_queue.is_empty()):
            return self.dequeueCat()

    def dequeueCat(self):
        return self.cat_queue.dequeue() if not self.cat_queue.is_empty() else None

    def dequeueDog(self):
        return self.dog_queue.dequeue() if not self.dog_queue.is_empty() else None

if __name__ == "__main__":
    shelter = AnimalShelter()
    print(shelter.dequeueCat())
    animal_1 = {"is_cat": True, "number": 1}
    animal_2 = {"is_cat": False, "number": 1}
    animal_3 = {"is_cat": True, "number": 1}
    animal_4 = {"is_cat": True, "number": 1}
    animal_5 = {"is_cat": False, "number": 1}
    animal_6 = {"is_cat": True, "number": 1}
    animal_7 = {"is_cat": False, "number": 1}
    print(shelter.enqueue(animal_1))
    print("cat, dog, full: ", shelter.cat_queue, shelter.dog_queue, shelter.full_queue)
    shelter.enqueue(animal_2)
    shelter.enqueue(animal_3)
    shelter.enqueue(animal_4)
    shelter.enqueue(animal_5)
    print("dequeueAny: ", shelter.dequeueAny())
    print("cat, dog, full: ", shelter.cat_queue, shelter.dog_queue, shelter.full_queue)
