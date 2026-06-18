Title: My One Month in GrapheneOS
Date: 2026-06-08 13:21:46.707030
Slug: my-one-month-in-grapheneos
Tags: smartphone, digital-lifestyle

I've been using iPhone since the day it was released and over the years, I've
slowly been getting more and more disappointed with the platform. I'm currently
using a two-year old iPhone 15 Pro Max. I decided recently to switch to Android
to see how some other folks live. I wanted to try and get away (by choice or
necessity) from some of the 800 pound gorillas in the tech space, and I'd been
hearing a lot of positive stories lately about
[GrapheneOS](https://grapheneos.org), so I looked at getting a best of breed
compatible phone model. I bought a Google Pixel 10 Pro XL in an unlocked state,
and installed GrapheneOS on it via the web installer (ironically, using Chrome
on my MacBook Air).

## What really got me looking

Now admittedly, my phone is 2+ years old, but the battery life was starting to
feel pretty atrocious. Coupled with the fact that I seem to have a tempermental
USB-C port, I could only reliably charge over MagSafe/Qi, and even that was
finicky at times. I hated waking up to a 20% charge. Furthermore, on the iOS
side, a neverending march towards patronizing safeguarding and lock-in left me
feeling further and further from my phone feeling like _my_ phone.

## What I liked about the Pixel with GrapheneOS

Contrasting it with a brand new phone without any hardware decay is a little
unfair, so we'll take the newness points as read. I was excited about the
prospects of the OS being More Open™ and configurable. By default, GrapheneOS
has several features that are a double-strike for privacy and performance. A
ruthless approach to turning off unnecessary networking (WiFi and Bluetooth are
set to turn off if not used after a short period of time) and automatically
rebooting the device after some interval of inactivity both increase security
and privacy by reducing vulnerability windows and increase battery life by
shutting down power draining services like searching for networks or connected
devices.

Even Google services, should you want them, are constrained in GrapheneOS. The
Services which provide for rich inter-application communication (and external
service telemetry and feedback) are run in a sandboxed environment, unlike the
privileged position it maintains in mainline Android. This allows (arguably)
for a tighter rein on how much insight external services can glean on your
activity on the device.

And I liked that you can easily, without a developer account, sideload
applications from a variety of sources (more on that later).

From an interface standpoint, I appreciated the ability to have the PIN entry
keypad scrambled, so even over-the-shoulder snooping would be made that much
more difficult.

## What I disliked about the new setup

All that freedom comes with a price. Notably, seemingly, a lack of any
overarching interface guidelines. The explicit, dedicated "Back" button of yore
is now exposed via gestures, but triggered, if not arbitrarily, fuzzily,
depending on just where you swipe from on the screen. Perhaps it's consistent,
but just different enough from iOS' affordances that I was regularly losing my
place among apps and views within apps. I never developed a good sense of
navigating the "stack" of interactable views lying just beneath (behind?) the
surface.

And the keyboard. Excuse me, keyboards. I would have paid good money just to
find a keyboard with the iOS layout. I'm honestly surprised one doesn't already
exist. I eventually settled on the Gboard to reclaim swipe typing, and I took
care to remove its network permissions. But 19 years of muscle memory was too
hard to overcome in the one month I gave it.

GrapheneOS suffers from other restrictions. Outside of a few EU-specific
applications, there's no abilty to make use of the Pixel's secure enclave, so
no ability to use Google Wallet. No tap-to-pay, no easy collection and
presentation of membership cards for insurance or transit. For what it was
worth, I tended to keep my physical wallet with me, but still, so often I'd
reach for my phone, just to do a double-take, put it back in my pocket, and
reach for a credit card.

I had hoped that the opinionated approach to PIN entry would have somehow
permeated the entire OS, but that wasn't the case. Once you'd authenticated
with a scrambled PIN to unlock the device, any time you re-entered your PIN,
you were presented with a standard 10-key layout. That felt like a promise not
met. Ultimately, I opted for biometric logins once the phone was unlocked via
PIN, and that annoyance largely went away (replaced by an all-too-frequent
frustration at the touch identification via screeen - possibly my screen
protector was to blame, I'm not sure).

And even the new hardware provided stumbling blocks. I could never get my Pixel
(even with a MagSafe (or whatever the Android branding equivalent is) case) to
connect to my car's Qi charger. That was a physical speedbump of a bummer. 

## What I wanted to like

GrapheneOS provides multiple user profiles, and a private space, but the
distinction isn't clear, and the restrictions placed on them felt arbitrary and
ultimately unhelpful. When I first learned of them, I imagined I'd be able to
fracture my online persona into all the various aspects and interests, and in
some way, reclaim compartmentalization of my Self from the Algorithm. But these
features aren't _quite_ that granular or discriminate. And even within the
community, it's difficult to find any consensus on what they're useful for or
how best to arrange your device to better safeguard your online interactions.
There's not even consensus on the best sources or means of getting apps on the
device. On the spectrum of walled-garden to wild-west, it's hard to find a
comfortable place to stop.

## What ultimately brought me back:

Explaining my decision to switch to Android to people I interact with almost
always centered around The Green Bubble™. iMessage was both the most obvious,
but also the most ubiquitous signifier that things were different. Coupled with
an inability to respond to my son's Screen Time requests or to locate my
college student on-campus, the gap became too wide. If I were already adrift, a
solo wanderer in the smartphone sea, I think I'd be… okay.

But goddamn, if I don't find myself utterly reliant on the iOS
tap-the-top-of-the-screen-to-scroll-to-the-top-of-a-scrollable-view _thing_.

## What I've changed about how I use iOS:

Security folks have long warned about the dangers of biometric access to our
smartphone devices. Bizarrely, courts have ruled that passcodes are worthy of
witholding and cannot be compelled, but biometric aspects of your own body are
not and can be. To that end, I've disabled FaceID on my iPhone for unlocking
the device, but re-enabled it to quickly authenticate servies and tools once
unlocked.

I've considered being more deliberate about how and when I enable WiFi and
Bluetooth as well.

## What I'd love to see come to iOS:

One of the first things I wanted to do with GrapheneOS was create things like
Shortcuts. Nonexistent (at least at the AOSP-level). But also, once back on
iOS, I was surprised to find that there don't seem to be any ways of
establishing timers or triggers based on any timed events. I'd love to see
something similar for WiFi and Bluetooth disabling after X minutes of
inactivity and an option to restart the device and bring it back to a Before
First Unlock state periodically.

More and more, I continue thinking that the best way forward is a return to
pure utility device. Dumbphones, featurephones, call them what you will. A
return to appliances that do one thing and one thing well.

Anyone wanna buy a Google Pixel 10 Pro XL and a set of Pixel Buds Pro?
