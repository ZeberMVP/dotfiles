from libqtile import layout
from libqtile.config import Match

layouts = [
    layout.Max(
        border_focus="#c62841",
        border_normal="#1c1516",
        margin=10,
        border_width=0,
    ),
    layout.MonadTall(
        border_focus="#c62841",
        border_normal="#1c1516",
        margin=10,
        border_width=0,
    ),
    # layout.MonadWide(**layout_conf),
    # layout.Bsp(**layout_conf),
    # layout.Matrix(columns=2, **layout_conf),
    # layout.RatioTile(**layout_conf),
    # layout.Columns(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    border_focus="#c62841",
    border_normal="#1c1516",
    border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
)
