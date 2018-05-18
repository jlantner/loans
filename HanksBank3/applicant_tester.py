import user 

from views import application
from user import user 

#print(user().Hello_world())\
print (__name__)



def main():
	Jared=user()
	return (application(Jared,"Jared","Lantner",18,"Summit","RIT", "Stevens", "Drexel", "Engineering",200000000000))
if __name__=='__main__':
	print (main())