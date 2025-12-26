# LightShow-Pico

## 📌 Description
A Raspberry Pi Pico project that creates a smooth forward-and-reverse LED chasing effect using MicroPython. LEDs light up one by one from the first to the last pin, then reverse direction to create a Light Show effect. Perfect for beginners learning GPIO control, loops, and timing in embedded systems.

## 🎯 Features
- Forward and reverse LED chasing effect
- Smooth animation (avoids double blinking at ends)
- Easy to adjust speed and number of LEDs
- Beginner-friendly MicroPython project

## 🧰 Hardware Required
- Raspberry Pi Pico
- 10 × LEDs
- 470Ω resistor
- Breadboard
- Jumper wires(if needed)
- USB cable

## 💻 Software Required
- MicroPython firmware installed on Pico
- Thonny IDE (recommended) or any MicroPython-compatible editor

## 🔌 Pin Configuration
Each LED is connected to the following GPIO pins: 0, 1, 2, 3, 4, 6, 8, 10, 12, 13

- LED Anode (+) → GPIO pins mentioned above
- LED Cathode (−) → -ve rail of breadboard
- 470Ω resistor → GND and -ve rail of breadboard

## 🧠 How It Works
1. Set all GPIO pins as OUTPUT.  
2. Turn on LEDs forward from first to last.  
3. Turn on LEDs backward from last to first, skipping first and last LED to avoid double blinking.  
4. Repeat infinitely for continuous light show effect.

## ⏱️ Customization
- Change speed by adjusting the delay between LEDs (smaller delay = faster, larger delay = slower).  
- Change number of LEDs by adding or removing GPIO pins in the configuration.

## 🚀 How to Run
1. Flash MicroPython onto the Pico.  
2. Open Thonny IDE.  
3. Paste the LED chase code.  
4. Save as `main.py` on the Pico.  
5. Run the script.

## 📚 Learning Outcomes
- GPIO pin control on Raspberry Pi Pico  
- Python list slicing  
- Infinite loops and timing control  
- Basic embedded system programming

## 🏷️ Topics / Tags
raspberry-pi-pico, micropython, embedded-systems, led-chaser, gpio, electronics, iot, beginner-project
