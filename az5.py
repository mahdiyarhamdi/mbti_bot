import requests 
url = 'http://smsg.ir/index2.php?goto=webservice/json&method=send&arg1=ali&arg2=maedeh&arg3=09397201006&arg4=30001341213594&arg5=س'
u1 = 'http://smsg.ir/index2.php?goto=webservice/json&method=send&arg1=ali&arg2=maedeh&arg3='
no = '09397201006'
u2 = '&arg4=30001341213594&arg5='
msg= 'سلام \n خوبی؟ \n چطوری؟'
uu = u1+no+u2+msg
# resp = requests.get(uu)
def cmp(a, b):
    return [c for c in a if c.isalpha()] == [c for c in b if c.isalpha()]
print(cmp("s s s","sss"))    
# print(resp.text)
# print(resp.text[2])
# if resp.text[2]=='sent':
#     print("yes")