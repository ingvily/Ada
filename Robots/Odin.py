#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot 


class Odin(Robot):
    
    def sensors(self):  #Nødvendig for å kunne observere arenaen
        pass

    def init(self):     # Pimp Din Bot    
        #(Rød, Gul, Blå) i verdier fra 0 til 255
        self.setColor(0, 0, 0)
        self.setGunColor(153, 0, 0)
        self.setRadarColor(153, 0, 0)
        self.setBulletsColor(200, 200, 200)
        self.radarVisible(True) 
        self.setRadarField("thin")

    
    def run(self): 
        self.gunTurn(360)
        self.radarTurn(360)
        self.pause(2)
  
    def onHitWall(self):
        self.move(-100)
        self.turn(180)

    def onRobotDeath(self):
        self.rPrint ("Til Valhall!")  
        
       
    def onTargetSpotted(self, botId, botName, botPos):
        self.fire(6)

    def onHitByBullet(self, bulletBotId, bulletBotName, bulletPower):
        self.move(90)
        self.turn(90)
        self.gunTurn(360)
        self.radarTurn(360)

