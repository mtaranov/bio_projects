#!/usr/bin/env python

"""
 Assignment:  run_tests_HW4.py
 YOUR NAME:  __________________ 
 CS 190/295  Winter 2012

 This is a template file for your homework assignment.  There are several
 functions defined below, each with instructions for you to make modifications.
 
 For some of these, you may need to do some on-your-own learning.  Google is your friend!
"""


"""
Any changes to this file WILL NOT BE SAVED.  You can modify it for testing, but
please make sure the ORIGINAL file works!  If it doesn't you'll get docked!

each test_problem is set up to test various aspects of your code.  You need to
fix your code so that none of the assertions given below will fail.
"""

from HW4 import *

def test_problem1a():
    print "Problem1a: Testing Point.distance_to: "
    pt1 = Point(3,5)
    pt2 = Point(5,6)
    assert pt1.distance_to(pt1) == 0  # distance from point to itself should be 0
    assert pt1.distance_to(pt2) == 2.23606797749979


def test_problem1b():
    print "Problem1b: Testing Point.closest_point: "
    pt1 = Point(3,5)
    pt2 = Point(5,6)
    pt3 = Point(10,12)
    assert pt1.closest_point([pt1, pt2]) == 0  # pt1 is closest to itself
    assert pt1.closest_point([pt2, pt3]) == 0  # pt1 is closest to pt2
    assert pt3.closest_point([pt1, pt2]) == 1  # pt3 is closest to pt2

def test_problem1c():
    print "Problem1b: Testing Point.distance_to_origin: "
    pt1 = Point(0,0)
    pt2 = Point(0,1)
    pt3 = Point(1,1)
    assert pt1.distance_to_origin() == 0
    assert pt2.distance_to_origin() == 1
    assert pt3.distance_to_origin() == 1.4142135623730951
    

def test_problem2a():
    print 'Problem2a: testing initialize_clusters'
    # create a new clustering of 4 data points, using K = 2
    pt1 = Point(3,5)
    pt2 = Point(5,6)
    pt3 = Point(10,12)
    pt4 = Point(11,13)
    kmeans = KMeansCluster(2, [pt1, pt2, pt3, pt4])
    assert isinstance(kmeans.clusters, dict)  # make sure they're using the prescribed datatype
    assert len(kmeans.clusters) == 2  # make sure there are the right number of clusters
    assert all(len(c) > 0 for c in kmeans.clusters.values()) # make sure every cluster has at least one element
    assert sum(len(c) for c in kmeans.clusters.values()) == 4 # make sure every datapoint is used

def test_problem2b():
    print 'Problem 2b: testing initialize_centroids'
    pt1 = Point(3,5)
    pt2 = Point(5,6)
    pt3 = Point(10,12)
    pt4 = Point(11,13)
    pt5 = Point(11,14)
    kmeans = KMeansCluster(2, [pt1, pt2, pt3, pt4, pt5])
    assert len(kmeans.centroids) == 2  # make sure you got the right number of centroids
    assert all(isinstance(c, Point) for c in kmeans.centroids)  # make sure you're using Point's inside
    assert isinstance(kmeans.centroids, list)  # make sure cluster indices are set up properly 

def test_problem2c():
    print 'Problem 2c: testing get_nearest_centroid_for_point'
    pt1 = Point(3,5)
    pt2 = Point(5,6)
    pt3 = Point(10,12)
    pt4 = Point(11,13)
    pt5 = Point(11,14)
    kmeans = KMeansCluster(2, [pt1, pt2, pt3, pt4, pt5])
    kmeans.centroids = [pt1, pt4]
    assert kmeans.get_nearest_centroid_for_point(pt1) == 0  # pt1 should be closest to itself
    assert kmeans.get_nearest_centroid_for_point(pt2) == 0  # pt2 should be closest to pt1
    assert kmeans.get_nearest_centroid_for_point(pt3) == 1  # pt3 should be closest to pt4

