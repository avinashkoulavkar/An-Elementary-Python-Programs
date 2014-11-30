'''
This code is to cover File and Exception handling on files.
'''
import os
import cPickle as p

def create_dir():                                                                   #Creating Directiory
		os.mkdir("/home/File-Program")
	
	
def read_file():                                                                    #Methods for Reading From File
	
	#create_dir()
	
	file_name=raw_input('Enter The File to Open:')
	
	try:
		
		fp=open(file_name,'r+')                                                        #Opening File in r+ mode
		
		for line in fp:                                                                #reading from file
			print line,
		
	except IOError:                                                                  #Handling IOError
		print 'IOError Occures'
	
	finally:
		if fp:
			fp.close()
	
def write_file():                                                                 #method for Writing File
	
	#create_dir()
	file_name=raw_input('Enter The File to Open:')
	
	try:
		fp=open(file_name,'w')

		ip=raw_input('Enter the Data to Write')
		
		fp.write('Avinash')
	except IOError:
		print 'IOError Occures'
	
	finally:
		fp.close()
	
def pickle():
	shoplistfile = 'shoplist.data' 							                           		   # the name of the file where we will store the objec
	shoplist = ['apple', 'mango', 'carrot']
	f = file(shoplistfile, 'w')
	p.dump(shoplist, f)                                                          # dump the object to a file
	f.close()
	del shoplist                                                                 # remove the shoplist
	
	f = file(shoplistfile)                                                       # Read back from the storage
	storedlist = p.load(f)
	print storedlist


option={1:read_file,2:write_file,3:pickle}

while True:

	print '======================== MENU =========================='
	print '\t\t 1 . Read From File'
	print '\t\t 2 . Write to The File'
	print '\t\t 3 . Use List Object as Pickle'
	print '\t\t 0 . Exit'
	print '========================================================'

	choice=input('Enter your Choice:')

	if choice==0:
		break

	option[choice]()
