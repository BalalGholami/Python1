# stack

browsing = []
for i in range(20):
    browsing.append(i)

while True:
    x = browsing.pop()
    print(x)
    print(browsing)
    if not browsing:
        break
    print("-------------")
