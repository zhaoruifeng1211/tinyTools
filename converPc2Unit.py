import trimesh
import numpy as np
import os
import random
import sys
import trimesh
import trimesh.proximity
import trimesh.path
import trimesh.repair
import trimesh.sample
sys.path.append(r'/home/zhaoruifeng1211/points2poly/points2poly/points2surf')


#sys.path.append(r'/home/zhaoruifeng1211/points2poly/points2poly')
from make_pc_dataset import _to_unit_cube
sys.path.append(r'/home/zhaoruifeng1211/points2poly/points2poly/points2surf/source/base')
from point_cloud import write_ply

#from points2poly.points2surf.make_pc_dataset import _to_unit_cube
#from points2poly.points2surf.source.base.point_cloud import write_xyz

def _convert_point_cloud(in_pc, out_pc_xyz,target_num_points=150000): #inout .ply

    mesh = None
    try:
        mesh = trimesh.load(in_pc)
    except AttributeError as e:
        print(e)
    except IndexError as e:
        print(e)
    except ValueError as e:
        print(e)
    except NameError as e:
        print(e)

    if mesh is not None:
        mesh = _to_unit_cube(mesh) #FUC@fred: convert points coordinates to normalize value
        points = mesh.vertices
        points = points[:, :3]  # remove normals
        points = points.astype(np.float32)
        write_ply(out_pc_xyz, points)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the file name as a command line argument.")
        sys.exit(1)
    
    file_name = sys.argv[1]
    file_path = os.path.splitext(file_name)[0]+'.ply'
    _convert_point_cloud(file_name,file_path)
    # Rest of your code here
    # Use the file_name variable as needed