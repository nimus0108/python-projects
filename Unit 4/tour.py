import urllib.request
from datetime import datetime

class Tour (object):
    
    def __init__(self):
        '''
            Constructor
            '''
        self.dest_list = []
        self.__cached = False
        self.__cached_distance = -1

    def __str__(self):
        out_str = ""
        for name in self.dest_list:
            out_str += name + ";"

        return out_str

    def __gt__(self, right):
        return (self.distance() > right.distance())

    def __lt__(self, right):
        return (self.distance() < right.distance())

    def __eq__(self, right):
        return self.distance() == right.distance()

    def __add__(self, right):
        new_tour = Tour()
        new_tour.dest_list += self.dest_list
        new_tour.dest_list += right.dest_list

        return new_tour

    def __setitem__(self, index, value):
        self.dest_list[index] = value
        self.__cached = False

    def __getitem__(self, index):
        return self.dest_list[index]

    def get_distance (self, from_city, to_city):
        # Replace the spaces with plus signs for the URL
        from_city = from_city.replace(" " , "+")
        to_city = to_city.replace(" " , "+")
        
        # Create and send the HTTP request
        request_str = "http://maps.googleapis.com/maps/api/distancematrix/json?origins=" + from_city
        request_str += "&destinations=" + to_city + "&mode=driving&sensor=false"
        web_obj = urllib.request.urlopen(request_str)
        results_str = str(web_obj.read())
        
        pos = results_str.find("value")
        results_str = results_str[pos+9:]

        pos = results_str.find("\\")
        results_str = results_str[:pos]

        web_obj.close()
        return int(results_str)
    
    
    def add_destination (self, dest):
        self.dest_list.append(dest)
    
    def distance (self):
        if (self.__cached):
            print("Cache hit")
            return self.__cached_distance

        dist = 0
        for i in range(1, len(self.dest_list)):
            dist += self.get_distance(self.dest_list[i - 1], self.dest_list[i])

        self.__cached_distance = dist
        self.__cached = True
        return dist

def main():
    start_time = datetime.now()
    print("Start time: ", start_time)
    t1 = Tour()
    print(t1.distance())

    t1 = Tour ()
    t1.add_destination ("New York NY")
    t1.add_destination ("Albany NY")
    t1.add_destination ("Rochester NY")
    t1.add_destination("West Pal Beach FL")
    print ("Tour 1: " + str(t1))
    print ("Tour 1 distance = " + str (t1.distance()))

    t1[2] = "Harrisburg PA"
    print ("Tour 1: " + str(t1))
    print ("Tour 1 distance = " + str (t1.distance()))

    t2 = Tour ()
    t2.add_destination ("Boston MA")
    t2.add_destination ("Trenton NJ")

    print ("Tour 2: " + str(t2))
    print ("Tour 2 distance = " + str (t2.distance()))

    if (t1 > t2):
        print("t1 is farther.")

    print("Less than = " , t1 < t2)
    print("Equal to = ", t1==t2)
    t3 = t1 + t2
    print ("Tour 3: " + str(t3))
    print ("Tour 3 distance = " + str (t3.distance()))

    end_time = datetime.now()
    print("Endtime: ", end_time)
    print("Runtime: ", end_time - start_time)

main()

# Notepad is love, notepad is life. Yes Su Min. Yes