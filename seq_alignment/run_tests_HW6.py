#!/usr/bin/env python

import os
import gzip
import random

from HW6 import ReadMapper, load_reads_from_file, load_reference_from_file

def problem1a():
    print 'testing ReadMapper.sliding_window with window_length 3...',
    reference = 'AAATTTGGGCCC'
    mapper = ReadMapper(reference, 3)
    actual = mapper.sliding_window(reference, 3)
    expected = ['AAA', 'AAT', 'ATT', 'TTT', 'TTG', 'TGG', 'GGG', 'GGC', 'GCC', 'CCC']
    if actual != expected:
        print "FAILED! expected\n%s\nbut got\n%s" % (expected, actual)
    else:
        print 'PASSED!'

def problem1b():
    print 'testing ReadMapper.sliding_window with window_length 5...',
    reference = 'AAATTTGGGCCC'
    mapper = ReadMapper(reference, 5)
    actual = mapper.sliding_window(reference, 5)
    expected = ['AAATT', 'AATTT', 'ATTTG', 'TTTGG', 'TTGGG', 'TGGGC', 'GGGCC', 'GGCCC']
    if actual != expected:
        print "FAILED! expected\n%s\nbut got\n%s" % (expected, actual)
    else:
        print 'PASSED!'

def problem1bb():
    print 'making sure ReadMapper.sliding_window doesnt report the N character...',
    reference = 'AAATTNGGGCCC'
    mapper = ReadMapper(reference, 3)
    actual = mapper.sliding_window(reference, 3)
    expected = ['AAA', 'AAT', 'ATT', None, None, None, 'GGG', 'GGC', 'GCC', 'CCC']
    if actual != expected:
        print "FAILED! expected\n%s\nbut got\n%s" % (expected, actual)
    else:
        print 'PASSED!'

def problem1bc():
    print 'making sure ReadMapper.sliding_window reports in all upper-case characters...',
    reference = 'AaAtttGGgCcc'
    mapper = ReadMapper(reference, 3)
    actual = mapper.sliding_window(reference, 3)
    expected = ['AAA', 'AAT', 'ATT', 'TTT', 'TTG', 'TGG', 'GGG', 'GGC', 'GCC', 'CCC']
    if actual != expected:
        print "FAILED! expected\n%s\nbut got\n%s" % (expected, actual)
    else:
        print 'PASSED!'

def problem1c():
    print 'testing ReadMapper.build_index with seed_length 2...',
    reference = 'AAATTTGGG'
    mapper = ReadMapper(reference, 2)
    print mapper.build_index('AAATTTGGG', 2)
    actual = mapper.build_index('AAATTTGGG', 2)
    expected = {'AA':[0,1], 'AT':[2], 'TT':[3,4], 'TG':[5], 'GG':[6,7]}

    if actual != expected:
        print 'FAILED! expected\n%s\nbut got \n%s' % (expected, actual)
    else:
        print 'PASSED!'
    
def problem1d():
    print 'testing ReadMapper.build_index with seed_length 3...',
    reference = 'AAATTTGGG'
    mapper = ReadMapper(reference, 3)
    actual = mapper.build_index('AAATTTGGG', 3)
    expected = {'AAA':[0], 'AAT':[1], 'ATT':[2], 'TTT':[3], 'TTG':[4], 'TGG':[5], 'GGG':[6]}
    if actual != expected:
        print 'FAILED! expected\n%s\nbut got \n%s' % (expected, actual)
    else:
        print 'PASSED!'

def problem1dd():
    print 'testing ReadMapper.build_index with seed_length 3 with an N character...',
    reference = 'AAATTNGGG'
    mapper = ReadMapper(reference, 3)
    actual = mapper.build_index('AAATTNGGG', 3)
    expected = {'AAA':[0], 'AAT':[1], 'ATT':[2], 'GGG':[6]}
    if actual != expected:
        print 'FAILED! expected\n%s\nbut got \n%s' % (expected, actual)
    else:
        print 'PASSED!'

