outer = 1
while outer <= 5:
    inner = 1
    while inner <= 5:
        product = outer * inner
        print(f"{outer} times {inner} = {product}")
        inner += 1
    outer += 1

# This is an example of a nested loop,
# meaning there is a second loop within the first,
# this way was a way to increase two counters at once
# to find all products of 1-5 x 1-5.