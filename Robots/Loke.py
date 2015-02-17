#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot 


class Loke(Robot):
    
    def sensors(self):  #Nødvendig for å kunne observere arenaen
        pass

    def init(self):     # Pimp Din Bot    
        #(Rød, Gul, Blå) i verdier fra 0 til 255
        self.setColor(0, 0, 0)
        self.setGunColor(255, 255, 255)
        self.setRadarColor(0, 0, 0)
        self.setBulletsColor(200, 200, 200)

    
    def run(self):     
        # Skriv din kode her for å gi roboten den oppførselen du ønsker
        self.pause(10)      
        self.move(30)
        self.turn(90)
        self.fire(4)
        self.gunTurn(40)
        self.fire(4)
        self.gunTurn(40)
        self.fire(4)
    
  
    def onHitWall(self):
        # Erstatt "pass" med den oppførselen du ønsker 
        # at roboten skal ha når den treffer veggen.  
        self.turn(90)
        self.move(30)
        selv.turn(90)
        
    def onRobotDeath(self):
        self.rPrint ("Til Valhall!")  
        
      
