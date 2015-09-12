if __name__ == '__main__':
    while True:
        reply = raw_input('Enter text:')
        if reply == 'stop': break
        print 'Hello! ' + reply.upper()
    print 'Bye' 