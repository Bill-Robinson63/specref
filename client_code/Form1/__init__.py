from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import stripe.checkout

# Greek Letters: Α α, Β β, Γ γ, Δ δ, Ε ε, Ζ ζ, Η η, Θ θ, Ι ι, Κ κ, Λ λ, Μ μ, Ν ν, Ξ ξ, Ο ο, Π π, Ρ ρ, Σ σ ς, Τ τ, Υ υ, Φ φ, Χ χ, Ψ ψ, Ω ω

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.canvas_1.reset_context()
    self.c_nm = 299792458 * 1e9

    self.WvToRGB = ['#610061', '#630064', '#640067', '#66006a', '#67006d', '#680070', '#690073', '#6a0076', '#6b0078', '#6c007b',
                    '#6d007e', '#6e0081', '#6e0084', '#6f0087', '#6f0089', '#6f008c', '#6f008f', '#6f0092', '#6f0094', '#6f0097',
                    '#6f009a', '#6f009c', '#6e009f', '#6e00a2', '#6d00a4', '#6c00a7', '#6c00aa', '#6b00ac', '#6a00af', '#6800b2',
                    '#6700b4', '#6600b7', '#6500b9', '#6300bc', '#6100be', '#6000c1', '#5e00c4', '#5c00c6', '#5a00c9', '#5700cb',
                    '#5500ce', '#5300d0', '#5000d3', '#4d00d5', '#4b00d8', '#4800da', '#4500dd', '#4100df', '#3e00e2', '#3a00e4',
                    '#3700e6', '#3300e9', '#2f00eb', '#2a00ee', '#2600f0', '#2100f3', '#1c00f5', '#1600f7', '#1000fa', '#0900fc',
                    '#0000ff', '#000bff', '#0013ff', '#001aff', '#0021ff', '#0028ff', '#002eff', '#0034ff', '#003aff', '#0040ff',
                    '#0046ff', '#004bff', '#0051ff', '#0056ff', '#005cff', '#0061ff', '#0066ff', '#006bff', '#0070ff', '#0075ff',
                    '#007aff', '#007fff', '#0084ff', '#0089ff', '#008dff', '#0092ff', '#0097ff', '#009bff', '#00a0ff', '#00a4ff',
                    '#00a9ff', '#00adff', '#00b2ff', '#00b6ff', '#00bbff', '#00bfff', '#00c4ff', '#00c8ff', '#00ccff', '#00d1ff',
                    '#00d5ff', '#00d9ff', '#00ddff', '#00e2ff', '#00e6ff', '#00eaff', '#00eeff', '#00f2ff', '#00f6ff', '#00faff',
                    '#00ffff', '#00fff4', '#00ffea', '#00ffdf', '#00ffd5', '#00ffca', '#00ffbf', '#00ffb4', '#00ffa9', '#00ff9e',
                    '#00ff92', '#00ff86', '#00ff7a', '#00ff6e', '#00ff61', '#00ff54', '#00ff46', '#00ff37', '#00ff28', '#00ff17',
                    '#00ff00', '#08ff00', '#0eff00', '#14ff00', '#19ff00', '#1eff00', '#23ff00', '#28ff00', '#2cff00', '#31ff00',
                    '#35ff00', '#3aff00', '#3eff00', '#42ff00', '#46ff00', '#4aff00', '#4eff00', '#52ff00', '#56ff00', '#59ff00',
                    '#5dff00', '#61ff00', '#65ff00', '#68ff00', '#6cff00', '#6fff00', '#73ff00', '#77ff00', '#7aff00', '#7eff00',
                    '#81ff00', '#84ff00', '#88ff00', '#8bff00', '#8fff00', '#92ff00', '#95ff00', '#99ff00', '#9cff00', '#9fff00',
                    '#a2ff00', '#a6ff00', '#a9ff00', '#acff00', '#afff00', '#b3ff00', '#b6ff00', '#b9ff00', '#bcff00', '#bfff00',
                    '#c2ff00', '#c5ff00', '#c9ff00', '#ccff00', '#cfff00', '#d2ff00', '#d5ff00', '#d8ff00', '#dbff00', '#deff00',
                    '#e1ff00', '#e4ff00', '#e7ff00', '#eaff00', '#edff00', '#f0ff00', '#f3ff00', '#f6ff00', '#f9ff00', '#fcff00',
                    '#ffff00', '#fffb00', '#fff800', '#fff500', '#fff200', '#ffef00', '#ffeb00', '#ffe800', '#ffe500', '#ffe200',
                    '#ffdf00', '#ffdb00', '#ffd800', '#ffd500', '#ffd200', '#ffce00', '#ffcb00', '#ffc800', '#ffc400', '#ffc100',
                    '#ffbe00', '#ffba00', '#ffb700', '#ffb300', '#ffb000', '#ffac00', '#ffa900', '#ffa500', '#ffa200', '#ff9e00',
                    '#ff9b00', '#ff9700', '#ff9400', '#ff9000', '#ff8d00', '#ff8900', '#ff8500', '#ff8100', '#ff7e00', '#ff7a00',
                    '#ff7600', '#ff7200', '#ff6f00', '#ff6b00', '#ff6700', '#ff6300', '#ff5f00', '#ff5b00', '#ff5700', '#ff5300',
                    '#ff4e00', '#ff4a00', '#ff4600', '#ff4200', '#ff3d00', '#ff3900', '#ff3400', '#ff2f00', '#ff2a00', '#ff2500',
                    '#ff2000', '#ff1b00', '#ff1500', '#ff0f00', '#ff0900', '#ff0000', '#fd0000', '#fc0000', '#fa0000', '#f90000',
                    '#f80000', '#f60000', '#f50000', '#f40000', '#f20000', '#f10000', '#ef0000', '#ee0000', '#ed0000', '#eb0000',
                    '#ea0000', '#e80000', '#e70000', '#e60000', '#e40000', '#e30000', '#e20000', '#e00000', '#df0000', '#dd0000',
                    '#dc0000', '#da0000', '#d90000', '#d80000', '#d60000', '#d50000', '#d30000', '#d20000', '#d10000', '#cf0000',
                    '#ce0000', '#cc0000', '#cb0000', '#c90000', '#c80000', '#c60000', '#c50000', '#c40000', '#c20000', '#c10000',
                    '#bf0000', '#be0000', '#bc0000', '#bb0000', '#b90000', '#b80000', '#b60000', '#b50000', '#b30000', '#b20000',
                    '#b00000', '#af0000', '#ad0000', '#ac0000', '#aa0000', '#a90000', '#a70000', '#a60000', '#a40000', '#a30000',
                    '#a10000', '#a00000', '#9e0000', '#9d0000', '#9b0000', '#9a0000', '#980000', '#970000', '#950000', '#940000',
                    '#920000', '#900000', '#8f0000', '#8d0000', '#8c0000', '#8a0000', '#890000', '#870000', '#850000', '#840000',
                    '#820000', '#810000', '#7f0000', '#7d0000', '#7c0000', '#7a0000', '#780000', '#770000', '#750000', '#730000',
                    '#720000', '#700000', '#6e0000', '#6d0000', '#6b0000', '#690000', '#680000', '#660000', '#640000', '#630000',
                    '#610000', '#600000', '#590000', '#580000', '#570000', '#560000', '#550000', '#540000', '#530000', '#520000',
                    '#510000', '#500000', '#490000', '#480000', '#470000', '#460000', '#450000', '#440000', '#430000', '#420000',
                    '#410000', '#400000', '#390000', '#380000', '#370000', '#360000', '#350000', '#340000', '#330000', '#320000']

    # Let's start off with Hα, Hβ, O_III, O_I, S_II, N_II which are said to be most common/prominent for ameture astronomers
    self.spectralLines = {}
    self.spectralLines["Hα"] = [656]
    self.spectralLines["Hβ"]  = [486]
    self.spectralLines["Hγ"] = [434]
    self.spectralLines["Hδ"] = [410]
    self.spectralLines["HeII"] = [454, 469, 541] # 657 would interfere with H_alpha
    self.spectralLines["NV"] = [461]
    self.spectralLines["OIII"] = [496, 501]
    self.spectralLines["SII"] = [672]

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
