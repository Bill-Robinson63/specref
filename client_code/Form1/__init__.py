from ._anvil_designer import Form1Template
from anvil import *
import stripe.checkout

# Greek Letters: Α α, Β β, Γ γ, Δ δ, Ε ε, Ζ ζ, Η η, Θ θ, Ι ι, Κ κ, Λ λ, Μ μ, Ν ν, Ξ ξ, Ο ο, Π π, Ρ ρ, Σ σ ς, Τ τ, Υ υ, Φ φ, Χ χ, Ψ ψ, Ω ω

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.canvas_1.reset_context()

    # Let's start off with Hα, Hβ, O_III, O_I, S_II, N_II which are said to be most common/prominent for ameture astronomers
    self.spectralLines = {}
    self.spectralLines["Hα"] = [[656, "#FF0000"], [486, "#00EFFF"], [434, "#2800FF"], [410, "#7E00DB"]]

  def displayLine(self, lineKey):
    canvas = self.canvas_1
    lineLength = canvas.get_width()
    lineData = self.spectralLines[lineKey]
    for line in lineData:
      canvas.begin_path()
      canvas.move_to(0, line[0] - 380)
      canvas.line_to(lineLength, line[0] - 380)
      canvas.stroke_style = line[1]
      canvas.line_width = 1
      canvas.stroke()
      canvas.close_path()

  def canvas_1_reset(self, **event_args):
    """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
    canWidth = self.canvas_1.get_width()
    canLength = self.canvas_1.get_height()
    self.canvas_1.begin_path()
    self.canvas_1.move_to(0, 0)
    self.canvas_1.line_to(canWidth, 0)
    self.canvas_1.line_to(canWidth, canLength)
    self.canvas_1.line_to(0, canLength)
    self.canvas_1.close_path()
    self.canvas_1.fill_style = "Black"
    self.canvas_1.fill()
    
    if self.H_alpha.checked:
      Form1.displayLine(self, "Hα")

  def H_alpha_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    self.canvas_1_reset()
