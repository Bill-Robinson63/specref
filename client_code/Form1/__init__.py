from ._anvil_designer import Form1Template
from anvil import *
import stripe.checkout

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

    # time lines
    #for t in range(0, 2*size, size/3):
      #for s in range(centerX - size, centerX + size):
        # u = 
        # c.fill_rect(s, t, 1, 1, "magenta")

  @handle("canvas_1", "reset")
  def canvas_1_reset(self, **event_args):
    #This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form.
    c = self.canvas_1
    if c.get_height() > c.get_width():
      canSize = c.get_width()
    else:
      canSize = c.get_height()
    canMid = c.get_width() / 2
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

  

