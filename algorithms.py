import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from math import acos,sqrt,pi

class Algorithms:
    def __init__(self):
        pass
    
    def point_on_vertex (self, q:QPointF, p:QPointF):
        # Checks if points p and q have identical coordinates
        if q.x() == p.x() and q.y() == p.y():
            return True
        else:
            return False
        
    def calculate_angle(self, q:QPointF, p1:QPointF, p2:QPointF):
        # Calculates angle defined by 3 points
        
        # Vector computattion
        v1x = p1.x() - q.x()
        v1y = p1.y() - q.y()
        v2x = p2.x() - q.x()
        v2y = p2.y() - q.y()
        
        # Vector norm computation
        norm_v1 = sqrt(v1x**2 + v1y**2)
        norm_v2 = sqrt(v2x**2 + v2y**2)
        
        # Dot product of two vectors
        scalar = v1x*v2x + v1y*v2y
        
        # Angle computation
        if norm_v1 == 0 or norm_v2 == 0:
            # Avoid division by zero
            return 0
        else:
            arg = scalar/(norm_v1*norm_v2)
            if arg <= 1 and arg >= -1:
                angle = acos(scalar/(norm_v1*norm_v2))
            elif arg > 1:   
                angle = acos(1)
            else:
                angle = acos(-1)
            
            return angle
        
    def get_point_location(self, q:QPointF, p1:QPointF, p2:QPointF):
        # Calculate determinant for half-plane test
        det = (p2.x() - p1.x())*(q.y() - p1.y()) - (p2.y() - p1.y())*(q.x() - p1.x())
        return det
        
    def ray_crossing(self, q:QPointF, pol:QPolygonF):
        # Analyze point and polygon position using ray crossing algorithm
        
        # Initialize ammont of intersections
        kl = 0 
        kr = 0
        
        # Number of polygon vertices
        n = len(pol)
        
        # Process all points
        for i in range(n): 
            
            #Get i-th point
            p1x = pol[i].x() - q.x()
            p1y = pol[i].y() - q.y()
            
            #Get (i+1)st point
            p2x = pol[(i+1)%n].x() - q.x()
            p2y = pol[(i+1)%n].y() - q.y()
            
            # Point is on vertex
            if p1x == 0 and p1y == 0:
                return -1
            
            # The ray goes trough both vertices of the edge, skip
            if (p2y - p1y) == 0:
                continue
            
            # Compute intersection x coordinate
            xm = (p2x*p1y - p1x*p2y)/(p2y-p1y)
            
            # Lower segment
            if (p2y < 0) != (p1y < 0):
                if xm < 0:
                    kl += 1
                    
            # Upper segment        
            if (p2y > 0) != (p1y > 0):
                if xm > 0:
                    kr += 1
                    
        # Point is on the edge
        if (kl % 2) != (kr % 2):
            return -1

        # Point is inside
        if kr % 2 == 1:
            return 1
        
        # Point is inside
        return 0    
    
    def winding_number(self, q:QPointF, pol:QPolygonF):
        # Analyze point and polygon position using winding number algorithm
        
        # Initialize Wnding Number Omega
        omega_sum = 0
        
        # Small variance to compare floating point number
        e = 1e-9
        
        # Number of vertices
        n = len(pol)
        
        # Process all points
        for i in range(n):
            this_point = pol[i]
            if i == (n-1):
                next_point = pol[0]
            else:
                next_point = pol[i+1]
            
            if self.point_on_vertex(q,this_point):
                # Check if point is identical with the vertex
                return -1
            
            # Half-plane test
            det = self.get_point_location(q,this_point,next_point)
            
            # Calulate angle omega
            omega = self.calculate_angle(q,this_point,next_point)
            
            
            if det == 0:
                # Check if point lies on the edge
                if omega <= pi + e and omega >= pi - e:
                    return -1
                else:
                    # Point is not on the edge and omega is 0
                    continue
            
            # Left half-plane
            if det > 0:
                omega_sum+=omega
                
            # Right half-plane    
            else:
                omega_sum-=omega
            
        if abs(omega_sum) <= 2*pi+e and abs(omega_sum) >= 2*pi-e:
            # Point is inside
            return 1 
        # Point is outside
        return 0 
            
    def in_min_max_box (self, q:QPointF, pol:QPolygonF):
        # Checks if a point is inside a min-max box
        
        # Create lists of x and y coordinates
        xs = [point.x() for point in pol]
        ys = [point.y() for point in pol]
        
        # Min/max x coordinates
        x_min = min(xs)
        x_max = max(xs)
        
        # Min/max y coordinates
        y_min = min(ys)
        y_max = max(ys)
        
        if q.x() <= x_max and q.x() >= x_min and q.y() <= y_max and q.y() >= y_min:
            # Point is inside a min-max box
            return 1
        else:
            # Point is outside a min-max box
            return 0        