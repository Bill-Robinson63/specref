from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import stripe.checkout
import math

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.Mets_blue   = "#002D72"
    self.Mets_orange = "#FF5910"
    self.Jets_Gotham_Green = "#125740"
    self.Jets_Stealth_Black = "#000000"
    self.Jets_Spotlight_White = "#FFFFFF"
    self.pi = 3.14159

  def Penrose_Grid(self, centerX, centerY, size):
    # border & background
    c = self.canvas_1
    c.line_width = 3
    c.stroke_style = self.Mets_orange
    c.fill_style = self.Jets_Stealth_Black
    c.begin_path()
    c.move_to(centerX, 0)
    c.line_to(centerX + size, size)
    c.line_to(centerX, 2*size)
    c.line_to(centerX - size, size)
    c.close_path()
    c.fill()
    c.stroke()

    # grid lines
    lines = [-4, -2, -1, -.5, 0, .5, 1, 2, 4]
    c.stroke_style = self.Jets_Spotlight_White
    c.line_width = 1
    #
    # vertical constant space lines
    for s in lines:
      c.begin_path()
      for T in range(-200, 201):
        t = T/10
        x = (math.atan(t+s) - math.atan(t-s)) * 65
        y = (math.atan(t+s) + math.atan(t-s)) * 65
        x += centerX
        y *= -1
        y += size
        if t == -20:
          c.move_to(x,y)
        else:
          c.line_to(x,y)
      c.stroke()
    #
    # horizontal constant time lines
    for t in lines:
      c.begin_path()
      for S in range(-200, 201):
        s = S/10
        x = (math.atan(t+s) - math.atan(t-s)) * 65
        y = (math.atan(t+s) + math.atan(t-s)) * 65
        x += centerX
        y *= -1
        y += size
        if s == -20:
          c.move_to(x,y)
        else:
          c.line_to(x,y)
      c.stroke()
      
    # eyes
    c.stroke_style = "cyan"
    c.fill_style = "cyan"
    c.begin_path()
    c.arc(centerX-80, 153, 5, 0, 2 * self.pi)
    c.close_path()
    c.stroke()
    c.fill()
    c.begin_path()
    c.arc(centerX+80, 153, 5, 0, 2 * self.pi)
    c.close_path()
    c.stroke()
    c.fill()
    
    # mouth
    t = -.5
    c.begin_path()
    for S in range(-10, 11):
      s = S/10
      x = (math.atan(t+s) - math.atan(t-s)) * 67
      y = (math.atan(t+s) + math.atan(t-s)) * 67
      x += centerX
      y *= -1
      y += size
      if s == -20:
        c.move_to(x,y)
      else:
        c.line_to(x,y)
    #c.close_path()
    c.stroke_style = "magenta"
    c.line_width = 10
    c.stroke()

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

  @handle("button_specref", "click")
  def button_specref_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("SpecRef")
