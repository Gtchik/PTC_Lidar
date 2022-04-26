from math import cos, pi, sqrt, sin
from typing import TypeVar
Point = TypeVar("Point")

class Point:
    # int __alpha
    # int __phi
    # Point __trigo_point
    # Point __anti_trigo_point

    def __init__(self, alpha:int, phi:int, trigo_point:Point = None) -> None:
        self.__alpha =alpha*pi/180
        self.__phi = phi
        if (trigo_point!=None):
            self.setTrigoPoint(trigo_point)
        # self.__setTrigoDistance()
            

    def setAlpha(self, alpha) -> None:
        self.__alpha = alpha
    def getAlpha(self) -> int:
        return self.__alpha
    def getAlphaDegre(self) -> int:
        return self.__alpha*180/pi
    def setPhi(self, phi) -> None:
        self.__phi = phi
    def getPhi(self) -> int:
        return self.__phi

    def setTrigoPoint(self, trigo_point:Point) -> None:
        self.__trigo_point = trigo_point
        self.__trigo_point.setAntiTrigoPoint(self)
    def getTrigoPoint(self) -> Point:
        return self.__trigo_point

    def setAntiTrigoPoint(self, anti_trigo_point:Point) -> None:
        self.__anti_trigo_point = anti_trigo_point
    def getAntiTrigoPoint(self) -> Point:
        return self.__anti_trigo_point

    def getX(self) -> int:
        return self.getPhi()*sin(self.getAlpha())
    def getY(self) -> int:
        return self.getPhi()*cos(self.getAlpha())

    def getXLisse(self) -> int:
        return (1*self.getTrigoPoint().getTrigoPoint().getX() + 
                    self.getTrigoPoint().getX() + 
                    self.getX() + 
                    self.getAntiTrigoPoint().getX()+
                1*self.getAntiTrigoPoint().getAntiTrigoPoint().getX())/5
    def getYLisse(self) -> int:
        return (1*self.getTrigoPoint().getTrigoPoint().getY() + 
                    self.getTrigoPoint().getY() + 
                    self.getY() + 
                    self.getAntiTrigoPoint().getY()+
                1*self.getAntiTrigoPoint().getAntiTrigoPoint().getY())/5

    def getCoefDirecteur(self) -> int:
        return (self.getYLisse()-self.getTrigoPoint().getYLisse())/(self.getXLisse()-self.getTrigoPoint().getXLisse())

    def getOrdonneeOrigine(self) -> int:
        return self.getYLisse()-self.getCoefDirecteur()*self.getXLisse()

    def getTangente(self) -> list:
        return [self.getCoefDirecteur(), self.getOrdonneeOrigine()]

    def getRegLin(self):
        x=[self.getAntiTrigoPoint().getXLisse(), self.getXLisse(), self.getTrigoPoint().getXLisse()]
        y=[self.getAntiTrigoPoint().getYLisse(), self.getYLisse(), self.getTrigoPoint().getYLisse()]
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
        # calcul des paramétras
        a = (npoints * xy_sum - x_sum * y_sum) / (npoints * x2_sum - x_sum**2)
        b = (x2_sum * y_sum - x_sum * xy_sum) / (npoints * x2_sum - x_sum**2)
        # renvoie des parametres
        return a, b
       
    def getTrigoDistance(self) -> int:
        trigo_x = self.getTrigoPoint().getX()
        trigo_y = self.getTrigoPoint().getY()
        x = self.getX()
        y = self.getY()
        trigo_distance = sqrt((x-trigo_x)**2 + (y-trigo_y)**2)
        return trigo_distance
    
    def getAntiTrigoDistance(self) -> int:
        trigo_x = self.getAntiTrigoPoint().getX()
        trigo_y = self.getAntiTrigoPoint().getY()
        x = self.getX()
        y = self.getY()
        anti_trigo_distance = sqrt((trigo_x-x)**2 + (trigo_y-y)**2)
        return anti_trigo_distance

    def getDistanceEntrePoints(self, point:Point) -> int:
        point_x = point.getX()
        point_y = point.getY()
        x = self.getX()
        y = self.getY()
        distance = sqrt((point_x-x)**2 + (point_y-y)**2)
        return distance
