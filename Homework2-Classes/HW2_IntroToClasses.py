# 1. fill in this class
#   it will need to provide for what happens below in the
#	main, so you will at least need a constructor that takes the values as (Brand, Price, Safety Rating),
# 	a function called showEvaluation, and an attribute carCount
class CarEvaluation:
    'A simple class that represents a car evaluation'

    carCount = 0

    def __init__(self, brand, price, safteyRating):
        self.price = price
        self.brand = brand
        self.safteyRating = safteyRating
        self.__class__.carCount += 1

    def showEvaluation(self):
        print "The", self.brand, "has a", self.price, "price and its safety is rated a", self.safteyRating

    # 2. fill in this function
    #   it takes a list of CarEvaluation objects for input and either "asc" or "des"
    #   if it gets "asc" return a list of car names order by ascending price
    # 	otherwise by descending price
def sortbyprice(L, order):
    high = []
    medium = []
    low = []
    finalOrder = []
    for i in L:
        if i.price == "High":
            high.append(i)
        elif i.price == "Med":
            medium.append(i)
        else:
            low.append(i)
    if order == "asc":
        for i in low:
            finalOrder.append(i.brand)
        for i in medium:
            finalOrder.append(i.brand)
        for i in high:
            finalOrder.append(i.brand)
    else:
        for i in high:
            finalOrder.append(i.brand)
        for i in medium:
            finalOrder.append(i.brand)
        for i in low:
            finalOrder.append(i.brand)

    return finalOrder



# 3. fill in this function
#   it takes a list for input of CarEvaluation objects and a value to search for
#	it returns true if the value is in the safety  attribute of an entry on the list,
#   otherwise false
def searchforsafety(L, safetyRating):

    for i in L:
        if ( i.safteyRating) == safetyRating:
            return True

    return False


# This is the main of the program.  Expected outputs are in comments after the function calls.



if __name__ == "__main__":
    eval1 = CarEvaluation("Ford", "High", 2)
    eval2 = CarEvaluation("GMC", "Med", 4)
    eval3 = CarEvaluation("Toyota", "Low", 3)

    print "Car Count = %d" % CarEvaluation.carCount  # Car Count = 3

    eval1.showEvaluation()  # The Ford has a High price and it's safety is rated a 2
    eval2.showEvaluation()  # The GMC has a Med price and it's safety is rated a 4
    eval3.showEvaluation()  # The Toyota has a Low price and it's safety is rated a 3

    L = [eval1, eval2, eval3]
    print sortbyprice(L, "asc");  # [Toyota, GMC, Ford]
    print sortbyprice(L, "des"); #[Ford, GMC, Toyota]
    print searchforsafety(L, 2); #true
    print searchforsafety(L, 1); #false
