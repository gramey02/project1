# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    filename = "./data/test.fa" #use test.fa as the test file
    obj1_fasta = FastaParser(filename) #generate an instance of the FastaParser object
    
    #check if there are 100 sequences read in
    count = 0
    for rec in obj1_fasta:
        assert(('>seq' in rec[0]) == True) #check to make sure each header was parsed properly
        assert(len(rec) == 2) #check to make sure each header and sequence was read in properly as a tuple of length 2 (header, seq)
        count+=1 #update count variable upon each iteration
    assert(count == 100) #check to see if count, the number of sequences, is 100


def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    filename = "./data/test.fq" #use test.fa as the test file
    obj1 = FastqParser(filename) #generate an instance of the FastqParser object
    
    #check if there are 100 sequences read in
    count = 0
    for rec in obj1:
        assert(('@seq' in rec[0]) == True) #check to make sure each header was parsed properly
        assert(len(rec) == 3) #check to make sure each header and sequence was read in properly as a tuple of length 3 (header, seq, quality)
        count+=1 #update count variable upon each iteration
    assert(count == 100) #check to see if count, the number of sequences, is 100
