for i in range(100):
    if i == 5:
        print("Breaking the loop at ", i)
        break
    print(i)

for i in range(100):
    if i == 10:
        print("Skipping the iteration at ", i) # it skips the iteration when i is 10 and continues with the next iteration
        continue
    print(i)