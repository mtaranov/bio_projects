#!/usr/bin/env python
from HW5 import Gene, GeneSet

def problem1a():
    print 'testing Gene constructor...',
    gene1 = Gene('chr1', 200, 300, '+', 'p53', 'NM_000546.4', [474], [568])
    if gene1.chrom == 'chr1' and gene1.start == 200 and gene1.stop == 300 \
                        and gene1.strand == '+' and gene1.name == 'p53' and \
                        gene1.gene_id == 'NM_000546.4' and gene1.exp1 == [474] \
                        and gene1.exp2 == [568]:
        print 'PASSED!'
    else:
        print 'FAILED!'

def problem1b():
    print 'testing Gene.length() function...',
    gene1 = Gene('chr1', 200, 300, '+', 'p53', 'NM_000546.4', [474], [568])
    length = gene1.length()
    if length == 100:
        print 'PASSED!'
    else:
        print 'FAILED!  Expected 100, got', length

def problem1c():
    print 'testing Gene.exp1_mean...',
    gene1 = Gene('chr1', 200, 300, '+', 'p53', 'NM_000546.4', [400,400,500,500], [568])
    mean = gene1.exp1_mean()
    if mean == 450:
        print 'PASSED!'
    else:
        print 'FAILED! Expect mean 450, got', mean

def problem1d():
    print 'testing Gene.exp2_mean...',
    gene1 = Gene('chr1', 200, 300, '+', 'p53', 'NM_000546.4', [400,400,500,500], [568])
    mean = gene1.exp2_mean()
    if mean == 568:
        print 'PASSED!'
    else:
        print 'FAILED! Expect mean 568, got', mean

def problem1e():
    print 'testing Gene.exp1_variance...',
    gene1 = Gene('chr1', 200, 300, '+', 'p53', 'NM_000546.4', [400,400,500,500], [568])
    var = gene1.exp1_variance()
    if var == 2500:
        print 'PASSED!'
    else:
        print 'FAILED! Expect variance 2500, got', var

def problem1f():
    print 'testing Gene.exp2_variance...',
    gene1 = Gene('chr1', 200, 300, '+', 'p53', 'NM_000546.4', [400,400,500,500], [568, 570])
    var = gene1.exp2_variance()
    if var == 1:
        print 'PASSED!'
    else:
        print 'FAILED! Expect variance 1, got', var

def problem1g():
    print 'testing Gene.normalized_differential_expression...',
    gene1 = Gene('chr1', 200, 300, '+', 'p53', 'NM_000546.4', [400,400,500,500], [568, 570])
    t_stat = gene1.normalized_differential_expression()
    if t_stat == -4.758:
        print 'PASSED!'
    else:
        print 'FAILED! Expect t-stat of -4.758, got', t_stat

def problem1h():
    print 'testing Gene.__str__ function...',
    gene1 = Gene('chr1', 200, 300, '+', 'p53', 'NM_000546.4', [400,400,500,500], [568, 570])
    as_string = str(gene1)
    expected_string = 'chr1\t200\t300\tNM_000546.4\t-4.758\t+\n'
    if as_string == expected_string:
        print 'PASSED!'
    else:
        print 'FAILED! expected\n%sbut got\n%s' % (expected_string, as_string)

def problem1i():
    print 'testing Gene.__eq__ function with positive example...',
    gene1 = Gene('chr1', 200, 300, '+', 'p53', 'NM_000546.4', [400,400,500,500], [568, 570])
    gene2 = Gene('blah', 100, 200, '-', 'jake', 'NM_000546.4', [3,2,1], [1,2])
    if gene1 == gene2:
        print 'PASSED!'
    else:
        print "FAILED! gene1 and gene2 gene_id's are the same; they should equal each other"

def problem1j():
    print 'testing Gene.__eq__ function with negative example...',
    gene1 = Gene('chr1', 200, 300, '+', 'p53', 'I_DONT_MATCH', [400,400,500,500], [568, 570])
    gene2 = Gene('blah', 100, 200, '-', 'jake', 'NM_000546.4', [3,2,1], [1,2])
    if gene1 == gene2:
        print "FAILED! gene1 and gene2 gene_id's are NOT the same; they should NOT equal each other"
    else:
        print 'PASSED!'


def problem2a():
    print 'testing GeneSet init on ONE datapoint...',
    geneset = GeneSet('ALL_test_1_datapoint.txt')
    gene1 = Gene('chr14', 44843498, 44868951, '+', 'AFFX-BioB-5_at (endogenous control)', 'AFFX-BioB-5_at', [1,2,3], [4,5,6])
    if gene1 in geneset:
        print 'PASSED!'
    else:
        print 'FAILED! Either the GeneSet.__init__ load failed or your Gene.__eq__ method isnt right. '

