import pylab as p
from numpy import *


class Visu:
    """Handles graphical visualization of the execution
    """
    def __init__(self) -> None:
        self.fig = p.figure(figsize=(15, 30))

        self.ax = []
        axes1 = self.fig.add_axes([0.07, 0.07, 0.75, 0.90])  # main axes
        axes2 = self.fig.add_axes([0.795, 0.1, 0.199, 0.4])  # inset axes
        axes3 = self.fig.add_axes([0.82, 0.55, 0.18, 0.4])

        self.ax = [axes1, axes2, axes3]

    def plotRoute(self, routeArr, dataArr):
        """Plot route's points to cordinates

        Args:
            routeArr (list[int]): list of vertices
            dataArr (list[int]): list of X and Y cordinates
        """ 
        x, y = getPoints(routeArr, dataArr)

        self.ax[0].cla()
        self.ax[0].plot(x, y, label='Best Route', color="blue", lw=0.5)
        self.ax[0].scatter(x, y, s=15)

        self.ax[0].set_ylabel('Y')
        self.ax[0].set_xlabel('X')

        self.ax[0].legend()
        self.ax[0].grid(True)

    def plotIndicators(self, xArr, y1Arr, y2Arr, y3Arr, y4Arr, iteration, elapsedTime):
        """Plot execution data to the chart

        Args:
            xArr: _description_
            y1Arr: _description_
            y2Arr: _description_
            y3Arr: _description_
            y4Arr: _description_
            iteration: _description_
            elapsedTime: _description_
        """
        self.ax[1].cla()

        self.ax[1].plot(xArr, y1Arr, label='Melhor global',
                        color="blue", lw=1.2)
        self.ax[1].plot(xArr, y2Arr, label='Melhor Local', color="red", lw=0.7)
        self.ax[1].plot(xArr, y3Arr, label='Pior Local', color="green", lw=0.7)
        self.ax[1].plot(xArr, y4Arr, label='Média Local',
                        color="purple", lw=0.7)

        self.ax[1].set_ylabel('D')
        self.ax[1].set_xlabel('Iteration')

        self.ax[1].legend()

        self.ax[2].cla()
        self.ax[2].axis('off')
        self.ax[2].text(0.05, 0.7, 'Iteracao: '+str(iteration), horizontalalignment='left',
                        verticalalignment='center', transform=self.ax[2].transAxes)
        self.ax[2].text(0.05, 0.6, 'Tempo Decorrido: '+str("%0.0f" % elapsedTime)+' seg',
                        horizontalalignment='left', verticalalignment='center', transform=self.ax[2].transAxes)

        self.ax[2].text(0.05, 0.5, 'Melhor Global: '+str("%0.0f" % y1Arr[len(y1Arr)-1]),
                        horizontalalignment='left', verticalalignment='center', transform=self.ax[2].transAxes)
        self.ax[2].text(0.05, 0.4, 'Melhor Local: '+str("%0.0f" % y2Arr[len(y2Arr)-1]),
                        horizontalalignment='left', verticalalignment='center', transform=self.ax[2].transAxes)
        self.ax[2].text(0.05, 0.3, 'Pior Local: '+str("%0.0f" % y3Arr[len(y3Arr)-1]),
                        horizontalalignment='left', verticalalignment='center', transform=self.ax[2].transAxes)
        self.ax[2].text(0.05, 0.2, 'Média Local: '+str("%0.0f" % y4Arr[len(y4Arr)-1]),
                        horizontalalignment='left', verticalalignment='center', transform=self.ax[2].transAxes)


    def drawChart(self):
        p.draw()
        p.pause(0.01)


    def exportChart(self, fileName):
        p.savefig(fileName+".png")


def getPoints(routeArr, dataArr):
    """return X and Y points for every step in the route

    Args:
        routeArr (list[int]): list of vertices 
        dataArr (list[int]): list of cordinates

    Returns:
        list[int]: route's cordinates
    """
    x = []
    y = []

    for i in range(len(routeArr)):
        x.append(dataArr[int(routeArr[i])][0])
        y.append(dataArr[int(routeArr[i])][1])
    x.append(dataArr[int(routeArr[0])][0])
    y.append(dataArr[int(routeArr[0])][1])

    return x, y
