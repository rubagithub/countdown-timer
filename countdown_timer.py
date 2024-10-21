import time
from datetime import datetime


class CountdownTimer:
    def __init__(self, target_date):
        """Initializes the countdown timer with a target date."""
        self.target_date = target_date

    def time_remaining(self):
        """Calculates the remaining time until the target date."""
        now = datetime.now()  # Get the current date and time
        remaining_time = self.target_date - now  # Calculate the remaining time
        days = remaining_time.days  # Get the number of days
        hours, remainder = divmod(remaining_time.seconds, 3600)  # Get hours and remainder
        minutes, seconds = divmod(remainder, 60)  # Get minutes and seconds
        return days, hours, minutes, seconds  # Return the remaining time

    def has_passed(self):
        """Checks if the target date has passed."""
        now = datetime.now()  # Get the current date and time
        return now > self.target_date  # Return True if the current time is after the target date

    def countdown(self):
        """Prints the countdown to the target date."""
        while not self.has_passed():  # Keep counting down until the date has passed
            days, hours, minutes, seconds = self.time_remaining()  # Get the remaining time
            print(f"Time remaining: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds", end="\r")
            time.sleep(1)  # Wait for 1 second
        print("\nThe countdown has ended!")  # Message when countdown finishes
