# BUIDL Wallet

If you have an m5stack, here are instructions to compile micropython firmware that includes all of Trezor's crypto code available as Python objects:

Install these prerequisites: https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/build

Build the custom Micropython firmware that includes trezor-crypto bindings:

```
git clone git@github.com:justinmoon/MicroPython_ESP32_psRAM_LoBo.git
cd MicroPython_ESP32_psRAM_LoBo/MicroPython_BUILD/
./BUILD.sh -v
./BUILD.sh -v flash
```

In another window run
```
git clone git@github.com:justinmoon/buidl-wallet.git
python3 -m pip install rshell
make sync
```

### Development Notes

`make repl`
* `ctrl-d` will restart the device
* `ctrl-a-d` will exit the repl

### Bugs

# TODOS
* I had to toggle the .endswith condition on line 193ish of /home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/pyboard.py
    * I was getting b'raw REPL; CTRL-B to exit\r\n>' instead of b'raw REPL; CTRL-B to exit\r\n' (caret at end)
* Copy this code over: https://github.com/justinmoon/micropython/blob/hd/ports/unix/src/main.py


##### failed to access /dev/ttyUSB0

```
$ make folder=src sync
rshell --port /dev/ttyUSB0 --timing --buffer-size=32 rsync --mirror --verbose ./src  /flash
Connecting to /dev/ttyUSB0 ...
failed to access /dev/ttyUSB0
make: *** [Makefile:20: sync] Error
```

##### I encounter this one when I try to re-sync files

* just now unplugging and plugging back in solved it
* this issue is on github https://github.com/dhylands/rshell/issues/68

```
$ make folder=src sync
rshell --port /dev/ttyUSB0 --timing --buffer-size=32 rsync --mirror --verbose ./src  /flash
Connecting to /dev/ttyUSB0 ...
b'\r\nInternal FS (SPIFFS): Mounted on partition \'internalfs\' [size: 2359296; Flash address: 0x1C0000]\r\n----------------\r\nFilesystem size: 2161152 B\r\n           Used: 18944 B\r\n           Free: 2142208 B\r\n----------------\r\nbip39 entropy= b\'\\x06^\\x9d\\xdeh\\x03\\x03\\x15\\xd2\\x11-\\xb0\\xa4<\\xad#j\\t_@\\x8b}\\xc7\\x9eW\\xb5\\xc8\\xa5V\\x05\\xda\\xb8\'\r\nmnemonic= alien visual jealous source coral memory embark certain radar capable clip egg party quick acquire hurry shy verify uniform mule fever actual helmet board\r\nseed= b"\\xf3U\\xd4;\\x92*\\xbbd1#\\xcc\\x1d4\\xb5\\x9d.1\\x8a\\xe2\\r\\xfc\\xf2\\x19*\\x9a\\x1f\\x90\\x03U\\x81\\x05$\\xdc\\x07\\xa4\\x88O\\xf3\\xfb2\\xb0\\xbe\\xbe\\x90A\\xc3\\x04\'\\xb8v%\\xbe\\xed\\r\\xbe\\xd2wR\\xcfZ\\xb5\\xa5\\xf9 "\r\nsaved seed to disk\r\nread seed from disk\r\nderiving node\r\nb"\\xf3U\\xd4;\\x92*\\xbbd1#\\xcc\\x1d4\\xb5\\x9d.1\\x8a\\xe2\\r\\xfc\\xf2\\x19*\\x9a\\x1f\\x90\\x03U\\x81\\x05$\\xdc\\x07\\xa4\\x88O\\xf3\\xfb2\\xb0\\xbe\\xbe\\x90A\\xc3\\x04\'\\xb8v%\\xbe\\xed\\r\\xbe\\xd2wR\\xcfZ\\xb5\\xa5\\xf9 "\r\nsigning...\r\nverifies? True\r\nMicroPython ESP32_LoBo_v3.2.24 - 2018-09-06 on ESP32 board with ESP32\r\nType "help()" for more information.\r\n>>> '
Traceback (most recent call last):
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/main.py", line 1186, in connect
    ip_address = socket.gethostbyname(port)
socket.gaierror: [Errno -2] Name or service not known

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/justin/dev/buidl-wallet/venv/bin/rshell", line 11, in <module>
    sys.exit(main())
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/command_line.py", line 4, in main
    rshell.main.main()
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/main.py", line 2712, in main
    real_main()
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/main.py", line 2674, in real_main
    connect(args.port, baud=args.baud, wait=args.wait, user=args.user, password=args.password)
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/main.py", line 1192, in connect
    connect_serial(port, baud=baud, wait=wait)
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/main.py", line 1216, in connect_serial
    dev = DeviceSerial(port, baud, wait)
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/main.py", line 1462, in __init__
    Device.__init__(self, pyb)
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/main.py", line 1265, in __init__
    self.has_buffer = self.remote_eval(test_buffer)
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/main.py", line 1379, in remote_eval
    return eval(self.remote(func, *args, **kwargs))
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/main.py", line 1357, in remote
    self.pyb.enter_raw_repl()
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/pyboard.py", line 187, in enter_raw_repl
    raise PyboardError('could not enter raw repl')
rshell.pyboard.PyboardError: could not enter raw repl
make: *** [Makefile:20: sync] Error 1
```

