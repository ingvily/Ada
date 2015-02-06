#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot 


class BaseBot(Robot):
    
    def init(self):     # Pimp Your Bot
        
        
        #(Rød, Gul, Blå) fra 0 til 256
        self.setColor(0, 0, 0)
        self.setGunColor(256, 256, 256)
        self.setRadarColor(0, 0, 0)
        self.setBulletsColor(0, 0, 0)

    
    def run(self):      #main loop to command the bot
        self.stop()
       
    def sensors(self): 
        """Tick each frame to have datas about the game"""
         
    def onTargetSpotted(self, botId, botName, botPos):
        "when the bot see another one"
        
    def onRobotDeath(self):#NECESARY FOR THE GAME
        """When my bot die"""
        self.rPrint ("damn I'm Dead")
