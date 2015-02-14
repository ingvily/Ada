#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot 


class MediumBot(Robot):
    
    def init(self):     # Pimp Your Bot
        
        
        #(Rød, Gul, Blå) fra 0 til 256
        self.setColor(0, 0, 254)
        self.setGunColor(200, 200, 0)
        self.setRadarColor(255, 60, 0)
        self.setBulletsColor(0, 200, 100)

    
    def run(self):      #main loop to command the bot

        self.move(90) # for moving (negative values go back)
        self.turn(300) #for turning (negative values turn counter-clockwise)
        self.stop()

        self.gunTurn(3)
        self.fire(3)
        self.stop()
        """
        the stop command is used to make moving sequences: here the robot will move 90steps and turn 360° at the same time
        and next, fire
        """
       
    def sensors(self): 
        """Tick each frame to have datas about the game"""
         
    def onTargetSpotted(self, botId, botName, botPos):
        "when the bot see another one"
        self.gunTurn(5)
        self.stop()
        self.fire(5)
        
    def onRobotDeath(self):#NECESARY FOR THE GAME
        """When my bot die"""
        self.rPrint ("damn I'm Dead")

    def onHitWall(self):
        self.reset() #To reset the run fonction to the begining (auomatically called on hitWall, and robotHit event) 
        self.pause(100)
        self.move(-100)

    def onHitByBullet(self, bulletBotId, bulletBotName, bulletPower): #NECESARY FOR THE GAME
        pass
        
    def onBulletHit(self, botId, bulletId):#NECESARY FOR THE GAME
        pass
        
    def onBulletMiss(self, bulletId):
        pass

    def onRobotHit(self, robotId, robotName): # when My bot hit another
        pass