##### timed out or error in transfer to remote

```
$ make folder=src sync
rshell --port /dev/ttyUSB0 --timing --buffer-size=32 rsync --mirror --verbose ./src  /flash
Connecting to /dev/ttyUSB0 ...
Removing /flash/seed.txt
Removing /flash/boot.py
/home/justin/dev/buidl-wallet/src/helpers.py is newer than /flash/helpers.py - copying
/home/justin/dev/buidl-wallet/src/tx.py is newer than /flash/tx.py - copying
/home/justin/dev/buidl-wallet/src/main.py is newer than /flash/main.py - copying
timed out or error in transfer to remote
```

##### another rshell.pyboard.PyboardError

Come to think of itt .... I'm not actually using a pyboard ... do they mean "micropython" when they say "pyboard" or is the wrong code being executed?

```
$ make reset
rshell --port /dev/ttyUSB0 --timing --buffer-size=32 repl "~ import machine ~ machine.reset()~"
Connecting to /dev/ttyUSB0 ...
Traceback (most recent call last):
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/main.py", line 1186, in connect
    ip_address = socket.gethostbyname(port)
socket.gaierror: [Errno -2] Name or service not known

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/justin/dev/buidl-wallet/venv/bin/rshell", line 11, in <module>
    sys.exit(main())
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/command_line.py", line 4, in main
    rshell.main.main()
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/main.py", line 2712, in main
    real_main()
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/main.py", line 2674, in real_main
    connect(args.port, baud=args.baud, wait=args.wait, user=args.user, password=args.password)
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/main.py", line 1192, in connect
    connect_serial(port, baud=baud, wait=wait)
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/main.py", line 1216, in connect_serial
    dev = DeviceSerial(port, baud, wait)
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/main.py", line 1462, in __init__
    Device.__init__(self, pyb)
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/main.py", line 1274, in __init__
    self.root_dirs = ['/{}/'.format(dir) for dir in self.remote_eval(listdir, '/')]
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/main.py", line 1379, in remote_eval
    return eval(self.remote(func, *args, **kwargs))
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/main.py", line 1363, in remote
    output, _ = self.pyb.follow(timeout=20)
  File "/home/justin/dev/buidl-wallet/venv/lib/python3.7/site-packages/rshell/pyboard.py", line 208, in follow
    raise PyboardError('timeout waiting for first EOF reception')
rshell.pyboard.PyboardError: timeout waiting for first EOF reception
make: *** [Makefile:29: reset] Error 1
```


# 2019 notes

This will show the ports:

python -m serial.tools.list_ports
