import numpy as np
import sys

def trans(t1,t2,points):
    homogeneous_points = np.hstack([points, np.ones((len(points), 1))])
    transformed_points = np.dot(-t1, homogeneous_points.T).T

    transformed_points_2 = np.dot(t2, transformed_points.T).T
    transformed_points_2 = transformed_points_2[:, :3] / transformed_points_2[:, 3][:, np.newaxis]

    return transformed_points_2


if __name__=='__main__':
    if len(sys.argv) < 2:
        print("Please provide the file name as a command line argument.")
        sys.exit(1)
    file_name = sys.argv[1]
    points = np.loadtxt(file_name)
    print(points)
    t1 = np.load('/home/zhaoruifeng1211/points2poly/points2poly/datasets/DALES/translation.npy')
    t2 = np.load('/home/zhaoruifeng1211/points2poly/points2poly/datasets/DALES/scale.npy')
    points_trans=trans(t1,t2,points)
    print(points_trans)


   
