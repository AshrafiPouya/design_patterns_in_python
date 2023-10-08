#this is singleton class

class SingletonClass(object):
	# we check here if the class has an instance attribute named 'instance' if it doesn't, we create one
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(SingletonClass, cls).__new__(cls)
		return cls.instance

singleton = SingletonClass()
new_singleton = SingletonClass()

print(singleton is new_singleton)

singleton.singl_variable = "Singleton Variable"
print(new_singleton.singl_variable)



# here we see singleton subclass shares the same state:
class SingletonClass(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(SingletonClass, cls).__new__(cls)
    return cls.instance
   
class SingletonChild(SingletonClass):
    pass
   
singleton = SingletonClass()  
child = SingletonChild()
print(child is singleton)
 
singleton.singl_variable = "Singleton Variable"
print(child.singl_variable)


#singleton borg
class BorgSingleton(object):
  _shared_borg_state = {}
   
  def __new__(cls, *args, **kwargs):
    obj = super(BorgSingleton, cls).__new__(cls, *args, **kwargs)
    obj.__dict__ = cls._shared_borg_state
    return obj
   
borg = BorgSingleton()
borg.shared_variable = "Shared Variable"
 
class ChildBorg(BorgSingleton):
  pass
 
childBorg = ChildBorg()
print(childBorg is borg)
print(childBorg.shared_variable)