import queue  # Importing the queue module for message queue implementation

class MessageQueue:
    def __init__(self):
        """
        Initialize the message queue object with an empty queue.
        """
        self.message_queue = queue.Queue()  # Creating an empty queue for message storage

    def send_message(self, message):
        """
        Add a message to the queue.

        :param message: The message to be added to the queue.
        """
        self.message_queue.put(message)  # Adding the message to the queue

    def receive_message(self):
        """
        Retrieve and remove a message from the queue if available.

        :return: The message from the queue or None if the queue is empty.
        """
        if not self.message_queue.empty():
            return self.message_queue.get()  # Retrieving and removing the message from the queue
        else:
            return None  # Returning None if the queue is empty
