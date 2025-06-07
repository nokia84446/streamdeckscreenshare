# 🔳 Stream Deck Live Screen Mirror

This Python project turns your Elgato Stream Deck into a **real-time tiled screen mirror**, where each key displays a portion of your screen like a tiny live monitor grid.

Perfect for tech demos, status dashboards, or just showing off your Stream Deck!


!!!to make it work make sure to change to rows and collums depending on your model!!!

---

## 🎥 How It Works

- Captures your screen using [`mss`](https://github.com/BoboTiG/python-mss)
- Splits the screen into tiles based on the Stream Deck’s button grid
- Uses [`Pillow`](https://python-pillow.org) and the official [`StreamDeck` library](https://github.com/OpenStreamDeck/python-elgato-streamdeck) to send each tile to a button
- Continuously updates the buttons with a short delay (adjustable)

---

## 🧰 Requirements

- Python 3.8 or newer
- Elgato Stream Deck (Mini, Standard, or XL)
- The following Python libraries:
  - `StreamDeck`
  - `Pillow`
  - `mss`

