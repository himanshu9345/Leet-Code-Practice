s="{I am|I'm} {working on|starting} this {online |}interview. I hope Cortx thinks I am {{very|extremely} {qualified|great|awesome}}{!|.}"
import random
stack=[]
count=0
ans1=""
for i,v in enumerate(s):

    if v=="{":
        stack.append(i)
        count+=1
    if v=="}":
        count-=1
        if count!=0:
            p=s[stack.pop()+1:i]
            gt=p.split("|")
            hh=gt[random.randint(0,len(gt)-1)]
            ans1+=hh+" "
            stack.append(i)
        if count==0:
            p = s[stack.pop() + 1:i]
            gt = p.split("|")
            hh = gt[random.randint(0, len(gt) - 1)]
            ans1 += hh.strip()+" "

    if count==0 and v!="}":
        ans1+=v

print (ans1)
