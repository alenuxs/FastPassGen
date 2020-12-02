#                                           Coded
#                                             By
#                                          Alenuxs
# 
# 
# Simply run this python file and three secure and easy to remember passwords will be generated insatntly!
# This password format is very hard to crack, but possible! You should always have strong passwords like these and always enable extra security measures such as 2fa!
import random
loopss = 0
for loopss in range(0,3):
    loopss = loopss + 1
    bridge = ["!", "@", "&", "+"]
    ran = random.randint(0,3)
    lol = "#"
    perc = random.randint(0,100)
    yeno = random.randint(1,4)
    numb = random.randint(0,10)
    rande = bridge[ran]
    s=open("a.txt","r")
    m=s.readlines()
    l=[]
    for i in range(0,len(m)-1):
     x=m[i]
     z=len(x)
     a=x[:z-1]
     l.append(a)
    l.append(m[i+1])
    var1=random.choice(l)
    s.close()
    bigv1 = var1 + rande
    ssd=open("b.txt","r")
    mk=ssd.readlines()
    ls=[]
    for il in range(0,len(mk)-1):
        xx=mk[il]
        zz=len(xx)
        app=xx[:zz-1]
        ls.append(app)
    ls.append(mk[il+1])
    var2=random.choice(ls)
    ssd.close()
    past = bigv1 + var2
    if yeno == 1:
        passs = past + "#" + str(numb) 
    elif yeno == 2:
        passs = past + "?"
    elif yeno == 3:
        passs = past + "*" 
    else:
        passs = past + str(perc) + "%"
    print("Secure password generated: " + passs)
