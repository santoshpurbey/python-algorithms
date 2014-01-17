#### Python OOP Review ####



# Fraction class
class Fraction(object):
    # Construtor which tells what data we need to create an object
    def __init__(self, top, bottom):
        # Self is a formal parameter that is used to reference the object
        # Self must always be the first parameter in Class methods + attributes
        self.num = top
        self.den = bottom

    # Returns a string representation of the object
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    # Override default add method in Python
    def __add__(self, otherfraction):
        new_den = self.den * otherfraction.den
        new_num = (self.num * otherfraction.den) + (otherfraction.num * self.den)
        return Fraction(new_num, new_den).lowestTerms()

    # Reduce fraction to lowest terms
    def lowestTerms(self):
        i = 1
        GCD = 1
        while i < min(self.num,self.den):
            if self.num % i == 0 and self.den % i == 0:
                GCD = i
            i += 1
        return Fraction(self.num / GCD, self.den / GCD)

    def __eq__(self,otherfraction):
        first_num = self.num * otherfraction.den
        second_num = otherfraction.num * self.den
        return first_num == second_num




# Python multiplication function
def multiply(a,b):
    sum = 0
    i = 0
    while i < b:
        sum += a
        i += 1
    return sum

#print multiply(5,6) 


def division(num,den):
    count = 0
    while num * count < den:
        count += 1
    if num * count > den:
        return count - 1
    return count


#print division(4,21)


def subtraction(a,b):
    count = 0
    if b < a:
        while b < a:
            count += 1
            b += 1
        return count
    else:
        while a < b:
            count += 1
            a += 1
        return int('-'+str(count))


#print subtraction(30,12)
#print subtraction(30,32)


# Parent class of a digital circuit
class LogicGate:
    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    # Calls a function here only defined by its Child classes
    def getOutput(self):
        # Writing a method that does not exist yet
        self.output = self.performGateLogic()
        return self.output
        

# Child class of LogicGate that holds AND and OR classes
class BinaryGate(LogicGate):
    def __init__(self, n):
        # Instantiate relationship with Parent Class
        LogicGate.__init__(self,n)

        # Instantiate child-only attributes
        self.pinA = None
        self.pinB = None

    # Ask user to provide label for each Pin (1 or 0)
    def getPinA(self):
        return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))

    def getPinB(self):
        return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))


# Child class of BinaryGate that holds AND gate
class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)
        
    def performGateLogic(self):
        # You can call functions from the parent class directly
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

# Child class of Binary Gate that holds OR gate
class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 or b==1:
            return 1
        else:
            return 0
    
ag = AndGate("A1")
og = OrGate("O1")
print ag.getOutput()
print og.getOutput()


# Child class of LogicGate that holds NOT class
class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self, n)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))

    

# Child class of UnaryGate that holds NOT class
class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)
    
    def performGateLogic(self, result):
        if result == 1:
            return 0
        else:
            return 1

ng = NotGate("N1")
print ng.performGateLogic(ag.getOutput())


