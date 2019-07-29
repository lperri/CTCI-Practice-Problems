''' 
Design a library system.

Entities: library (name, address, employees), libraryCard, borrower, employee (name, salary, employeeID, service(librarian)) 

Functions of libraryCard:
- allows you to be able to check out book
- identifies borrower (like a borrower id)
- check current status of what books you have checked out/when they are due

Functions of Library:
- maintain list of currently available items, how many out of total are checked out/available

Functions of Borrower:
- check out item 
- return item
- renew item

Functions of Librarian:
- lend item

Functions of Item
- check availability (T/F)
'''
import random
import string



class Library(object):
	def __init__(self, libName, libAddress, employees=None, members=None, totalInventory=None, checkedOut=None):
		self.libName = libName
		self.libAddress = libAddress
		if employees is None:
			self.employees = [] # list of <Employee>
		else:
			self.employees = employees
		if members is None:
			self.members = []
		else:
			self.members = members
		if totalInventory is None:
			self.totalInventory = {} # {bookID:[numberOwned, numberAvaiable]}
		else:
			self.totalInventory = totalInventory
		if checkedOut is None:
			self.checkedOut = {} # {<Borrower>:[[<Book>,dueDate]]}
		else:
			self.checkedOut = checkedOut


	def newEmployee(self, new_employee):
		if new_employee not in self.employees:
			self.employees.append(new_employee)
			

	def removeEmployee(self, employee):
		if employee in self.employees:
			self.employees.remove(employee)
		
	def showEmployees(self):
		for employee in self.employees:
			print '--------------'
			print 'Employee name: ',employee.employeeName
			print 'ID: ',employee.employeeID
			print 'Service: ',employee.service
			print 'Salary: ',employee.salary
		print '--------------'	

	def newBook(self, book):
		if book.bookID in self.totalInventory:
			# add 1 to number owned
			self.totalInventory[book.bookID][0] += 1 
			# add 1 to number available
			self.totalInventory[book.bookID][1] += 1 
		else:
			self.totalInventory[book.bookID] = [1, 1]


class Employee(object):

	std_salary = 60000

	def __init__(self, employeeName, employeeID=None, service="Librarian", salary=std_salary):
		self.employeeName = employeeName
		self.employeeID = employeeID
		self.service = service
		self.salary = salary
		if employeeID is None:
			self.employeeID = self.generateEmployeeID()

	def generateEmployeeID(self, stringLength=10):
		lettersAndDigits = string.ascii_letters + string.digits
		return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))



class Librarian(Employee):

	def __init__(self, employeeName):
		super(Librarian, self).__init__(employeeName, employeeID=None, service="Librarian",salary=Employee.std_salary)

	def lendItem(self, book, totalInventory):
		if book.bookID in totalInventory:
			if totalInventory[book.bookID][1] > 0:
				totalInventory[book.bookID][1] -= 1
			else:
				print 'Sorry, all copies are checked out at the moment.'
		else:
			print 'Sorry, we don\'t carry that book.'



class LibraryCard(object):
	def __init__(self, borrowerName, number):
		self.borrowerName = borrowerName
		self.number = randomStringDigits()



class Borrower(object):
	#def __init__(self, name, libCard, booksCheckedOut):
	pass

# assumption for simplicity that library only contains literature -- no other media types
class Book(object):
	def __init__(self, title, author, bookID=None, publisher=None):
		# note: bookID is specific to a (Title, Author) -- not an individual physical copy
		self.bookID = bookID
		self.title = title
		self.author = author
		self.publisher = publisher
		self.currentBorrower = None
		if self.bookID is None:
			self.bookID = self.generateBookID()

	def isAvailable(self, totalInventory):
		if book in totalInventory:
			if totalInventory[book][1] > 0:
				return True
		return False

	def generateBookID(self, stringLength=20):
		lettersAndDigits = string.ascii_letters + string.digits
		return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


my_lib = Library('Glenview Public Library', '1544 Hawthorne Ln Glenview, IL 60025')

librarian_1 = Librarian('Leah Perri')
my_lib.newEmployee(librarian_1)

librarian_2 = Librarian('Jenna Geary')
my_lib.newEmployee(librarian_2)

librarian_3 = Librarian('Trisha Lorde')
my_lib.newEmployee(librarian_3)


books = [Book('The Great Gatsby', 'F. Scott Fitzgerald'), Book('The Unbearable Lightness of Being', 'Milan Kundera')]
for book in books:
	my_lib.newBook(book)

print my_lib.totalInventory






