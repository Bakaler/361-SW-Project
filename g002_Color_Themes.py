#[Main, Off, CL, EL]
Themes = {
    "Theme_1" : ["#b5b3c2", "#ceccd9", "#e3f0f0", "#829f9f"],
    "Theme_2" : ["#c6ac8f", "#eae0d5", "#cad2c5", "#84a98c"],
    "Theme_3" : ["#ff8fa3", "#fcb9b2", "#ffccd5", "#ffb3c1"],
    "Theme_4" : ["#76c893", "#99d98c", "#34a0a4", "#1e6091"],
    "Theme_5" : ["#CBAD92", "#E3E2C6", "#99DFE3", "#4CA6C1"],
}


def set_theme(theme, CLD, ELD, Buttons):
    Buttons.set_color(Themes[f"Theme_{theme}"][0], Themes[f"Theme_{theme}"][1])
    CLD.set_color(Themes[f"Theme_{theme}"][2])
    ELD.set_color(Themes[f"Theme_{theme}"][3])
