from ._anvil_designer import Form1Template
from anvil import *
import stripe.checkout

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.canvas_1.reset_context()

    self.spectralLines = {}
    self.spectralLines["H_alpha"] = [[656, "#FF0000"], [486, "#00EFFF"], [434, "#2800FF"], [410, "#7E00DB"]]

  def displayLine():


    def canvas_1_reset(self, **event_args):
    """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
    if self.H_alpha:
      self.canvas_1.begin_path()
      self.canvas_1.move_to(100, 100)
    self.canvas_1.line_to(150, 100)
    self.canvas_1.line_to(150, 150)
    self.canvas_1.line_to(100, 150)
    self.canvas_1.close_path()
    self.canvas_1.stroke()"""

  def H_alpha_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    self.canvas_1_reset()


