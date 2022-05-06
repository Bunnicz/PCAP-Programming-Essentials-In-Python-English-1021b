class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.__queue = []  # __var - private variable, _var - protected variable

    def put(self, elem):
        self.__queue.insert(0, elem)

    def get(self):
        if len(self.__queue) > 0:
            val = self.__queue[-1]
            self.__queue.pop(-1)
            return val
        else:
            raise QueueError


class SuperQueue(Queue):
    def isempty(self):
        return len(self._Queue__queue) == 0  # accessing private variable _<class name>__<variable name>


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
