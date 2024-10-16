
var_1 = int(input("Input your first number please: "))
var_2 = int(input("Input your second number please: "))
var_3 = int(input("Input your third number please: "))
var_4 = int(input("Input your fourth number please: "))
var_5 = int(input("Input your fifth number please: "))

def find_highest(var_1, var_2, var_3, var_4, var_5):
    if var_1 > var_2:
        if var_1 > var_3:
          if var_1 > var_4:
            if var_1 > var_5: 
                return var_1
    elif var_2 > var_3:
        if var_2 > var_4:
            if var_2 > var_5:
                return var_2
    elif var_3 > var_4:
        if var_3 > var_5:
            return var_3
    elif var_4 > var_5:
        return var_4
    else: 
        return var_5
   
result = find_highest(var_1, var_2, var_3, var_4, var_5)
print (result)

