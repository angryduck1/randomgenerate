import random

random_txt = open("random.txt", "w")
list = [] 
 
def rand():
  global count_2
  while count_2 != count:
    count_2 += 1 
    list.append(int(random.uniform(rang, rang_2))) 
    print(list)
  
while True:  
 keep_again = input("Generate? (y/n): ") 
  
 if keep_again == "n": 
  random_txt.close() 
  break 
 
 elif keep_again == "y":
  rang = int(input("From: "))
  rang_2 = int(input("To: "))
  count = int(input("Count: "))
  count_2 = 0

  rand()
  random_txt.write(str(list))
 else:  
   print("Invalid command") 

#в данном коде я использовал нейросеть
