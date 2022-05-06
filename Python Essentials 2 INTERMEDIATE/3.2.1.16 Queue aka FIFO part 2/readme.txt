3.2.1.16 Queue aka FIFO: part 2

LAB

Estimated time

15-30 minutes
Level of difficulty

Easy/Medium
Objectives

    improving the student's skills in defining subclasses;
    adding a new functionality to an existing class.

Scenario

Your task is to slightly extend the Queue class' capabilities. We want it to have a parameterless method that returns True if the queue is empty and False otherwise.

Complete the code we've provided in the editor. Run it to check whether it outputs a similar result to ours.

Below you can copy the code we used in the previous lab:
class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []
    def put(self,elem):
        self.queue.insert(0,elem)
    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError

Expected output

1
dog
False
Queue empty