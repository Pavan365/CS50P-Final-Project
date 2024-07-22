class LangfordAttractor:
    """
    Represents a Langford attractor.

    Attributes
    ----------
    a : float
        The a parameter for the Langford attractor.
    b : float
        The b parameter for the Langford attractor.
    c : float
        The c parameter for the Langford attractor.
    d : float
        The d parameter for the Langford attractor.
    e : float
        The e parameter for the Langford attractor.
    f : float
        The f parameter for the Langford attractor.
    init_coords : list[float]
        The initial cartesian coordinates of the strange attractor.
    """

    def __init__(self, a=0.95, b=0.7, c=0.6, d=3.5, e=0.25, f=0.1, init_coords = [0.1, 0.0, 0.0]):
        """
        Constructs a LangfordAttractor object.

        Parameters
        ----------
        a : float
            The a parameter for the Langford attractor.
        b : float
            The b parameter for the Langford attractor.
        c : float
            The c parameter for the Langford attractor.
        d : float
            The d parameter for the Langford attractor.
        e : float
            The e parameter for the Langford attractor.
        f : float
            The f parameter for the Langford attractor.
        init_coords : list[float]
            The initial cartesian coordinates of the strange attractor.
        """

        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.init_coords = init_coords

    def dxdt(self, x, y, z, t):
        """
        Returns the differential equation for dx/dt of the Langford
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

        return ((z - self.b) * x) - (self.d * y)

    def dydt(self, x, y, z, t):
        """
        Returns the differential equation for dy/dt of the Langford
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

        return (self.d * x) + ((z - self.b) * y)

    def dzdt(self, x, y, z, t):
        """
        Returns the differential equation for dz/dt of the Langford
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

        return self.c + (self.a * z) - ((z ** 3) / 3) - (((x ** 2) + (y ** 2)) * (1 + (self.e * z))) + (self.f * z * (x ** 3))
