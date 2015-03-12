#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot 


class Idunn(Robot):
    
    def sensors(self):  #Nødvendig for å kunne observere arenaen
        pass

    def init(self):
        #(Rød, Gul, Blå) i verdier fra 0 til 255
        self.setColor(100, 100, 255)
        self.setGunColor(255, 0, 0)
        self.setRadarColor(0, 0, 0)
        self.setBulletsColor(200, 200, 200)
        self.radarVisible(True) 
        self.setRadarField("thin")
    
    def run(self):
        #self.move(100)

        # Skriv din kode her for å gi roboten den oppførselen du ønsker
        #self.pause(10)   

        for i in range (0,359):
            self.radarTurn(2*i)
            self.gunTurn(2*i)
            self.move(3)
            self.pause(1)


    def onBulletMiss(self, bulletId):
        self.fire(0)

    def onHitByBullet(self, bulletBotId, bulletBotName, bulletPower):
        for i in range(0,89):
            self.move(3*i)
            self.turn(3*i)
        #    self.radarTurn(3*i)
        #    self.gunTurn(3*i)


  
    def onHitWall(self):
        self.move(-150)
        self.turn(180)
        self.radarTurn(180)
        self.gunTurn(180)

        # Erstatt "pass" med den oppførselen du ønsker 
        # at roboten skal ha når den treffer veggen.  

    def onRobotHit(self):
        self.move(-100)

        
    def onRobotDeath(self):
        self.rPrint ("Til Valhall!")

    def onTargetSpotted(self, botId, botName, botPos):
        self.fire(1)
       # if onBulletMiss:
        #    self.fire(0)
        #else:
         #   self.fire(2)


