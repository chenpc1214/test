with open ("ch14_20.txt","r") as name:
    result = name.readlines()

mark = ""

for finally_result in result:
    mark += finally_result.rstrip()

print(mark)
    
