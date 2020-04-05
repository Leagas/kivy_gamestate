import math

from kivy.app import App
from kivy.properties import (
	NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock


class Ball(Widget):
	degrees = 0
	radius = 10

	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)
	velocity = ReferenceListProperty(velocity_x, velocity_y)

	def tick(self):
		self.degrees = self.degrees + 5

	def rads(self, value):
		return value*(math.pi/180)

	def calcX(self, d):
		return math.cos(d)*self.radius

	def calcY(self, d):
		return math.sin(d)*self.radius

	def getVelocity(self):
		radians = self.rads(self.degrees)
		self.velocity = self.calcX(radians), self.calcY(radians)

	def move(self):
		self.getVelocity()
		self.tick()
		if (self.degrees > 360):
			self.degrees = 0
		print(self.degrees)
		self.pos = Vector(*self.velocity) + self.pos



class State(Widget):
	ball_ref = ObjectProperty(None)

	def update(self,  dt):
		self.ball_ref.move()


class Game(App):
	def build(self):
		state = State()
		Clock.schedule_interval(state.update, 1.0/10.0)
		return state


if __name__ == '__main__':
    Game().run()
