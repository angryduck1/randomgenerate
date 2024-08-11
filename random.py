import random  
 
list = [] 
rang = int(input("From 1 to: "))
count = int(input("Count: "))
count_2 = 0
 
random_txt = open("random.txt", "w") 
 
def rand():
  global count_2
  while count_2 != count:
    count_2 += 1 
    list.append(int(random.uniform(1, rang))) 
    print(list)

  random_txt.write(" ".join(map(str, list)))
  
while True:  
 keep_again = input("Generate? (y/n): ") 
  
 if keep_again == "n": 
  break 
 elif keep_again == "y": 
  rand() 
 else:  
   print("Invalid command") 
 
random_txt.close() 

#в данном коде я использовал нейросеть