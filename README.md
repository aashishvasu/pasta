Welcome to **`pasta`**, the stupidly simple point to point file transfer tool written in python!

## Introduction

Here are some highlights of what pasta has to offer:

* Uses python-zeroconf for seamless discovery, no fiddling around with IP addresses!
* Simple point to point file transfer between devices
* Thats it really

With `pasta`, you can easily transfer files between devices on the same network without any complex setup or configuration.

## Installation

### Windows Installer
* Grab the [latest release](https://github.com/aashishvasu/pasta/releases/latest) and install it.

### Linux
`(Install script coming soon)`

### From source
1. Clone the repo
2. Create virtualenv `py -m venv venv`
3. Install requirements `pip install -r requirements.txt`
4. Create binary `venv\Scripts\pyinstaller.exe pasta.py -F --icon resources\abp.ico` or on Windows, run `buid.bat`
5. Add parent directory for `pasta` bin to PATH environment variable

## Usage

#### Sender
* Open term/cmd and type
```sh
pasta send file1.pdf /folder1
```
* It will generate a code to paste in the recepient computer, for example:
```sh
pasta recieve obstiante-happy-red-gorilla
```

#### Receiver
* Open a terminal/cmd in the target directory.
* Paste the code you're given. And you're done!

### Author Notes
Using `zeroconf` (and socket programming in general) is pretty new to me, so you should not use this as an example of good python hygiene. In the words of the great Todd Howard:
![It just works](/docs/img/th.jpg)

### Contributing
Obviously as I mentioned above, there are improvements to be made all over the codebase. Any help would be appreciated! Open a PR and I can review it. A couple of things next on my todo list are:

- [ ] Build and installer script for linux
- [ ] Streamlining zeroconf from the listener side (in [sender.py](/src/sender.py))
