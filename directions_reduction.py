
def dirReduc(arr):
   
   config_dict = {"SOUTH" : "NORTH", "NORTH" : "SOUTH", "EAST" : "WEST", "WEST" : "EAST"}
   
   stack = []
   
   for obj in arr:
          
      if len(stack) == 0 or stack[-1] != config_dict[obj]:
         stack.append(obj)
      
      else:
             stack.pop()

   return stack

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

print(dirReduc(a))





