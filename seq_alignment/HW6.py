
class ReadMapper():
    """A ReadMapper is a class that handles finding the locations of short
    sequences of DNA (reads) in a very long sequence of DNA (reference).
    
    For simplicity, a seed-and-extend approach is taken, meaning a portion of
    the read must match exactly to the reference genome.
    
    """
    def __init__(self, reference, seed_length, method='hamming'):
        """Create a new ReadMapper, with a fixed reference and seed_length.
        
        You should use build_index to build an index on this reference and call
        the resulting dictionary `self.ref_index`
        
        You should also store the seed_length as `self.seed_length`
        
        Finally, you should store the reference sequence as `self.reference`
        
        """
        self.ref_index = self.build_index(reference, seed_length)
        self.seed_length = seed_length
        self.reference = reference.upper()
        self.method = method

    def sliding_window(self, reference, window_length):
        """Create a sliding window on reference, returning a list of all substrings
        in the reference.
        
        You should convert the reference to upper-case characters before
        working on it. You should NOT REPORT any substrings that have an N character in them.        
        """        
        my_reference = reference.upper()
        sliding_window = []
        for i in range(0, len(my_reference)-window_length+1):
             if 'N' not in my_reference[i:i+window_length]:
                 sliding_window.append(my_reference[i:i+window_length])
             else: 
                 sliding_window.append(None)
        return sliding_window
         
        """ 
        For example:
        >>> reference = 'AAATTTGGGCCC'
        >>> mapper = ReadMapper(reference, 3)
        >>> mapper.sliding_window(reference, 3)
        ['AAA', 'AAT', 'ATT', 'TTT', 'TTG', 'TGG', 'GGG', 'GGC', 'GCC', 'CCC']
        >>> mapper.sliding_window(reference, 5)
        ['AAATT', 'AATTT', 'ATTTG', 'TTTGG', 'TTGGG', 'TGGGC', 'GGGCC', 'GGCCC']
        
        # make sure you don't report the N character
        >>> reference = 'AAATTNGGGCCC'
        >>> mapper = ReadMapper(reference, 3)
        >>> mapper.sliding_window(reference, 3)
        ['AAA', 'AAT', 'ATT', 'GGG', 'GGC', 'GCC', 'CCC']
        
        # make sure you convert to upper case first
        >>> reference = 'AaAtttGGgCcc'
        >>> mapper = ReadMapper(reference, 3)
        >>> mapper.sliding_window(reference, 3)
        ['AAA', 'AAT', 'ATT', 'TTT', 'TTG', 'TGG', 'GGG', 'GGC', 'GCC', 'CCC']
        
        """

    def build_index(self, reference, seed_length):
        """Create an index from all substrings in reference to their positions
        within reference. Returns a dictionary whose keys are the substrings of
        length window_length and whose values are a list of positions where that
        substring occurs.
        
        Note: you should use `sliding_window` to get all the substrings in `reference`.
        
        REMEMBER TO CONVERT REFERENCE TO UPPER CASE!
        """
        index_dic={}
        i=0
        for item in self.sliding_window(reference, seed_length):
            if item !=None: 
                if item not  in index_dic.keys():
                    index_dic[item] = []
                index_dic[item].append(i)  
            i=i+1 
        return  index_dic


        """         
        For example:
        >>> build_index('AAATTTGGG', 2)
        {'AA':[0,1], 'AT':[2], 'TT':[3,4], 'TG':[5], 'GG':[6,7]}
        >>> build_index('AAATTTGGG', 3)
        {'AAA':[0], 'AAT':[1], 'ATT':[2], 'TTT':[3], 'TTG':[4], 'TGG':[5], 'GGG':[6]}
        
        """

    def get_candidate_starts(self, read):
        """Get all candidate mappings for a read by using the first seed_length
        bases as a seed into reference. Reads that don't seed into the reference
        should have an empty list returned.
        
        Note: `read` may be longer than `seed_length`.  Only the FIRST `seed_length`
        bases of the read are used as an index.
        
        REMEMBER TO CONVERT YOUR READ TO UPPER CASE!
        """
        if read[0:self.seed_length] in self.build_index(self.reference, self.seed_length):
            return self.build_index(self.reference, self.seed_length).get(read[0:self.seed_length])
        else:
             return []
     
        """
        For example:
        >>> reference = 'AAATTTGGGCCC'
        >>> mapper = ReadMapper(reference, 3)
        >>> mapper.get_candidate_starts('AAAAAA')
        [0]
        >>> mapper = ReadMapper(reference, 2)  # use a shorter seed length
        >>> mapper.get_candidate_starts('AAAAAA')
        [0,1]
        >>> get_candidate_starts('GTAGTA')  # seed GT doesn't match reference
        []
        
        """

    def score_candidate(self, read, candidate_start):
        """For a given read and its candidate placement on reference, return the
        number of mismatches between read and reference.
        
        REMEMBER TO CONVERT YOUR READ TO UPPER CASE!
        
        For example, if the candidate started at the V in the following:
        # candidate_loc      V
        >>> reference = 'AAATTTGGGCCC'
        
        >>> mapper = ReadMapper(reference, 4)
        >>> mapper.score_candidate('TTGGGCC', 4)  # perfect match!
        0
        >>> mapper.score_candidate('TTGGACC', 4)  # A mismatches
        1
        >>> mapper.score_candidate('TTGGACG', 4)  # A and G mismatch
        2
        
        """
        if self.method == 'hamming':
            counter=0
            position=0
            for letter in read:
