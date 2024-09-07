my_list = sorted([int(x) for x in input("ENTER THE LIST : ").split()])
s = int(input("ENTER THE SEARCH NUMBER: "))

low = 0
high = len(my_list) -1

while low <= high:
    mid = (low + high) // 2
    
    if my_list[mid] < s:
        low = mid + 1
    elif my_list[mid] > s:
        high = mid - 1
    else:
        print(f"Found {s} at index {mid+1}")
        break
else:
    print(f"{s} not found in the list.")

