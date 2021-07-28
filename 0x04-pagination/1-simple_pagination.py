#!/usr/bin/env python3
"""Simple pagination task 1"""
from typing import Tuple, List
import csv
import math


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """finds the correct indexes to paginate the dataset correctly
        and return the appropriate page of the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0
        range_p = index_range(page, page_size)
        server = Server()
        s = range_p[0]
        e = range_p[1]
        if e > len(server.dataset()):
            return []
        return(server.dataset()[s:e])


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters
    """
    start = abs((page - 1) * page_size)
    end = page * page_size
    return (start, end)