def problem1e():
    print 'testing ReadMapper.__init__...',
    reference = 'AAATTTGGG'
    mapper = ReadMapper(reference, 3)
    expected_refindex = {'AAA':[0], 'AAT':[1], 'ATT':[2], 'TTT':[3], 'TTG':[4], 'TGG':[5], 'GGG':[6]}
    if mapper.seed_length != 3:
        print 'FAILED! mapper.seed_length is %s instead of 3' % mapper.seed_length
    elif mapper.reference != reference:
        print 'FAILED! mapper.reference is %s instead of %s' % (mapper.reference, reference)
    elif mapper.ref_index != expected_refindex:
        print 'FAILED! mapper.ref_index is %s instead of %s' % (mapper.ref_index, expected_refindex)
    else:
        print 'PASSED!'


def problem1f():
    print 'testing ReadMapper.get_candidate_starts with seed_length 3...',
    reference = 'AAATTTGGGCCC'
    mapper = ReadMapper(reference, 3)
    actual = mapper.get_candidate_starts('AAAAAA')
    expected = [0]
    if actual != expected:
        print 'FAILED! expected\n%s\nbut got \n%s' % (expected, actual)
    else:
        print 'PASSED!'    
    

def problem1g():
    print 'testing ReadMapper.get_candidate_starts with seed_length 2...',
    reference = 'AAATTTGGGCCC'
    mapper = ReadMapper(reference, 2)
    actual = mapper.get_candidate_starts('AAAAAA')
    expected = [0,1]
    if actual != expected:
        print 'FAILED! expected\n%s\nbut got \n%s' % (expected, actual)
    else:
        print 'PASSED!'    

def problem1h():
    print 'testing ReadMapper.get_candidate_starts with seed_length 2 and no matching seed...',
    reference = 'AAATTTGGGCCC'
    mapper = ReadMapper(reference, 2)
    actual = mapper.get_candidate_starts('GTAGTA')
    expected = []
    if actual != expected:
        print 'FAILED! expected\n%s\nbut got \n%s' % (expected, actual)
    else:
        print 'PASSED!'    


def problem1i():
    print 'testing ReadMapper.score_candidate with seed_length 2, perfect match',
    reference = 'AAATTTGGGCCC'
    mapper = ReadMapper(reference, 2)
    actual = mapper.score_candidate('TTGGGCC', 4)  # perfect match
    expected = 0
    if actual != expected:
        print 'FAILED! expected\n%s\nbut got \n%s' % (expected, actual)
    else:
        print 'PASSED!'

def problem1j():
    print 'testing ReadMapper.score_candidate with seed_length 2, one mismatch',
    reference = 'AAATTTGGGCCC'
    mapper = ReadMapper(reference, 2)
    actual = mapper.score_candidate('TTGGACC', 4)  # A mismatches
    expected = 1
    if actual != expected:
        print 'FAILED! expected\n%s\nbut got \n%s' % (expected, actual)
    else:
        print 'PASSED!'

def problem1k():
    print 'testing ReadMapper.score_candidate with seed_length 2, two mismatches',
    reference = 'AAATTTGGGCCC'
    mapper = ReadMapper(reference, 2)
    actual = mapper.score_candidate('TTGGACG', 4)  # A and G mismatch
    expected = 2
    if actual != expected:
        print 'FAILED! expected\n%s\nbut got \n%s' % (expected, actual)
    else:
        print 'PASSED!'

def problem1l():
    print 'testing ReadMapper.best_mapping with seed_length 2 and 2 candidate mappings...',
    reference = 'AAATTTGGGCCC'
    mapper = ReadMapper(reference, 2)
    actual = mapper.best_mapping('AAAATT')
    expected = (0,1)  # best to align at 0, with 1 mismatch... better than 1 with 3 mismatches
    if actual != expected:
        print 'FAILED! expected\n%s\nbut got \n%s' % (expected, actual)
    else:
        print 'PASSED!'

def problem1m():
    print 'testing ReadMapper.best_mapping with seed_length 2 and 2 candidate mappings...',
    reference = 'AAATTTGGGCCC'
    mapper = ReadMapper(reference, 2)
    actual = mapper.best_mapping('TTGGGCC')
    expected = (4,0)  # best to align at 4, with 0 mismatches... better than aligning at 3
    if actual != expected:
        print 'FAILED! expected\n%s\nbut got \n%s' % (expected, actual)
    else:
        print 'PASSED!'

