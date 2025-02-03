#region imports
from numericalMethods import GPDF, Probability
#endregion

#region function definitions
def main():
    """
    This program is designed to solicit input from the CLI and return a probability from the Gaussian Normal Distribution
    by integrating the probability density function using Simpson's 1/3 rule for numerical integration.

    The user may decide upon a two-sided integration or one-sided integration.
    If one-sided, we integrate from the smaller of mean-5*stDev or c-stDev.
    If two-sided, we integrate from -c to c.
    Here is my step-by-step plan:
    1. Decide mean, stDev, and c and if I want P(x>c) or P(x<c) or P(-c<x<c) or P(-c>x>c).
    2. Define args tuple and c to be passed to Probability
    3. Pass args, and a callback function (GPDF) to Probability
    4. In probability, pass along GPDF to Simpson along with the appropriate args tuple
    5. Return the required probability from Probability and print to screen.
    :return: Nothing to return, just print results to screen.
    """
    #region testing user input
    Again = True
    mean = 0
    stDev = 1.0
    c = 0.5
    while Again==True:
        # The following code solicites user input through the CLI.
        response = input(f"Population mean? ({mean:0.3f})")
        # "clean the user input
        response = response.strip().lower()  # strip of leading or trailing spaces and make lower case.
        if response == '':
            mean=mean
        else:
            mean = float(response)  # Whatever the user types, it is a string.  I need to convert it to a floating point number.

        stDev = 1.0
        response = input(f"Standard deviation? ({stDev:0.3f})").strip().lower()
        stDev = float(response) if response != '' else stDev
        c=2.0
        response = input(f"c value? ({c:0.3f})").strip().lower()

        c = float(response) if response != '' else c

        GT = False
        response=input(f"Probability greater than c? ({GT})").strip().lower()
        GT = True if response in ["y","yes","true"] else GT
        prob = Probability(GPDF,(mean,stDev),c,GT=GT)
        print(f"P(x"+(">" if GT == True else "<") + f"{c:0.2f}" +"|"+f"{mean:0.2f}"+", "+f"{stDev:0.2f}" +f") = {prob:0.2f}")
        response = input(f"Go again? (Y/N)").strip().lower()
        Again = True if response in ["y","yes","true"] else False
    #endregion

#endregion

if __name__ == "__main__":
    main()