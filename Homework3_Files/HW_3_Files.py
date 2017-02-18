import re


class Invalid_Data_Exception(Exception):
    pass

class BUYING:
    low, med, high, vhigh = range(4)


class LUG_BOOT:
    small, med, big = range(3)


class MAINT:
    low, med, high, vhigh = range(4)


class SAFTEY:
    low, med, high = range(3)


class CAR_CLASS:
    unacc, acc, good, vgood = range(4)


class Car_Data(object):
    def __init__(self, line):

        self.buying = None

        self.valid = True


        line_parsed = line.split(",")


        if(len(line_parsed) < 7):
            raise Invalid_Data_Exception( "The following record is invalid:\n" + str(line))

        self.buying = line_parsed[0]
        self.maint = line_parsed[1]
        self.doors = str(line_parsed[2])
        self.persons = str(line_parsed[3])
        self.lug_boot = line_parsed[4]
        self.saftey = line_parsed[5]
        self.car_class = line_parsed[6]

        
        if line_parsed[0] == "low":
            self.buying_sort = BUYING.low
        elif line_parsed[0] == "med":
            self.buying_sort = BUYING.med
        elif line_parsed[0] == "high":
            self.buying_sort = BUYING.high
        elif line_parsed[0] == "vhigh":
            self.buying_sort = BUYING.vhigh
        else:
            raise Invalid_Data_Exception( "The following record is invalid:\n" + str(line))

        if line_parsed[1] == "low":
            self.maint_sort = MAINT.low
        elif line_parsed[1] == "med":
            self.maint_sort = MAINT.med
        elif line_parsed[1] == "high":
            self.maint_sort = MAINT.high
        elif line_parsed[1] == "vhigh":
            self.maint_sort = MAINT.vhigh
        else:
            raise Invalid_Data_Exception( "The following record is invalid:\n" + str(line))

        self.doors_sort = str(line_parsed[2])

        self.doors = str(line_parsed[2])

        valid_doors = ["2", "3", "4", "5more"]


        if re.match("2|3|4|5more", self.doors ) == False:
            raise Invalid_Data_Exception( "The following record is invalid:\n" + str(line))

        if re.match("2|4|more", self.persons ) == False:
            raise Invalid_Data_Exception( "The following record is invalid:\n" + str(line))


        self.persons_sort = str(line_parsed[3])
        self.persons = str(line_parsed[3])



        if line_parsed[4] == "small":
            self.lug_boot_sort = LUG_BOOT.small
        elif line_parsed[4] == "med":
            self.lug_boot_sort = LUG_BOOT.med
        elif line_parsed[4] == "big":
            self.lug_boot_sort = LUG_BOOT.big
        else:
            raise Invalid_Data_Exception( "The following record is invalid:\n" + str(line))

        if line_parsed[5] == "low":
            self.saftey_sort = SAFTEY.low
        elif line_parsed[5] == "med":
            self.saftey_sort = SAFTEY.med
        elif line_parsed[5] == "high":
            self.saftey_sort = SAFTEY.high
        else:
            raise Invalid_Data_Exception( "The following record is invalid:\n" + str(line))

        if line_parsed[6] == "unacc":
            self.car_class_sort = CAR_CLASS.unacc
        elif line_parsed[6] == "acc":
            self.car_class_sort = CAR_CLASS.acc
        elif line_parsed[6] == "good":
            self.car_class_sort = CAR_CLASS.good
        elif line_parsed[6] == "vgood":
            self.car_class_sort = CAR_CLASS.vgood
        else:
            self.valid = False

        if (self.valid != True):
            raise Invalid_Data_Exception( "The following record is invalid:\n" + str(line))

    def __str__(self):
        record = self.buying
        record += ","
        record += self.maint
        record += ","
        record += self.doors
        record += ","
        record +=self.persons
        record += ","
        record += self.lug_boot
        record += ","
        record += self.saftey
        record += ","
        record += self.car_class


        return record

def sort_car_list( l,  member, asc_or_desc):

        if asc_or_desc == "desc":
            reversed = True
        else:
            reversed = False

        member += "_sort"

        return  sorted(l, key=lambda car_data: getattr(car_data, member) , reverse = reversed)


if __name__ == "__main__":

    try:

        in_file = open("car.data.txt", "r")

        car_list = []

        lines = in_file.read().splitlines()

        for line in lines:

            cd = Car_Data(line)
            car_list.append(cd)

    except Invalid_Data_Exception as error:
        print("**Error in file**")
        print(error)
        exit(1)



    car_list_q1 = sort_car_list(car_list, "saftey", asc_or_desc="asc")

    print("A) Print to the console the top 10 rows of the data sorted by 'safety' in descending order:")

    for car in car_list_q1[:10]:
        print(car)

    print("==============")
    print(" ")
    print(" " )

    print("B) Print to the console the bottom 15 rows of the data sorted by 'maint' in ascending order:")


    car_list_q2 = sort_car_list(car_list, "maint", asc_or_desc="asc")

    for car in car_list_q2[-15:]:
       print(car)

    print("==============")
    print(" ")
    print(" " )

    print("==============")
    print(" ")
    print(" " )

    print("C) Print to the console all rows that are high or vhigh in fields 'buying', 'maint', and 'safety',")
    print( "    sorted by 'doors' in ascending order:")



    car_list_q3 = []


    for car in car_list:
        if  re.match("high|vhigh",car.buying) and re.match("high|vhigh", car.saftey) \
                and re.match("high|vhigh", car.maint) :
            car_list_q3.append(car)


    car_list_q3 = sort_car_list(car_list,"doors","asc")

    for car in car_list_q3:
        print(car)

    print("==============")
    print(" ")
    print(" " )
    print("D) Save to a file all rows (in any order) that are: "
          "   'buying': vhigh, 'maint': med, 'doors': 4, and 'persons': 4 or more.")
    print("    The file path can be a hard-coded location name it output.txt")

    out_file = open("output.txt", "w")

    car_list_q4 = []

    for car in car_list:
        if  re.match("vhigh",car.buying) and re.match("4|more", car.persons) \
                and re.match("med", car.maint)  and re.match("4", car.doors) :
            out_file.write(str(car)+"\n")

    out_file.close()