def test_problem2d():
    print 'Problem 2d: testing assign_all_data_to_nearest_centroids'
    pt1 = Point(3,5)
    pt2 = Point(5,6)
    pt3 = Point(10,12)
    pt4 = Point(11,13)
    pt5 = Point(11,14)
    kmeans = KMeansCluster(2, [pt1, pt2, pt3, pt5])
    kmeans.centroids = [pt1, pt4]
    kmeans.assign_all_data_to_nearest_centroids()
    assert pt1 in kmeans.clusters[0]  # pt1 closest to pt1
    assert pt2 in kmeans.clusters[0]  # pt2 closest to pt1
    assert pt3 in kmeans.clusters[1]  # pt3 closest to pt4
    assert pt5 in kmeans.clusters[1]  # pt5 closest to pt4

def test_problem2e():
    print 'Problem 2e: testing update_centroid_positions'
    pt1 = Point(3,5)
    pt2 = Point(5,6)
    pt3 = Point(10,12)
    pt4 = Point(11,13)
    pt5 = Point(11,14)
    kmeans = KMeansCluster(2, [pt1, pt2, pt3, pt5])
    kmeans.clusters = {0 : [pt1, pt2], 1 : [pt3, pt5]}
    kmeans.update_centroid_positions()
    assert kmeans.centroids[0].x == 4
    assert kmeans.centroids[0].y == 5.5
    assert kmeans.centroids[1].x == 10.5
    assert kmeans.centroids[1].y == 13

def test_problem2f():
    print 'Problem 2f: testing get_mean_of_points'
    pt1 = Point(3,5)
    pt2 = Point(5,6)
    pt3 = Point(10,12)
    pt4 = Point(11,13)
    pt5 = Point(11,14)
    kmeans = KMeansCluster(2, [pt1, pt2, pt3, pt5])
    mean_point = kmeans.get_mean_of_points([pt1, pt2])
    assert mean_point.x == 4
    assert mean_point.y == 5.5
    mean_point = kmeans.get_mean_of_points([pt3, pt4, pt5])
    assert round(mean_point.x, 4) == 10.6667
    assert mean_point.y == 13

def test_problem3():
    print 'Problem 3: testing read_points_from_file'
    filename = 'testme.txt'
    with open(filename, 'w') as outfile:
        outfile.write('50\t60\n20\t30')
    points = read_points_from_file(filename)
    assert points[0].x == 50
    assert points[0].y == 60
    assert points[1].x == 20
    assert points[1].y == 30

def brownie_point_extra_coolness():
    """This function tests the complete KMeans classification algorithm and
    plots intermediate steps.  For this brownie point, get you code completely
    working and upload your killer plots to EEE Dropbox.  You can play around
    with the data generation and especially the number of clusters.
    """
    print 'testing K means clustering on some overlapping gaussians'
    import scipy
    from matplotlib import pyplot
    
    # generate some data from several different gaussians
    data = [Point(x,y) for x,y in scipy.random.normal([[0,2]] * 800, .5)]
    data.extend([Point(x,y) for x,y in scipy.random.normal([[2,2]] * 800, .5)])
    data.extend([Point(x,y) for x,y in scipy.random.normal([[1,0]] * 300, .5)])
    data.extend([Point(x,y) for x,y in scipy.random.normal([[1.4,.2]] * 300, .5)])
    data.extend([Point(x,y) for x,y in scipy.random.normal([[.6,.2]] * 300, .5)])
    
    # initialize
    num_clusters = 10
    kmeans = KMeansCluster(num_clusters, data)
    for i in range(10):
        # cluster
        print 'iteration', i
        kmeans.iterate()
        
        # plot
        pyplot.figure()
        for k in range(num_clusters):
            # draw the clusters in different colors
            xs, ys = zip(*[(p.x,p.y) for p in kmeans.clusters[k]])
            pyplot.plot(xs, ys, 'o', label='cluster %s' % k)
            pyplot.plot(kmeans.centroids[k].x, kmeans.centroids[k].y, 'k+', lw=3)
        #pyplot.legend()
        pyplot.savefig('kmeans_iteration_%s.png' % i)
        

def main():
    test_problem1a()
    test_problem1b()
    test_problem1c()
    test_problem2a()
    test_problem2b()
    test_problem2c()
    test_problem2d()
    test_problem2e()
    test_problem2f()
    test_problem3()
    brownie_point_extra_coolness()
    

main()

