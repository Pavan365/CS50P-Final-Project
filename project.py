# Import standard libraries.
import argparse

# Import external libraries.
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

# Import local modules.
from attractors.langford import LangfordAttractor
from attractors.lorenz import LorenzAttractor
from attractors.rossler import RosslerAttractor
from attractors.sprott import SprottAttractor


def main():
    # Configure the simulation with command line arguments.
    args = arguments()
    valid(args.output, args.time)

    # Simulate the strange attractor.
    steps = calc_steps(args.output, args.time)
    attractor = get_attractor(args.attractor)
    data = runge_kutta_four(attractor.dxdt, attractor.dydt, attractor.dzdt, args.time, steps, attractor.init_coords)

    # Visualise the simulation.
    if args.output == "image":
        plot(args.attractor, data)

    else:
        animate(args.attractor, data, steps)


def arguments():
    """
    Defines and returns command line arguments.
    The command line arguments will be used to configure the simulation.

    CLI Arguments
    -------------
    attractor : The strange attractor that should be simulated.
                {langford, lorenz, rossler, sprott}.
    output    : The output format of the simulation.
                {animation, image}.
    time      : The total time of the simulation.
                Max time for animation = 60, image = 600.

    Returns
    -------
    object argparse.Namespace
        Contains the attractor, output and time arguments.
    """

    parser = argparse.ArgumentParser()

    strange_attractors = ["langford", "lorenz", "rossler", "sprott"]

    parser.add_argument("attractor", choices=strange_attractors, type=str.lower, help="strange attractor to be simulated")
    parser.add_argument("output", choices=["animation", "image"], type=str.lower, help="output format of simulation")
    parser.add_argument("time", type=int, help="total time of simulation {animation : 1-60, image : 1-600}")

    return parser.parse_args()


def valid(output, time):
    """
    Validates the "time" argument for the simulation.

    The simulation time should be a positive integer. If the output
    format is "animation", the maximum allowed time is 60 seconds.
    If the output format is "image", the maximum allowed time is 600
    seconds. All of these conditions are checked.

    Parameters
    ----------
    output : str
        The output format of the simulation.
    time   : int
        The total time of the simulation.

    Returns
    -------
    bool True
        If the "time" argument is valid.

    Raises
    ------
    error ValueError
        If the "time" argument is invalid.
    """

    if time < 1:
        raise ValueError("invalid simulation time")

    elif output == "image" and time > 600:
        raise ValueError("simulation time too long for image")

    elif output == "animation" and time > 60:
        raise ValueError("simulation time too long for animation")

    return True


def calc_steps(output, time):
    """
    Calculates the number of steps to use in the simulation.

    A step size of 0.02 is used for a simulation with output format
    "animation". A step size of 0.01 is used for a simulation with
    output format "image".

    Parameters
    ----------
    output : str
        The output format of the simulation.
    time   : int
        The total time of the simulation.
    Returns
    -------
    int
        The number of steps to use in the simulation.
    """

    step = 0.01 if output == "image" else 0.02
    return int(time / step)


def get_attractor(attractor):
    """
    Returns an object of the class corresponding to the strange
    attractor that is being simulated.

    Parameters
    ----------
    attractor : str
        The strange attractor that is being simulated.

    Returns
    -------
    object LangfordAttractor
        To simulate a Langford attractor.
    object LorenzAttractor
        To simulate a Lorenz attractor.
    object RosslerAttractor
        To simulate a Rossler attractor.
    object SprottAttractor
        To simulate a Sprott attractor.

    Raises
    ------
    error ValueError
        If an object corresponding to the strange attractor could not
        be found.
    """

    match attractor:
        case "langford":
            return LangfordAttractor()
        case "lorenz":
            return LorenzAttractor()
        case "rossler":
            return RosslerAttractor()
        case "sprott":
            return SprottAttractor()
        case _:
            raise ValueError("attractor not found")


