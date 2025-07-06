def hanoi(n, start,helper,end):
    if n==1:
        print(f"Move disk from {start} to {end}")
    else:
        hanoi(n-1,start,end,helper)
        print(f"Move disk from {start} to {end}")
        hanoi(n-1,helper,start,end) 


num_disks = int(input("Enter the number of disks:"))
print("\nSteps to solve Tower of Hanoi:\n")
hanoi(num_disks,'A','B','C')           