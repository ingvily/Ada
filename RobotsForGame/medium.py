#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot 


class MediumBot(Robot):
    
    def init(self):     # Pimp Your Bot
        
        
        #(Rød, Gul, Blå) fra 0 til 256
        self.setColor(0, 200, 100)
        self.setGunColor(200, 200, 0)
        self.setRadarColor(255, 60, 0)
        self.setBulletsColor(0, 200, 100)

    
    def run(self):      #main loop to command the bot
        self.stop()
       
    def sensors(self): 
        """Tick each frame to have datas about the game"""
         
    def onTargetSpotted(self, botId, botName, botPos):
        "when the bot see another one"
        
    def onRobotDeath(self):#NECESARY FOR THE GAME
        """When my bot die"""
        self.rPrint ("damn I'm Dead")
