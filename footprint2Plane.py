import numpy as np
# from convertnew import trans
import sys
import os

def trans(t1,t2,points):
    homogeneous_points = np.hstack([points, np.ones((len(points), 1))])
    transformed_points = np.dot(-t1, homogeneous_points.T).T

    transformed_points_2 = np.dot(t2, transformed_points.T).T
    transformed_points_2 = transformed_points_2[:, :3] / transformed_points_2[:, 3][:, np.newaxis]

    return transformed_points_2

def getPlane(A,B):
    # 直线AB的两个点坐标
    A = np.array(A)  # 替换为实际坐标
    B = np.array(B)  # 替换为实际坐标

    # 计算直线AB的方向向量
    direction_vector_AB = B - A

    # 找到垂直于xoy平面且过直线AB的平面的法向量
    normal_vector = np.cross(direction_vector_AB, np.array([0, 0, 1]))

    # 构建平面方程 ax + by + cz + d = 0
    a, b, c = normal_vector
    d = -np.dot(normal_vector, A)

    # 将平面方程转换至单位立方体空间内
    # 可以通过将平面方程中的系数除以单位立方体的尺寸来实现
    # 假设单位立方体的尺寸为1
    # unit_cube_size = 1
    # a /= unit_cube_size
    # b /= unit_cube_size
    # c /= unit_cube_size
    # d /= unit_cube_size

    return [a,b,c,d]

def objLine2Plane(filepath):
    points = []
    with open(filepath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('v '):
                # 读取点坐标
                x, y, z = line.strip().split()[1:]
                points.append([float(x), float(y), float(z)])
    points=np.array(points)
    filebase= os.path.dirname(filepath)
    filename=os.path.basename(filepath)
    t1_path=os.path.join(os.path.dirname(filebase),'09_homo',filename[:-14]+'_translation.npy')
    t2_path=os.path.join(os.path.dirname(filebase),'09_homo',filename[:-14]+'_scale.npy')

    t1 = np.load(t1_path)
    t2 = np.load(t2_path)
    points_trans=trans(t1,t2,points)
    plane=[]
    for i in range(len(points_trans)-1):
        plane.append(getPlane(points_trans[i], points_trans[i+1]))
    plane.append(getPlane(points_trans[-1], points_trans[0]))

    planeSavedPath=os.path.join(os.path.dirname(filebase),'08_footprint',filename[:-4]+'_FTplane.npy')
    np.save(planeSavedPath,plane)
    # print(plane)
    # print(points_trans)
# 打印平面方程
if __name__=='__main__':
    filepath=sys.argv[1]
    objLine2Plane(filepath)
    print("trans done")

