#decorator function


def decorator_f(func):
    def wrapper_f(*args,**kwargs):
        print(f"start")
        result=func(*args,**kwargs)
        print(f"end")
        return result
    return wrapper_f

@decorator_f
def myMessage():
    print("This is an example function")

myMessage()

print("*****************************")

def authentication(func):
    def wrapper(user,*args,**kwargs):
        if not user.get("auth",False):
            print("Authorization failed!")
            return
        return func(user,*args,**kwargs)
    return wrapper



@authentication
def view_account(user):
    print(f"Welcome, {user['name']}")
    
user1={"name":"Enes YEL", "auth":True}

view_account(user1)

print("*****************************")

def flexible_decorator(func):
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        print(f"Fonksiyonun adı:{func.__name__}")
        if(args):
            print(f"Konumsal argümanlar",end=":") # alt alta yazdırmak için.
            for i,item in enumerate(args):
                print(item,end=" ")
        if(kwargs):
            print(f"Anahtar-değer argümanlar:{kwargs}")
        return result
    return wrapper


@flexible_decorator
def add(x,y):
    return x+y

add(3,4)