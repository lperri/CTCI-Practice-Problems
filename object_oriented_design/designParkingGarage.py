'''
Design a parking garage - Requirements:

The parking lot should have multiple entry and exit points.

Customers can collect a parking ticket from the entry points and can pay the parking fee at the exit points on their way out.

Customers can pay the tickets at the automated exit panel or to the parking attendant.

Customers can pay via both cash and credit cards.

Customers should also be able to pay the parking fee at the customers info portal on each floor. If the customer has paid at the info portal, they dont have to pay at the exit.

The system should not allow more vehicles than the maximum capacity of the parking lot. If the parking is full, the system should be able to show a message at the entrance panel and on the parking display board on the ground floor.

Each parking floor will have many parking spots. The system should support multiple types of parking spots such as Compact, Large, Handicapped, Motorcycle, etc.

The Parking lot should have some parking spots specified for electric cars. These spots should have an electric panel through which customers can pay and charge their vehicles.

The system should support parking for different types of vehicles like car, truck, van, motorcycle, etc.

Each parking floor should have a display board showing any free parking spot for each spot type.

The system should support a per-hour parking fee model. For example, customers have to pay $4 for the first hour, $3.5 for the second and third hours, and $2.5 for all the remaining hours.
'''
import datetime


class ParkingGarage(object):
	def __init__(self, capacity=0, floors=None, occupancy=0):
		self.capacity = capacity
		if not floors:
			self.floors = []
			self.addFloor(GarageFloor(floorNumber=1))
		else:
			self.floors = floors
		self.occupancy = occupancy

	def addFloor(self, new_floor):
		numNewSpots = new_floor.floorCapacity
		if self.occupancy < self.capacity or (self.occupancy == self.capacity == 0):
			self.floors.append(new_floor)
			self.capacity += numNewSpots
		else:
			return 'Cannot add another floor -- this structure\'s capacity has been reached!'


class GarageFloor(object):
	def __init__(self, floorOccupancy=0, parkingSpots=None, floorNumber=0):
		self.floorCapacity = raw_input('How many spots would you like there to be on this floor?\nPlease type an integer number: ')
		self.floorOccupancy = 0
		self.floorCapacity = floorCapacity
		self.floorNumber = floorNumber
		if not parkingSpots:
			self.parkingSpots = [0]*self.floorCapacity
			self.generateSpots()
		else:
			self.parkingSpots = parkingSpots
		if self.floorNumber == 1:
			self.entrances = self.generateEntrances()
			self.exits = self.generateExits()
			self.displayBoard = self.generateDisplayBoard()
		self.infoPanel = self.generateInfoPanel()

	def generateSpots(self):
		for i in xrange(1, self.floorCapacity+1):
			if i <= (self.floorCapacity/2):
				# if cap=10, spots 1,2,3,4,5 are Reg
				new_spot = ParkingSpot(self.floorNumber, i, 'Regular')
			elif i > (self.floorCapacity/2) and i <= (self.floorCapacity/2 + self.floorCapacity/10):
				# spots 6 are Motor
				new_spot = ParkingSpot(self.floorNumber, i, 'Motorcycle')
			elif i > (self.floorCapacity/2 + self.floorCapacity/10) and i <= (self.floorCapacity/2 + self.floorCapacity/5):
				# spots 7 and 8 are Handi
				new_spot = ParkingSpot(self.floorNumber, i, 'Handicapped')
			elif i > (self.floorCapacity/2 + self.floorCapacity/5) and i <= (self.floorCapacity/2 + self.floorCapacity/5 + self.floorCapacity/10):
				# spots 9 are large
				new_spot = ParkingSpot(self.floorNumber, i, 'Large Vehicles')
			elif i > (self.floorCapacity/2 + self.floorCapacity/5 + self.floorCapacity/10) and i <= self.floorCapacity:
				# spots 10 are compact
				new_spot = ParkingSpot(self.floorNumber, i, 'Compact')
			self.parkingSpots.append((new_spot, self.floorNumber, i))
		return self.parkingSpots

	def generateEntrances(self):
		if self.floorNumber == 1:
			num = raw_input('How many entrances would you like there to be on the ground floor? ')
			entrances = []
			for i in range(num):
				new_entrance = Entrance(self)
				entrances.append(new_entrance)
			return entrances
		return

	def generateExits(self):
		if self.floorNumber == 1:
			num = raw_input('How many exits would you like there to be on the ground floor? ')
			exits = []
			for i in range(num):
				new_entrance = Entrance(self)
				exits.append(new_entrance)
			return exits

	def generateDisplayBoard(self):
		return

	def generateInfoPanel(self):
		return


class ParkingSpot(object):
	def __init__(self, floorNumber, spotNumber, spotType, occupied=False):
		self.floorNumber = floorNumber
		self.spotNumber = spotNumber
		self.spotType = spotType
		self.occupied = occupied
	
	def markOccupied(self):
		self.occupied = True
		

class Customer(object):
	def __init__(self, car, ticket, spotNumber):
		self.car = car
		self.ticket = ticket
		self.spotNumber = spotNumber

	def amountOwed(self, ticket):
		if not ticket.paid:
			total_time = self.hours(datetime.datetime.now() - ticket.entrance_time)
			return total_time

	def hours(self, timeDelta):
		days, hours, minutes = timeDelta.days, timeDelta.seconds/3600, (timeDelta.seconds/60)%60
		if minutes > 0:
			hours += 1
		return days*24 + hours

	def payTicket(self, ticket, method='exit'):
		if not ticket.paid:
			if method == 'attendant':
				ticket.payAttendant()
			elif method == 'portal':
				ticket.payAtPortal()
			elif method == 'exit':
				ticket.payAtExit()


class Entrance(object):
	def __init__(self, floor, panel=None):
		self.floor = floor
		if panel:
			self.panel = panel
		else:
			self.panel = floor.generateInfoPanel()

	
class Attendant(object):
	def __init__(self, name):
		self.name = name

	def receivePayment(self, customer):
		print 'Hello, {}. Your total today will be {}.'.format(customer.name)


class Ticket(object):
	def __init__(self, barcode, entrance_time, paid=False):
		self.barcode = barcode
		self.entrance_time = datetime.datetime.now()
		self.paid = paid
	
	def payAtExit(self, customer, exit):
			print 'Payment of ${} processed. Thank you!'.format(customer.amountOwed.round(2))		
			customer.amountOwed = 0
			self.paid = True

	def payAtPortal(self, customer):
		print 'Payment of ${} processed. Thank you!'.format(customer.amountOwed.round(2))		
		customer.amountOwed = 0
		self.paid = True


class Car(object):
	def __init__(self, owner, licensePlate, carType='Regular'):
		self.carType = carType
		self.owner = owner
		self.licensePlate = licensePlate

	def park(self, floors, spots):
		possible_spots = []
		for floor in floors:
			for spot in spots:
				if spot.spotType == self.carType and not spot.occupied:
					# take the first spot you can
					spot.markOccupied()
					break


class InfoPortal(object):
	# on each floor, can pay
	pass


class DisplayBoard(object):
	# on ground floor -- display message that lot is full if isFull
	# on every floor saying if floor is full + what # spots are open,
	pass


class Exit(object):
	# multiple, on ground floor
	# check if paid via info panel, if not pay here
	pass


my_garage = ParkingGarage()
print my_garage.occupancy, my_garage.capacity
new_floor = GarageFloor()
my_garage.addFloor(new_floor)
print my_garage.occupancy, my_garage.capacity



