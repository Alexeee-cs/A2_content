def bubblesort(array):
   string=[]
   for i in range(0,len(array)):
       string.append(array[i].split('('))
   for i in range(0,len(array)):
       for j in range(0,len(array)-1):
           if string[j][1] > string[j+1][1]:
               temp = string[j]
               string[j] = string[j+1]
               string[j+1] = temp
               temp2 = array[j]
               array[j] = array[j+1]
               array[j+1] = temp2
   return array

print(bubblesort(phone_case_options))
