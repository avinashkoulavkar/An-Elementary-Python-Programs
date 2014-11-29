'''Covering the three built-in data structures in Python - list, tuple and dictionary from in module __builtin__.
In the Given Program :
1)List is mapped with shopping list
2)Tupple is mapped with Animal in zoo
3)Dictionary is mapped with name and corresponding Emails
'''

def shopping_list():
    
    count=input('How Many element you want to shop?')
    shoplist=list()
    for i in range(0,count):
	item=raw_input('Enter The Item:')
	shoplist.append(item)

    
    while True:
		print '1. Create Shopping_list'
		print '2. Append an item'
		print '3. insert an item to specific position'
		print '4. Slice a List'
		print '5. Remove from List'
		print '6. Pop from top of list'                      #Using lists as stacks
		print '7. Pop from left of list'                     #Using Lists as Queues
		print '8. Index of item'
		print '9. sort the list'
		print '10.reverse the list'
		print '11.clear the list'
		print '12.Display the List'
		print '13.display distinct Items'
		print '0.Exit\n'
		
		#Further we can use List as Functional Programming Tools or for List Comprehensions
		
		choice=input('Enter Your Choice:')
		
		if choice==1:
			count=input('How Many element you want to shop?')
			shoplist=list()
			for i in range(0,count):
				item=raw_input('Enter The Item:')
				shoplist.append(item)

		elif choice==2:
			item=raw_input('Enter The Item:')
			shoplist.append(item)

		elif choice==3:
			item=raw_input('Enter The Item:')
			pos=input('Enter the position')
			shoplist.insert(pos,item)

		elif choice==4:
			index1=input('Enter the starting index')
			index2=input('Enter the Ending Index')
			print shoplist[index1:index2]

		elif choice==5:
			item=raw_input('Enter The Item to remove:')
			
			if item in shoplist:
				shoplist.remove(item)
				print 'Item removed successfully'
			else:
				print 'Item not present in list'
		
		elif choice==6:
			print 'here the item popped:'+ shoplist.pop()

		elif choice==7:
			print 'here the item popped:'+ shoplist.popleft()
		
		elif choice==8:
			item=raw_input( 'Enter the Item to search index:')
			
			if item in shoplist:
				print shoplist.index(item)
			else:
				print 'Item not present in list'
		
		elif choice==9:
			shoplist.sort()
			print 'Here is your shopping cart:'
			for item in shoplist:
				print item

		elif choice==10:
			shoplist.reverse()
			print 'Here is your shopping cart:'
			for item in shoplist:
				print item

		elif choice==11:
			del shoplist[:]			

		elif choice==12:
			print 'Here is your shopping cart:'
			for item in shoplist:
				print item
		
		elif choice==13:
			print 'Here is your distinct shopping cart:'
			for item in set(shoplist):
				print item
		
		
		elif choice==0:
			break
    

def zoo():
    animals = ('wolf', 'elephant', 'penguin','tigers','lion')
    
    while True:
		print '1 . Display the Animals'
		print '2 . Count How many animals'
		print '3 . Display the slice'
		print '4 . Find the Index'
		print '0 . Exit'
		
		choice=input('Enter Your Choice:')
		
		if choice==1:
			print 'Animals in zoo:'
			for animal in animals:
				print animal
		
		elif choice==2:
			print len(animals)
			
		elif choice==3:
			index1=input('Enter the starting index')
			index2=input('Enter the Ending Index')
			
			print animals[index1:index2]
			
		elif choice==4:
			animal=raw_input('Enter the Animal:')
			
			if animal in animals:
				print animals.index(animal)
		
		elif choice==0:
			break


def emails():
	
	email={'abc':'abc@domain.com','xyz':'xyz@gmail.com','pqr':'pqr@earn4post.com','lmn':'lmn@foundersplanet.com'}
	
	while True:
		print '1 . Create a Dictionary of emails'
		print '2 . Add email'
		print '3 . Display The Dictiniory'
		print '4 . modify the value'
		print '5 . delete the email'
		print '6 . Clear the Emails'
		print '0 . Exit'
		
		choice=input('Enter Your Choice:')
		
		if choice==1:
			del email[:]
			count=input('How Many element you want to shop?')
			for i in range(0,count):
				key=raw_input('Enter The name:')
				value=raw_input('Enter The Email:')
				email[key]=value
		
		elif choice==2:
			key=raw_input('Enter The name:')
			value=raw_input('Enter The Email:')
			email[key]=value
			
		elif choice==3:
			for k,v in email.items():
				print k,v
		
		elif choice==4:
			key=raw_input('Enter the name:')
						
			if key in email.keys():
				value=raw_input('Enter the Email')
				email[key]=value
			else:
				print 'No key present'
				
		elif choice==5:
			key=raw_input('Enter the Name:')
			if key in email.keys():
				del email[key]

		if choice==6:
			email.clear()
			
		if choice==0:
			break


option={1:shopping_list,2:zoo,3:emails}

while True:

	print '======================== MENU =========================='
	print '\t\t 1 . use List for shopping list'
	print '\t\t 2 . Use Tuple Animals in Zoo'
	print '\t\t 3 . Use Dictionary for Emails'
	print '\t\t 0 . Exit'
	print '========================================================'

	choice=input('Enter your Choice:')

	if choice==0:
		break

	option[choice]()