#                if (candidate_start+position) <= len(self.reference):
                if letter != self.reference[candidate_start+position]:
#                    print letter, self.reference[candidate_start+position]
                    counter=counter+1
                position=position+1
#                else: #if the seed is aligned to the end of the reference and the read is longer than the reference, we assign the score value to inf
#                    counter=float('inf') 
            return counter


        elif self.method == 'edit':
            print 'TODO for extra credit...'
        elif self.method == 'edit_freesuffix':
            print 'TODO for extra credit...'
        else:
            raise ValueError('method must be either "hamming", "edit", or "edit_freesuffix", not %s' % method)
    
    
    def best_mapping(self, read):
        """return the BEST mapping to the reference (the one with fewest mismatches)
        
        In this function, you'll need to find all the candidate mappings for
        this read, then score each one.  Then return the best start and score as
        a tuple:
        return (best_start, best_score)
        
        If a read has no candidates, then return (None, float('inf'))
        
        REMEMBER TO CONVERT YOUR READ TO UPPER CASE!
        
        """
        start_dic={}
        if self.get_candidate_starts(read)==[]:
            return (None, float('inf'))
        else:
            for start in self.get_candidate_starts(read):
                start_dic[start]=self.score_candidate(read,start)
            best_start=min(start_dic, key=start_dic.get)
            best_score=start_dic[min(start_dic, key=start_dic.get)]
            return (best_start, best_score)

    def map_reads(self, all_reads):
        """return a list of mappings obtained from best_mapping.
        
        REMEMBER TO CONVERT YOUR READ TO UPPER CASE!
        
        """
        list_of_mappings = []
        for read in all_reads:
            list_of_mappings.append(self.best_mapping(read))
        return list_of_mappings
             

def load_reads_from_file(filename):
    """load a list of reads from a file.  The reads are all on separate lines,
    one line per read.
    
    The file *could* be a zipped file.  You should check to see if the filename
    ends with '.gz' and if it does, open it as a zipped file (see python gzip module).
    If it doesn't, open it as a regular file.
     """
    import gzip
    if filename[-3:]=='.gz':
        file = gzip.open(filename,"r")
        text = file.readlines()
        file.close()
    else:
        file = open(filename,"r")
        text = file.readlines()
        file.close()
    
    list_of_reads=[]
    for line in text:
#        list_of_reads.append(line.replace('\n', ''))
        list_of_reads.append(line.rstrip())
    return list_of_reads
        
    
def load_reference_from_file(filename):
    """load a reference genome from a file. The file will only contain only
    one chromosome from the reference genome and should be returned as a string.
    
    The file *could* be a zipped file.  You should check to see if the filename
    ends with '.gz' and if it does, open it as a zipped file (see python gzip module)
    If it doesn't, open it as a regular file.
    """
    import gzip
    if filename[-3:]=='.gz':
        file = gzip.open(filename,"r")
        text = file.readlines()
        file.close()
    else:
        file = open(filename,"r")
        text = file.readlines()
        file.close()
    return ''.join(line.replace('\n', '') for line in text)
