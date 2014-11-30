'''
The OOP concepts from python is simply mapped with SchoolMember of the school. The following OOP principle will be covered:
1. Class
2. Object
3. Inheritance
4. Polymorphism (Will cover only Method overriding)
5. Data Hiding
'''

class SchoolMember:                                             #Represents any school member.
	
	__count=0
	
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print '(Initialized SchoolMember: %s)' % self.name
		SchoolMember.__count+=1
	
	def tell(self):                                             #Tell my details.
		print 'Name:"%s" Age:"%s"' % (self.name, self.age),

	def tell_count(self):
		print 'Count of schoolmember is ',SchoolMember.__count

class Teacher(SchoolMember):                                    #Represents a teacher.

	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print '(Initialized Teacher: %s)' % self.name

	def tell(self):                                             #overriding method
		SchoolMember.tell(self)
		print 'Salary: "%d"' % self.salary

class Student(SchoolMember):                                    #Represents a student.
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print '(Initialized Student: %s)' % self.name
	
	def tell(self):
		SchoolMember.tell(self)
		print 'Marks: "%d"' % self.marks
	
	def talented(self,other):                                      #Represents a Overloading
		
		if self.marks > other.marks:
			print self.name,'is talented.!'
		else:
			print other.name,'is talented.!'


t1=Teacher('Apasangi',40,30000)
s1=Student('abc',20,80)
s2=Student('xyz',25,70)

s1.talented(s2)

members = [t1, s1]
for member in members:
	member.tell()                                               # works for both Teachers and Students

s2.tell_count()
