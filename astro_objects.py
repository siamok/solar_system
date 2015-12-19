#masa załóżymy, że w kg :S

#############################################################
AU = 149597870.7 ## do skalowania jakbym robił GUI albo to wsadze w innym pliku
mercury = ["Mercury", 3.3302*10**23, 2439.7, 57909176.0]
venus = ["Venus", 4.8685*10**24, 6051.85, 108208926.0]
earth = ["Earth", 5.97219*1024, 6378.1366, 149598261.0]
mars = ["Mars", 3.3302*10**23, 3402.45, 227936637.0]
jupiter = ["Jupiter", 1.8986*10**27,71492.0, 778412020.0]
saturn = ["Saturn", 5.6846*10**26, 60268.0, 1426725413.0]
uranus = ["Uranus", 8.6832*10**25, 25559.0, 2870972220.0]
neptune = ["Neptune", 1*0244*10**26, 24764.0, 4498252900.0]
#default_planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
##default_planets = {"Mercury": mercury,"Venus":venus,"Earth":earth,
##                   "Mars":mars,"Jupiter":jupiter,"Saturn":saturn,
##                   "Uranus":uranus,"Neptune":neptune } #NIE JEST PO KOLEI!
default_planets = [mercury,venus,earth,mars,jupiter,saturn,uranus,neptune]


class Star_system (object):
    def __init__(self,name="Solar system",mass=0):
        self.name = name
        
        
        
        
class Star (Star_system):
    planets = []
    def __init__(self,name = "Slonce" , mass=1.98855*10**30,
                 radius = 696342.0,typ = "yellow",no_of_plnts=8,
                 names_plnts=default_planets):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.no_of_plnts = no_of_plnts
        for i in range(no_of_plnts):
            self.planets.append(Planet.mk_planet(names_plnts[i]))
            
    def __repr__(self):
        return repr((self.name,self.mass,self.radius,self.no_of_plnts))
    def __str__(self):
        return "Nazwa gwiazdy: %s\nMasa: %.2ekg\
    \nPromien: %.2fkm\
    \nLiczba planet:%d\n" % (self.name,self.mass,self.radius,self.no_of_plnts)
    def show_planets(self):
        for i in range(self.no_of_plnts):
            print self.planets[i]
        
class Planet (Star_system):
    def __init__(self,name,mass,radius,dist_from_star):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.dist_from_star = dist_from_star
    def __str__(self):
        return "Nazwa planety: %s\nMasa: %.2ekg\
    \nPromien: %.2fkm\
    \nOdleglosc od gwiazdy:%fAU\n" % (self.name,self.mass,self.radius,self.dist_from_star/AU)
        
    @classmethod
    def mk_planet(cls,lista):
        return Planet(lista[0],lista[1],lista[2],lista[3])
            
        
##class Moon (Astrom_object):
##    def __init__(self,name,mass,radius,dist_from_planet):
##        pass


if __name__ == "__main__":
    print ["name","mass","radius","no_of_plnts"]
    Sun=Star()
    print Sun
