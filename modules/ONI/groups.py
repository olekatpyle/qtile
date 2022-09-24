from libqtile.config import Key, Group, ScratchPad, DropDown, Match
from libqtile.lazy import lazy
from .keys import keys, mod

groups = [
    ScratchPad(
        name="ddm",
        dropdowns=[
            DropDown(
                "SessionManager",
                "foobar",
                match=Match(wm_class=["Tk"]),
                x=0.01,
                y=0.25,
                on_focus_lost_hide=False,
                opacity=1.0,
            )
        ],
        single=True,
    ),
    Group("a", label="一", layout="MonadTall"),
    Group(
        "s",
        label="二",
        layout="MonadTall",
        matches=[
            Match(wm_class=["firefox"]),
            Match(wm_class=["chromium"]),
            Match(wm_class=["brave-browser"]),
        ],
    ),
    Group("d", label="三", layout="MonadTall", matches=[Match(wm_class="DBeaver")]),
    Group(
        "f",
        label="四",
        layout="MonadTall",
        matches=[
            Match(wm_class=["Steam"]),
        ],
    ),
    Group("u", label="五", layout="MonadTall"),
    Group(
        "i",
        label="零",
        layout="MonadTall",
        matches=[
            Match(wm_class=["vscodium"]),
            Match(wm_class=["thonny"]),
        ],
    ),
    Group(
        "o",
        label="九",
        layout="MonadTall",
        matches=[
            Match(wm_class=["discord"]),
            Match(wm_class=["telegram-desktop"]),
            Match(wm_class=["microsoft teams - preview"]),
        ],
    ),
    Group("p", label="八", layout="Max", matches=[]),
]

for i in range(1, len(groups)):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                groups[i].name,
                lazy.group[groups[i].name].toscreen(),
                desc="Switch to group {}".format(groups[i].name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                groups[i].name,
                lazy.window.togroup(groups[i].name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    groups[i].name
                ),
            ),
        ]
    )

keys.extend([Key([mod], "q", lazy.group["ddm"].dropdown_toggle("SessionManager"))])
