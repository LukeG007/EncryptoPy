import os
import pandas as pd
import random
CurrentDirectory = os.path.dirname(os.path.abspath(__file__))
DataDirectory = os.path.join(CurrentDirectory, 'Data')
emoji = pd.read_excel(DataDirectory + "\\emoji.xlsx")

my_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ',',','.','<','>','/','?',"'",'"',';',':','1','2','3','4','5','6','7','8','9','0','\\','|','[',']','{','}','+','=','-','_',')','(','*','&','^','%','$','#','@','!','~','`']

def Encode(sen):
    ln = len(sen)
    b = sen[::-1]
    if(ln%2==0):
        ln_h = int(ln/2)
        a_a = b[:ln_h]
        a_b = b[ln_h:]
    else:
        ln_h = int(ln/2)
        a_a = b[:ln_h]
        a_b = b[ln_h:]
    a_a = a_a[::-1]
    res = a_a + a_b
    return(res)

def Decode(sen):
    ln = len(sen)
    if(ln%2==0):
        ln_h = int(ln/2)
        a_a = sen[ln_h:]
        a_b = sen[:ln_h]
    else:
        ln_h = int(ln/2)
        a_a = sen[ln_h:]
        a_b = sen[:ln_h]
    a_a = a_a[::-1]
    final = a_a + a_b
    return(final)

def EmojiEncryption(inp):
    if(len(inp) !=0):
        li = list(inp) 
        an_list=[]
        st = random.randint(0,444)
        an_list.append(emoji.iloc[st,0])
        s = pd.Series(li)
        r = s.isin(emoji['emj'])
        if(r.any(axis = 0)==True):
            
            inn = False
            for i in range(len(li)):
                
                s_in = pd.Series(list(li[i]))
                r_in = s_in.isin(emoji['emj'])
                
                if(r_in.values==True):
                    if(inn!= True):
                        inn = True
                        an_list.append('♪')
                    an_list.append(li[i])
                else:
                    if(inn== True):
                        inn = False
                        an_list.append('♫')
                    pos = my_list.index(li[i])
                    pos = pos + st
                    an_list.append(emoji.iloc[pos,0])               
        else:
            for i in range(len(li)):
                pos = my_list.index(li[i])
                pos = pos + st
                an_list.append(emoji.iloc[pos,0])
        output='' 
        for x in an_list: 
                output += x
        output = Encode(output)
        return(output)
    else:
        return('Error')

def EmojiDecryption(einp):
    einp = Decode(einp)
    if(len(einp)>=2):
        sent=''
        val = emoji.loc[emoji['emj']==einp[0]].index[0]
        i=1
        while(True):
            if(einp[i]=='♪'):
                for j in range(i+1,len(einp)):
                    if(einp[j]=='♫'):
                        break
                    else:
                        sent += einp[j]
                i=j
            else:
                d = emoji.loc[emoji['emj']==einp[i]].index[0]
                sent+= my_list[d-val]
            if((i+1)>=len(einp)):
                break
            else:
                i+=1
        return(sent)
    else:
        return('Error')