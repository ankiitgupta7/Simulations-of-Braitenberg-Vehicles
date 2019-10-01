#import vehicle_tools
#tool = vehicle_tools.tools()
#c=tool.coordinates
#def run():
#   print(test.fun2())

#def x():
#    run()

#t= testo()
#t.x()
#x()

x=0

class A():
    def foo():
        global x
        x+=5
        print(x)
    foo()
