class RosslerAttractor:
    """
    Represents a Rossler attractor.

    Attributes
    ----------
    a : float
        The a parameter for the Rossler attractor.
    b : float
        The b parameter for the Rossler attractor.
    c : float
        The c parameter for the Rossler attractor.
    init_coords : list[float]
        The initial cartesian coordinates of the strange attractor.
    """

    def __init__(self, a=0.2, b=0.2, c=5.7, init_coords=[0.1, 0.0, -0.1]):
        """
        Constructs a RosslerAttractor object.

        Parameters
        ----------
        a : float
            The a parameter for the Rossler attractor.
        b : float
            The v parameter for the Rossler attractor.
        c : float
            The c parameter for the Rossler attractor.
        init_coords : list[float]
            The initial cartesian coordinates of the strange attractor.
        """

        self.a = a
        self.b = b
        self.c = c
        self.init_coords = init_coords

    def dxdt(self, x, y, z, t):
        """
        Returns the differential equation for dx/dt of the Rossler
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

        return - y - z

    def dydt(self, x, y, z, t):
        """
        Returns the differential equation for dy/dt of the Rossler
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

        return x + (self.a * y)

    def dzdt(self, x, y, z, t):
        """
        Returns the differential equation for dz/dt of the Rossler
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

        return self.b + (z * (x - self.c))
