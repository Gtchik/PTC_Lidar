from matplotlib import pyplot as plt
from Point import Point
from Droite import Droite
from data import data

class Main:
    # liste<Point> __points
    # liste<Droite> __droites

    def __init__(self):
        self.__droites=[]
        self.__creationPoints()
        self.__creationDroites()

    def getDroites(self) -> list:
        return self.__droites

    def addDroite(self, droite) -> None:
        self.__droites.append(droite)

    def getPoints(self) -> list:
        return self.__points

    def __creationPoints(self):
        data_copy = list(data)
        self.__points=[Point(data[0][1], data[0][2], None)]
        del data_copy[0]
        for point in data_copy:
            point_avant = self.__points[-1]
            self.__points.append(Point(point[1],point[2], point_avant))
        self.__points[0].setTrigoPoint(self.__points[-1])

    def __creationDroites(self):
        for point in self.getPoints():
            place=0
            for droite in self.getDroites():
                if (abs(point.getCoefDirecteur()-droite.getCoefDirecteurMoy())<700 and 
                    abs(droite.compareAnglePoint(point)) < 30 and
                    place==0):
                    if(point.getDistanceEntrePoints(droite.getPoints()[-1])<400):
                        droite.addPoint(point)
                        place=1
                        break
            if place==0:
                self.addDroite(Droite(point))
    


    def PlotPoints(self, liste_points, marqueur='--', type='normal', text='no'):
        x=[]
        y=[]
        for i in range(len(liste_points)):
            point=liste_points[i]
            if type=='lissage':
                x.append(point.getXLisse())
                y.append(point.getYLisse())
            else:
                x.append(point.getX())
                y.append(point.getY())
            if text=='yes':
                plt.annotate(str(round(point.getX()))+'|'+str(round(point.getY()))+':'+str(round(point.getDistanceEntrePoints(liste_points[i-1]))),(point.getX(),point.getY()))
        plt.plot(x,y,marqueur)

    def PlotDroitesMoy(self):
        for droite in self.getDroites():
            if len(droite.getPoints())>20:
                self.PlotDroiteMoy(droite.getCoefDirecteurMoy(), droite.getOrdonneeOrigineMoy())


    def PlotDroiteMoy(self, a, b, marqueur='-'):
        x=[-4000,0, 4000]
        y=[a*xpoint+b for xpoint in x]
        plt.plot(x,y, marqueur)

    def PlotTangente(self, liste_points):
        for point in self.getPoints():
            [a,b] = point.getTangente()
            X=point.getXLisse()
            Y=point.getYLisse()
            x=[X-100, X, X+100]
            y=[a*xpoint+b for xpoint in x]
            if(abs(y[0]-y[2])<1000):
                plt.plot(x,y)


    def PlotDroites(self):
        print(len(self.getDroites()))
        colors = ['k','g','b','r','c','m','y']
        i=0
        for droite in self.getDroites():
            if len(droite.getPoints())>20:
                color=colors[i%len(colors)]
                i+=1
                self.PlotPoints(droite.getPoints(), color+'o', text='no', type="lissage")
                self.PlotDroiteMoy(droite.getCoefDirecteurMoy(), droite.getOrdonneeOrigineMoy(), color+'-')

    
main = Main()
# main.PlotPoints(main.getPoints(), 'o')
main.PlotPoints(main.getPoints(), 'o', 'lissage')
# main.PlotTangente(main.getPoints())

# main.PlotDroites()
# main.PlotDroitesMoy()
plt.show()