Title: In Media Res
Date: 2015-01-08 10:48
Slug: in-media-res
Tags: Hardware, Hacking, Keyboards, Nerdery

I realized that in my first [post]({filename}/2014-12-16-nimitz-alive.markdown) about my new keyboard, I didn’t
really explain the process to build the firmware for the Teensy 2.0 microcontroller. Since then, I’ve modified
my keymap to [swap caps lock with control]({filename}/2014-12-19-getting-control-over-caps-lock.markdown), and
now I’ve added back in most of the media key functionality. I’ll show you how to do that now, and explain the
compilation process.

Getting the Tools
-----------------

There are two tools required for compiling and installing the firmware to the Teensy. The first is 
[CrossPack](http://www.obdev.at/products/crosspack/index.html) by Objective Development. The tools are
installed into /usr/local/CrossPack-AVR/bin/, so you’ll want to add that directory to your $PATH environment
variable, either permanently or during compilation. The examples below will use the latter.

To install the resulting firmware code onto the Teensy, you’ll need the 
[Teensy Loader](http://www.pjrc.com/teensy/loader.html) application.

Both these tools predate the signing requirements to get past OS X’s quarantine, so you’ll need to open them
via context menu in the Finder.

Getting the Code
----------------

You’ll need a copy of hasu’s tmk_keyboard project:

    $ git clone git@github.com:tmk/tmk_keyboard.git

Modifying the Keymap
--------------------

We’ll start with the keymap_ansi.c file and modify it. The ANSI layout makes a very sensible default for the
stock keyboard, since it uses the locking caps lock.

{% include_code keymap_ansi.c lang:c %}

    $ cd tmk_keyboard/converter/adb_usb/
    $ cp keymap_ansi.c keymap_zbir.c

To create media keys, we’ll need to add another keyboard layer to our keymap. We can duplicate the base
layer, and change one key’s code to be FN0. In my case, I’ve chosen the Print Screen key. I’ve designated its
action to be ACTION_LAYER_MOMENTARY to switch to layer 1, which has the media keys assigned to F7 through
F12.

{% include_code keymap_zbir_2015-01-08.c lang:c %}

Compiling the Firmware
----------------------

By default, with nothing specified, the Makefile will compile keymap_ansi.c. You can specify a KEYMAP parameter
to `make` to choose an alternate. It matches the part of the filename like this: `keymap_{KEYMAP}.c`.  Remember
to include the CrossPack AVR location in your $PATH:

    $ set PATH /usr/local/CrossPack-AVR/bin $PATH; make KEYMAP=zbir

This will create a number of output files, but we’re interested in `adb_usb_lufa.hex`, as that’s the file
format Teensy Loader will install.

Installing the Firmware
-----------------------

Launch the Teensy app. It’s just one little window. Isn’t it cute? Four little buttons along the top. Press
the reset button on the Teensy itself to start the conversation. Click the first button to locate your .hex
file. Click the second to erase the Teensy and install the new firmware. Click the third button to reboot the
Teensy. Don’t bother with Automatic Mode.

You’re done! If you use a layout like mine, pressing Print Screen and F8 will play/pause iTunes. And since
it’s part of the firmware, it works and sends the same commands no matter what computer you plug the keyboard
into (or if you use a virtual KV like Teleport, no matter which computer is receiving the keyboard and mouse
events).
