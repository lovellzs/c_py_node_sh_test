import traceback
from twisted.internet import reactor

def stack():
    print 'The python stack:'
    traceback.print_stack()


reactor.callWhenRunning(stack)
reactor.run()

# def main():
#     print 111
#
# if __name__ == '__main__':
#     main()