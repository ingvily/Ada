#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot 


class Loke(Robot):
    
    def sensors(self):  #Nødvendig for å kunne observere arenaen
        pass

    def init(self):
        #(Rød, Gul, Blå) i verdier fra 0 til 255
        self.setColor(100, 128, 28)
        self.setGunColor(128, 0, 0)
        self.setRadarColor(50, 50, 50)
        self.setBulletsColor(230, 200, 210)
        self.radarVisible(True) 
        self.setRadarField("thin")

    
    def run(self):     
        # Skriv din kode her for å gi roboten den oppførselen du ønsker
        self.radarTurn(-10)
        self.move(10)
        self.gunTurn(-10)
        self.turn(-10)

    def onTargetSpotted(self, bitId, botName, botPos):
        self.fire(5)
        self.pause(5)
        
  
    def onHitWall(self):
        # Erstatt "pass" med den oppførselen du ønsker 
        # at roboten skal ha når den treffer veggen.  
        self.move(-20)
       # self.turn(90)

    def onRobotHit(self, robotId, robotName):
        self.gunTurn(0)
        self.fire(2)
        self.move(20)
        
    def onRobotDeath(self):
        self.rPrint ("Til Valhall!")

    def onHitByRobot(self, robotId, robotName):
        self.move(-20)
        self.turn(45)
        self.move(50)

    def onBulletMiss(self, bulletId):
        self.move(30)


    def onBulletHit(self, botId, bulletId):
        self.fire(2)

    def onHitByBullet(self, bulletBotId, bulletBotName, bulletPower):
        self.turn(20)
        self.move(50)

