import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


from datetime import datetime

def convert_date(iso_string):
    """Converts an ISO formatted date into a human-readable format.
    
    Args:
        iso_string: An ISO date string.
    
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # Step 1: Parse the ISO string using fromisoformat (handles full ISO 8601 format)
    date_object = datetime.fromisoformat(iso_string)
    
    # Step 2: Format the datetime object into the desired format
    human_readable_date = date_object.strftime("%A %d %B %Y")
    
    # Step 3: Return the formatted date
    return human_readable_date

# Example Test
print(convert_date("2021-07-06T07:00:00+08:00"))  # Output: Tuesday 06 July 2021


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    # Step 1: from fahrenheit to celcius
    temp_in_celsius = (float(temp_in_fahrenheit) - 32) * 5 / 9
    # Step 2: return
    return round(temp_in_celsius, 1)



def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    return sum([float(item) for item in weather_data]) / len(weather_data) 


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    weather_data = []

    with open(csv_file) as weather_data_csv:
        csv_dictreader = csv.DictReader(weather_data_csv)
        for row in csv_dictreader:
            if row:
                weather_data.append([row["date"], float(row["min"]), float(row["max"])])

    return weather_data


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:  # Check if the list is empty
        return ()  # Return an empty tuple if the list is empty

    try:
        # Convert all items to float and find the minimum value
        numeric_data = [float(item) for item in weather_data]
        min_value = min(numeric_data)
    except ValueError:
        # If conversion fails, return None values
        return None, None

    # Find the last index of the minimum value in the numeric data
    last_index = len(numeric_data) - 1 - numeric_data[::-1].index(min_value)

    return min_value, last_index

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:  # Check if the list is empty
        return ()  # Return an empty tuple if the list is empty

    try:
        # Convert all items to float and find the maximum value
        numeric_data = [float(item) for item in weather_data]
        max_value = max(numeric_data)
    except ValueError:
        # If conversion fails, return None values
        return None, None

    # Find the last index of the maximum value in the numeric data
    last_index = len(numeric_data) - 1 - numeric_data[::-1].index(max_value)

    return max_value, last_index


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    dates = [sublist[0] for sublist in weather_data]

    min_temps_f = [float(sublist[1]) for sublist in weather_data]
    min_temp_f, min_temp_f_index = find_min(min_temps_f)
    min_temp_c = convert_f_to_c(min_temp_f)
    min_temp_date = convert_date(dates[min_temp_f_index])
    min_temp_avg_c = convert_f_to_c(calculate_mean(min_temps_f))

    max_temps_f = [float(sublist[2]) for sublist in weather_data]
    max_temp_f, max_temp_f_index = find_max(max_temps_f)
    max_temp_c = convert_f_to_c(max_temp_f)
    max_temp_date = convert_date(dates[max_temp_f_index])
    max_temp_avg_c = convert_f_to_c(calculate_mean(max_temps_f))

    return (
        f"{len(weather_data)} Day Overview\n"
        f"  The lowest temperature will be {format_temperature(min_temp_c)}, and will occur on {min_temp_date}.\n"
        f"  The highest temperature will be {format_temperature(max_temp_c)}, and will occur on {max_temp_date}.\n"
        f"  The average low this week is {format_temperature(min_temp_avg_c)}.\n"
        f"  The average high this week is {format_temperature(max_temp_avg_c)}.\n"
    )


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""

    for data in weather_data:
        date = data[0]
        min_temp_c = convert_f_to_c(float(data[1]))
        max_temp_c = convert_f_to_c(float(data[2]))

        summary += (
            f"---- {convert_date(date)} ----\n"
            f"  Minimum Temperature: {format_temperature(min_temp_c)}\n"
            f"  Maximum Temperature: {format_temperature(max_temp_c)}\n\n"
        )

    return summary
