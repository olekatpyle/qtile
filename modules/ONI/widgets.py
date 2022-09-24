from libqtile import widget
from libqtile import qtile


class UpdateVolume(widget.Volume):
    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        if self.volume <= 0:
            self.text = ""
        elif self.volume <= 15:
            self.text = ""
        elif self.volume < 50:
            self.text = ""
        else:
            self.text = ""
        # drawing here crashes Wayland

    def _update_drawer(self, wob=False):
        if self.volume <= 0:
            self.text = ""
        elif self.volume <= 15:
            self.text = ""
        elif self.volume < 50:
            self.text = ""
        else:
            self.text = ""
        self.draw()

        if wob:
            with open(self.wob, "a") as f:
                f.write(str(self.volume) + "\n")


volume = UpdateVolume(
    foreground="#ffffff",
    # background='#2f343f',
    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("pavucontrol")},
)
