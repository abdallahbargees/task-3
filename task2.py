students=[{ 'name':'ahmed','grades':[25,23,22] },
          { 'name':'omar','grades':[40,40,21] },
          { 'name':'ali','grades':[19,23,29] },
          { 'name':'abdallah','grades':[250,23,29] }
           
          ]
for i in range(len(students)):
       subjectno=len(students[i]['grades'])
       total=0
       for j in range(subjectno):   
            total+=(students[i]['grades'][j]) 
            if j==subjectno-1:
                  print(f'average grades are {total/3}')
for i in range(len(students)):
       subjectno=len(students[i]['grades'])
       total=0
       for j in range(subjectno):   
            total+=(students[i]['grades'][j]) 
            if j==subjectno-1:
                  print(students[i]['name'],total/3)


            