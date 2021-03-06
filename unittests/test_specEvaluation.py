import unittest
import numpy as np
from typing import List
from importData import get_database, get_test_spectra
from specCorrelation import correlate_spectra, mapSpectrasetsToSameWavenumbers


class TestSpecEvaluation(unittest.TestCase):
    def test_match_specSets(self) -> None:
        specs1: np.ndarray = np.zeros((10, 21))  # i.e., 20 spectra with 10 wavenumbers
        specs1[:, 0] = np.arange(10)
        specs1[:, 1:] = np.random.rand(10, 20)
        specs2: np.ndarray = np.zeros((5, 11))  # i.e. 10 spectra with 5 wavenumbers
        specs2[:, 0] = np.arange(5)
        specs2[:, 1:] = np.random.rand(5, 10)

        newSpecs1, newSpecs2 = mapSpectrasetsToSameWavenumbers(specs1, specs2)
        self.assertTrue(newSpecs1.shape[0] == newSpecs2.shape[0] == specs2.shape[0])
        self.assertTrue(np.array_equal(newSpecs2, specs2))
        self.assertTrue(np.array_equal(newSpecs1[:, 0], newSpecs2[:, 0]))

        newSpecs1, newSpecs2 = mapSpectrasetsToSameWavenumbers(specs2, specs1)
        self.assertTrue(newSpecs1.shape[0] == newSpecs2.shape[0] == specs2.shape[0])
        self.assertTrue(np.array_equal(newSpecs1, specs2))
        self.assertTrue(np.array_equal(newSpecs1[:, 0], newSpecs2[:, 0]))

    def test_specCorr(self) -> None:
        names, specs = get_test_spectra(maxSpectraPerFolder=5)  # we don't need aaaall the spectra...
        db = get_database()

        # just to see that no errors occur..
        results: List[str] = correlate_spectra(specs, db)
