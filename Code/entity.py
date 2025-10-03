#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from tkinter.font import names


class entity(ABC):
    def __init__(self, nome: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./Asset'/+ name + '.png')
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0


    @abstractmethod
    def move(self, ):
        pass
