students=[{ 'name':'ahmed','grades':[25,23,22] },
          { 'name':'omar','grades':[40,40,21,5] },
          { 'name':'ali','grades':[19,23,29,2,1] },
          { 'name':'abdallah','grades':[19,255,29,2,1] }
          ] 
           
          
for i in range(len(students)):
       subjectno=len(students[i]['grades'])
       total=0
       for j in range(subjectno):   
            total+=(students[i]['grades'][j]) 
            if j==subjectno-1:
                  print(total/subjectno)
for i in range(len(students)):
       subjectno=len(students[i]['grades'])
       total=0
       for j in range(subjectno):   
            total+=(students[i]['grades'][j]) 
            if j==subjectno-1:
                  print(students[i]['name'],total/subjectno)


            