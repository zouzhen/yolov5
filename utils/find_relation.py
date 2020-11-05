"""
使用图结构中深度优先遍历的操作来解决当前的问题
"""
from itertools import compress
import time


class Graph(object):
    """
    docstring
    """
    pass

    def __init__(self):
        pass
    # def __init__(self, graph, row, column):
        # self.row = row
        # self.column = column
        # self.visted = [[0] * column for _ in range(row)]
        # self.graph = graph

    # def dfs_fake(self):
    #     self.flag =

    def dfs_filter_relation(self, flag, avalible, stack, count_element):
        """
        判断当前节点和那些节点相连
        """
        deviation_list = [item for item in avalible if (
            abs(item[0] - flag[0]) + abs(item[1] - flag[1])) == 1]

        for item in deviation_list:
            avalible.remove(item)

        stack.extend(deviation_list)
        count_element.extend(deviation_list)
        # deviation_list = [(abs(item[0]-flag[0]), abs(item[1]-flag[1]))
        #                     for item in avalible]
        #     result = map(lambda x: x[0] + x[1] == 1, deviation_list)
        #     result = compress(avalible, result)
        # result = list(result)
        return deviation_list

    def dfs_filter_available(self, graph):
        filter_available = []
        for row_index, values in enumerate(graph):
            for column_index, value in enumerate(values):
                if value == 1:
                    filter_available.append((row_index, column_index))

        return filter_available

    def dfs_filter(self, graph):
        stack = []
        count = []
        filter_available = self.dfs_filter_available(graph)
        un_count = filter_available
        while un_count:
            element = un_count.pop(0)
            count_element = [element]
            self.dfs_filter_relation(element, un_count, stack, count_element)
            # map(un_count.remove, element_relation)
            while stack:
                element_i = stack.pop()
                self.dfs_filter_relation(
                    element_i, un_count, stack, count_element)
            # print(count_element)
            count.append(count_element)

        print(count)
        return max(map(len, count))


tmp = [
    [1, 1, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1]
]
if __name__ == "__main__":
    gra = Graph()
    start = time.time()
    max_unions = gra.dfs_filter(tmp)
    end = time.time()
    print('Consume :', end - start)
    print('Max Unions :', max_unions)
    # gra.dfs_filter_relation((0, 1), [(1, 2), (1, 0), (0, 2),(3,4)])
