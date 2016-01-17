# masa w kg!


#################################################################################################
AU = 149597870.7  ## do skalowania jakbym robil GUI albo to wsadze w innym pliku
mercury = {"Name": "Mercury", "Mass": 3.3302 * 10 ** 23, "Radius": 2439.7, "Dist_to_star": 57909176.0}
venus = {"Name": "Venus", "Mass": 4.8685 * 10 ** 24, "Radius": 6051.85, "Dist_to_star": 108208926.0}
earth = {"Name": "Earth", "Mass": 5.97219 * 10 ** 24, "Radius": 6378.1366, "Dist_to_star": 149598261.0}
mars = {"Name": "Mars", "Mass": 3.3302 * 10 ** 23, "Radius": 3402.45, "Dist_to_star": 227936637.0}
jupiter = {"Name": "Jupiter", "Mass": 1.8986 * 10 ** 27, "Radius": 71492.0, "Dist_to_star": 778412020.0}
saturn = {"Name": "Saturn", "Mass": 5.6846 * 10 ** 26, "Radius": 60268.0, "Dist_to_star": 1426725413.0}
uranus = {"Name": "Uranus", "Mass": 8.6832 * 10 ** 25, "Radius": 25559.0, "Dist_to_star": 2870972220.0}
neptune = {"Name": "Neptune", "Mass": 1 * 0244 * 10 ** 26, "Radius": 24764.0, "Dist_to_star": 4498252900.0}

default_planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
default_star = {"Name": "Sun", "Mass": 1.98855 * 10 ** 30,
                "Radius": 696342.0, "Color": "yellow"}


#################################################################################################
class Astro_object(object):
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass


#################################################################################################
class Star(Astro_object):
    def __init__(self, star_info):
        Astro_object.__init__(self, star_info["Name"], star_info["Mass"])
        self.color = star_info["Color"]
        self.radius = star_info["Radius"]

    def __repr__(self):
        return repr((self.name, self.mass, self.radius, self.color))

    def __str__(self):
        return "Name of the star: %s\nMass: %.2ekg\
    \nRadius: %.2fkm\
    \nColor of the star:%s\n" % (self.name, self.mass, self.radius, self.color)


#################################################################################################
class Planets(Astro_object):
    def __init__(self, plnts_dict):
        Astro_object.__init__(self, plnts_dict["Name"], plnts_dict["Mass"])
        self.radius = plnts_dict["Radius"]
        self.dist_to_star = plnts_dict["Dist_to_star"]

    def __repr__(self):
        return repr({"Name": self.name, "Mass": self.mass, "Radius": self.radius, "Dist_to_star": self.dist_to_star})

    def __str__(self):
        return "Name of the planet: %s\nMass: %.2ekg\
    \nRadius: %.2fkm\
    \nDistance from the star:%fAU\n" % (self.name, self.mass, self.radius, self.dist_to_star / AU)

    @classmethod
    def mk_planet(cls, plnts_dict):
        return Planets.__init__(plnts_dict)

    def __getitem__(self, key):
        if not isinstance(key, str):
            raise TypeError()
        if not key.lower() in dir(self):  # czy jest taki obiekt w tej klasie
            raise KeyError()
        return getattr(self, key.lower())


#################################################################################################
class Star_system:
    planets = []

    def __init__(self, name="Solar System", star_info=default_star, names_plnts=default_planets):
        self.name = name
        self.star = Star(star_info)
        for i in range(len(names_plnts)):
            temp = Planets(names_plnts[i])
            self.planets.append(temp)

    def show_planets(self):
        for i in range(len(self.planets)):
            print self.planets[i].__str__()

    def __getitem__(self, index):
        if index == 0:
            return self.star
        else:
            return self.planets[index-1]

    def __del__(self):
        print "You monster! You have just destroyed your Star System!"
        del self

    def __repr__(self):
        return repr(self.name)

    def __str__(self):
        temp = ""
        for i in range(len(self.planets)):
            temp += self.planets[i]["Name"] + "\n"
        return "Name of the system: %s\nStar: %s\nPlanets:\n%s" % (self.name, self.star.name, temp)

    class Decorator(object):
        def __init__(self, what):
            if what == "size":
                self.what = "Size of the system "
                self.units = " AU"
            elif what == "mass":
                self.what = "System weights "
                self.units = " kg"
            elif what == "":
                pass
            else:
                raise TypeError()

        def __call__(self, funk):
            def _i_(cls):
                test = funk(cls)
                print self.what, test, self.units
                _i_.__name__ = funk.__name__
                _i_.__doc__ = funk.__doc__
            return _i_

    def list_of_planets(self):
        #names = [self.planets[i]["Name"] for i in range(self.planets.__len__())]    # list compr jest czytelniejsze, ale...
        names = map(lambda x: self.planets[x]["Name"], range(self.planets.__len__()))# <- nice :D trzy pieczenie na jednym ogniu
        return names

    @Decorator("mass")
    def mass_of_system(self):
        mass = 0
        for j in range(self.planets.__len__()):
            mass += self.planets[j]["Mass"]
        return mass

    @Decorator("size")
    def size(self):
        return self.planets[-1]["Dist_to_star"]

    ##
    def max_gen(self):
        def prize(what):
            if not isinstance(what, str):
                raise TypeError()
            temp = 0
            for i in range(self.planets.__len__()):
                if self.planets[i][what] > temp:
                    try:
                        temp = self.planets[i][what]
                    except KeyError:
                        print "dupa"
            return temp
        return prize

#################################################################################################

#######################################################
if __name__ == "__main__":

    star_system = Star_system()
    print star_system
    planet = Planets(mercury)
    print planet
    star_system.mass_of_system()
    star_system.size()
    print
    print star_system[0]

    u = star_system.list_of_planets()
    print u
    print
    temp = star_system.max_gen()("Mass")
    print "%.2ekg" % temp
    del star_system
