from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import stripe.checkout
from anvil_extras import animation 

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.canvas_size = 600
    self.canvas_1.height = self.canvas_size
    self.star = [300, 300, 1, 2]
    self.canvas_1.reset_context()

  def canvas_1_reset(self, **event_args):
    """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
    # Adjust these coordinates if you want the drawing area to not be centered
    self.canvas_offset = (self.canvas_1.get_width() - self.canvas_size)/2
    self.canvas_1.translate(self.canvas_offset, 0)

    # Restrict drawing to the section that we want visible
    self.canvas_1.begin_path()
    self.canvas_1.move_to(0, 0)
    self.canvas_1.line_to(self.canvas_size, 0)
    self.canvas_1.line_to(self.canvas_size, self.canvas_size)
    self.canvas_1.line_to(0, self.canvas_size)
    self.canvas_1.close_path()
    self.canvas_1.fill_style = "Black"
    self.canvas_1.fill()
    self.canvas_1.clip()

    """# Draw a square
    self.canvas_1.begin_path()
    self.canvas_1.move_to(100, 100)
    self.canvas_1.line_to(150, 100)
    self.canvas_1.line_to(150, 150)
    self.canvas_1.line_to(100, 150)
    self.canvas_1.close_path()
    self.canvas_1.stroke()"""

    # Draw a star
    self.canvas_1.begin_path()
    self.canvas_1.arc(self.star[0], self.star[1], 2)
    self.canvas_1.close_path()
    self.canvas_1.fill_style = "White"
    self.canvas_1.fill()

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.star[0] += self.star[2]
    self.star[1] += self.star[3]
    if self.star[0] <= 0 or self.star[0] >= self.canvas_size:
      self.star[2] = -self.star[2]
    if self.star[1] <= 0 or self.star[1] >= self.canvas_size:
      self.star[3] = -self.star[3]

    self.canvas_1.begin_path()
    self.canvas_1.arc(self.star[0], self.star[1], 2)
    self.canvas_1.close_path()
    self.canvas_1.fill_style = "White"
    self.canvas_1.fill()
    self.canvas_1.reset_context()
  
  @handle("link_1", "click")
  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass  # Write Code Here

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Pong")
