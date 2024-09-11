dic = {}
for i in range(0,len(phone_case_options)):
   string = phone_case_options[i].split('–')
   key = (string[0])[:-1]
   description = string[1].split('(')
   colour = description[0].strip()
   type = (description[1].strip())[:-1]
   dic[key] = [colour,type]


def binarySearch(dict,x):
   low = 0
   high = len(dict)
   while low <= high:
       mid = (high + low)//2
       if dict[mid-1] < x:
           low = mid + 1
       elif dict[mid-1] > x:
           high = mid - 1
       else:
           return mid
   return -1


wanted = input("Enter a name of the case: ")
dict = sorted(list(dic.keys()))
result = binarySearch(dict,wanted)
if result != -1:
  colour,type = dic[wanted]
  print(f'The wanted phone case name is {wanted}, the colour is {colour} and the phone type is {type}')
else:
  print(f"{wanted} is not found in the given list")
