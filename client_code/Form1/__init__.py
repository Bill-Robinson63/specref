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
    self.spectralLines["H_alpha"] = [656, "#FF0000"]
    self.spectralLines["H_beta"]  = [486, "#00EFFF"]
    self.spectralLines["H_gamma"] = [434, "#2800FF"]
    self.spectralLines["H_delta"] = [410, "#7E00DB"]
  
  def wavelength_to_rgb(self, wavelength):
    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 440:
      attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
      R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** 0.8
      G = 0.0
      B = (1.0 * attenuation) ** 0.8
    elif wavelength >= 440 and wavelength <= 490:
      R = 0.0
      G = ((wavelength - 440) / (490 - 440)) ** 0.8
      B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
      R = 0.0
      G = 1.0
      B = (-(wavelength - 510) / (510 - 490)) ** 0.8
    elif wavelength >= 510 and wavelength <= 580:
      R = ((wavelength - 510) / (580 - 510)) ** 0.8
      G = 1.0
      B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
      R = 1.0
      G = (-(wavelength - 645) / (645 - 580)) ** 0.8
      B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
      attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
      R = (1.0 * attenuation) ** 0.8
      G = 0.0
      B = 0.0
    else:
      R = 0.0
      G = 0.0
      B = 0.0
    R *= 255
    G *= 255
    B *= 255
    return (int(R), int(G), int(B))

  def WvToRGB(self, wv):
    dRed, dGreen, dBlue = self.wavelength_to_rgb(wv)
    return "#" + hex(dRed)[2:] + hex(dGreen)[2:] + hex(dBlue)[2:]

  def displayLine(self, lineKey):
    canvas = self.canvas_1
    lineLength = canvas.get_width()
    line = self.spectralLines[lineKey]
    canvas.begin_path()
    canvas.move_to(0, line[0] - 380)
    canvas.line_to(lineLength, line[0] - 380)
    canvas.stroke_style = self.WvToRGB(line[0])
    canvas.line_width = 1
    canvas.stroke()
    canvas.close_path()

  def canvas_1_reset(self, **event_args):
    """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
    canWidth  = self.canvas_1.get_width()
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
      Form1.displayLine(self, "H_alpha")
    if self.H_beta.checked:
      Form1.displayLine(self, "H_beta")
    if self.H_gamma.checked:
      Form1.displayLine(self, "H_gamma")
    if self.H_delta.checked:
      Form1.displayLine(self, "H_delta")

  def H_alpha_change(self, **event_args):
    self.canvas_1_reset()

  def H_beta_change(self, **event_args):
    self.canvas_1_reset()

  def H_gamma_change(self, **event_args):
    self.canvas_1_reset()

  def H_delta_change(self, **event_args):
    self.canvas_1_reset()
