#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot 
import math


class HardBot(Robot):
    
    def init(self):    

        #(Rød, Gul, Blå) i verdier fra 0 til 255
        self.setColor(250, 10, 20)
        self.setGunColor(0, 0, 0)
        self.setRadarColor(200, 100, 0)
        self.setBulletsColor(100, 150, 250)
        
        self.radarVisible(True) 

        size = self.getMapSize()
        
        self.lockRadar("gun")
        self.setRadarField("thin")
        self.inTheCorner = False
        

    
    def run(self): 
        
        pos = self.getPosition()
        if pos.x() > 50 or pos.y() > 50:
            angle = self.getHeading()
            a = 90 + math.degrees(math.acos(pos.x()/math.sqrt(pos.x()**2+pos.y()**2)))
            if angle < a:
                self.turn(a-angle)
            elif angle > a-0.5:
                self.turn(angle-a)
            self.stop()
            self.move(10)
            self.gunTurn(30)
            self.stop()
        else:
            angle = self.getGunHeading()
            if angle < 315:
                self.gunTurn(315 - angle)
            elif angle > 315:
                self.gunTurn(angle-315)
            self.inTheCorner = True

    def onHitWall(self):
        self.reset()        #vil resette run-metoden 
        self.pause(100)
        self.move(-100)
        self.rPrint('au!')

    def sensors(self): 
        pass
        
    def onRobotHit(self, robotId, robotName): 
        pass
        
    def onHitByRobot(self, robotId, robotName):
        pass

    def onHitByBullet(self, bulletBotId, bulletBotName, bulletPower): 
        self.move(20)
        
    def onBulletHit(self, botId, bulletId):
        pass
        
    def onBulletMiss(self, bulletId):
        pass
        
    def onRobotDeath(self):
        pass
        
    def onTargetSpotted(self, botId, botName, botPos):#NECESARY FOR THE GAME
        self.setRadarField("thin")
        self.gunTurn(5)

        self.stop()
        self.fire(5)
