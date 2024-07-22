class LorenzAttractor:
    """
    Represents a Lorenz attractor.

    Attributes
    ----------
    beta  : float
        The beta parameter for the Lorenz attractor.
    rho   : float
        The rho parameter for the Lorenz attractor.
    sigma : float
        The sigma parameter for the Lorenz attractor.
    init_coords : list[float]
        The initial cartesian coordinates of the strange attractor.
    """

    def __init__(self, beta=8/3, rho=28.0, sigma=10.0, init_coords=[0.1, 0.1, 0.1]):
        """
        Constructs a LorenzAttractor object.

        Parameters
        ----------
        beta  : float
            The beta parameter for the Lorenz attractor.
        rho   : float
            The rho parameter for the Lorenz attractor.
        sigma : float
            The sigma parameter for the Lorenz attractor.
        init_coords : list[float]
            The initial cartesian coordinates of the strange attractor.
        """

        self.beta = beta
        self.rho = rho
        self.sigma = sigma
        self.init_coords = init_coords

    def dxdt(self, x, y, z, t):
        """
        Returns the differential equation for dx/dt of the Lorenz
        attractor.

        Parameters
        ----------
        x : float
            The x cartesian coordinate.
        y : float
            The y cartesian coordinate.
        z : float
            The z cartesian coordinate.
        t : float
            Time.
        """

        return (self.sigma * (y - x))

    def dydt(self, x, y, z, t):
        """
        Returns the differential equation for dy/dt of the Lorenz
        attractor.

        Parameters
        ----------
        x : float
            The x cartesian coordinate.
        y : float
            The y cartesian coordinate.
        z : float
            The z cartesian coordinate.
        t : float
            Time.
        """

        return ((x * (self.rho - z)) - y)

    def dzdt(self, x, y, z, t):
        """
        Returns the differential equation for dz/dt of the Lorenz
        attractor.

        Parameters
        ----------
        x : float
            The x cartesian coordinate.
        y : float
            The y cartesian coordinate.
        z : float
            The z cartesian coordinate.
        t : float
            Time.
        """
        return ((x * y) - (self.beta * z))
