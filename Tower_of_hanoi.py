def hanoi(n, start,helper,end):
    if n==1:
        print(f"Move disk from {start} to {end}")
    else:
        hanoi(n-1,start,end,helper)
        print(f"Move disk from {start} to {end}")
        hanoi(n-1,helper,start,end) 

hanoi(3,'A','B','C')           