import random
import string


class TelephoneDirectory():
	def __init__(self):
		self.hashtable=[[] for i in range(0,335923)]
		self.hashsize=335923



	def hash(self,a):
	    h=0
	    a=str(a)
	    a=string.lower(a)
	    for i in range(0,len(a)):
	        h=h+(ord(a[i])-97)*(26**i)
	    return h%self.hashsize

	def AddEntry(self,name, number):
		if self.search(name):
			i=self.hash(name)
			for j in range(0,len(self.hashtable[i])):
				if name==self.hashtable[i][j][0]:
					self.hashtable[i][j].append(number)
		else:
			i=self.hash(name)
			self.hashtable[i].append([name,number])

	def search(self,name):
		i=self.hash(name)
		for j in range(0,len(self.hashtable[i])):
			if name==self.hashtable[i][j][0]:
				return True
		return False

	def GetNumber(self,name):
		if self.search(name):
			i=self.hash(name)
			print "Searched number is: "
			for j in range(0,len(self.hashtable[i])):
				if name==self.hashtable[i][j][0]:
					for k in range(1,len(self.hashtable[i][j])):
						print self.hashtable[i][j][k]
					break


		else:
			print 'Number is not stored'

	def DeleteEntry(self,name, number=None):
		if self.search(name):
			i=self.hash(name)
			m=1
			for j in range(0,len(self.hashtable[i])):
				if name==self.hashtable[i][j][0]:
					if number==None:
						del self.hashtable[i][j]
					elif len(self.hashtable[i][j])==2:
						del self.hashtable[i][j]
					else:
						for k in range(1,len(self.hashtable[i][j])):
							if number==self.hashtable[i][j][k]:
								del self.hashtable[i][j][k]
								m=0
								break
				if m==0:
					break
			if m==1:
				print 'Number is not stored'
		else:
			print 'Number is not stored'


	def UpdateNumber(self,name, old_number, new_number):
		if self.search(name):
			i=self.hash(name)
			m=1
			for j in range(0,len(self.hashtable[i])):
				if name==self.hashtable[i][j][0]:
					for k in range(1,len(self.hashtable[i][j])):
						if old_number==self.hashtable[i][j][k]:
							self.hashtable[i][j][k]=new_number
							m=0
							break
				if m==0:
					break

			if m==1:
				self.hashtable[i][j].append(new_number)
				print "Old number is not stored"

					#self.hashtable[i][j][1]=new_number

		else:
			print "Contact with this name is not stored"


myDir = TelephoneDirectory()
myDir.AddEntry("Harpreet",9999999999)
myDir.GetNumber("Harpreet")


