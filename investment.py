def calculate_investment(investment_amount, num_years, interest_rate):
    # Initialize variables
    year = 1
    total_investment = investment_amount
    report = []

    # Calculate investment for each year
    while year <= num_years:
        interest_earned = total_investment * (interest_rate / 100)
        total_investment += interest_earned
        report.append((year, total_investment))
        year += 1

    return report

def display_report(investment_report):
    print("Year\tTotal Investment")
    for year, total_investment in investment_report:
        print(f"{year}\t${total_investment:.2f}")

investment_amount = float(input("Enter the investment amount: "))
num_years = int(input("Enter the number of years: "))
interest_rate = float(input("Enter the interest rate (as a percentage): "))

investment_report = calculate_investment(investment_amount, num_years, interest_rate)
display_report(investment_report)
