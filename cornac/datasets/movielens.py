# -*- coding: utf-8 -*-

"""
@author: Quoc-Tuan Truong <tuantq.vnu@gmail.com>
"""

from ..utils.download_utils import DownloadItem
from ..utils.generic_utils import validate_data_format
from ..data.reader import Reader


class MovieLens:

    @property
    def base_url(self):
        """Return the base url of the MovieLens datasets"""
        return 'http://files.grouplens.org/datasets/movielens'


class MovieLens100K(MovieLens):

    @staticmethod
    def load_data(format='UIR', verbose=False):
        """Load the MovieLens 100K dataset

        Parameters
        ----------
        format: str, default: 'UIR'
            Data format to be returned.

        verbose: bool, default: False
            The verbosity flag.

        Returns
        -------
        data: array-like
            Data in the form of a list of tuples depending on the given data format.

        """
        download_item = DownloadItem(url='{}/ml-100k/u.data'.format(MovieLens.base_url),
                                     relative_path='ml-100k/u.data')
        fpath = download_item.maybe_download(verbose)

        format = validate_data_format(format)
        if format == 'UIR':
            return Reader.read_uir_triplets(fpath)


class MovieLens1M(MovieLens):

    @staticmethod
    def load_data(format='UIR', verbose=False):
        """Load the MovieLens 1M dataset

        Parameters
        ----------
        format: str, default: 'UIR'
            Data format to be returned.

        verbose: bool, default: False
            The verbosity flag.

        Returns
        -------
        data: array-like
            Data in the form of a list of tuples depending on the given data format.

        """
        download_item = DownloadItem(url='{}/ml-1m.zip'.format(MovieLens),
                                     relative_path='ml-1m/ratings.dat', unzip=True)
        fpath = download_item.maybe_download(verbose)

        format = validate_data_format(format)
        if format == 'UIR':
            return Reader.read_uir_triplets(fpath, sep='::')