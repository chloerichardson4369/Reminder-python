import time
import platform
import os
import sys

def notify(title, message):
    system = platform.system()

    if system == "Darwin":  # macOS
        os.system(f"""osascript -e 'display notification "{message}" with title "{title}"'""")
    elif system == "Linux":
        os.system(f'notify-send "{title}" "{message}"')
    elif system == "Windows":
        try:
            from plyer import notification
            notification.notify(
                title=title,
                message=message,
                timeout=10
            )
        except ImportError:
            print("Для уведомлений на Windows установите пакет: pip install plyer")
    else:
        print(f"[Уведомление] {title}: {message}")

def main():
    print("🕑 Напоминалка")
    message = input("Введите текст напоминания: ")
    try:
        minutes = float(input("Через сколько минут напомнить? "))
    except ValueError:
        print("Ошибка: нужно ввести число.")
        sys.exit(1)

    seconds = minutes * 60
    print(f"Ок! Напомню через {minutes} минут...")
    time.sleep(seconds)

    notify("⏰ Напоминание", message)
    print(f"\n🔔 Напоминание: {message}")

if __name__ == "__main__":
    main()
