'''
Created on 2013-3-15

@author: Administrator
'''

import  chardet
class Encoding(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def ToUTF8(self,value,encoding=''):
        if(encoding==''):
            encoding=chardet.detect(value)['encoding']
        return unicode(value,encoding).encode("UTF-8")
    
    def GetEncoding(self,value):
        return chardet.detect(value)['encoding']