def runge_kutta_four(dxdt, dydt, dzdt, time, steps, init_coords):
    """
    Solves the ODES's (differential equations) for the strange attractor
    that is being simulated using the 4th order Runge-Kutta method.

    Parameters
    ----------
    dxdt : function
        The function which returns the differential equation for dx/dt
        of the strange attractor.
    dydt : function
        The function which returns the differential equation for dy/dt
        of the strange attractor.
    dzdt : function
        The function which returns the differential equation for dz/dt
        of the strange attractor.
    time  : int
        The total time of the simulation.
    steps : int
        The number of steps to use for the simulation.
    init_coords : list[float]
        The initial cartesian coordinates of the strange attractor.

    Returns
    -------
    data : numpy.ndarray
        The data containing the coordinates for the entire simulation of
        the strange attractor.
    """

    # Initialise arrays for each of the cartesian coordinates and time.
    x = np.zeros(steps + 1)
    y = np.zeros(steps + 1)
    z = np.zeros(steps + 1)
    t = np.zeros(steps + 1)

    # Calculate the step size.
    dt = time/steps

    # Set the initial coordinates.
    x[0] = init_coords[0]
    y[0] = init_coords[1]
    z[0] = init_coords[2]

    # Perform the 4th order Runge-Kutta method.
    for i in range(steps):

        # 1st order calculations.
        k1_x = dxdt(x[i], y[i], z[i], t[i])
        k1_y = dydt(x[i], y[i], z[i], t[i])
        k1_z = dzdt(x[i], y[i], z[i], t[i])

        # 2nd order calculations.
        x_k2 = x[i] + (0.5 * k1_x * dt)
        y_k2 = y[i] + (0.5 * k1_y * dt)
        z_k2 = z[i] + (0.5 * k1_z * dt)
        t_k2 = t[i] + (0.5 * dt)

        k2_x = dxdt(x_k2, y_k2, z_k2, t_k2)
        k2_y = dydt(x_k2, y_k2, z_k2, t_k2)
        k2_z = dzdt(x_k2, y_k2, z_k2, t_k2)

        # 3rd order calculations.
        x_k3 = x[i] + (0.5 * k2_x * dt)
        y_k3 = y[i] + (0.5 * k2_y * dt)
        z_k3 = z[i] + (0.5 * k2_z * dt)
        t_k3 = t[i] + (0.5 * dt)

        k3_x = dxdt(x_k3, y_k3, z_k3, t_k3)
        k3_y = dydt(x_k3, y_k3, z_k3, t_k3)
        k3_z = dzdt(x_k3, y_k3, z_k3, t_k3)

        # 4th order calculations.
        x_k4 = x[i] + (k3_x * dt)
        y_k4 = y[i] + (k3_y * dt)
        z_k4 = z[i] + (k3_z * dt)
        t_k4 = t[i] + dt

        k4_x = dxdt(x_k4, y_k4, z_k4, t_k4)
        k4_y = dydt(x_k4, y_k4, z_k4, t_k4)
        k4_z = dzdt(x_k4, y_k4, z_k4, t_k4)

        # Update the cartesian coordinates and time of the simulation.
        x[i + 1] = x[i] + ((dt * (k1_x + (2 * k2_x) + (2 * k3_x) + k4_x)) / 6)
        y[i + 1] = y[i] + ((dt * (k1_y + (2 * k2_y) + (2 * k3_y) + k4_y)) / 6)
        z[i + 1] = z[i] + ((dt * (k1_z + (2 * k2_z) + (2 * k3_z) + k4_z)) / 6)
        t[i + 1] = t[i] + dt

    # Return the data for the entire simulation.
    return np.array([x, y, z, t])


def plot(attractor, data):
    """
    Creates a plot of the simulation.

    Parameters
    ----------
    attractor : str
        The strange attractor that is being simulated.
    data : numpy.ndarray
        The data for the plot, which contains the coordinates for the
        entire simulation of the strange attractor.

    Ouput
    -----
    png
        Image file containing a plot of the simulation.

    """

    ax = plt.figure().add_subplot(projection="3d")

    ax.plot(data[0], data[1], data[2], linewidth=1, color="rebeccapurple")
    ax.tick_params(left=False, right=False, bottom=False, labelleft=False, labelright=False, labelbottom=False)

    plt.savefig(f"{attractor}.png")


def animate(attractor, data, steps):
    """
    Creates an animation of the simulation.

    Parameters
    ----------
    attractor : str
        The strange attractor that is being simulated.
    data : numpy.ndarray
        The data for the animation, which contains the coordinates for
        the entire simulation of the strange attractor.
    steps : int
        The number of steps used in the simulation.

    Ouput
    -----
    gif
        GIF file containing an animation of the simulation.

    """

    def update_animation(frame, data, line):
        """
        Updates the line being plotted in the animation.

        Parameters
        ----------
        frame : int
            The frame of the animation.
        data : numpy.ndarray
            The data for the animation, which contains the coordinates
            for the entire simulation of the strange attractor.
        line : object mpl_toolkits.mplot3d.art3d.Line3D
            The line being plotted in the animation.

        Returns
        -------
        line : object mpl_toolkits.mplot3d.art3d.Line3D
            The line being plotted in the animation.
        """

        line.set_data(data[:2, :frame])
        line.set_3d_properties(data[2, :frame])
        line.set_color("rebeccapurple")

        return line

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    line = ax.plot([], [], [])[0]

    ax.set(xlim3d=(min(data[0]), max(data[0])))
    ax.set(ylim3d=(min(data[1]), max(data[1])))
    ax.set(zlim3d=(min(data[2]), max(data[2])))
    ax.tick_params(left=False, right=False, bottom=False, labelleft=False, labelright=False, labelbottom=False)

    animate = FuncAnimation(fig, update_animation, steps, fargs=(data, line), interval=1)
    animate.save(f"{attractor}.gif", fps=30)


if __name__ == "__main__":
    main()