def problem1n():
    print 'testing ReadMapper.best_mapping with seed_length 2 and no matching seed...',
    reference = 'AAATTTGGGCCC'
    mapper = ReadMapper(reference, 2)
    actual = mapper.best_mapping('GTAGTA')
    expected = (None, float('inf'))
    if actual != expected:
        print 'FAILED! expected\n%s\nbut got \n%s' % (expected, actual)
    else:
        print 'PASSED!'

def problem1o():
    print 'testing ReadMapper.map_reads with seed_length 2 and several reads...',
    reference = 'AAATTTGGGCCC'
    mapper = ReadMapper(reference, 2)
    actual = mapper.map_reads(['AAAATT', 'TTGGGCC', 'GTAGTA'])
    expected = [(0,1), (4,0), (None, float('inf'))]
    if actual != expected:
        print 'FAILED! expected\n%s\nbut got \n%s' % (expected, actual)
    else:
        print 'PASSED!'

def problem2a():
    print 'testing ReadMapper.load_reads_from_file with a regular file...',
    expected = ''.join(random.sample('ATGC', 1)[0] for i in range(30)) 
    outfile = open('test_reads.txt', 'w')
    outfile.write(expected)
    outfile.close()
    actual = load_reads_from_file('test_reads.txt')
    if [expected] == actual:
        print 'PASSED!'
    else:
        print 'FAILED! Expected:\n%s\nbut got\n%s' % (repr(expected), repr(actual))

def problem2b():
    print 'testing ReadMapper.load_reads_from_file with a zipped file...',
    expected = ''.join(random.sample('ATGC', 1)[0] for i in range(30)) 
    outfile = gzip.open('test_reads.txt.gz', 'w')
    outfile.write(expected)
    outfile.close()
    actual = load_reads_from_file('test_reads.txt.gz')
    if [expected] == actual:
        print 'PASSED!'
    else:
        print 'FAILED! Expected:\n%s\nbut got\n%s' % (repr(expected), repr(actual))


def problem2c():
    print 'testing ReadMapper.load_reference_from_file with a regular file...',
    expected = ''.join(random.sample('ATGC', 1)[0] for i in range(30))
    outfile = open('test_reference.txt', 'w')
    outfile.write(expected)
    outfile.close()
    actual = load_reference_from_file('test_reference.txt')
    if expected == actual:
        print 'PASSED!'
    else:
        print 'FAILED! Expected:\n%s\nbut got\n%s' % (repr(expected), repr(actual))

def problem2d():
    print 'testing ReadMapper.load_reference_from_file with a zipped file...',
    expected = ''.join(random.sample('ATGC', 1)[0] for i in range(30)) 
    outfile = gzip.open('test_reference.txt.gz', 'w')
    outfile.write(expected)
    outfile.close()
    actual = load_reference_from_file('test_reference.txt.gz')
    if expected == actual:
        print 'PASSED!'
    else:
        print 'FAILED! Expected:\n%s\nbut got\n%s' % (repr(expected), repr(actual))
#    print actual, expected

def problem2e():
    print 'testing entire ReadMapper on a real dataset...',
#    reference = load_reference_from_file('chr21_trimmed.fa.gz')
    reference = load_reference_from_file('chr21_trimmed_small.fa.gz')
    reads = load_reads_from_file('real_reads_verysmall.txt.gz')
#    reads = load_reads_from_file('real_reads_test.txt.gz')
    mapper = ReadMapper(reference, 11)
#    mapper = ReadMapper(reference, 11)
#    print map(str, mapper.map_reads(reads))
#    print mapper.map_reads(['GCTCAATACAAAAAATATGATATGATTTTGTGGTGGGACAACTGTGGGACA'])
    print mapper.map_reads(reads)
#    actual = map(str, mapper.map_reads(reads))
#    expected = gzip.open('real_reads.results.txt.gz')
#    for index, expected_line in enumerate(expected):
#        if expected_line.rstrip() != actual[index].rstrip():
#            expected_start = int(expected_line.split(',')[0][1:])
#            ref_sequence = reference[expected_start : expected_start + len(reads[index])]
#            print 'FAILED! on line %r...\nreference: %r\nread     : %r\nexpected\n%r\nbut got\n%r' % (index, ref_sequence, reads[index], expected_line, actual[index])
#            break
#    else:
#        print 'PASSED!'


