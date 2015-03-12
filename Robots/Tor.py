#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot 


class Tor(Robot):

    position = 90
       
    def sensors(self):  #Nødvendig for å kunne observere arenaen
        pass

    def init(self):     # Pimp Din Bot    
        #(Rød, Gul, Blå) i verdier fra 0 til 255
        self.setColor(232, 46, 117)
        self.setGunColor(255, 0, 0)
        self.setRadarColor(0, 200, 0)
        self.setBulletsColor(200, 200, 200)
        self.radarVisible(True) 
        self.setRadarField("thin")

    
    def run(self):     
        #self.radarTurn(180)# Skriv din kode her for å gi roboten den oppførselen du ønsker
        self.move(40)
        self.turn(30)
        self.radarTurn(30)
        self.gunTurn(30)
    
    def onTargetSpotted(self, botId, botName, botPos):
        self.fire(3)
        self.pause(10)
  
    def onHitWall(self):
        self.move(-90)
        self.stop()

        self.turn(90)
        self.radarTurn(90)
        self.gunTurn(90)
        #self.move(-90)
        #self.pause(2)
        
    def onRobotDeath(self):
        self.rPrint ("Til Valhall!")  
    
    def onBulletHit(self, botId, bulletId):
        self.setColor(200, 0, 0)
        self.fire(4)
        

    def onBulletMiss(self, bulletId):
        self.setColor(0, 0, 200)
        self.turn(40)
        self.radarTurn(40)
        self.gunTurn(40)
        return True 

    def onHitByBullet(self, bulletBotId, bulletBotName, bulletPower):
        self.setColor(0, 0, 153)
        self.turn(-30)
        self.move(90)
        self.radarTurn(-30)
        self.gunTurn(-30)


