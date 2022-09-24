from libqtile import hook
from libqtile import bar
from .widgets import *
from .groups import groups
from libqtile.config import Screen
from libqtile.lazy import lazy
import os
import subprocess
import random


# check what display setup we are using (single monitor or double)
def setup_display() -> str:
    sh = os.path.expanduser("~/.config/qtile/scripts/check_display.sh")
    subprocess.run([sh])

    try:
        tmp = subprocess.check_output("autorandr --current", shell=True)
        profile = str(tmp)[2:][:-3]
    except subprocess.CalledProcessError as ex:
        subprocess.Popen(
            f"echo {ex} | tee -a /.local/share/qtile/error.log", shell=True
        )
        profile = "mobile"
    return profile


def random_wp_pickr(images) -> str:
    image: str = images[random.randint(0, len(images) - 1)]
    path = home + "/.atpyle/assets/screen/" + image
    return path


home = os.path.expanduser("~")
profile = setup_display()
images = [
    "onigeisha.jpg",
    "sadgirl.jpg",
    "fishgirl.jpg",
    "onigirl1.jpg",
    "onigirl2.jpg",
    "onigirl4.jpg",
    "onigirl3.jpg",
    "maskgirl.jpg",
    "maskgirl2.jpg",
    "maskgirl3.jpg",
]
wallpaper = random_wp_pickr(images)
bar_opacity = 1
bar_bg = ["#000000"]
bar_size = 38

# Graphs settings
g_space = 20
g_bg = "#000000"
g_bor_col = "#4a4a4a"
g_mar_y = 4

main = bar.Bar(
    [
        widget.Spacer(length=8),
        widget.Image(
            filename=home + "/.config/qtile/eos-c.png",
            # filename=home + "/.local/assets/icons/blackhole.ico",
            margin=3,
            mouse_callbacks={
                "Button1": lazy.group["ddm"].dropdown_toggle("SessionManager")
            },
        ),
        widget.Spacer(length=bar.STRETCH),
        widget.GroupBox(
            fontsize=24,
            fontshadow="#222222",
            active="#3de5a7",
            inactive="#ffffff",
            center_aligned=True,
            margin=4,
            padding=4,
            spacing=6,
            highlight_method="block",
            rounded=False,
            this_current_screen_border="#d75fff",
            other_current_screen_border="#f0f571",
            this_screen_border="#5a5a5a",
            other_screen_border="#5a5a5a",
            urgent_border="#f16e00",
        ),
        widget.CurrentLayoutIcon(background="#5a5a5a", padding=0, scale=0.7),
        widget.Spacer(length=bar.STRETCH),
        volume,
        widget.Systray(
            icon_size=20,
        ),
        widget.Spacer(length=20),
        widget.Clock(
            format="%H:%M",
            fontsize=22,
            padding=2,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e calcurse")},
        ),
        # widget.BatteryIcon(update_interval=1, theme_path='/home/olek/bin/qtile/libqtile/resources/battery-icons/'),
        widget.Spacer(length=10),
    ],
    # margin=[0, 5, 0, 5],
    size=bar_size,
    background=bar_bg,
    opacity=bar_opacity,
    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
    # border_color=["ff00ff", "000000", "ff00ff", "000000"],  # Borders are magenta
)


secondary = bar.Bar(
    [
        widget.Spacer(length=2),
        widget.Clock(format="%H:%M", fontsize=22, padding=2),
        widget.Spacer(length=bar.STRETCH),
        widget.CurrentLayoutIcon(background="#4a4a4a", padding=0, scale=0.7),
        widget.Spacer(length=bar.STRETCH),
    ],
    size=32,
    background=bar_bg,
    opacity=bar_opacity,
)

screens = [  # primary screen
    Screen(wallpaper=wallpaper, wallpaper_mode="stretch", top=main)
]
if profile == "workstation":
    # add secondary screen
    screens.append(Screen(wallpaper=wallpaper, wallpaper_mode="stretch", top=secondary))
