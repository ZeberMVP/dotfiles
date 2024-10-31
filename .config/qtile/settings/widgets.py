from libqtile import widget, qtile

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = [widget_defaults.copy()]


def search():
    qtile.cmd_spawn("rofi -show drun")


def power():
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/power")


primary_widgets = [
    widget.Spacer(
        length=15,
        background="#1c1516",
    ),
    widget.Image(
        filename="~/.config/qtile/Assets/launch_Icon.png",
        margin=2,
        background="#1c1516",
        mouse_callbacks={"Button1": power},
    ),
    widget.Image(
        filename="~/.config/qtile/Assets/6.png",
    ),
    widget.GroupBox(
        fontsize=24,
        borderwidth=3,
        highlight_method="text",
        active="#c62841",
        block_highlight_text_color="#ca233b",
        highlight_color="#ca233b",
        inactive="#6c2128",
        foreground="#fbd7dc",
        background="#302d3e",
        this_current_screen_border="#fc4d88",
        this_screen_border="#ca233b",
        other_current_screen_border="#302d3e",
        other_screen_border="#302d3e",
        urgent_border="#df426f",
        rounded=True,
        disable_drag=True,
    ),
    widget.Spacer(
        length=8,
        background="#302d3e",
    ),
    widget.Image(
        filename="~/.config/qtile/Assets/1.png",
    ),
    widget.Image(filename="~/.config/qtile/Assets/layout.png", background="#302d3e"),
    widget.CurrentLayout(
        background="#302d3e",
        foreground="#fbd7dc",
        fmt="{}",
        font="JetBrains Mono Bold",
        fontsize=13,
    ),
    widget.Image(
        filename="~/.config/qtile/Assets/5.png",
    ),
    widget.Image(
        filename="~/.config/qtile/Assets/search.png",
        margin=2,
        background="#1c1516",
        mouse_callbacks={"Button1": search},
    ),
    widget.TextBox(
        fmt="Search",
        background="#1c1516",
        font="JetBrains Mono Bold",
        fontsize=13,
        foreground="#fbd7dc",
        mouse_callbacks={"Button1": search},
    ),
    widget.Image(
        filename="~/.config/qtile/Assets/4.png",
    ),
    widget.WindowName(
        background="#302d3e",
        format="{name}",
        font="JetBrains Mono Bold",
        foreground="#fbd7dc",
        empty_group_string="Desktop",
        fontsize=14,
    ),
    widget.Image(
        filename="~/.config/qtile/Assets/3.png",
    ),
    widget.Systray(
        background="#1c1516",
        fontsize=2,
    ),
    widget.TextBox(
        text=" ",
        background="#1c1516",
    ),
    widget.Image(
        filename="~/.config/qtile/Assets/6.png",
        background="#302d3e",
    ),
    widget.Image(
        filename="~/.config/qtile/Assets/Misc/ram.png",
        background="#302d3e",
    ),
    widget.Spacer(
        length=-7,
        background="#302d3e",
    ),
    widget.Memory(
        background="#302d3e",
        format="{MemUsed: .0f}{mm}",
        foreground="#fbd7dc",
        font="JetBrains Mono Bold",
        fontsize=13,
        update_interval=5,
    ),
    widget.Image(
        filename="~/.config/qtile/Assets/2.png",
    ),
    widget.Spacer(
        length=4,
        background="#302d3e",
    ),
    widget.TextBox(
        text=" ",
        font="Font Awesome 6 Free Solid",
        fontsize=20,
        background="#302d3e",
        foreground="#ca233b",
    ),
    widget.Battery(
        font="JetBrainsMono Nerd Font Bold",
        fontsize=13,
        background="#302d3e",
        foreground="#fbd7dc",
        format="{percent:2.0%}",
    ),
    widget.Image(
        filename="~/.config/qtile/Assets/2.png",
    ),
    widget.Volume(
        font="JetBrainsMono Nerd Font",
        theme_path="~/.config/qtile/Assets/Volume/",
        emoji=True,
        fontsize=13,
        background="#302d3e",
    ),
    widget.Spacer(
        length=-5,
        background="#302d3e",
    ),
    widget.Volume(
        font="JetBrains Mono Bold",
        background="#302d3e",
        foreground="#fbd7dc",
        fontsize=13,
    ),
    widget.Image(
        filename="~/.config/qtile/Assets/5.png",
        background="#302d3e",
    ),
    widget.Image(
        filename="~/.config/qtile/Assets/Misc/clock.png",
        background="#1c1516",
        margin_y=6,
        margin_x=5,
    ),
    widget.Clock(
        format="%a %d-%m %H:%M %p",
        background="#1c1516",
        foreground="#fbd7dc",
        font="JetBrains Mono Bold",
        fontsize=13,
    ),
    widget.Spacer(
        length=18,
        background="#1c1516",
    ),
]
