def test_imports():
    import numpy
    import mne
    import torch

    assert hasattr(numpy, "array")
    assert mne.__version__
    assert torch.__version__
