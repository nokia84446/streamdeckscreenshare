from StreamDeck.DeviceManager import DeviceManager
from StreamDeck.ImageHelpers import PILHelper
from PIL import Image
import mss
import time

# Configuration: adjust these to your Stream Deck model
ROWS = 3
COLS = 5

def capture_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Primary monitor
        screenshot = sct.grab(monitor)
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
        return img

def split_image(img, rows, cols, tile_width, tile_height):
    tiles = []
    for row in range(rows):
        for col in range(cols):
            left = col * tile_width
            upper = row * tile_height
            right = left + tile_width
            lower = upper + tile_height
            tile = img.crop((left, upper, right, lower))
            tiles.append(tile)
    return tiles

def main():
    streamdecks = DeviceManager().enumerate()
    if not streamdecks:
        print("No Stream Deck found.")
        return

    deck = streamdecks[0]
    deck.open()
    deck.reset()

    # Get button dimensions
    button_size = deck.key_image_format()['size']
    tile_width = button_size[0]
    tile_height = button_size[1]


    try:
        while True:
            screen = capture_screen()
            # Resize screen to fit total tiles area
            total_width = tile_width * COLS
            total_height = tile_height * ROWS
            resized_screen = screen.resize((total_width, total_height))

            tiles = split_image(resized_screen, ROWS, COLS, tile_width, tile_height)

            for i, tile in enumerate(tiles):
                image = PILHelper.to_native_format(deck, tile)
                deck.set_key_image(i, image)

            time.sleep(0.005)  # adjust for refresh speed

    except KeyboardInterrupt:
        print("Exiting...")

    finally:
        deck.reset()
        deck.close()

if __name__ == "__main__":
    main()
