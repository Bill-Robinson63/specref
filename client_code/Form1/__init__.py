from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import stripe.checkout
from anvil_extras import animation 

# Greek Letters: Α α, Β β, Γ γ, Δ δ, Ε ε, Ζ ζ, Η η, Θ θ, Ι ι, Κ κ, Λ λ, Μ μ, Ν ν, Ξ ξ, Ο ο, Π π, Ρ ρ, Σ σ ς, Τ τ, Υ υ, Φ φ, Χ χ, Ψ ψ, Ω ω

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.canvas_size = 500
    self.canvas_1.height = self.canvas_size
    self.canvas_1.reset_context()
    self.star = [100, 100, 1, 2]

  def displayLine(self, lineKey):
    canvas = self.canvas_1
    lineLength = canvas.get_width()/2
    wvs = self.spectralLines[lineKey]
    tag = lineKey
    last_wv = 0
    for wv in wvs:
      tag += " "
      canvas.begin_path()
      canvas.move_to(lineLength, wv - 380)
      canvas.line_to(canvas.get_width(), wv - 380)
      if self.absorption.selected:
        canvas.stroke_style = "Black"
      else:
        canvas.stroke_style = self.WvToRGB[wv - 380]
      canvas.line_width = 1
      canvas.stroke()
      canvas.close_path()
      if self.frequency.selected:
        tag += str(int((self.c_nm / wv) / 1e12))
      else:
        tag += str(wv)
      if wv - last_wv > 8:
        if self.frequency.selected:
          tag += "THz"
        else:
          tag += "nm"
        canvas.fill_style = "#FFFFFF"
        canvas.font = "11px consolas"
        canvas.fill_text(tag, 2, wv - 380)
        tag = lineKey
      last_wv = wv

  def canvas_1_reset(self, **event_args):
    """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
    canvas = self.canvas_1
    canWidth  = canvas.get_width()
    canLength = canvas.get_height()
    canvas.fill_style = "Black"
    canvas.fill_rect(0, 0, canWidth, canLength)
    
    if self.absorption.selected:
      lineLength = canvas.get_width()/2
      for i in range(len(self.WvToRGB)):
        wv = i + 380
        canvas.begin_path()
        canvas.move_to(lineLength, wv - 380)
        canvas.line_to(canvas.get_width(), wv - 380)
        canvas.stroke_style = self.WvToRGB[i]
        canvas.line_width = 1
        canvas.stroke()
        canvas.close_path()
    
    if self.H_alpha.checked:
      Form1.displayLine(self, "Hα")
    if self.H_beta.checked:
      Form1.displayLine(self, "Hβ")
    if self.H_gamma.checked:
      Form1.displayLine(self, "Hγ")
    if self.H_delta.checked:
      Form1.displayLine(self, "Hδ")
    if self.He_II.checked:
      Form1.displayLine(self, "HeII")
    if self.N_V.checked:
      Form1.displayLine(self, "NV")
    if self.O_III.checked:
      Form1.displayLine(self, "OIII")
    if self.S_II.checked:
      Form1.displayLine(self, "SII")

  def H_alpha_change(self, **event_args):
    self.canvas_1_reset()

  def H_beta_change(self, **event_args):
    self.canvas_1_reset()

  def H_gamma_change(self, **event_args):
    self.canvas_1_reset()

  def H_delta_change(self, **event_args):
    self.canvas_1_reset()

  def emission_clicked(self, **event_args):
    self.canvas_1_reset()

  def absorption_clicked(self, **event_args):
    self.canvas_1_reset()

  def frequency_clicked(self, **event_args):
    self.canvas_1_reset()

  def wavelength_clicked(self, **event_args):
    self.canvas_1_reset()

  def He_II_change(self, **event_args):
    self.canvas_1_reset()

  def O_III_change(self, **event_args):
    self.canvas_1_reset()

  def S_II_change(self, **event_args):
    self.canvas_1_reset()

  def N_V_change(self, **event_args):
    self.canvas_1_reset()

  @handle("link_1", "click")
  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass  # Write Code Here
