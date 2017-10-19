#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 16:41:32 2016

@author: artipengoriya
"""

from cluster import *
from pylab import *

class dbscanner:
    
    dataSet = []
    count = 0
    visited = []
    member = []
    Clusters = []
    
    def dbscan(D,eps,MinPts):
        dataSet = D
        
        C = -1
        Noise = None
        
        for i in D:
            if i not in visited:
                visited.append(point)
                NeighbourPoints = _regionQuery(point,eps)
                
                if len(NeighbourPoints) < MinPts:
                    Noise.addPoint(point)
                else:
                    name = 'Cluster'+str(count);
                    C = cluster(name)
                    count+=1;
                    expandCluster(point,NeighbourPoints,C,eps,MinPts)
                    
     
    
    def expandCluster(point,NeighbourPoints,C,eps,MinPts):
        
        C.addPoint(point)
        
        for p in NeighbourPoints:
            if p not in visited:
                visited.append(p)
                np = _regionQuery(p,eps)
                if len(np) >= MinPts:
                    for n in np:
                        if n not in NeighbourPoints:
                            NeighbourPoints.append(n)
                    
            for c in Clusters:
                if not c.has(p):
                    if not C.has(p):
                        C.addPoint(p)
                        
            if len(Clusters) == 0:
                if not C.has(p):
                    C.addPoint(p)
                        
        Clusters.append(C)
        
       
        
                    
                
                     
    def _regionQuery(point,eps):
        result = []
        for d in dataSet:
            if (((d[0]-point[0])**2 + (d[1] - point[1])**2)**0.5)<=eps:
                result.append(d)
        return result
        
        
        dbscan(points,0.3,10)