def problem2f():
    print 'EXTRA CREDIT pt1: testing ReadMapper edit distance...',
    reference = 'AGCATGCATCGTA' 'TTTT' 'AAAACCCTTTAACTTATTAGGCGATTGACG'
    read =      'AGCATGCATCGTA'        'AAAACCCTTT'  # deletion of 4 T's
    mapper = ReadMapper(reference, 11, method='edit')
    actual = mapper.score_candidate(read, 0)
    expected = 8
    if actual != expected:
        print 'FAILED! expected %s but got %s' % (expected, actual)
    else:
        print 'PASSED!'


def problem2g():
    print 'EXTRA CREDIT pt1: testing entire ReadMapper on a real dataset using edit distance...',
    reference = load_reference_from_file('chr21_trimmed.fa.gz')
    reads = load_reads_from_file('real_reads.txt.gz')
    mapper = ReadMapper(reference, 11, method='edit')
    actual = map(str, mapper.map_reads(reads))
    expected = gzip.open('real_reads.results_edit.txt.gz')
    for index, expected_line in enumerate(expected):
        if expected_line.rstrip() != actual[index].rstrip():
            expected_start = int(expected_line.split(',')[0][1:])
            ref_sequence = reference[expected_start : expected_start + len(reads[index])]
            print 'FAILED! on line %r...\nreference: %r\nread     : %r\nexpected\n%r\nbut got\n%r' % (index, ref_sequence, reads[index], expected_line, actual[index])
            break
    else:
        print 'PASSED!'

def problem2h():
    print 'EXTRA CREDIT pt2: testing ReadMapper free-suffix edit distance...',
    reference = 'AGCATGCATCGTA' 'TTTT' 'AAAACCCTTTAACTTATTAGGCGATTGACG'
    read =      'AGCATGCATCGTA'        'AAAACCCTTT'  # deletion of 4 T's
    mapper = ReadMapper(reference, 11, method='edit_freesuffix')
    actual = mapper.score_candidate(read, 0)
    expected = 4
    if actual != expected:
        print 'FAILED! expected %s but got %s' % (expected, actual)
    else:
        print 'PASSED!'

def problem2i():
    print 'EXTRA CREDIT pt2: testing ReadMapper free-suffix edit distance with short reference',
    read = 'AGCATGCATCGTA' 'TTTT' 'AAAACCCTTTAACTTATTAGGCGATTGACG'
    reference  =      'AGCATGCATCGTA'        'AAAACCCTTT'  # deletion of 4 T's
    mapper = ReadMapper(reference, 11, method='edit_freesuffix')
    actual = mapper.score_candidate(read, 0)
    expected = 4
    if actual != expected:
        print 'FAILED! expected %s but got %s' % (expected, actual)
    else:
        print 'PASSED!'

def problem2j():
    print 'EXTRA CREDIT pt2: testing entire ReadMapper on a real dataset using free-suffix edit distance...',
    reference = load_reference_from_file('chr21_trimmed.fa.gz')
    reads = load_reads_from_file('real_reads.txt.gz')
    mapper = ReadMapper(reference, 11, method='edit_freesuffix')
    actual = map(str, mapper.map_reads(reads))
    expected = gzip.open('real_reads.results_freesuffix.txt.gz')
    for index, expected_line in enumerate(expected):
        if expected_line.rstrip() != actual[index].rstrip():
            expected_start = int(expected_line.split(',')[0][1:])
            ref_sequence = reference[expected_start : expected_start + len(reads[index])]
            print 'FAILED! on line %r...\nreference: %r\nread     : %r\nexpected\n%r\nbut got\n%r' % (index, ref_sequence, reads[index], expected_line, actual[index])
            break
    else:
        print 'PASSED!'



if __name__ == '__main__':
    problem1a()
    print '\n\n*** Be sure to uncomment the other tests when you are ready to run them! ***'
    problem1b()
    problem1bb()
    problem1bc()
    problem1c()
    problem1d()
    problem1dd()
    problem1e()
    problem1f()
    problem1g()
    problem1h()
    problem1i()
    problem1j()
    problem1k()
    problem1l()
    problem1m()
    problem1n()
    problem1o()
    problem2a()
    problem2b()
    problem2c()
    problem2d()
#    problem2e()
#    problem2f()
#    problem2g()
#    problem2h()
#    problem2i()
#    problem2j()
#
#
