import os


def test_notebook_exists():
    assert os.path.exists(os.path.join('notebooks', 'baseline.ipynb')), \
        "notebooks/baseline.ipynb no encontrada. Por favor mueva el cuaderno a la carpeta notebooks/"
