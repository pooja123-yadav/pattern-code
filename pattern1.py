# 1234
# 1234
# 1234
# 1234

def pattern1(n):
  row = 1
  while(row<=n):
    col = 1
    while(col<=n):
      print(col, end=" ")
      col = col + 1
    
    row = row +1
    print("\r")

pattern1(n=4)
  
