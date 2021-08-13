from Filter import Filter
from typing import Type
from Specification import Specification


class NewFilter(Filter):
    def filter(self, items, spec: Type[Specification]):
        for item in items:
            if spec.is_satisfied(item):
                yield item
