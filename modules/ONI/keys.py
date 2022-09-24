from libqtile.lazy import lazy
from libqtile.config import Key
from libqtile import extension

mod = "mod4"
terminal = "/usr/bin/kitty"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "n", lazy.layout.next()),
    Key([mod, "shift"], "m", lazy.layout.previous()),
    # Key([mod], "r", lazy.spawn("rofi -show combi"), desc="spawn rofi"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(
        [],
        "XF86KbdLightOnOff",
        lazy.execute("$HOME/.config/qtile/scripts/toggle_kbd_backlight.sh"),
    ),
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle")),
    Key([], "XF86AudioMicMute", lazy.spawn("pactl set-sink-input-mute 0 toggle")),
    Key([], "XF86AudioPlay", lazy.spawn("spotifycli --playpause")),
    Key([mod], "space", lazy.spawn("spotifycli --playpause")),
    Key([], "XF86AudioPrev", lazy.spawn("spotifycli --prev")),
    Key([mod], "Left", lazy.spawn("spotifycli --prev")),
    Key([], "XF86AudioNext", lazy.spawn("spotifycli --next")),
    Key([mod], "Right", lazy.spawn("spotifycli --next")),
    Key([], "XF86Calculator", lazy.spawn("qalculate-qt")),
    Key([], "XF86Bluetooth", lazy.spawn("bluetoothctl power off")),
    Key([mod], "Print", lazy.spawn("flameshot gui")),
    Key([mod], "period", lazy.next_screen(), desc="Move focus to next monitor"),
    Key([mod], "comma", lazy.prev_screen(), desc="Move focus to prev screen"),
    # DMenu
    Key(
        [mod],
        "z",
        lazy.run_extension(
            extension.DmenuRun(
                dmenu_prompt="\ufb0c",
                background="#000000",
                foreground="#FFFFFF",
                selected_background="#FFFFFF",
                selected_foreground="#000000",
                dmenu_bottom=False,
                font="Fira Code Regular Nerd Font Complete Mono",
                font_size=20,
                dmenu_lines=16,
            )
        ),
    ),
    Key([mod], "t", lazy.spawn("kitty -e calcurse")),
    Key([mod], "r", lazy.spawn("kitty -e ranger")),
    Key([mod], "0", lazy.spawn("spotify-tray -t")),
]
