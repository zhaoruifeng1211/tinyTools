import os
import sys
import numpy as np


def trans(t1,t2,points):
    homogeneous_points = np.hstack([points, np.ones((len(points), 1))])
    transformed_points = np.dot(-t1, homogeneous_points.T).T

    transformed_points_2 = np.dot(t2, transformed_points.T).T
    transformed_points_2 = transformed_points_2[:, :3] / transformed_points_2[:, 3][:, np.newaxis]

    return transformed_points_2

def transModelObj(filepath,translation,scale):
    points=[]
    polys=[]
    with open(filepath,'r') as file:
        lines=file.readlines()
        for line in lines:
            if line.startswith('v '):
                x,y,z=line.strip().split()[1:]
                points.append([float(x),float(y),float(z)])
            if line.startswith('f '):
                polys.append(line)

    points=np.array(points)
    filebase= os.path.dirname(filepath)
    filename=os.path.basename(filepath)
    # t1_path=os.path.join(os.path.dirname(filebase),'09_homo',filename[:-18]+'_translation.npy')
    # t2_path=os.path.join(os.path.dirname(filebase),'09_homo',filename[:-18]+'_scale.npy')

    t1 = np.load(translation)
    t2 = np.load(scale)
    points_trans=trans(t1,t2,points)

    transedModel_path=os.path.join(filebase,filename[:-4]+'_trans.obj')
    with open(transedModel_path,'w') as f:
        for point in points_trans:
            f.write('v ')
            f.write(str(point[0])+' '+str(point[1])+' '+str(point[2]))
            f.write('\n')
        for poly in polys:
            f.write(poly)
            f.write('\n')

if __name__=='__main__':
    filepath=sys.argv[1]
    translation=sys.argv[2]
    scale=sys.argv[3]
    transModelObj(filepath,translation,scale)
    print("trans done!")