'''
Working with Decorators

Challenge 3, MAKE A DECORATOR AS U WANT!
'''
import webbrowser as wb

def myFirstDecorator(myfunction):
    def inside_function(*args):
        print("Let's, open the browser bro")
        myfunction(*args)
    return inside_function



#Web's list
mikes_websites = ['Facebook', 'Google', 'Youtube', 'Github']



@myFirstDecorator
def open_web(websites):
    for _ in websites:
        print(f"I just opened { _ }")
        for np in range(2):
            wb.open("http://" + _ + ".com")



open_web(mikes_websites)
