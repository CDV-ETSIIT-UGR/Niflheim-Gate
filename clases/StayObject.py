
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
#
#       Copyright 2017 Niflheim-Gate
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import pygame
from pygame.locals import *

class StayObject(pygame.sprite.Sprite):
	def __init__(self, game_config):
		self.game_config = game_config

	@staticmethod
	def load_image(filename, transparent=False):
		"""Function to reurn a image object."""
		try:
			image = pygame.image.load(filename)
		except pygame.error:
			print("Error al cargar la imagen.")
			raise SystemExit
		image = image.convert()
		if transparent:
			color = image.get_at((0, 0))
			image.set_colorkey(color, RLEACCEL)
		return image

	@staticmethod
	def fText(text1, posx, posy, color=(255, 255, 255)):
		"""Manage text box in pygame."""
		fuente = pygame.font.Font("media/font/DroidSans.ttf", 25)
		salida = pygame.font.Font.render(fuente, text1, 1, color)
		salida_rect = salida.get_rect()
		salida_rect.centerx = posx
		salida_rect.centery = posy
		return salida, salida_rect

	def menu(self):
		"""Manage main menu."""
		pygame.init()
		pygame.display.set_caption("Niflheim-Gate")
		#self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((int(self.game_config["window-width"]), int(self.game_config["window-height"])))
		self.background_image = StayObject.load_image("media/image/menu.png")

		arrow1 = Arrow(int(self.game_config['window-width']))
		while True:
			#time = self.clock.tick(60)
			keys = pygame.key.get_pressed()
			for eventos in pygame.event.get():
				if eventos.type == QUIT:
					sys.exit(0)

			arrowReturn = arrow1.arrowMove(keys)
			t1 = StayObject.fText(self.game_config['lang']['start'], int(self.game_config['window-width'])/2, 200)
			t2 = StayObject.fText(self.game_config['lang']['exit'], int(self.game_config['window-width'])/2, 300)
			t3 = StayObject.fText("Niflheim-Gate", int(self.game_config['window-width'])/2, 100)

			self.screen.blit(arrow1.image, arrow1.rect)
			self.screen.blit(t1[0], t1[1])
			self.screen.blit(t2[0], t2[1])
			self.screen.blit(t3[0], t3[1])
			pygame.display.flip()
			if arrowReturn == 1:
				break;

class Arrow():
	"""Class to control the arrow."""

	def __init__(self, window_width):
		self.image = StayObject.load_image("media/image/arrow.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = window_width / 3
		self.rect.centery = 200

	def arrowMove(self, keys):
		"""Manage Player."""
		salida = 0
		if self.rect.centery != 200:
			if keys[K_UP]:
				self.rect.centery = 200
		if self.rect.centery != 300:
			if keys[K_DOWN]:
				self.rect.centery = 300
		if self.rect.centery == 300:
			if keys[K_RETURN]:
				raise SystemExit
		if self.rect.centery == 200:
			if keys[K_RETURN]:
				salida = 1
		return salida
