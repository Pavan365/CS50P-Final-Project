# Import needed libraries.
import pytest

# Import local modules.
from attractors.langford import LangfordAttractor
from attractors.lorenz import LorenzAttractor
from attractors.rossler import RosslerAttractor
from attractors.sprott import SprottAttractor

# Import functions to be tested.
from project import valid, calc_steps, get_attractor

def test_valid():
    """
    Test the "validate" function.
    """

    # Test invalid cases.
    invalid_image_times = [0, -20, 601, 800]
    invalid_animation_times = [0, -20, 61, 80]

    for time in invalid_image_times:
        with pytest.raises(ValueError):
            valid("image", time)

    for time in invalid_animation_times:
        with pytest.raises(ValueError):
            valid("animation", time)

    # Test valid cases.
    assert valid("image", 1) == True
    assert valid("image", 200) == True
    assert valid("image", 400) == True
    assert valid("image", 600) == True

    assert valid("animation", 1) == True
    assert valid("animation", 20) == True
    assert valid("animation", 40) == True
    assert valid("animation", 60) == True


def test_calc_steps():
    """
    Test the "calc_steps" function.
    """

    # Test valid cases.
    assert calc_steps("image", 1) == 100
    assert calc_steps("image", 60) == 6000
    assert calc_steps("image", 120) == 12000
    assert calc_steps("image", 600) == 60000

    assert calc_steps("animation", 1) == 50
    assert calc_steps("animation", 20) == 1000
    assert calc_steps("animation", 40) == 2000
    assert calc_steps("animation", 60) == 3000


def test_get_attractor():
    """
    Test the "get_attractor" function.
    """

    # Test invalid case.
    with pytest.raises(ValueError):
        get_attractor("random")

    # Test valid cases.
    assert isinstance(get_attractor("langford"), LangfordAttractor)
    assert isinstance(get_attractor("lorenz"), LorenzAttractor)
    assert isinstance(get_attractor("rossler"), RosslerAttractor)
    assert isinstance(get_attractor("sprott"), SprottAttractor)
