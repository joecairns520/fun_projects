# A 3-dimensional vector class to be used in the development of
# computer simulations of various physical systems.
#
# 
# The 3-dimensional vector represents a standard cartesian vector
# given by <b> xi + yj +zk</b> where <b>i</b>, <b>j</b>, and <b>k</b> are unit
# vectors in the x, y, and z direction respectively. 
#
# This code is developed from the original java script from Iain A. Bertram
# @author Joseph Cairns
# @version 1.0

import numpy as np

class PhysicsVector:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    # Method to return a string of the vector in the xi + yj + zk format
    def return_string(self):
        return str(self.x)+'i + '+str(self.y)+'j + '+str(self.z)+'k'
    
    # Method to return a simple string of the vector in the form x y z separated by spaces
    def return_simple_string(self):
        return str(self.x)+' '+str(self.y)+' '+str(self.z)
    
    # Method to return the vector as a list in the form [x,y,z]
    def return_list(self):
        return [self.x,self.y,self.z]
    
    # Method that prints the string in the xi + yj + zk format
    def print_vector(self):
        print(str(self.x)+'i + '+str(self.y)+'j + '+str(self.z)+'k')
    
    # Method that sets the x component of the vector to a particular value    
    def set_x(self, x):
        self.x = x
        
    # Method that sets the y component of the vector to a particular value    
    def set_y(self, y):
        self.y = y
        
    # Method that sets the z component of the vector to a particular value    
    def set_z(self, z):
        self.z = z
        
    # Method that returns the x component of the vector    
    def get_x(self):
        return self.x
        
    # Method that returns the y component of the vector    
    def get_y(self):
        return self.y
        
    # Method that returns the z component of the vector    
    def get_z(self):
        return self.z
    
    # Method that sets the x, y and z components of the vector to particular values    
    def set_vector(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    # Method that increases the desired vector by another vector    
    def increase_by(self, vector):
        self.x = self.x + vector.x
        self.y = self.y + vector.y
        self.z = self.z + vector.z
    
    # Method that decreases the desired vector by another vector    
    def decrease_by(self, vector):
        self.x = self.x - vector.x
        self.y = self.y - vector.y
        self.z = self.z - vector.z
    
    # Method that scales the vector by a scalar
    def scale_by(self, scalar):
        self.x = self.x * scalar
        self.y = self.y * scalar
        self.z = self.z * scalar
    
    # Method that scales a given vector by a scalar    
    def scale(u, scalar):
        x = u.x * scalar
        y = u.y * scalar
        z = u.z * scalar
        return PhysicsVector(x, y, z)
        
    # Method that calculates the unit vector of the given vector (i.e. same direction
    # but with magnitude scaled to 1)
    def get_unit_vector(self):
        mag = self.magnitude()
        vector = PhysicsVector(self.x, self.y, self.z)
        vector.scale_by(1./mag)
        return vector
    
    # Method that calculates the magnitude of a vector
    def magnitude(self):
        return np.sqrt(PhysicsVector.dot(self,self))
        
    # Method that returns the dot product of two vectors
    def dot(u, v):
        return (u.x * v.x) + (u.y * v.y) + (u.z * v.z)
    
    # Method that returns the cross product of two vectors
    def cross(u, v):
        a = u.y*v.z - u.z*v.y
        b = u.x*v.z - u.z*v.x
        c = u.x*v.y - u.y*v.x
        return PhysicsVector(a,b,c)
    
    # Method that returns the addition of two vectors
    def add(u, v):
        x = u.x + v.x
        y = u.y + v.y
        z = u.z + v.z
        return PhysicsVector(x, y, z)
    
    # Method that returns the subtraction of two vectors
    def subtract(u, v):
        x = u.x - v.x
        y = u.y - v.y
        z = u.z - v.z
        return PhysicsVector(x, y, z)
        
    
    
    
        
        
        
        
    