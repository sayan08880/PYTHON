start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for num in range(start, end + 1):
    if str(num) == str(num)[::-1]:
        print(num, end=" ")




