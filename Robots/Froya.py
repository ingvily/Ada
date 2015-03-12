#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot 


class Froya(Robot):
    
    def sensors(self):  #Nødvendig for å kunne observere arenaen
        pass

    def init(self):     # Pimp Din Bot    
        #(Rød, Gul, Blå) i verdier fra 0 til 255
        self.setColor(255, 100, 23)
        self.setGunColor(29, 24, 255)
        self.setRadarColor(0, 0, 0)
        self.setBulletsColor(255, 22, 19)
        self.radarVisible(True) 
        self.setRadarField("thin")

    
    def run(self):     
        # Skriv din kode her for å gi roboten den oppførselen du ønsker 
        #self.move(10)
        self.setColor(255, 100, 23)
        self.setGunColor(29, 24, 255)
        self.setRadarColor(0, 0, 0)
        self.turn(-5)
        self.radarTurn(-5)
        self.gunTurn(-5)

    def onTargetSpotted(self, botId, botName, botPos):
        self.fire(8)
        self.pause(2)
        self.turn(-5)
        self.radarTurn(-5)
        self.gunTurn(-5)

    def onHitByBullet(self, bulletBotId, bulletBotName, bulletPower):
        self.turn(-90)
        self.radarTurn(-90)
        self.gunTurn(-90)
        while not onHitWall(self):
            self.move(50)

  
    def onHitWall(self):
        self.move(-100)
        self.turn(180)
        self.radarTurn(180)
        self.gunTurn(180)
        
    def onRobotDeath(self):
        self.rPrint ("Til Valhall!")  
        
    def onHitByRobot(self, robotId, robotName):
        self.turn(90)
        self.move(50)

    def onBulletHit(self, botId, bulletId):
        self.rPrint("Ta den, du!")
        self.setColor(255, 0, 70)
        self.setGunColor(255, 0, 70)
        self.setRadarColor(255, 0, 70)



