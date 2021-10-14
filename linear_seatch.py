my_list = [1,3,5,6,45,6,7,7,88,9,0]

def linear_search(n,item):
  for i in range(len(n)):
    if n[i] == item:
      return i 
  return None
print(linear_search(my_list,3))  

