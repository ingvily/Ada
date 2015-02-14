#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot 
import math


class HardBot(Robot):
    
    def init(self):     # Pimp Your Bot
        
        
        #(Rød, Gul, Blå) fra 0 til 256
        self.setColor(254, 0, 0)
        self.setGunColor(200, 200, 0)
        self.setRadarColor(255, 60, 0)
        self.setBulletsColor(0, 200, 100)

        self.radarVisible(True) # if True the radar field is visible
        
        #get the map size
        size = self.getMapSize()
        
        self.lockRadar("gun")

        self.setRadarField("thin")
        self.inTheCorner = False
    
    def run(self):      #main loop to command the bot
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
            self.stop()
        else:
            angle = self.getGunHeading()
            if angle < 315:
                self.gunTurn(315 - angle)
            elif angle > 315:
                self.gunTurn(angle-315)
            self.inTheCorner = True    

    def sensors(self): 
        """Tick each frame to have datas about the game"""        
        pos = self.getPosition() #return the center of the bot
        x = pos.x() #get the x coordinate
        y = pos.y() #get the y coordinate
        
        angle = self.getGunHeading() #Returns the direction that the robot's gun is facing
        angle = self.getHeading() #Returns the direction that the robot is facing
        angle = self.getRadarHeading() #Returns the direction that the robot's radar is facing
        list = self.getEnemiesLeft() #return a list of the enemies alive in the battle
        for robot in list:
            id = robot["id"]
            name = robot["name"]
            # each element of the list is a dictionnary with the bot's id and the bot's name
        
    def onHitWall(self):
        self.reset() #To reset the run fonction to the begining (auomatically called on hitWall, and robotHit event) 
        self.pause(100)
        self.move(-100)
        self.rPrint('ouch! a wall !')
    
    def onTargetSpotted(self, botId, botName, botPos):
        "when the bot see another one"
        self.setRadarField("thin")
        self.rPrint("I see the bot:" + str(botId) + "on position: x:" + str(botPos.x()) + " , y:" + str(botPos.y()))
        self.gunTurn(5)

        self.stop()
        self.fire(5)
        
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
