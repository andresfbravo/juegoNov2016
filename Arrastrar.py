import os,sys
import pygame
import random

ANCHO = 1200
ALTO = 650

BLANCO = [250,250,250]
NEGRO = [0,0,0]
ROJO = [250,0,0]
AZUL = [0,0,250]
##############################FONDO#####################################
class kfondo(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("ffondo.jpg").convert_alpha() #dibujo de snoppy
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y

class inter(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("carrf/ver-hor2.jpg").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y

class horizontal(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("carrf/horizontal.jpg").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y

class vertical(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("carrf/vertical1.jpg").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y

class esAbDer(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("carrf/ab-der.jpg").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y

class esArIzq(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("carrf/arr-iz.jpg").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y

class esIzqAb(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("carrf/izq-ab.jpg").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y

class esArDer(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("carrf/arr-der.jpg").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y

class verHor(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("carrf/ver-hor.jpg").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
####################################JUGADOR#######################################
class jugador(pygame.sprite.Sprite):
    choque=None
    def __init__(self, x, y):   #constructor
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("juga/bebe.jpg").convert_alpha() 
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.x=x
        self.y=y
        self.rect.y=y
        self.var_x=0
        self.var_y=0
        self.limi1x=200
        self.limi1y=245
        self.limi2x=575
        self.limi2y=245
        self.limi3x=575
        self.limi3y=95
        self.limi4x=1015
        self.limi4y=95
        self.limi5x=1015
        self.limi5y=345
        self.limi6x=435
        self.limi6y=345
        self.limi7x=435
        self.limi7y=415
        self.limi8x=195
        self.limi8y=415
        self.sonido=pygame.mixer.Sound("explosion.wav")
        
        #self.vida=20

    def golpe(self):
    	self.var_x=0
    	self.var_y=0
    	self.sonido.play()
    	#surface.blit(self.image,self.rect)

        
    def update(self,surface):
        #ls_golpes=pygame.sprite.spritecollide(self, self.choque,False)
        if ((self.rect.top == 0) and (self.rect.left==self.limi1x)):
            self.var_y=1
            self.var_x=0
        
        if ((self.rect.top == self.limi1y) and (self.rect.left==self.limi1x)):
            self.var_y=0
            self.var_x=1
        
        if ((self.rect.left == self.limi2x)and(self.rect.top == self.limi2y)):
            self.var_y=-1
            self.var_x=0

        if ((self.rect.top == self.limi3y)and(self.rect.left==self.limi3x)):
            self.var_y=0
            self.var_x=1

        if ((self.rect.left == self.limi4x)and(self.rect.top==self.limi4y)):
            self.var_y=1
            self.var_x=0

        if ((self.rect.left == self.limi5x)and(self.rect.top==self.limi5y)):
            self.var_y=0
            self.var_x=-1

        if ((self.rect.left == self.limi6x)and(self.rect.top==self.limi6y)):
            self.var_y=1
            self.var_x=0

        if ((self.rect.left == self.limi7x)and(self.rect.top==self.limi7y)):
            self.var_y=0
            self.var_x=-1

        if ((self.rect.left == self.limi8x)and(self.rect.top==self.limi8y)):
            self.var_y=1
            self.var_x=0

        if ((self.rect.left == self.limi8x)and(ALTO-self.rect.height==self.rect.top)):
            self.var_y=0
            self.var_x=0
        
        self.rect.x += self.var_x
        self.rect.y += self.var_y
        surface.blit(self.image,self.rect)

#######################################AYUDAS##############################################
class Pare(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image  = pygame.image.load("ayudas/pare.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.click = False
        self.rect.x = x
        self.rect.y = y
        self.id = 0

    def golpe(self):
		pass

    def update(self,surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        surface.blit(self.image,self.rect)    


class Agua(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image  = pygame.image.load("ayudas/agua.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.click = False
        self.rect.x = x
        self.rect.y = y
        self.id = 0

    def golpe(self):
		pass

    def update(self,surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        surface.blit(self.image,self.rect)


class Perro(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image  = pygame.image.load("ayudas/perro.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.click = False
        self.rect.x = x
        self.rect.y = y
        self.id = 0

    def golpe(self):
		pass

    def update(self,surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        surface.blit(self.image,self.rect)


class Policia(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image  = pygame.image.load("ayudas/policia.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.click = False
        self.rect.x = x
        self.rect.y = y
        self.id = 0

    def golpe(self):
		pass

    def update(self,surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        surface.blit(self.image,self.rect)


class Puente(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image  = pygame.image.load("ayudas/puente.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.click = False
        self.rect.x = x
        self.rect.y = y
        self.id = 0

    def golpe(self):
		pass

    def update(self,surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        surface.blit(self.image,self.rect)

######################################parte del fono######################################
class tetero(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("ayudas/tete.jpg").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
######################################PELIGROS###############################################
class carro(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("peligros/carro.jpg").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.stop=False
		self.var_x=0
		self.var_y=0
		self.limi1x=0
		self.limi1y=178
		self.limi2x=198
		self.limi2y=178
		self.limi3x=198
		self.limi3y=98
		self.limi4x=368
		self.limi4y=98
		self.limi5x=368
		self.limi5y=0

	
	def update(self,surface): #nada

		if ((self.rect.left == 0) and (self.rect.top==self.limi1y)):
			
			self.var_y=0
			self.var_x=1
		
		if ((self.rect.top == self.limi2y) and (self.rect.left==self.limi2x)):
			self.var_y=-1
			self.var_x=0
		
		if ((self.rect.top == self.limi3y) and (self.rect.left==self.limi3x)):
			self.var_y=0
			self.var_x=1

		if ((self.rect.top == self.limi4y) and (self.rect.left==self.limi4x)):
			self.var_y=-1
			self.var_x=0

		if ((self.rect.bottom == 0) and (self.rect.left==self.limi4x)):
			print "hola5"
			self.var_y=0
			self.rect.y=178
			self.rect.x=0

		if (self.stop==True):
			self.var_x=0
			self.var_y=0
		
		self.rect.x += self.var_x
		self.rect.y += self.var_y
		surface.blit(self.image,self.rect)

                


class chuzos(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("peligros/hueco.jpg").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y

	def update(self,surface):
		surface.blit(self.image,self.rect)

class ladron(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("peligros/ladron.png").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y	

	def update(self,surface):
		surface.blit(self.image,self.rect)

class raton(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("peligros/raton.jpg").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y	

	def update(self,surface):
		surface.blit(self.image,self.rect)

class fuego(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("peligros/fuego.jpg").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y

	def update(self,surface):
		surface.blit(self.image,self.rect)

##################################MUESTRA LA VICTORIA################################
class gano(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("gano.jpg").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y

##############################MUESTRA LA DERROTA###################################
class perdio(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("perdido.jpg").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y


if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pantalla=pygame.display.set_mode((ANCHO,ALTO))
    presentacion = pygame.image.load("Presentacion.jpg").convert()
    pantalla.blit(presentacion,(0,0))
    pygame.display.flip()

    I=False
    reloj=pygame.time.Clock()
    while not I:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:#si presiono barra espaciadora cambia al escenario el principio es la introduccion del juego
                    I=True 


    #pantalla.fill(BLANCO)
    Botonpare = Pare(498.75,408.75)      #cambie ayuda pare y los otros nombres por botonpare etc
    Botonagua = Agua(498.75,458.75)
    Botonperro = Perro(498.75,608.75)
    Botonpolicia = Policia(498.75,558.75)
    Botonpuente = Puente(498.75,508.75)


    listaayudas = pygame.sprite.Group()  #meto todas las ayudas que son los botones
    todos = pygame.sprite.Group()
    fondo=pygame.sprite.Group()
    fffondo=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()
    enemigo1=pygame.sprite.Group()
    enemigo2=pygame.sprite.Group()
    enemigo3=pygame.sprite.Group()
    enemigo4=pygame.sprite.Group()
    enemigo5=pygame.sprite.Group()
    jugador1=pygame.sprite.Group()
    final=pygame.sprite.Group()
    ganador1=pygame.sprite.Group()
    perdedor1=pygame.sprite.Group()

    haganado=gano(300,200)
    ganador1.add(haganado)
    #todos.add(haganado)

    haperdido=perdio(300,200)
    perdedor1.add(haperdido)
    #todos.add(haperdido)

    pfondo=kfondo(0,0)
    fffondo.add(pfondo)

    #intersecciones
    cen=inter(180,160)
    
    
    fondo.add(cen)
    #todos.add(cen)
    

    #verticales
    ver=vertical(180,0)
    ver1=vertical(180,10)
    verhor=verHor(180,80)
    ver2=vertical(180,100)
    ver3=vertical(350,0)
    ver4=vertical(350,10)
    ver5=vertical(180,470)
    ver6=vertical(180,540)
    ver7=vertical(180,610)
    ver8=vertical(560,150)
    ver9=vertical(560,160)
    ver10=vertical(1000,150)
    ver11=vertical(1000,220)
    ver12=vertical(1000,260)

    """
    todos.add(ver)
    todos.add(ver1)
    todos.add(verhor)
    todos.add(ver2)
    todos.add(ver3)
    todos.add(ver4)
    todos.add(ver5)
    todos.add(ver6)
    todos.add(ver7)
    todos.add(ver8)
    todos.add(ver9)
    todos.add(ver10)
    todos.add(ver11)
    todos.add(ver12)
    """

    fondo.add(ver)
    fondo.add(ver1)
    fondo.add(verhor)
    fondo.add(ver2)
    fondo.add(ver3)
    fondo.add(ver4)
    fondo.add(ver5)
    fondo.add(ver6)
    fondo.add(ver7)
    fondo.add(ver8)
    fondo.add(ver9)
    fondo.add(ver10)
    fondo.add(ver11)
    fondo.add(ver12)

    #horizontales
    hor=horizontal(0, 160)
    hor1=horizontal(70, 160)
    hor2=horizontal(110, 160)
    hor3=horizontal(250, 230)
    hor4=horizontal(320, 230)
    hor5=horizontal(390, 230)
    hor6=horizontal(460, 230)
    hor7=horizontal(490, 230)
    hor8=horizontal(630, 80)
    hor9=horizontal(700, 80)
    hor10=horizontal(770, 80)
    hor11=horizontal(840, 80)
    hor12=horizontal(910, 80)
    hor13=horizontal(930, 80)
    hor14=horizontal(250, 80)
    hor15=horizontal(280, 80)
    hor16=horizontal(250, 400)
    hor17=horizontal(320, 400)
    hor18=horizontal(350, 400)
    hor19=horizontal(490, 330)
    hor20=horizontal(560, 330)
    hor21=horizontal(630, 330)
    hor22=horizontal(700, 330)
    hor23=horizontal(770, 330)
    hor24=horizontal(840, 330)
    hor25=horizontal(910, 330)
    hor26=horizontal(930, 330)
    
    """
    todos.add(hor)
    todos.add(hor1)
    todos.add(hor2)
    todos.add(hor3)
    todos.add(hor4)
    todos.add(hor5)
    todos.add(hor6)
    todos.add(hor7)
    todos.add(hor8)
    todos.add(hor9)
    todos.add(hor10)
    todos.add(hor11)
    todos.add(hor12)
    todos.add(hor13)
    todos.add(hor14)
    todos.add(hor15)
    todos.add(hor16)
    todos.add(hor17)
    todos.add(hor18)
    todos.add(hor19)
    todos.add(hor20)
    todos.add(hor21)
    todos.add(hor22)
    todos.add(hor23)
    todos.add(hor24)
    todos.add(hor25)
    todos.add(hor26)
    """

    fondo.add(hor)
    fondo.add(hor1)
    fondo.add(hor2)
    fondo.add(hor3)
    fondo.add(hor4)
    fondo.add(hor5)
    fondo.add(hor6)
    fondo.add(hor7)
    fondo.add(hor8)
    fondo.add(hor9)
    fondo.add(hor10)
    fondo.add(hor11)
    fondo.add(hor12)
    fondo.add(hor13)
    fondo.add(hor14)
    fondo.add(hor15)
    fondo.add(hor16)
    fondo.add(hor17)
    fondo.add(hor18)
    fondo.add(hor19)
    fondo.add(hor20)
    fondo.add(hor21)
    fondo.add(hor22)
    fondo.add(hor23)
    fondo.add(hor24)
    fondo.add(hor25)
    fondo.add(hor26)

    #esquinas

    #abDe
    esqAbDe=esAbDer(180,400)
    esqAbDe1=esAbDer(420,330)
    esqAbDe2=esAbDer(560,80)
    """
    todos.add(esqAbDe)
    todos.add(esqAbDe1)
    todos.add(esqAbDe2)
    """

    fondo.add(esqAbDe)
    fondo.add(esqAbDe1)
    fondo.add(esqAbDe2)

    #arIz
    esqArrIzq=esArIzq(350,80)
    esqArrIzq1=esArIzq(560,230)
    esqArrIzq2=esArIzq(1000,330)
    esqArrIzq3=esArIzq(420,400)
    """
    todos.add(esqArrIzq)
    todos.add(esqArrIzq1)
    todos.add(esqArrIzq2)
    todos.add(esqArrIzq3)
    """
    fondo.add(esqArrIzq)
    fondo.add(esqArrIzq1)
    fondo.add(esqArrIzq2)
    fondo.add(esqArrIzq3)

    #izqAb
    esqIzqAb=esIzqAb(1000,80)

    #todos.add(esqIzqAb)
    fondo.add(esqIzqAb)

    #arrDer
    esqArrDer=esArDer(180,230)

    #todos.add(esqArrDer)
    fondo.add(esqArrDer)

    ayudaTete=tetero(198.75,615.75)
    #todos.add(ayudaTete)
    final.add(ayudaTete)

    #enemigos
    trampaCarro=carro(0,178)
    todos.add(trampaCarro)
    enemigo1.add(trampaCarro)
    enemigos.add(trampaCarro)
    
    trampaRaton=raton(428.75,248.75)
    todos.add(trampaRaton)
    enemigo2.add(trampaRaton)
    enemigos.add(trampaRaton)
    
    trampaLadron=ladron(798.75,90.75)
    todos.add(trampaLadron)
    enemigo3.add(trampaLadron)
    enemigos.add(trampaLadron)
    
    trampaChuzos=chuzos(888.75,348.75)
    todos.add(trampaChuzos)
    enemigo4.add(trampaChuzos)
    enemigos.add(trampaChuzos)
    
    trampaFuego=fuego(198.75,418.75)
    todos.add(trampaFuego)
    enemigo5.add(trampaFuego)
    enemigos.add(trampaFuego)


    jp=jugador(200,0)
    jugador1.add(jp)
    todos.add(jp)


    listaayudas.add(Botonpare)
    listaayudas.add(Botonagua)
    listaayudas.add(Botonperro)
    listaayudas.add(Botonpolicia)
    listaayudas.add(Botonpuente)
    todos.add(Botonpare)
    todos.add(Botonagua)
    todos.add(Botonperro)
    todos.add(Botonpolicia)
    todos.add(Botonpuente)
    ganar=False
    perder=False
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin =True
            if event.type == pygame.MOUSEBUTTONDOWN: #este if con elif mas cercano a el es para mover el boton de pare osea es para arrastrar y soltar los 5 botones en el otro modulo funciona
                if Botonpare.rect.collidepoint(event.pos):
                    Botonpare.click = True
            elif event.type == pygame.MOUSEBUTTONUP:
                Botonpare.click = False

            if event.type == pygame.MOUSEBUTTONDOWN:   #este if con elif mas cercano a el es para mover el boton de agua
                if Botonagua.rect.collidepoint(event.pos):
                    Botonagua.click = True
            elif event.type == pygame.MOUSEBUTTONUP:
                Botonagua.click = False

            if event.type == pygame.MOUSEBUTTONDOWN:   #este if con elif mas cercano a el es para mover el boton de perro
                if Botonperro.rect.collidepoint(event.pos):
                    Botonperro.click = True
            elif event.type == pygame.MOUSEBUTTONUP:
                Botonperro.click = False

            if event.type == pygame.MOUSEBUTTONDOWN:    #este if con elif mas cercano a el es para mover el boton de policia
                if Botonpolicia.rect.collidepoint(event.pos):
                    Botonpolicia.click = True
            elif event.type == pygame.MOUSEBUTTONUP:
                Botonpolicia.click = False

            if event.type == pygame.MOUSEBUTTONDOWN:    #este if con elif mas cercano a el es para mover el boton de puente
                if Botonpuente.rect.collidepoint(event.pos):
                    Botonpuente.click = True
            elif event.type == pygame.MOUSEBUTTONUP:
                Botonpuente.click = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

			

            
            if event.type == pygame.KEYDOWN:
            	"""
            	if event.key == pygame.K_RIGHT:
            		jp.var_x=1
            		jp.var_y=0
            	
            	if event.key == pygame.K_LEFT:
            		jp.var_x=-1
            		jp.var_y=0
            	
            	if event.key == pygame.K_UP:
            		jp.var_y=-1
            		jp.var_x=0
            	
            	if event.key == pygame.K_DOWN:
            		jp.var_y=1
            		jp.var_x=0
            	"""
            	if event.key== pygame.K_SPACE:
            		jp.var_x=0
            		jp.var_y=0
            		carro.var_x=0
            		carro.var_y=0

        	if ((jp.var_x==0)and(jp.var_y==0)):
            		#print "perdiste"
            		carro.stop=True
            		perder=True

        l_col=pygame.sprite.spritecollide(jp,enemigos,True)
        for en in l_col:
            jp.golpe()
            perder=True

        l_gana=pygame.sprite.spritecollide(jp,final,True)
        for ga in l_gana:
        	jp.golpe()
        	jp.var_y=1

        l_col1=pygame.sprite.spritecollide(Botonpare,enemigo1,True)
        for ay in l_col1:
        	Botonpare.golpe()

        l_col2=pygame.sprite.spritecollide(Botonperro,enemigo2,True)
        for ay in l_col2:
        	Botonperro.golpe()

        l_col3=pygame.sprite.spritecollide(Botonpolicia,enemigo3,True)
        for ay in l_col3:
        	Botonpolicia.golpe()

        l_col4=pygame.sprite.spritecollide(Botonpuente,enemigo4,True)
        for ay in l_col4:
        	Botonpuente.golpe()

        l_col5=pygame.sprite.spritecollide(Botonagua,enemigo5,True)
        for ay in l_col5:
        	Botonagua.golpe()


        pantalla.fill(0)
        fffondo.draw(pantalla)
        fondo.draw(pantalla)
        final.draw(pantalla)
        enemigos.update(pantalla)
        enemigos.draw(pantalla)
        todos.update(pantalla)                
        todos.draw(pantalla)
        jugador1.update(pantalla)
        jugador1.draw(pantalla)
        
        if perder==True:
        	#print "has perdido"
    		perdedor1.draw(pantalla)
    	
    	if jp.rect.top == ALTO-30:
    		ganar=True
    		ganador1.draw(pantalla)
    		#fin=True
        pygame.display.update()
        pygame.display.flip()
        reloj.tick(40)