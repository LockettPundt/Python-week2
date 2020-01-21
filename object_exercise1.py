


class Person:

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.people_greeted = []
        self.greeting_count = 0
         
         

    def greet(self, other_person):
        self.greeting_count += 1
        print('Hello {}, I am {}!\n'.format(other_person.name, self.name))
        if other_person not in self.people_greeted:
          self.people_greeted.append(other_person)
        

    def contact_info(self):
        print("{}'s contact info is:\n{}\n{}\n".format(self.name, self.email, self.phone))
    
    def friend_list(self):
        print("{} is friends with: {}\n".format(self.name, self.friends))

    def add_friend(self, name):
        return self.friends.append(name)

    def num_friends(self):
        print("{} has {} friends.\n".format(self.name, len(self.friends)))
    
    def __str__(self):
        return "Hi, I'm {}. My email is: {}. My phone number is: {}\n".format(self.name, self.email, self.phone)
    
    def num_unique_people_greeted(self): 
        #bonus method that add unique greets to an array
        #and return the number of unique people greeted
        if len(self.people_greeted) == 1:
          return "{} has met {} unique person.\n".format(self.name, len(self.people_greeted))
        else:
          return "{} has met {} unique people.\n".format(self.name, len(self.people_greeted))
        

        



sonny = Person("Sonny", "sonny@hotmail.com" , "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3465")
#the __str__ method is called when you print objects name.
print(jordan)
print(sonny)
print(jordan.num_unique_people_greeted())
sonny.greet(jordan)
jordan.greet(sonny)
sonny.contact_info()
jordan.contact_info()
print(jordan.num_unique_people_greeted())
sonny.friends.append(jordan.name)
jordan.friends.append(sonny.name)
jordan.friends.append("Madonna")
jordan.add_friend("Willheim")
jordan.num_friends()
sonny.friend_list()
jordan.friend_list()
print(jordan.greeting_count)
jordan.greet(sonny)
print(jordan.greeting_count)
jordan.greet(sonny)
jordan.greet(sonny)
jordan.greet(sonny)
print(jordan.greeting_count)
print(jordan.num_unique_people_greeted())


