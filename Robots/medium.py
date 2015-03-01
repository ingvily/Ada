#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot 


class MediumBot(Robot):
    
    def init(self):    
        
        #(Rød, Gul, Blå) i verdier fra 0 til 255
        self.setColor(0, 0, 0)
        self.setGunColor(0, 0, 0)
        self.setRadarColor(255, 60, 0)
        self.setBulletsColor(255, 255, 255)

        self.radarVisible(True) 
        
        size = self.getMapSize()
        
        self.lockRadar("gun")
        
    
    def run(self): 
        self.gunTurn(180)
        self.stop()


    def onHitWall(self):
        pass

    def sensors(self): 
        pass
        
    def onRobotHit(self, robotId, robotName): 
        pass
        
    def onHitByRobot(self, robotId, robotName):
        pass

    def onHitByBullet(self, bulletBotId, bulletBotName, bulletPower): 
        pass
        
    def onBulletHit(self, botId, bulletId):
        pass

    def onBulletMiss(self, bulletId):
        pass

    def onRobotDeath(self):
        pass

    def onTargetSpotted(self, botId, botName, botPos):
        self.setRadarField("thin")
        self.stop()
        self.fire(3)
