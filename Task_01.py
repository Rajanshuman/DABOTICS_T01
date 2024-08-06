import datetime
import time
import winsound

def set_alarm(alarm_time, sound_duration=5000):
    """
    Set an alarm for the specified time.

    Args:
        alarm_time (str): The time for the alarm in HH:MM:SS format.
        sound_duration (int): The duration of the alarm sound in milliseconds. Default is 5000 (5 seconds).

    Returns:
        None
    """
    print(f"Alarm set for {alarm_time}")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake Up!")
            winsound.Beep(2500, sound_duration)  # 2500 Hz frequency, sound_duration ms duration
            break
        time.sleep(1)

def main():
    alarm_time = input("Enter the alarm time in HH:MM:SS format: ")
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()