#d
def main(d):
    num = 0
    prev = 0
    cur = ""
    for i in d:
        if i == cur:
            num += 1
        else:
            cur = i
            num = 1
        if num > prev:
            prev = num
    return prev
print(main(input()))

