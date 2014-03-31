"""
 Assignment:  HW4.py
 YOUR NAME: Maryna Taranova __________________ 
 CS 190/295  Winter 2012

 This is a template file for your homework assignment.  There are several
 functions defined below, each with instructions for you to make modifications.
 
 * Write your name in the space above
 * Modify this file and save your changes
 * Submit the final version on the EEE Dropbox
 
 For some of these, you may need to do some on-your-own learning.  Google is your friend!
"""


"""
This homework follows a similar structure to the previous homework.  You are
allowed to make changes to this file, but NOT to the run_tests_HW4.py file.

This homework is probably tougher than previous homeworks, but don't stress!
The code doesn't have to actually work for you to get credit. Meaning you may have a lot
of bugs but as long as you pass the assert tests from run_tests_HW4.py, you'll be fine.
Plus, there is plenty of room here for partial credit.

Just go through the run_tests_HW4.py file and implement what's needed one by one.

And again, you should ONLY turn in HW4.py (and maybe some plots if you're super-cool)
"""

class Point():
    """A Point is a single point in 2 dimensional space"""
    def __init__(self, new_x, new_y):
        """Create a new point at coordinates (new_x, new_y)
        NOTE: this function is already implemented.  Nothing more to do :)
        """
        self.x = float(new_x)
        self.y = float(new_y)
    
    def __str__(self):
        """This lets you convert points into a pretty string use the str() function.
        So now you can type:
            print 'here is a point', Point(3,2)
        And it won't print junk.
            
        You don't need to change this function :)
        """
        return '(%s, %s)' % (self.x, self.y)

    def __repr__(self):
        """More extras for pretty-printing.  This function applies when the Point
        is inside a list or other object.
        
        You don't need to change this function :)
        """
        return '(%s, %s)' % (self.x, self.y)

    
    def distance_to(self, other_point):
        """TODO: Return the distance from this point to other_point.
        HINT: You'll need to use self.x and self.y, as well as
              other_point.x and other_point.y
        """
        return ((self.x-other_point.x)**2+(self.y-other_point.y)**2)**.5   
        
    
    def closest_point(self, list_of_other_points):
        """TODO: Return the INDEX of the point that is closest to me (NOT the distance)
        HINT: for each point in the list, use self.distance_to()
        """
        list=[]
        for i in list_of_other_points:
            list.append(self.distance_to(i))
        return list.index(min(list))
           
    
    def distance_to_origin(self):
        """TODO: Return the distance from this point to the origin, i.e.,
        from this point to (0,0).
        """
        origin = Point(0,0)
        return ((self.x-origin.x)**2+(self.y-origin.y)**2)**.5


class KMeansCluster():
    """This is a class that will cluster your data. Clustering helps us summarize
    data, showing similarities between data points.
    """
    def __init__(self, new_K, new_data_points):
        """Create a new clusterer with new_K clusters, using new_data_points
        NOTE: you don't need to touch this function.  It's already done :)
        """
        if new_K > len(new_data_points):
            raise ValueError("K (%s) cannot be larger than the number of datapoints (%s)!" % (new_K, new_data_points))
        self.K = new_K
        self.initialize_clusters(new_data_points)
        self.initialize_centroids()
        self.assign_all_data_to_nearest_centroids()

    
    def iterate(self):
        """Go through one iteration of k-means clustering.
        You don't need to change this function.  It's already done.
        """
        self.update_centroid_positions()
        self.assign_all_data_to_nearest_centroids()

    
    def initialize_clusters(self, new_data_points):
        """TODO: create a dictionary whose keys are from 0 to K and whose values
        are a list of Points (the class Point) assigned to each cluster.
        
        You may initialize the clusters any way you like, so long as each datapoint
        goes into one cluster, and each cluster has at least one datapoint.
        
        self.clusters should look something like {0 : [Point(.5, .5), Point(.6,4))],
                                                  1 : [Point(3, 3)]}
            in this example, there are 2 clusters.  Cluster 0 has 2 datapoints
            assigned to it, while cluster 1 has a datapoint assigned to it.
        """
        #self.clusters = {}  # TODO: fill in this dictionary
        
                 
        n=len(new_data_points)/self.K # avereage number of points per cluster
        m=len(new_data_points)%self.K
        if m==0:
            self.clusters=dict([(i, new_data_points[0+n*i:n+n*i]) for i in range(self.K)]) 
        else:
            self.clusters=dict([(i, new_data_points[0+n*i:n+n*i]) for i in range(self.K)])     
            for reminder in range(m):            
                self.clusters.get(self.K-1).append(new_data_points[n+n*(self.K-2):][reminder-1])
        return self.clusters      
  
    
    def initialize_centroids(self):
        """TODO: create a list of K points representing the cluster centers.
        
        You can initialize the x and y values of these points however you like,
        but make sure that each cluster will recieve at least one datapoint.
        
        For K=2, self.centroids should look something like [Point(0,0), Point(1,1)]
        """
        # TODO: initialize centroids with some points from self.clusters
        
        self.centroids = []
        for i in range(self.K):
            self.centroids.append(self.clusters.values()[i][0])
        return self.centroids
        
        
        
    def get_nearest_centroid_for_point(self, other_point):
        """TODO: Return the INDEX of the centroid that is closest to other_point
        HINT: if you've implemented the closest_point method in the Point class,
              you can reuse that function here, just passing self.centroids as
              the argument.
        """
        return other_point.closest_point(self.centroids) 
    
    
    def assign_all_data_to_nearest_centroids(self):
        """TODO: For each datapoint, assign the point to its nearest centroid
        by modifying which list the datapoint is a part of in self.clusters.
        """
#        print self.clusters
        for j in range(self.K):
#            print self.clusters.values()[j]
            for i in self.clusters.values()[j]:
#                print i,i.closest_point(self.centroids)
                if i.closest_point(self.centroids) != j: 
                    self.clusters.values()[i.closest_point(self.centroids)].append(i)
                    self.clusters.values()[j].remove(i)
            
        return self.clusters    


    def update_centroid_positions(self):
        """TODO: for each centroid, update the centroid's location to the
        mean of the points that belong to this centroid's cluster
        
        HINT: if you implement get_mean_of_points, you can use it here.
        Just pass in the points that belong to this cluster.
        """
        self.centroids=[]
        for j in range(self.K):      
            self.centroids.append(self.get_mean_of_points(self.clusters.values()[j]))
#        print self.centroids
    
    def get_mean_of_points(self, list_of_points):
        """TODO: calculate the mean of the list of points.  Return a new Point
        whose x and y are the respective mean values.
        
        NOTE: you'll need to calculate the mean of the x component separately
              from the mean of the y component.
        """
#        mean_point = Point(0,0)
        
        # do something to calculate the mean of the points in list_of_points
        
        sum1=0
        sum2=0
        for point in list_of_points:
            sum1=sum1+point.x 
        point.x_mean = sum1/len(list_of_points)
      
        for point in list_of_points:
            sum2=sum2+point.y 
        point.y_mean = sum2/len(list_of_points)
 
        mean_point=Point(point.x_mean, point.y_mean)
        return mean_point



def read_points_from_file(filename):
    """Last but not least, read in a set of datapoints from a file and create
    a list of points.  The file will be formatted like this:
    
50<TAB>40
20<TAB>11
7<TAB>12
60<TAB>46

    """
    all_points = []
    
    # TODO: read in the file...
    import string
    file = open(filename,"r")
    text = file.readlines()
    file.close()
    for line in text:
        x = int(line.split('\t')[0])
        y = int(line.split('\t')[1])
        all_points.append(Point(x,y))
    return all_points
