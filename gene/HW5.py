#Maryna Taranova 

class Gene():
    """A Gene represents basic information about a particular gene in a
    particular experiment.
    
    """
    # TODO: define an init function that takes a chromosome, start, stop, strand, name, gene_id, exp1, and exp2
    #   strand must either be '+' or '-'  (you should check to make sure this is the case)
    #   exp1 and exp2 are each lists of expression values, corresponding to two experimental conditions.
    #       we'll be looking for differences between these two lists
    
    def __init__(self, chromosome, start, stop, strand, name, gene_id, exp1, exp2):
       
        if (strand != '+') & (strand != '-'):
            raise ValueError(" Strand must be + or - !")
        self.chrom = chromosome
        self.start = start
        self.stop = stop
        self.strand = strand
        self.name = name
        self.gene_id=gene_id
        self.exp1 = exp1
        self.exp2 = exp2
    
    # TODO: define a function "length" that gives this gene's length (stop - start)
    def length(self):
        return self.stop - self.start

    # TODO: define a function "exp1_mean" which returns the mean of experiment 1
    def exp1_mean(self):
        return self.get_mean(self.exp1)
       
    # TODO: define a function "exp2_mean" which returns the mean of experiment 2
    def exp2_mean(self):
        return self.get_mean(self.exp2)
 
    def get_mean(self, data):
        return round(sum([point  for point in data])/len(data), 3)   
    
    # TODO: define a function "exp1_variance" that gets experiment 1's variance
    #   If a particular sample is x_i, and the mean of all samples in an experiment
    #   is sample_mean, then you can calculate the variance by finding the average:
    #       (x_i - sample_mean)**2
    #   across all i values.  In other words, it's the AVERAGE of the squared difference
    #   between each datapoint and the mean of all datapoints.
    
    def exp1_variance(self):
        return self.get_variance(self.exp1)

    # TODO: define a function "exp2_variance" that gets experiment 2's variance
    def exp2_variance(self):
        return self.get_variance(self.exp2)

    def get_variance(self, data):
        return round(sum([(point - self.get_mean(data))**2 for point in data])/len(data), 3)
 
    # TODO: define a function "normalized_differential_expression" which 
    #   calculates the value:
    #       (exp1_mean - exp2_mean) / sqrt(exp1_variance / num_samples_exp1 + exp2_variance / num_samples_exp2)
    # NOTE: this value is the t-test statistic when exp1 and exp2 have independent variances
    #   see http://en.wikipedia.org/wiki/Welch%27s_t_test for more information
    # NOTE: you should round your answer to 3 decimal places
     
    def normalized_differential_expression(self):
        return round((self.exp1_mean()-self.exp2_mean())/(self.exp1_variance()/len(self.exp1)+self.exp2_variance()/len(self.exp2))**0.5, 3)
    
    # Brownie point:  add a function test_differential_expression which in addition to the t_test
    #   statistic, also reports the associated p-value (you'll need to look up a t-test table, and
    #   will need to determine the degrees of freedom.  See the wikipedia page...
    
    # TODO: define an __str__ function that returns a string "chrom\tstart\tstop\tgene_id\tname\tnormalized_differential_expression\tstrand\n"
    def __str__(self):
        a=str(self.chrom),'\t', str(self.start), '\t', str(self.stop), '\t', str(self.gene_id), '\t', str(self.normalized_differential_expression()), '\t', str(self.strand), '\n'
        return "".join(a)
                

    # TODO: define an __eq__ function which, given another gene, checks if the gene_id
    #   is the same for both genes (returns True if it's the same, False otherwise)
    def  __eq__(self, other):
        if self.gene_id==other.gene_id:
            return True
        else:
            return False    
    

class GeneSet():
    """A GeneSet is a collection of genes and their expression values in several
    different experiments.
    
    """
    # TODO: define an __init__ function which, given a filename will load a geneset from a file
    def __init__(self, filename):
        
        import string
        file = open(filename,"r")
        text = file.readlines()
        file.close()
     
        self.data=[]
        for line in text:
            self.data = self.data + [Gene(line.split()[0], line.split()[1], line.split()[2], line.split()[3], "".join(line.split()[4:len(line.split())-39]), line.split()[len(line.split())-39], [float(line.split()[i]) for i in range(len(line.split())-38, len(line.split())-11)], [float(line.split()[i]) for i in range(len(line.split())-11, len(line.split()))])]
 
        self.index = 0
    def __iter__(self):
        return self
    def next(self):
        if self.index == len(self.data):
            raise StopIteration
        self.index = self.index + 1
        return self.data[self.index-1]
         

    # TODO: write a function __contains__ which, given a particular Gene, returns
    #   whether or not that gene is in the GeneSet.

    #_contains method is not really necessary for the entire flow since _iter_ method was implemented earlier
    def __contains__(self, gene):
        if gene in self.data:
            return True
        else:
            return False

    
    # TODO: define an __str__ function that returns a string with all the genes you read in from the file
    #   the format of each gene should be the same as the Gene.__str__ function.
    def __str__(self):
        for gene in self.data:
            a=str(gene.chrom),'\t', str(gene.start), '\t', str(gene.stop), '\t', str(gene.gene_id), '\t', str(gene.normalized_differential_expression()), '\t', str(gene.strand), '\n'
        return "".join(a)

    # TODO: define a function "most_differentiated_genes" which returns the N most differentiated genes,
    #   use normalized_differential_expression in each gene, returning a list of genes that are most
    #   different.  N should be a parameter of this function.
    #   NOTE:  We only care about *differential* expression, not about the *direction*
    #       of the change.  So in choosing the top ten, you'll need to use the absolute value
    #       of the t_test statistic.
    

    def most_differentiated_genes(self, N):
        sorted_list=sorted(self.data, key=lambda gene: abs(gene.normalized_differential_expression()))
        sorted_list.reverse()
        return sorted_list[0:N] 














            
