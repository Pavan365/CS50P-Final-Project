class SprottAttractor:
    """
    Represents a Sprott attractor.

    Attributes
    ----------
    a : float
        The a parameter for the Sprott attractor.
    b : float
        The b parameter for the Sprott attractor.
    init_coords : list[float]
        The initial cartesian coordinates of the strange attractor.
    """

    def __init__(self, a=2.07, b=1.79, init_coords=[0.1, 0.0, 0.0]):
        """
        Constructs a SprottAttractor object.
        Parameters
        ----------
        a : float
            The a parameter for the Sprott attractor.
        b : float
            The b parameter for the Sprott attractor.
        init_coords : list[float]
            The initial cartesian coordinates of the strange attractor.
        """

        self.a = a
        self.b = b
        self.init_coords = init_coords

    def dxdt(self, x, y, z, t):
        """
        Returns the differential equation for dx/dt of the Sprott
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

        return y + (self.a * x * y) + (x * z)

    def dydt(self, x, y, z, t):
        """
        Returns the differential equation for dy/dt of the Sprott
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

        return 1 - (self.b * (x ** 2)) + (y * z)

    def dzdt(self, x, y, z, t):
        """
        Returns the differential equation for dz/dt of the Sprott
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

        return x - (x ** 2) - (y ** 2)
