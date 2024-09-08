def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # calculate the total sum of the list
    total_sum=sum(weather_data)
    #calculate the number of elements  in the list
    count=len(weather_data)
    #calculate the mean
    mean=(total_sum/count)

    return mean