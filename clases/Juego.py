
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
import os
import json
import pygame
from pygame.locals import *

class Juego(pygame.sprite.Sprite):

	def __init__(self, game_config):
		self.lang = game_config["lang"]
		self.max_time_to_move = int(game_config["max-time-to-move"])
		self.window_height = int(game_config["window-height"])
		self.window_width = int(game_config["window-width"])
		self.frames_per_second = int(game_config['frames-per-second'])
		self.half_width = self.window_width / 2
		"""
		try:
			json_data = open(os.path.join(game_config['default_profile_file']))
			game_config['lang'] = json.load(json_data)
			json_data.close()
			print(game_config['lang']['string_02'])
		except:
			print("The file '"+game_config['default_profile_file']+"' can not be loaded.")
			exit(3)
		"""

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
		menu_level="main"
		pygame.init()
		pygame.display.set_caption("Niflheim-Gate")
		self.clock = pygame.time.Clock()
		print(str(self.window_width) + " --- " + str(self.window_height))
		screen = pygame.display.set_mode((self.window_width, self.window_height))
		background_image = Juego.load_image("media/image/menu.png")

		arrow1 = Arrow1(self.window_width)
		while True:
			keys = pygame.key.get_pressed()
			for eventos in pygame.event.get():
				if eventos.type == QUIT:
					sys.exit(0)

			screen.fill((0,0,0))
			if menu_level == "main" :
				arrowReturn = arrow1.arrowMove(keys)
				t1 = Juego.fText("Niflheim-Gate", self.half_width, 200)
				t2 = Juego.fText(self.lang['start'], self.half_width, 300)
				t3 = Juego.fText(self.lang['configuration'], self.half_width, 400)
				t4 = Juego.fText(self.lang['exit'], self.half_width, 500)


				screen.blit(arrow1.image, arrow1.rect)
				screen.blit(t1[0], t1[1])
				screen.blit(t2[0], t2[1])
				screen.blit(t3[0], t3[1])
				screen.blit(t4[0], t4[1])

			if menu_level == "configuration" :
				arrowReturn = arrow1.arrowMove(keys)
				t1 = Juego.fText(self.lang['start'], self.half_width, 300)
				t2 = Juego.fText(self.lang['exit'], self.half_width, 400)
				t3 = Juego.fText("Niflheim-Gate", self.half_width, 200)

				screen.blit(arrow1.image, arrow1.rect)
				screen.blit(t1[0], t1[1])
				screen.blit(t2[0], t2[1])
				screen.blit(t3[0], t3[1])


			pygame.display.flip()
			time = self.clock.tick(self.frames_per_second)




class Arrow1():
	"""Class to control the arrow."""

	def __init__(self, window_width):
		self.image = Juego.load_image("media/image/arrow.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = window_width / 3
		self.rect.centery = 300

	def arrowMove(self, keys):
		"""Manage Player."""
		salida = 0
		"""
		if self.rect.centery != 300:
			if keys[K_UP]:
				print("Arriba")
				self.rect.centery = 300
		if self.rect.centery != 400:
			if keys[K_DOWN]:
				print("Abajo")
				self.rect.centery = 400
		if self.rect.centery == 500:
			if keys[K_RETURN]:
				raise SystemExit
		if self.rect.centery == 300:
			if keys[K_RETURN]:
				print("OP - 2")
				salida = 1
		"""

		##============================================
		if keys[K_UP]:
			print("Arriba")
			if self.rect.centery <= 300:
				self.rect.centery = self.rect.centery + 100

		if keys[K_DOWN]:
			print("Abajo")
			if self.rect.centery >= 500:
				self.rect.centery = self.rect.centery - 100

		if keys[K_RETURN]:
			if self.rect.centery == 300:
				print("OP - 1")
				salida = 1
			if self.rect.centery == 400:
				print("OP - 2")
				salida = 2
			if self.rect.centery == 500:
				print("OP - 3")
				salida = 3


		return salida
