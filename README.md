# BUIDL Wallet

If you have an m5stack, here are instructions to compile micropython firmware that includes all of Trezor's crypto code available as Python objects:

Install these prerequisites: https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/build

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

TODO
Copy this code over: https://github.com/justinmoon/micropython/blob/hd/ports/unix/src/main.py
