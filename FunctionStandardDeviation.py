date = [147,152,152,160,160,165,165,165,172,172,172,178,178,178,182,182,185,185,190,205]
def sd(date, args=None):
    """
    Args:
        date (list): List of values
        args (int, tuple, None): Additional argument for displaying comments.
        - 1: Displays the mean.
        - 2: Displays the variance.
        - 3: Displays the standard deviation.
        - 12: Displays the mean and variance.
        - 13: Displays the mean and standard deviation.
        - 23: Displays the variance and standard deviation.
        - 0: Displays all values ​​(mean, variance, standard deviation).
    """
    # D = (sum(Xi - mean)^2) / n-1
    # sd = sqrt(D)
    # We are looking for the mean from the list
    mean = sum(date) / len(date)
    # Find the sum of the values ​​(date[i] - x) 
    # Square this sum and then divide by the number of values ​​in the list 
    # This way we get the dispersion
    D = sum((i - mean) ** 2 for i in date) / (len(date) - 1)
    # We take the square of the variance and get the standard deviation
    sd = D ** 0.5

    if args is not None:
        if args == 1:
            print('Mean =', mean)
            return mean
        elif args == 2:
            print('Dispersion =', D)
            return D
        elif args == 3:
            print('Standard deviation =', sd)
            return sd
        elif args == 12:
            print('Mean =', mean)
            print('Dispersion =', D)
            return mean, D
        elif args == 13:
            print('Mean =', mean)
            print('Standard deviation = ', sd)
            return mean, sd
        elif args == 23:
            print('Dispersion =', D)
            print('Standard deviation =', sd)
            return D, sd
        elif args == 0:
            print('Mean =', mean)
            print('Dispersion =', D)
            print('Standard deviation =', sd)
            return mean, D, sd
        else:
            return sd
print(sd(date,23))