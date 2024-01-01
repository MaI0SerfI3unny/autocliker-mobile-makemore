import cv2
import numpy as np
import pyautogui
from modules import validate_args

pyautogui.FAILSAFE = False


def main():
    get_path_template = validate_args.validate_args_path()
    get_per_click = validate_args.validate_args_per_click()
    get_threshold = validate_args.validate_threshold()

    template = cv2.imread(get_path_template)
    while True:
        screenshot = np.array(pyautogui.screenshot())
        screenshot_cv = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        # Пошук співпадінь за допомогою алгоритму Template Matching
        result = cv2.matchTemplate(screenshot_cv, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)


        if max_val >= get_threshold:
            print("Елемент знайдено.")
            height, width, _ = template.shape
            
            left, top = max_loc
            print(f"Координати знайденого елемента: left={left}, top={top}")

            # Розрахунок центральних координат елемента
            center_x = left + width // 2
            center_y = top + height // 2

            # Масштабування координат відносно розмірів екрана
            scaled_x = center_x * (pyautogui.size().width / screenshot.shape[1])
            scaled_y = center_y * (pyautogui.size().height / screenshot.shape[0])

            # Переміщення миші на координати знайденого елемента
            pyautogui.moveTo(scaled_x, scaled_y)
            for i in range(get_per_click):
                pyautogui.click()
        else:
            print("Елемент не знайдено.")


if __name__ == "__main__": main()