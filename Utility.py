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
    
    def GetAccountInfo(self):
        url=''
        user_name=''
        password=''
        try:    
            account_info = open("account.txt").read()
            url=self.ToUTF8(account_info.split(';')[0])
            user_name = self.ToUTF8(account_info.split(';')[1])
            password=self.ToUTF8(account_info.split(';')[2])
        except:
            ''
        while (url=='' or user_name=='' or password==''):
            url = raw_input('Your Site Addr:')
            user_name = self.ToUTF8(raw_input('Your user name:'))
            password = self.ToUTF8(raw_input('Password:'))
        
        account_info={
                     'url':url,
                     'user_name':user_name,
                     'password':password
                     }
        return account_info