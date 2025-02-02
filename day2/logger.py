def logger(func):
    def wrapper():
        print(f"Someone called {func.__name__} ")
        func()
        print(f" {func.__name__} is excecuted successfully ")
    return wrapper
#--------------------------------------------------


@logger()
def processData():
    print("connecting to db")
    print("data processed")

processData()