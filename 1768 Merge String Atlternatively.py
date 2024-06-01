#1768. Merge Strings Alternately
#You are given two strings word1 and word2. 
#Merge the strings by adding letters in alternating order, starting with word1. 
#If a string is longer than the other, append the additional letters onto the end of the merged string.
#Return the merged string.
class Solution(object):
    def mergeAlternately(self, word1, word2):
        word3=''
        if len(word1)>len(word2):
            for i in range(len(word2)):
                word3+=word1[i]
                word3+=word2[i]
            word3 += word1[i+1:]
            return word3
        elif len(word2)==len(word1):
            for i in range(len(word1)):
                word3 += word1[i]
                word3 += word2[i]
            return word3
        else:
            for i in range(len(word1)):
                word3+=word1[i]
                word3+=word2[i]
            word3+=word2[i+1:]
            return word3

        