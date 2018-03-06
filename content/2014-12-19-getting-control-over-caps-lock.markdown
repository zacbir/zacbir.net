Title: Getting Control over Caps Lock
Date: 2014-12-19 10:41
Slug: getting-control-over-caps-lock
Tags: Hardware, Hacking, Keyboards, Nerdery, Software

So, one of the first things I wanted to do with my newly resurrected
[Apple Extended Keyboard II]({filename}/2014-12-16-nimitz-alive.markdown) was to return to the “proper”
behavior with respect to the horribly misplaced Caps Lock key.

As a developer, I make extensive use of OS X’s built-in text editing features, many of which have origins in
UNIX. I use a lot of Control key shortcuts: Control-A to go to the beginning of a line, Control-E to go to the
end, Control-N to advance to the next line, Control-P to go to the previous line, and so on… I don’t know the
whole history of keyboard hardware development, but I’m sure there was some reason why Caps Lock got the
placement it did, wrong as it was. Personally, I find using Control works much better situated next to the ‘A’
key.

Normally, OS X makes it very easy to change the behavior of the Caps Lock key (as we’ll see below). However,
Apple’s mechanical keyboards use locking Alps key switches, which behave as a key-down-key-up with each press,
rather than as a momentary key-down like other modifier keys. This means the OS can’t simply treat it as it
does a non-locking switch (like on Apple’s new keyboards). These locking switches are easily modifiable though,
as I’ll explain.

There are three parts to upgrading your Caps Lock to Control: One mechanical, one in the firmware of the
adapter, and one in the OS.

\[**Edit 2015-01-19**\]: Actually, you don’t even need to fiddle with the OS. You can
[just change the firmware]({filename}/2015-01-19-self-control.markdown)

Mechanical
----------

 1. You’ll need to remove the keycap of the Caps Lock key. I have a wire keycap puller, but if you exhibit a
    bit of care, you can gently pry the keycaps off.
 {% img /images/keycap-pulled.JPG 'Caps Lock keycap pulled' 'Caps Lock keycap pulled' clear %}
 2. You’ll need to **gently** remove the inner sleeve of the key switch. Watch
    [this video](http://www.youtube.com/watch?v=9wqnt2mGJ2Y) to see the process in action. This is the housing
    where you’ll be able to remove the locking pin. If you accidentally pry out the entire switch, like I did,
    the best that will happen is you’ll break the soldering connection on the board, like I did, and have to
    clean it up, and re-solder, or you’ll damage the switch, possibly irrevocably. I was not too thrilled about
    prying out the entire switch, but I managed to reseat it, and get it cleanly soldered again.
 {% img /images/where-to-pry.JPG 'Where to pry' 'Where to pry' clear %}
 {% img /images/resoldered-switch.JPG 'Resoldered switch' 'Resolded switch' clear %}
 3. With the inner housing removed, use tweezers to remove the small, plastic locking pin. Now you have a
    regular switch. Gently replace the housing in the switch, and replace the keycap. I saved the pin because
    reasons.
 {% img /images/locking-pin.JPG 'Locking pin' 'Locking pin' clear %}

Firmware
--------

All you need to change in Hasu’s tmk code is the keymap code for the Caps Lock key in keymap_ansi.c:

{% include_code keymap_ansi.c.diff lang:diff %}

Apply this change, recompile, reinstall the firmware, and reboot your Teensy.

Operating System
----------------

Open your Keyboard preference pane, select the “ADB keyboard converter” keyboard, and set Caps Lock to “^ Control”.

{% img /images/keyboard-preference-pane.PNG 'Keyboard Preference Pane' 'Keyboard Preference Pane' clear %}

Now you have a Control key where it belongs.

