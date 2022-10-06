# https://tenderleo.gitbooks.io/leetcode-solutions-/content/GoogleEasy/359.html


class Logger:
    def __init__(self) -> None:
        self.logs = {}

    def shouldPrintMessage(self, timestamp, message):
        if message in self.logs:
            if timestamp - self.logs[message]["timestamp"] < 10:
                return False

        self.logs[message] = {"timestamp": timestamp}
        return True


logger = Logger()
print(logger.shouldPrintMessage(1, "foo"))
print(logger.shouldPrintMessage(2, "bar"))
print(logger.shouldPrintMessage(3, "foo"))
print(logger.shouldPrintMessage(8, "bar"))
print(logger.shouldPrintMessage(10, "foo"))
print(logger.shouldPrintMessage(11, "foo"))

# Time complexity: O(1)
# Space complexity: O(n), where n is the number of logs, since they can have
# very spaced timestamps, and timestamps within no order, it's not possible
# to clean the logs from time to time.
