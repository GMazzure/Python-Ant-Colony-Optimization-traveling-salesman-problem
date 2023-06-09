import os


class Log:
    def __init__(self, localization) -> None:
        self.logPath = makeLogPath(localization)

def makeLogPath(localization) -> str:
    """Finds an linear name for the execution to save image logs

    Returns:
        str: path to the execution log folder
    """
    testNumber = 1
    path_occupied = os.path.exists("./Log/"+str(localization)+'/teste'+str(testNumber))

    while (path_occupied):
        testNumber += 1
        path_occupied = os.path.exists("./Log/"+str(localization)+'/teste'+str(testNumber))

    logPath = "Log/"+str(localization)+'/teste'+str(testNumber)
    os.makedirs(logPath)
    return logPath
