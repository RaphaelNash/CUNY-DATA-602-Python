import pandas as pd
import matplotlib.pyplot as plot
import re
import numpy as np
import pandas as pd

"""
This is assingment was "plot everything"

"""

"""
Begin code copied form Files  and linear regression Homework
"""
class BrainBody(object):
    def __init__(self, line):
        line_parsed = line.split(",")
        self.species = line_parsed[0]
        self.body = float(line_parsed[1])
        self.brain = float(line_parsed[2])

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

class PERSONS:
    two, four, five_or_more = range(3)
class DOORS:
    two, three, four, five_or_more = range(4)


class Car_Data(object):
    def __init__(self, line):

        self.buying = None

        self.valid = True


        line_parsed = line.split(",")


        if(len(line_parsed) < 7):
            raise Invalid_Data_Exception( "The following record is invalid 3:\n" + str(line))

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
            raise Invalid_Data_Exception( "The following record is invalid 2:\n" + str(line))

        if line_parsed[1] == "low":
            self.maint_sort = MAINT.low
        elif line_parsed[1] == "med":
            self.maint_sort = MAINT.med
        elif line_parsed[1] == "high":
            self.maint_sort = MAINT.high
        elif line_parsed[1] == "vhigh":
            self.maint_sort = MAINT.vhigh
        else:
            raise Invalid_Data_Exception( "The following record is invalid 1 :\n" + str(line))

        self.doors_sort = str(line_parsed[2])

        self.doors = str(line_parsed[2])

        if line_parsed[3] == "2":
            self.doors_sort = DOORS.two
        elif line_parsed[3] == "3":
            self.doors_sort = DOORS.three
        elif line_parsed[3] == "4":
            self.doors_sort = DOORS.four
        elif line_parsed[3] == "more":
            self.doors_sort = DOORS.five_or_more
        else:
            raise Invalid_Data_Exception( "The following record is invalid 4: "  +  line_parsed[3] + "\n" + str(line))

        valid_doors = ["2", "3", "4", "5more"]


        if re.match("2|3|4|5more", self.doors ) == False:
            raise Invalid_Data_Exception( "The following record is invalid: " + line_parsed[3] + "\n" + str(line))

        if re.match("2|4|more", self.persons ) == False:
            raise Invalid_Data_Exception( "The following record is invalid:\n" + str(line))

        if line_parsed[3] == "2":
            self.persons_sort = PERSONS.two
        elif line_parsed[3] == "4":
            self.persons_sort = PERSONS.four
        elif line_parsed[3] == "more":
            self.persons_sort = PERSONS.five_or_more
        else:
            raise Invalid_Data_Exception( "The following record is invalid:\n" + str(line))



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


"""
Plot Car Data from HW 2

    """


in_file = open("car.data.txt", "r")

car_list = []

lines = in_file.read().splitlines()

for line in lines:
    cd = Car_Data(line)
    car_list.append(cd)

in_file.close()


"""
end code copied from files and linear regression homework
"""

"""
Various histograms of the cars data
"""
plot.figure(1)
plot.subplot(221)

maint_cat  = ["low", "med", "high", "vhigh"]
maint_freq = [0,0,0,0]

saftey_cat = ["low", "med", "high"]
saftey_freq = [0,0,0]

doors_cat = ["2", "3", "4", "5 or more"]
doors_freq = [0,0,0,0]

persons_cat = ["2",  "4", "5 or more"]
persons_freq = [0,0,0]

buying_cat = ["low",  "med", "high", "vhigh"]
buying_freq = [0,0,0,0]




for cd in car_list:
    maint_freq[cd.maint_sort] += 1
    saftey_freq[cd.saftey_sort] += 1
    persons_freq[cd.persons_sort] +=1
    doors_freq[cd.doors_sort] += 1
    buying_freq[cd.buying_sort] +=1

plot.subplot(221)
plot.bar(  range(maint_freq.__len__()) , maint_freq)
plot.xticks(range(maint_freq.__len__()), maint_cat)
plot.title('Maintence')
plot.ylabel('Number of Cars')

plot.subplot(222)
plot.bar(  range(buying_freq.__len__()) , buying_freq)
plot.xticks(range(buying_freq.__len__()), buying_cat)
plot.title('Buying ')
plot.ylabel('Number of Cars')



plot.subplot(223)
plot.bar(  range(saftey_freq.__len__()) , saftey_freq)
plot.xticks(range(saftey_freq.__len__()), saftey_cat)
plot.title('Saftey ')
plot.ylabel('Number of Cars')


plot.subplot(224)
plot.bar(  range(doors_freq.__len__()) , maint_freq)
plot.xticks(range(doors_freq.__len__()), doors_cat)
plot.title('Doors ')
plot.ylabel('Number of Cars')




plot.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

"""
Plot data points from brain/body linear regression homework with the linear regression line
"""
plot.figure(2)


brain_body_list = []
in_file = open("brainandbody.csv", "r")
lines = in_file.read().splitlines()

body = []
brain = []

for line in lines:
    if line[:1] != ",":         #ignore first row as it is just a header
        brain_body_item = BrainBody(line)
        brain_body_list.append(brain_body_item)
        body.append(brain_body_item.body)
        brain.append(brain_body_item.brain)

in_file.close()


plot.scatter( body, brain )
plot.xlabel("Body Mass")
plot.ylabel( "Brain Mass")

axes = plot.gca()
m, b = np.polyfit(brain, body, 1)
X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
plot.plot(X_plot, m*X_plot + b, 'r')

plot.show()

"""
Plot center points of objects from the image processing homework
"""

plot.figure(3)

im = plot.imread("objects.png")
plot.imshow(im)
plot.scatter([509,181,409,159,419,266,93,171], [73,159,148,310,371,293,399,437], color = "red")

plot.show()

"""
Plot histogram of webvists by hour from the log processing homework.
"""
plot.figure(4)

hour = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
visits = [684,434,399,248,347,374,303,846,1994,3096,3209,3820,3827,4391,4716,4284,4042,2793,1820,1493,1310,1015,1117,1186]


plot.plot(visits, 'bo-')
plot.xticks(range(24))
plot.title("Visit by Hour of the Day")
plot.xlabel("Hour")
plot.ylabel("# of Visits")
plot.show()


