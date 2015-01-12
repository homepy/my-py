# The try ... except statement has an optional else clause, which, when present, 
# must follow all except clauses. 
# It is useful for code that must be executed
# if the try clause does not raise an exception. For example:

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
        
# The use of the else clause is better
# than adding additional code to the try clause
# because it avoids accidentally catching an exception
# that wasn’t raised by the code being protected by the try ... except statement.


