from countdown_timer import CountdownTimer
from prompt_target_date import prompt_target_date

if __name__ == "__main__":
    target_date = prompt_target_date()  # Prompt user for target date
    timer = CountdownTimer(target_date)  # Create a CountdownTimer instance
    timer.countdown()  # Start the countdown
