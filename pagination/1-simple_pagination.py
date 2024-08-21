#!/usr/bin/env python3
"""
this module contains a server class
"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        retrives a page data from the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = self.index_range(page, page_size)

        dataset = self.dataset()
        if start >= len(dataset):
            return []
        return dataset[start:end]

    def index_range(self, page: int = 1, page_size: int = 10) -> Tuple[int, int]:
        """
        retrurns tuple containing the start index and the
        end index for the given pagination parameters.
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return (start_index, end_index)
