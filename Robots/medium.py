#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot 


class MediumBot(Robot):
    
    def init(self):    
        
<<<<<<< HEAD
        
        #(Rød, Gul, Blå) fra 0 til 256
=======
        #(Rød, Gul, Blå) i verdier fra 0 til 255
>>>>>>> 2ab292d... Endret easy-medium-hard-roboter
        self.setColor(0, 200, 100)
        self.setGunColor(200, 200, 0)
        self.setRadarColor(255, 60, 0)
        self.setBulletsColor(255, 150, 150)

        self.radarVisible(True) 
        
        size = self.getMapSize()
        
        self.lockRadar("gun")
        
    
<<<<<<< HEAD
    def run(self):      #main loop to command the bot
        self.stop()
       
    def sensors(self): 
        """Tick each frame to have datas about the game"""
         
    def onTargetSpotted(self, botId, botName, botPos):
        "when the bot see another one"
        
    def onRobotDeath(self):#NECESARY FOR THE GAME
        """When my bot die"""
        self.rPrint ("damn I'm Dead")
=======
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
>>>>>>> 2ab292d... Endret easy-medium-hard-roboter
