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
    
    def compareAnglePoint(self, point:Point, unit:str = "degre") -> int:
        coef_tang = point.getCoefDirecteur()
        coef_droite = self.getCoefDirecteurMoy()
        angle = arctan(abs((coef_droite-coef_tang)/(1+coef_tang*coef_droite)))
        if unit=="degre":
            angle=angle*180/pi
        return angle
