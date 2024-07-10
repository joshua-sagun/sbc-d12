u_int = input("Enter the Words: ")
arr = []
result = ""

for i in u_int:
    if i != " ":
        result += i
    else:
        if result:
            arr.append(result)
            result = ""
if result:
    arr.append(result)

print(arr)