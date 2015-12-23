#masa załóżymy, że w kg :S

#################################################################################################
AU = 149597870.7 ## do skalowania jakbym robił GUI albo to wsadze w innym pliku
mercury = {"Name":"Mercury", "Mass":3.3302*10**23, "Radius":2439.7, "Dist_to_star":57909176.0}
venus = {"Name":"Venus", "Mass":4.8685*10**24, "Radius":6051.85, "Dist_to_star":108208926.0}
earth = {"Name":"Earth", "Mass":5.97219*1024, "Radius":6378.1366, "Dist_to_star":149598261.0}
mars = {"Name":"Mars", "Mass":3.3302*10**23, "Radius":3402.45, "Dist_to_star":227936637.0}
jupiter = {"Name":"Jupiter", "Mass":1.8986*10**27,"Radius":71492.0, "Dist_to_star":778412020.0}
saturn = {"Name":"Saturn", "Mass":5.6846*10**26, "Radius":60268.0, "Dist_to_star":1426725413.0}
uranus = {"Name":"Uranus", "Mass":8.6832*10**25, "Radius":25559.0, "Dist_to_star":2870972220.0}
neptune = {"Name":"Neptune", "Mass":1*0244*10**26, "Radius":24764.0, "Dist_to_star":4498252900.0}

default_planets = [mercury,venus,earth,mars,jupiter,saturn,uranus,neptune]
default_star = {"Name":"Sun","Mass": 1.98855*10**30,
                "Radius": 696342.0,"Type": "yellow dwarf"}
#################################################################################################
class Astro_object (object):
    def __init__(self,name,mass):
        self.name = name
        self.mass = mass
        
class Star (Astro_object):
    def __init__(self,star_info):
        Astro_object.__init__(self,star_info["Name"],star_info["Mass"])
        self.typ = star_info["Type"]
        self.radius = star_info["Radius"]
    def __repr__(self):
        return repr((self.name,self.mass,self.radius,self.typ))
    def __str__(self):
        return "Name of the star: %s\nMass: %.2ekg\
    \nRadius: %.2fkm\
    \nType of the star:%d\n" % (self.name,self.mass,self.radius,self.typ)
    
class Planet (Astro_object):
    def __init__(self,plnts_dict):
        Astro_object.__init__(self,plnts_dict["Name"],plnts_dict["Mass"])
        self.radius = plnts_dict["Radius"]
        self.dist_to_star = plnts_dict["Dist_to_star"]
    def __repr__(self):
        return repr({"Name":self.name, "Mass":self.mass, "Radius":self.radius, "Dist_to_star":self.dist_to_star})
    def __str__(self):
        return "Name of the planet: %s\nMass: %.2ekg\
    \nRadius: %.2fkm\
    \nDistance from the star:%fAU\n" % (self.name,self.mass,self.radius,self.dist_to_star/AU)
    @classmethod
    def mk_planet(cls,plnts_dict):
        return (Planet.__init__(self,plnts_dict))
    def __getitem__(self,str):
        return self.name
        
class Star_system:
    planets = []
    def __init__(self,name="Solar System",star_info=default_star,names_plnts=default_planets):
        self.name = name
        self.star = Star(star_info);
        for i in range(len(names_plnts)):
            temp = Planet(names_plnts[i])
            self.planets.append(temp)
    def show_planets(self):
        for i in range(len(self.planets)):
            print self.planets[i].__str__()
          
    def __repr__(self):
        return repr(self.name)
    def __str__(self):
        temp = ""
        for i in range(len(self.planets)):
            temp += self.planets[i]["Name"] + "\n"
        return "Name of the system: %s\nStar: %s\nPlanets:\n%s" % (self.name,self.star.name,temp)

if __name__ == "__main__":
    star_system = Star_system()
    print star_system
    raw_input()

