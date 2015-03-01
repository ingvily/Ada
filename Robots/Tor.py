#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot 


class Tor(Robot):
       
    def sensors(self):  #Nødvendig for å kunne observere arenaen
        pass

    def init(self):     # Pimp Din Bot    
        #(Rød, Gul, Blå) i verdier fra 0 til 255
        self.setColor(0, 0, 153)
        self.setGunColor(255, 255, 255)
        self.setRadarColor(0, 0, 0)
        self.setBulletsColor(200, 200, 200)

    
    def run(self):     
        # Skriv din kode her for å gi roboten den oppførselen du ønsker
        self.pause(10)      
    
  
    def onHitWall(self):
        # Erstatt "pass" med den oppførselen du ønsker 
        # at roboten skal ha når den treffer veggen.  
        pass
        
    def onRobotDeath(self):
        self.rPrint ("Til Valhall!")  
        
      
