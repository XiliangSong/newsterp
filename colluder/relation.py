#! /usr/bin/python2.4



__author__ = 'jhebert@cs.washington.edu (Jack Hebert)'



""" Hold relation text, pointer back to article. """



class Relation:
    def __init__(self, dataLine, articleURL):
        end = dataLine.find(')+[snum:')
        self.success = not (end==-1)
            
        text = dataLine[:end]
        for char in ',.()[]':
            text = text.replace(char, ' ')
        self.relation = text
        end2 = dataLine.find('hrs:', end)
        self.sentenceNumber = dataLine[end+8:end2]
        self.originalSentence = dataLine[end2:-1]
        self.articleURL = articleURL
        #print 'Article:', self.articleURL
        if(self.articleURL[-1]=='/'):
            self.articleURL = self.articleURL[:-1]

    def ToString(self):
        return ''.join([self.articleURL, ' : ', self.relation])

    def RelationAsText(self):
        toReturn = self.relation
        for char in '();.&#$':
            toReturn = toReturn.replace(char, '')
        return toReturn

    def RelationSentence(self):
        return self.originalSentence