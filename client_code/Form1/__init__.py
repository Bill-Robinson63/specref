from ._anvil_designer import Form1Template
from anvil import *
import stripe.checkout


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.canvas_size = 500
    self.canvas_1.height = self.canvas_size
    self.canvas_1.reset_context()
    self.star = [100, 100, 1, 2]
    
    self.waveColor = [[]]

  def canvas_1_reset(self, **event_args):
    """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
    pass

    
