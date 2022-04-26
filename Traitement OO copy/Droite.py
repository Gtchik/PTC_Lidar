from cmath import pi
from numpy import arctan
from Point import Point
from typing import TypeVar
Point = TypeVar("Point")
class Droite:
    # Liste<Point> __points
    def __init__(self, point:Point = None) -> None:
        self.__points=[]
        if point!=None:
            self.addPoint(point)

    def addPoint(self, point:Point):
        self.__points.append(point)
    
    def getPoints(self) -> list:
        return self.__points
    
    def getCoefDirecteurMoy(self):
        sum=0
        for point in self.getPoints():
            sum+=point.getCoefDirecteur()
        return sum/len(self.getPoints())

    def getOrdonneeOrigineMoy(self):
        sum=0
        for point in self.getPoints():
            sum+=point.getOrdonneeOrigine()
        return sum/len(self.getPoints())

    def getRegLin(self):
        x=[]
        y=[]
        if len(self.getPoints())>1:
            for point in self.getPoints():
                x.append(point.getXLisse())
                y.append(point.getYLisse())
            # initialisation des sommes
            x_sum = 0.
            x2_sum = 0.
            y_sum = 0.
            xy_sum = 0.
            # calcul des sommes
            for xi, yi in zip(x, y):
                x_sum += xi
                x2_sum += xi**2
                y_sum += yi
                xy_sum += xi * yi
            # nombre de points
            npoints = len(x)
            # print(npoints, npoints * x2_sum, x_sum**2, npoints * x2_sum - x_sum**2)
            # calcul des paramétras
            a = (npoints * xy_sum - x_sum * y_sum) / (npoints * x2_sum - x_sum**2)
            b = (x2_sum * y_sum - x_sum * xy_sum) / (npoints * x2_sum - x_sum**2)
        else:
            a=self.getCoefDirecteurMoy()
            b=self.getOrdonneeOrigineMoy()
        # renvoie des parametres
        return (a, b)
    
    def compareAnglePoint(self, apoint:int, unit:str = "degre") -> int:
        coef_tang = apoint
        coef_droite = self.getRegLin()[0]
        angle = arctan(abs((coef_droite-coef_tang)/(1+coef_tang*coef_droite)))
        if unit=="degre":
            angle=angle*180/pi
        return angle
