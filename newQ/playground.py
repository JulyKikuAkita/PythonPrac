__author__ = 'July'

# Explanantion: python is neither both pass by value nor pass by ref
# In Python a variable is not an alias for a location in memory. Rather, it is simply a binding to a Python object.
'''
"call-by-object," or "call-by-object-reference" is a more accurate way of describing it.
In Python, (almost) everything is an object. What we commonly refer to as "variables" in Python are more properly called names.
Likewise, "assignment" is really the binding of a name to an object.
Each binding has a scope that defines its visibility, usually the block in which the name originates.
'''
# explanation: http://stupidpythonideas.blogspot.com/2013/11/does-python-pass-by-value-or-by.html
# java: http://www.programcreek.com/2013/09/string-is-passed-by-reference-in-java/
class playGround:
    def printS(self):
        x = "123"
        self.change(x)
        print x
        self.swap("x", "y")

        ham = [0]
        self.spam(ham)
        print(ham)


    def change(self, s):
        s = "456"

    def swap(self, x, y):
        print "({},{})".format(x, y)
        tmp = x
        x = y
        y = tmp
        print "({},{})".format(x, y)

    def spam(self, eggs):
        eggs.append(1)
        eggs = [2, 3]


class Twitch:
    def split(self, s, deli):
        # s: string
        # deli: a list of string as deliminator

        res = []
        cur = ""
        for d in deli:
            cur += s.split(d)[0]
            cur += " "
            s = s.split(d)[1]
            print cur, s
        if s:
            cur += s
        res.append("".join(cur))
        return res

if __name__ == "__main__":
    s = "abcdefg"
    deli = ["c", "ef"]
    cur = Twitch()
    print cur.split(s, deli)

    #playGround().printS()
    #print chr(ord('1')+ 1)