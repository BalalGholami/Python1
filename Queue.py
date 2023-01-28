# Queue

from collections import deque

queue = deque([])
for i in range(5):
    queue.append(i)
print(queue)

while True:
    x = queue.popleft()
    print(x)
    print(queue)
    print('--------')
    if not queue:
        print("Queue is Empty")
        break
