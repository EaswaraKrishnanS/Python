def change_case(func):
    def inner(name):
        return "HI " + name.upper()
    return inner

@change_case

def display(name):
    return(name)

print(display("Aathithya"))
print(display("Siva balan"))