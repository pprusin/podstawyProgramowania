"""
Write a Python program to print the alphabet pattern 'Z'.
Expected Output:

*******                                                                 
     *                                                                  
    *                                                                   
   *                                                                    
  *                                                                     
 *                                                                      
*******
"""
for i in range(7):
    for j in range(7):
        if i == 0 or i == 6:
            print("*", end="")
        elif i + j == 6:
            print("*", end="")
        else:
            print(" ", end="")
    print()
