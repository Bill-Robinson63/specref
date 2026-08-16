from ._anvil_designer import PongTemplate
from anvil import *
import anvil.server
import stripe.checkout


class Pong(PongTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.
