'''this script generates dates in order
script created to obtain cbse results of ryan noida 17-18
considering all students dob lies in 1998 to 2001 inclusive
format dd/mm/yyyy'''

import datetime
file = open('date.txt','w')

a=datetime.date(1998,1,1)
end=datetime.date(2001,12,31)
t=datetime.timedelta(days=1)
s=''

while a<=end:
    s= str(a.day).zfill(2) + '/' + str(a.month).zfill(2) + '/' + str(a.year).zfill(4)
    file.write(s+'\n')
    a+=t

file.close()