import click
import numpy as np
from numpy import pi
import pandas as pd

@click.command()
@click.argument("function")
@click.option(
    "-n",
    "--number",
    default=10,
    help="Number of steps between 0 and 2pi.",
    show_default=True,  # show default in help
)
def smallangle(function, number):
    if function == "sin":
        sin(number)
    if function == "tan":
        tan(number)
    if function != "sin" and function!= "tan":
        print("Function not recognized: try sin or tan")

def sin(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

def tan(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    sin(10)