def problem2b():
    print 'testing GeneSet init on ONE datapoint, with a phony match...',
    geneset = GeneSet('ALL_test_1_datapoint.txt')
    gene1 = Gene('chr14', 44843498, 44868951, '+', 'AFFX-BioB-5_at (endogenous control)', 'PHONY_ID', [1,2,3], [4,5,6])
    if gene1 not in geneset:
        print 'PASSED!'
    else:
        print 'FAILED! Either the GeneSet.__init__ load failed or your Gene.__eq__ method isnt right... was not supposed to find PHONY_ID'

def problem2c():
    print 'testing GeneSet init on ONE datapoint, converting whole file to string...',
    geneset = GeneSet('ALL_test_1_datapoint.txt')
    expected = 'chr14\t44843498\t44868951\tAFFX-BioB-5_at\t-1.427\t+\n'
    actual = str(geneset)
    if expected == actual:
        print 'PASSED!'
    else:
        print 'FAILED! Expected\n%sbut recieved\n%s' % (expected, actual)

def problem2d():
    print 'testing GeneSet init on ONE datapoint...',
    geneset = GeneSet('ALL_test_1_datapoint.txt')
    expected = 'chr14\t44843498\t44868951\tAFFX-BioB-5_at\t-1.427\t+\n'
    actual = str(geneset)
    if expected == actual:
        print 'PASSED!'
    else:
        print 'FAILED! Expected\n%sbut recieved\n%s' % (expected, actual)

def problem2e():
    print 'testing GeneSet init on COMPLETE dataset...',
    geneset = GeneSet('ALL_vs_AML.txt')
    for linenum, line in enumerate(open('ALL_vs_AML.txt')):
        gene_id = line.split('\t')[5]
        gene = Gene('blank',5,10,'+','whatever', gene_id, [2,3,4], [5,6,7])
        if gene not in geneset:
            print 'FAILED!  missing gene_id %s at line %s' % (gene_id, linenum)
            break
    else:
        print 'PASSED!'

def problem2f():
    print 'testing GeneSet.most_differentiated_genes with 3 genes on complete dataset...',
    geneset = GeneSet('ALL_vs_AML.txt')
    expected = ['chr19\t46934519\t46951122\tM55150_at\t-8.432\t+\n', 'chr20\t23530971\t23538744\tU22376_cds2_s_at\t8.076\t+\n', 'chr21\t48167021\t48174366\tX59417_at\t6.962\t-\n']
    actual = geneset.most_differentiated_genes(3)
    actual = map(str, actual)  # convert each entry to a string
    if expected == actual:
        print 'PASSED!'
    else:
        print 'FAILED! Expected\n%sbut your answer was\n%s' % (expected, actual)


def problem2g():
    print 'testing GeneSet.most_differentiated_genes with 10 genes on complete dataset...',
    geneset = GeneSet('ALL_vs_AML.txt')
    expected = ['chr19\t46934519\t46951122\tM55150_at\t-8.432\t+\n',
 'chr20\t23530971\t23538744\tU22376_cds2_s_at\t8.076\t+\n',
 'chr21\t48167021\t48174366\tX59417_at\t6.962\t-\n',
 'chr5\t5053254\t5054788\tU50136_rna1_at\t-6.73\t+\n',
 'chr7\t48659786\t48683624\tU82759_at\t-6.533\t+\n',
 'chr19\t20675121\t20699976\tM31211_s_at\t6.463\t+\n',
 'chr7\t9709088\t9726609\tL13278_at\t6.441\t-\n',
 'chr14\t44685937\t44696875\tU12471_cds1_at\t-6.379\t+\n',
 'chr8\t19788194\t19792479\tM92287_at\t6.355\t-\n',
 'chr8\t31108481\t31120259\tU05259_rna1_at\t6.304\t-\n']
    actual = geneset.most_differentiated_genes(10)
    actual = map(str, actual)  # convert each entry to a string
    if expected == actual:
        print 'PASSED!'
    else:
        print 'FAILED! Expected\n%sbut your answer was\n%s' % (expected, actual)


if __name__ == '__main__':
    problem1a()
    problem1b()
    problem1c()
    problem1d()
    problem1e()
    problem1f()
    problem1g()
    problem1h()
    problem1i()
    problem1j()
    problem2a()
    problem2b()
    problem2c()
    problem2d()
    problem2e()
    problem2f()
    problem2g()

