class ProductFilter:
    @staticmethod
    def filter_by_color(products, color):
        for product in products:
            if product.color == color:
                yield product

    @staticmethod
    def filter_by_size(products, size):
        for product in products:
            if product.color == size:
                yield product

    @staticmethod
    def filter_by_color_and_size(products, color, size):
        for product in products:
            if product.color == color and product.size == size:
                yield product

# This type of implementation (a separate method for each filter type) can cause 'State Space Explosion'
# For example,
# we have 2 criteria, then then are at least 3 methods needed to filter properly
#
# if we have 3 criteria, then minimum methods with only 'and' operation will be 7
# c s w -> c s w cs cw sw csw
