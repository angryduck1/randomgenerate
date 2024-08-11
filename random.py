import random 

list = []
rang = int(input("From 1 to: "))

random_txt = open("random.txt", "w")

def rand():
  list.append(int(random.uniform(1, rang)))
  random_txt.write(str(list) + "\n")
  print(list)
 
while True: 
 keep_again = input("Generate? (y/n): ")
 
 if keep_again == "n":
  break
 elif keep_again == "y":
  rand()
 else: 
   print("Invalid command")

random_txt.close()