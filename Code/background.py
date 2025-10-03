#!/usr/bin/python
# -*- coding: utf-8 -*-
from Code.const import WIN_WIDTH
from Code.entity import entity


class Background(entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        pass

    def move(self, ):
        self.rect.centerx -=1
        if self.rect.right <=0:
            self.rect.left = WIN_WIDTH
        pass
