import cv2
import numpy as np
import time

def create_background(cap, num_frames=30):
    print("Capturing background. Please move out of frame.")
    backgrounds = []
    for i in range(num_frames):
        ret, frame = cap.read()
        if ret:
            backgrounds.append(frame)
        else:
            print(f"Warning: Could not read frame {i+1}/{num_frames}")
        time.sleep(0.1)
    if backgrounds:
        return np.median(backgrounds, axis=0).astype(np.uint8)
    else:
        raise ValueError("Could not capture any frames for background")

def create_mask(frame, lower_color1, upper_color1, lower_color2, upper_color2):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv, lower_color1, upper_color1)
    mask2 = cv2.inRange(hsv, lower_color2, upper_color2) if lower_color2 is not None else 0
    mask = cv2.bitwise_or(mask1, mask2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)
    return mask

def apply_cloak_effect(frame, mask, background):
    mask_inv = cv2.bitwise_not(mask)
    fg = cv2.bitwise_and(frame, frame, mask=mask_inv)
    bg = cv2.bitwise_and(background, background, mask=mask)
    return cv2.add(fg, bg)

def select_color():
    # Predefined HSV ranges for colors
    colors = {
        "red": [(0, 120, 70), (10, 255, 255), (170, 120, 70), (180, 255, 255)],
        "blue": [(90, 50, 50), (130, 255, 255), None, None],
        "green": [(40, 50, 50), (80, 255, 255), None, None],
        "yellow": [(20, 100, 100), (30, 255, 255), None, None],
    }

    print("Select the color of your cloak:")
    for idx, color in enumerate(colors.keys(), 1):
        print(f"{idx}. {color.capitalize()}")

    choice = int(input("Enter the number corresponding to your choice: "))
    selected_color = list(colors.keys())[choice - 1]
    print(f"You selected: {selected_color.capitalize()}")
    return colors[selected_color]

def main():
    print("OpenCV version:", cv2.__version__)

    # Ask the user to select a cloak color
    lower_color1, upper_color1, lower_color2, upper_color2 = select_color()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Capture the background once (whether live or static)
    try:
        background = create_background(cap)
    except ValueError as e:
        print(f"Error: {e}")
        cap.release()
        return

    print("Starting main loop. Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            time.sleep(1)
            continue

        mask = create_mask(frame, lower_color1, upper_color1, lower_color2, upper_color2)
        result = apply_cloak_effect(frame, mask, background)

        cv2.imshow('Invisible Cloak', result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()