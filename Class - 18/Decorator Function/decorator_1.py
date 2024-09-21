def login_required(func):
    def inner(name,is_login):
        if is_login == False:
            print('Login Is Required')
        else :
            func(name,is_login)
    return inner

def home_page(name,is_login):
    print('Home Page')

def about_page(name,is_login):
    print('About Page')
@login_required
def order_page(name,is_login):
    print('Order Page')

home_page('Aathi',False)
about_page('Aathi',False)
order_page('Aathi',False)
