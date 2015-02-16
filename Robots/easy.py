#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot 


class EasyBot(Robot):
    
    def init(self):     # Pimp Your Bot
        
        #(Rød, Gul, Blå) fra 0 til 256
        self.setColor(0, 200, 100)
        self.setGunColor(200, 200, 0)
        self.setRadarColor(254, 60, 0)
        self.setBulletsColor(0, 200, 100)

    
    def run(self):      #main loop to command the bot
        self.move(50)
        self.fire(2) # To Fire (power between 1 and 10)
        self.stop()

        self.turn(50)
        self.gunTurn(50)
        self.fire(2) # To Fireioioio (power between 1 and 10)
        self.stop()

        self.move(-30)

    def sensors(self): 
        """Tick each frame to have datas about the game"""
    
    def onHitWall(self):
        pass

    def onTargetSpotted(self, botId, botName, botPos):
        "when the bot see another one"
        pass 
        
    def onRobotDeath(self):#NECESARY FOR THE GAME
        """When my bot die"""
        self.rPrint ("damn I'm Dead")

    def onHitByBullet(self, bulletBotId, bulletBotName, bulletPower): #NECESARY FOR THE GAME
        pass
        
    def onBulletHit(self, botId, bulletId):#NECESARY FOR THE GAME
        pass
        
    def onBulletMiss(self, bulletId):
        pass

    def onRobotHit(self, robotId, robotName): # when My bot hit another
        pass

