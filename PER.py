def calculate_per(net_return, max_drawdown, max_unrealized_gain):
    """
    Calculates the Path Efficiency Ratio (PER)
    
    PER = Net Return / (abs(Max Drawdown) + (Max Unrealized Gain - Net Return))
    """
    denominator = abs(max_drawdown) + (max_unrealized_gain - net_return)
    if denominator == 0:
        return float('inf') if net_return > 0 else float('-inf')
    return net_return / denominator

def main():
    print("Path Efficiency Ratio (PER) Calculator")
    print("--------------------------------------")
    try:
        net_return = float(input("Enter Net Return use negative sign to denote a loss($): "))
        max_drawdown = float(input("Enter Max Drawdown in absolute value form ($): "))
        max_unrealized_gain = float(input("Enter Max Unrealized Gain ($): "))

        per = calculate_per(net_return, max_drawdown, max_unrealized_gain)
        print(f"\nPER = {per:.4f}")

        if per > 0.75:
            print("High efficiency")
        elif per > 0.25:
            print("Moderate efficiency")
        elif per > 0:
            print("Low efficiency")
        else:
            print("Inefficient trade resulting in a loss")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()
