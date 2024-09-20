import pygame
white = (255, 255, 255)
pygame.init() 
font = pygame.font.Font("AnonymousPro-Regular.ttf", 20)
colorActive = pygame.Color("#808080")  
colorPassive = pygame.Color("#FFFFFF") 
width=100
height=20
class textbox:
    def __init__(self, x,y,label,word):
        self.x=x
        self.y=y
        self.label=label
        self.color=colorPassive
        self.word=word
            
    
    def drawing(self,window):
        rect = pygame.Rect(self.x, self.y+height, width, height) 
        text = font.render(self.label, False, white)
        textRect = text.get_rect()
        textRect.center = (self.x+(width/2), self.y)
        window.blit(text, textRect)
        pygame.draw.rect(window, self.color, rect) 
        
        textnew=self.word[-9:]
        text_surface = font.render(textnew, True, (0, 0, 0)) 
        window.blit(text_surface, (rect.x, rect.y)) 
        rect.w = max(300, text_surface.get_width()+10) 
        
    def clickedOn(self,window):
        self.color=colorActive
        self.drawing(window)  
        
    def resetColor(self,window):
        self.color=colorPassive
        self.drawing(window)      
    
    def keyInput(self,letter):
        if (self.color==colorActive):
            self.word+=letter   
            
    def delKey(self):
        if (self.color==colorActive):
            self.word = self.word[:-1]  
            
    def getVal(self):
        return self.word
        