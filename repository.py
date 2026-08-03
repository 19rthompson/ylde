from abc import ABC, abstractmethod

from comic import Comic


class Repository(ABC):

    @abstractmethod
    def get_comic_by_num(self, comic_num: int) -> Comic | None:
        """Return one comic by its XKCD number."""
        raise NotImplementedError