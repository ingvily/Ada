#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot 


class LF(Robot):
    
    def sensors(self):  #Nødvendig for å kunne observere arenaen
        pass

    def init(self):     # Pimp Din Bot    
        #(Rød, Gul, Blå) i verdier fra 0 til 255
        self.setColor(0, 0, 0)
        self.setGunColor(255, 255, 255)
        self.setRadarColor(0, 0, 0)
        self.setBulletsColor(200, 200, 200)

        size = self.getMapSize() 

    
    def run(self):     
        # Skriv din kode her for å gi roboten den oppførselen du ønsker
        self.move(360)
        self.turn(360)
        self.fire(2)
        self.pause(10) 
    
  
    def onHitWall(self):
        # Erstatt "pass" med den oppførselen du ønsker 
        # at roboten skal ha når den treffer veggen.  
        self.move(-100)

    def onHitByBullet(self, bulletBotId, bulletBotName, bulletPower): 
        self.move(100)
        self.turn(50)
        self.stop()
        self.gunTurn(360)

    def onTargetSpotted(self, botId, botName, botPos):
        self.gunTurn(3)
        self.fire(5)

    def onRobotDeath(self):
        self.rPrint ("Til Valhall!")  


       