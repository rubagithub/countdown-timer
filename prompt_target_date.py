from datetime import datetime


def prompt_target_date():
    """Prompts the user to enter a target date and time."""
    print("Enter the day and time of our next meeting:")
    # Get year, month, day, hour, and minute from user
    year = int(input("Year: "))
    month = int(input("Month (1-12): "))
    day = int(input("Day (1-31): "))
    hour = int(input("Hour (0-23): "))
    minute = int(input("Minute (0-59): "))

    # Create a datetime object from the user's input
    target_date = datetime(year, month, day, hour, minute)
    # Format the date to display it in a user-friendly way
    formatted_date = target_date.strftime("%A, %B %d, %Y, %I:%M %p")

    # Print the formatted date before starting the countdown
    print(f"Counting down to: {formatted_date}")

    return target_date  # Return the target date
