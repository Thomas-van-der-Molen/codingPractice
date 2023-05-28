def recolor(blocks, k):
    blocks = blocks.split("W")
    if not any(blocks): return k
    for block in blocks:
        if len(block) >= k: return 0
    
    
    print(blocks)


blocks, k = "WBBWWBBWBW", 7
print(recolor(blocks, k))

blocks, k = "WBWBBBW", 2
print(recolor(blocks, k))

blocks, k = "WWWWW", 5
print(recolor(blocks, k))