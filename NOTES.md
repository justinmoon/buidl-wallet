Tails your system log. Useful when rshell or ampy cannot find /dev/ttyUSB0. Run this, then plug and unplug your device. You'll see what port it's being connected to (for me it's often /dev/ttyUSB1

```
dmesg -w
```

Nice UART video: https://www.youtube.com/watch?v=V6m2skVlsQI

m5stack-specific uart docs: https://m5stack.readthedocs.io/en/master/api-reference/peripherals/uart.html?highlight=uart

cool unrelated esp32 tutorial: https://learn.sparkfun.com/tutorials/micropython-programming-tutorial-getting-started-with-the-esp32-thing/all

This says I need a usb-to-uart driver: https://titech-aos.github.io/tutorial_en.html#installing-usb-uart-driver

CROSS THE WIRES!!! Connect tx<->rx and rx<->tx
