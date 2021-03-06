#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot 


class LekeBot(Robot):
    
    def sensors(self):  #Nødvendig for å kunne observere arenaen
        pass

    def init(self):     # Pimp Din Bot    
        #(Rød, Gul, Blå) i verdier fra 0 til 255
        self.setColor(0, 0, 0)
        self.setGunColor(255, 255, 255)
        self.setRadarColor(0, 0, 0)
        self.setBulletsColor(200, 200, 200)
        self.radarVisible(True)
        self.setRadarField("thin") #Change the radar field form
        size = self.getMapSize() #get the map size

    def run(self):     
        # Skriv din kode her for å gi roboten den oppførselen du ønsker
        self.pause(10)
        self.radarTurn(180) #to turn the radar (negative values turn counter-clockwise)
        self.gunTurn(180);
        self.move(50);
        self.turn(30); 
  
    def onHitWall(self):
        # Erstatt "pass" med den oppførselen du ønsker 
        # at roboten skal ha når den treffer veggen.  
        pass

    def onRobotDeath(self):
        pass      
    
    def onTargetSpotted(self, botId, botName, botPos):
        self.fire(1)
        self.move(20)
        self.pause(10)

#tester gerfra treffer av kuler 
  
    def onRobotHit(self, robotId, robotName):
            self.rPrint("jeg traff en bot")

    def onHitWall(self):
        self.rPrint("au, jeg traff veggen")


    def onHitByBullet(self, bulletBotId, bulletBotName, bulletPower): #NECESARY FOR THE GAME
        self.rPrint("ble truffet av en kule")

    def onBulletHit(self, botId, bulletId):#NECESARY FOR THE GAME
        self.rPrint("yey")

    def onBulletMiss(self, bulletId):
        self.rPrint("jeg misset!")

#tester treffer roboter 
    def onHitByRobot(self, robotId, robotName):
        self.rPrint("jeg ble truffet av en bot")

    def onRobotHit(self, robotId, robotName):
        self.rPrint("jeg traff en bot")

    def onHitWall(self):
        self.rPrint("au, jeg traff veggen")

