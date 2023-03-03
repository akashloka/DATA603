#import liblary
from mrjob.job import MRJob
import re
#match any sequence of words
match_occurences= re.compile(r"[\w']+")
#defines a class called WordCount
class WordCount(MRJob):
#processing each line of text in the input file using mapper
    def mapper(self, _, line):
        words = match_occurences.findall(line)
        for word in words:
            yield word.lower(), 1
#receive all the key-value pairs emitted by the mapper() method and sum up the values for each key using reduce
    def reducer(self, word, counts):
        yield word, sum(counts)
#executed the main program
if __name__ == '__main__':
    WordCount.run()
