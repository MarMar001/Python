def calculate_present_value_annuity(monthly_payment, annual_rate, years):
    """
    Calculate the present value of an annuity based on monthly payments.
    
    :param monthly_payment: The amount of each monthly payment.
    :param annual_rate: The annual discount rate (expected rate of return).
    :param years: The total number of years the payments will be made.
    :return: The present value of the annuity.
    """
    if annual_rate <= 0 or years <= 0 or monthly_payment <= 0:
        raise ValueError("Annual rate, years, and monthly payment must be positive values.")
    monthly_rate = annual_rate / 12  # Convert annual rate to monthly
    number_of_payments = years * 12  # Total number of payments

    present_value = monthly_payment * ((1 - (1 + monthly_rate) ** -number_of_payments) / monthly_rate)
    return present_value

def compare_lump_sum_vs_annuity(lump_sum, monthly_payment, annual_rate, years):
    """
    Compare a lump sum payment to the present value of an annuity.
    
    :param lump_sum: The lump sum amount offered.
    :param monthly_payment: The monthly payment amount in the annuity option.
    :param annual_rate: The annual discount rate (expected rate of return).
    :param years: The number of years the annuity will be paid.
    :return: A comparison result indicating which option is more valuable.
    """
    # Calculate present value of the annuity
    pv_annuity = calculate_present_value_annuity(monthly_payment, annual_rate, years)

    # Compare the lump sum to the present value of the annuity
    if lump_sum > pv_annuity:
        return f"Lump sum of ${lump_sum:,.2f} is better than the present value of the annuity (${pv_annuity:,.2f})."
    else:
        return f"The present value of the annuity (${pv_annuity:,.2f}) is better than the lump sum of ${lump_sum:,.2f}."

# Example Usage
lump_sum = 500000  # Lump sum amount
monthly_payment = 2500  # Monthly annuity payment
annual_rate = 0.05  # Expected rate of return (5%)
years = 30  # Number of years the annuity will be paid

result = compare_lump_sum_vs_annuity(lump_sum, monthly_payment, annual_rate, years)
print(result)
