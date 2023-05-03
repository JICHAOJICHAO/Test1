import math

def euclidean_distance(p1, p2):
    """
    计算欧几里得距离（二维空间）
    """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def brute_force(points):
    """
    暴力枚举所有点对的距离，找出最短距离并返回
    """
    n = len(points)
    min_distance = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
    return min_distance

def strip_closest(points, d):
    """
    在距离为 d 的带状区域内查找最短距离点对
    """
    n = len(points)
    min_distance = d
    # 将点按照 y 坐标从小到大排序
    sorted_points = sorted(points, key=lambda x: x[1])
    # 在每个点与其后面 7 个点之间计算距离
    for i in range(n):
        for j in range(i+1, min(i+8, n)):
            distance = euclidean_distance(sorted_points[i], sorted_points[j])
            if distance < min_distance:
                min_distance = distance
    return min_distance

def closest_pair(points):
    """
    使用分治法实现最近点对问题
    """
    n = len(points)
    # 如果点数小于等于 3，直接使用暴力枚举方法求解
    if n <= 3:
        return brute_force(points)
    # 将点集按照 x 坐标从小到大排序
    sorted_points = sorted(points, key=lambda x: x[0])
    # 将点集平分为两个子集
    mid = n // 2
    left_points = sorted_points[:mid]
    right_points = sorted_points[mid:]
    # 对子集递归求解最近点对距离
    d_left = closest_pair(left_points)
    d_right = closest_pair(right_points)
    # 取两个子集的最小距离
    d_min = min(d_left, d_right)
    # 计算跨越左右子集的最短距离
    strip_points = [p for p in sorted_points if abs(p[0] - sorted_points[mid][0]) < d_min]
    d_strip = strip_closest(strip_points, d_min)
    # 返回三种情况下的最小值
    return min(d_min, d_strip)

# 测试代码
points = [(2,3), (10, 1), (3, 25), (23,15),(18,3), (8,9), (12,30), (25,30),(9,2), (13,10), (3,4), (5,6), (22,32), (5,32), (23,9), (19,25),(14,1), (11,25), (26,26), (12,9),(18,9), (27,13), (32,13)]
print(closest_pair(points))
