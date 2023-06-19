<p align="center">
  <a href="https://careamics.github.io/">
    <img src="https://raw.githubusercontent.com/CAREamics/.github/main/profile/images/banner_careamics.png">
  </a>
</p>

# CAREamics Portfolio

[![License](https://img.shields.io/pypi/l/careamics-portfolio.svg?color=green)](https://github.com/CAREamics/careamics-portfolio/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/careamics-portfolio.svg?color=green)](https://pypi.org/project/careamics-portfolio)
[![Python Version](https://img.shields.io/pypi/pyversions/careamics-portfolio.svg?color=green)](https://python.org)
[![CI](https://github.com/CAREamics/careamics-portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/CAREamics/careamics-portfolio/actions/workflows/ci.yml)
[![Datasets CI](https://github.com/CAREamics/careamics-portfolio/actions/workflows/datasets_ci.yml/badge.svg)](https://github.com/CAREamics/careamics-portfolio/actions/workflows/datasets_ci.yml)
[![codecov](https://codecov.io/gh/CAREamics/careamics-portfolio/branch/main/graph/badge.svg)](https://codecov.io/gh/CAREamics/careamics-portfolio)

A helper package to download example datasets used in various publications by the Jug lab, including data featured in N2V, P(P)N2V, DivNoising, HDN, EmbedSeg, etc.

The portfolio relies on [pooch](https://github.com/fatiando/pooch) to download the datasets.

The complete list of datasets can be found [here](https://raw.githubusercontent.com/CAREamics/careamics-portfolio/src/careamics_portfolio/datasets/datasets.json).


## Installation

To install the portfolio in your conda environment, simply use `pip`:
```bash
$ pip install careamics-portfolio
```

## Usage

Follow the [example notebook](examples/example.ipynb) for details on how to use the package.

The portfolio can be instantiated as follow:

```python
from careamics_portfolio import PortfolioManager

portfolio = PortfolioManager()
```

You can explore the different datasets easily:
```python
print(portfolio)
print(portfolio.denoising)
print(portfolio.denoising.N2V_SEM)
```

Finally, you can download the dataset of your choice:
```python
from pathlib import Path

data_path = Path('data')
portfolio.denoising.N2V_SEM.download(data_path)
```

By default, if you do not pass `path` to the `download()` method, all datasets
will be saved in your system's cache. New queries to download will not cause
the files to be downloaded again (thanks pooch!).

## Add a dataset to the repository

To add a dataset, subclass a `PortfolioEntry` and enter the following information 
(preferably in one of the current categories, e.g. `denoising_datasets.py`):
```python
class MyDataset(PortfolioEntry):
    def __init__(self) -> None:
        super().__init__(
            portfolio="Denoising", # for instance
            name="MyDataset",
            url="https://url.to.myfile/MyFile.zip",
            file_name="MyFile.zip",
            hash="953a815333805a423b7342971289h10121263917019bd16cc3341", # sha256
            description="Description of the dataset.",
            license="CC-BY 3.0",
            citation="Citation of the dataset",
            files={
                "/folder/in/the/zip": ["file1.tif", "file2.tif"], # folder can be "."
            },
            size=13.0, # size in MB
            tags=["tag1", "tag2"],
            is_zip=True,
        )
```

To obtain sha256 hash of your file, you can run the following code and read out
the sha256 from pooch prompt:
```python
import pooch

url = "https://url.to.myfile/MyFile.zip"
pooch.retrieve(url, known_hash=None)
```

Likewise, to get the size in MB of your file:
```python
import os

os.path.getsize(file_path) / 1024 / 1024
```

Finally, add the file class to one of the categories (e.g. denoising) in 
`portfolio.py`:
```python
class Denoising(IterablePortfolio):
    def __init__(self) -> None:
        self._N2V_BSD68 = N2V_BSD68()
        self._N2V_SEM = N2V_SEM()
        self._N2V_RGB = N2V_RGB()
        self._flywing = Flywing()

        # add your dataset as a private attribute
        self._myDataset = MyDataset()

        [...]

    # and add a public getter
    @property
    def MyDataset(self) -> MyDataset:
        return self._myDataset
```
