# jd-i3status

My i3bar configuration for i3wm.

<img src="img/picture.png" width="100%">

## i3/config

```
bar {
        position top
        status_command i3status | python -u /PATH/TO/jd-i3status/main.py
        font pango:DejaVu Sans Mono 10
}