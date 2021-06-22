
from django.shortcuts import redirect, render, HttpResponse
from django.core.files.storage import FileSystemStorage
import pandas as pd
from itertools import repeat
import csv

# Create your views here.
def index(request):
    if request.method == 'POST':
        num = int(request.POST['num'])
        n = range(1,num+1)
        return render(request,'file.html',{'n':n,'no':num})
    else:
        return render(request,'num.html')

def file(request):
    if request.method=='POST':
        head = ['Name']
        attendees = []
        p = []
        attendance = {}
        num = int(request.POST['num'])
        for i in range(1,num+1):
            data=request.FILES[str(i)]
            fs = FileSystemStorage()
            name = fs.save(data.name,data)
            f = pd.read_csv('uploads/'+name, sep='\t', encoding='UTF-16')
            names = f['Full Name'].unique()
            add = [name for name in names if name not in attendees]
            attendees = attendees+add
            if i != 1:
                for j in range(1,len(add)+1):
                    for k in range(1,len(p)+1):
                        p[-1*k].append('A')
            pre=[]
            pre.extend(repeat('P',len(attendees)))
            for x,name in enumerate(attendees):
                if name not in names:
                    pre[x]='A'
            p.append(pre)
            date = f['Timestamp'][0].split(',')[0]
            head.append(date)
        attendance['1Name'] = attendees
        i=0
        for date in head[1:]:
            attendance[date]=p[i]
            i=i+1
        final = pd.DataFrame(attendance)
        final.sort_values('1Name').sort_index(axis=1).to_csv('attendance/files/Attendance.csv',index=False)
        m = open('attendance/files/Attendance.csv','r')
        data = m.readlines()
        response = HttpResponse(content_type = 'text/csv',headers={'Content-Disposition':'attachment;filename ="attendance.csv"'},)
        writer = csv.writer(response)
        for line in data:
            writer.writerow(line.split(','))
        return response