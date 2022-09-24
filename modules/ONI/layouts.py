from libqtile import layout
from libqtile.config import Match

lay_def = {"focus": "#FFFFFF", "unfocus": "#000000", "b_width": 1, "margin": 10}

layouts = [
    layout.Max(margin=5),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.Columns(
        border_width=lay_def["b_width"],
        border_focus=lay_def["focus"],
        border_normal=lay_def["unfocus"],
        margin=5,
        margin_on_single=10,
    ),
    layout.MonadTall(
        border_width=lay_def["b_width"],
        border_focus=lay_def["focus"],
        border_normal=lay_def["unfocus"],
        margin=5,
        single_margin=10,
        ratio=0.6,
    ),
    # layout.MonadWide(
    #     border_width=lay_def["b_width"],
    #     border_focus=lay_def["focus"],
    #     border_normal=lay_def["unfocus"],
    #     margin=5,
    #     single_margin=10,
    #     ratio=0.75,
    # ),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="Steam"),
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="foobar", wm_class="Tk"),
        Match(wm_class="nm-applet"),
        Match(wm_class="balena-etcher-electron"),
        Match(wm_class="src.App"),
    ],
    border_width=0,
    border_focus="#FFFFFF",
    border_normal=lay_def["unfocus"],
    margin=lay_def["margin"],
    margin_on_single=lay_def["margin"],
)
