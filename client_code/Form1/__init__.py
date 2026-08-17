from ._anvil_designer import Form1Template
from anvil import *
import stripe.checkout
import math

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.Mets_blue   = "#002D72"
    self.Mets_orange = "#FF5910"

  def Penrose_Grid(self, centerX, centerY, size):
    c = self.canvas_1
    c.line_width = 3
    c.stroke_style = self.Mets_orange
    c.fill_style = "black"
    c.begin_path()
    c.move_to(centerX, 0)
    c.line_to(centerX + size, size)
    c.line_to(centerX, 2*size)
    c.line_to(centerX - size, size)
    c.close_path()
    c.fill()
    c.stroke()

    lines = [-5, -2, -1, -.5, 0, .5, 1, 2, 5]
    # vertical constant space lines
    for s in lines:
      for t in range(-20, 20):
        x = (math.atan(t+s) - math.atan(t-s)) * 67
        y = (math.atan(t+s) + math.atan(t-s)) * 67
        x += centerX
        y += 200
      c.fill_style = "white"
      c.fill_rect(x,y,2,2)

  @handle("canvas_1", "reset")
  def canvas_1_reset(self, **event_args):
    #This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form.
    c = self.canvas_1
    if c.get_height() > c.get_width():
      canSize = c.get_width()
    else:
      canSize = c.get_height()
    canMid = int(c.get_width() / 2)
    self.Penrose_Grid(canMid, int(canSize/2), int(canSize/2))
    
  @handle("link_1", "click")
  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass  # Write Code Here

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
    #open_form("")

  

