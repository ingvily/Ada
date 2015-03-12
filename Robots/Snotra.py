#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot 


class Snotra(Robot):
    
    def sensors(self):  #Nødvendig for å kunne observere arenaen
        pass

    def init(self):     # Pimp Din Bot    
        #(Rød, Gul, Blå) i verdier fra 0 til 255
        self.setColor(150, 150, 150)
        self.setGunColor(70, 70, 70)
        self.setRadarColor(0, 0, 0)
        self.setBulletsColor(200, 200, 200)
        self.radarVisible(True) 
        self.setRadarField("thin")

    
    def run(self):     
        # Skriv din kode her for å gi roboten den oppførselen du ønsker
        self.move(50)
        self.turn(70)
        self.radarTurn(70)
        self.gunTurn(70)
        self.move(90)


    def onTargetSpotted (self, botId, botName, botPos):
        self.rPrint("Exterminate!")
        self.fire(6)
        

    def onBulletMiss(self, bulletId):
        self.turn(20)
        self.gunTurn(20)
        self.radarTurn(20)
        
  
    def onHitWall(self):
        # Erstatt "pass" med den oppførselen du ønsker 
        # at roboten skal ha når den treffer veggen.  
        self.move(-100)
        self.turn(90)
        self.gunTurn(90)
        self.radarTurn(90)
      

    def onHitByRobot(self, robotId, robotName):
        self.move(-70)

    def onRobotHit(self, robotId, robotName):
        self.move(-70)

    def onHitByBullet(self):
        self.move(50)
        self.fire(1)
        
    def onRobotDeath(self):
        self.rPrint ("Til evighten og forbi!! ^..")  
        
      
