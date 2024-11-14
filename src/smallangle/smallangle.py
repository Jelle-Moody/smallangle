import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def smallangle():
    """Initializes the click group. Shows The help text when run.
    """    
    pass

@smallangle.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Number of steps between 0 and 2pi.",
    show_default=True,  # show default in help
)
def sin(number):
    """Produces a list of points between 0 and 2pi and their sine.

    Args:
        number (int): number of steps between 0 and 2pi
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@smallangle.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Number of steps between 0 and 2pi.",
    show_default=True,  # show default in help
)
def tan(number):
    """Produces a list of points between 0 and 2pi and their tangent.

    Args:
        number (int): number of steps between 0 and 2pi
    """ 
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    smallangle()