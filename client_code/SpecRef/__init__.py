from ._anvil_designer import SpecRefTemplate
from anvil import *
import anvil.server
import stripe.checkout
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class SpecRef(SpecRefTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.Mets_blue   = "#002D72"
    self.Mets_orange = "#FF5910"
    self.Jets_Gotham_Green = "#125740"
    self.Jets_Stealth_Black = "#000000"
    self.Jets_Spotlight_White = "#FFFFFF"
    self.pi = 3.14159

  @handle("button_return", "click")
  def button_return_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1')
