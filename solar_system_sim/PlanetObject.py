#
# A Class which creates an object that is to be used a planet in the simulation of
# the solar system.
#
# @author Joseph Cairns
# @version 1.0

import numpy as np
from PhysicsVector import PhysicsVector
from constants import c

class Planet:
    
    def __init__(self, mass, radius, velocity, position, name):
        self.mass = mass
        self.radius = radius
        self.velocity = velocity
        self.position = position
        self.name = name
    
    # Method used to set the mass of a planet
    def set_mass(self, mass):
        self.mass = mass
        
    # Method used to set the radius of a planet
    def set_radius(self, radius):
        self.radius = radius
        
    # Method used to set the velocity of a planet
    def set_velocity(self, velocity):
        self.velocity = velocity
        
    # Method used to set the position of a planet
    def set_position(self, position):
        self.position = position
        
    # Method used to set the name of a planet
    def set_name(self, name):
        self.name = name
        
    # Method used to get the mass of a planet
    def get_mass(self):
        return self.mass
        
    # Method used to get the radius of a planet
    def get_radius(self):
        return self.radius
        
    # Method used to get the velocity of a planet
    def get_velocity(self):
        return self.velocity
        
    # Method used to get the position of a planet
    def get_position(self):
        return self.position
        
    # Method used to get the name of a planet
    def get_name(self):
        return self.name
    
    # Method to return the gravitational acceleration on the surface of a planet
    def surface_g(self):
        return (c.G*self.mass)/self.radius**2.
    
    # Method that returns the magnitude of the gravitational force between two planets
    def grav_force_mag(p1, p2):
        r = (PhysicsVector.subtract(p1.position, p2.position)).magnitude()
        return (c.G * p1.mass * p2.mass)/(r**2.)
    
    # Method that returns the vector of the gravitational force that a planet feels due to another planet
    def grav_force_vector(self, planet):
        r = PhysicsVector.subtract(self.position,planet.position)
        vector = r.get_unit_vector()
        vector.scale_by(-Planet.grav_force_mag(self, planet))
        return vector

    # Method that uses the Euler-Cramer algorithm to calculate the new position and velocity of a planet
    # after a time step t_step based on the gravitatinal influence of a list of N other planets
    def update(self, t_step, planets):
        grav_vectors = []
        for planet in planets:
            if not planet.get_name() == self.name:
                grav_vectors.append(self.grav_force_vector(planet))
                #print(self.grav_force_vector(planet).return_string())
        total_grav_vector = PhysicsVector(0.,0.,0.)
        for grav_vector in grav_vectors:
            total_grav_vector.increase_by(grav_vector)
            
            
        # Divide by mass to get acceleration    
        total_grav_vector.scale_by(1./self.mass)
        # Multiply by the time step to apply Euler-Cromer algorithm
        total_grav_vector.scale_by(t_step)
        self.velocity.increase_by(total_grav_vector)
        
        pos_next = PhysicsVector.scale(self.velocity, t_step)
        self.position.increase_by(pos_next)
        
            
        
            
        
        
    
        
        
    
    
    
        
        
