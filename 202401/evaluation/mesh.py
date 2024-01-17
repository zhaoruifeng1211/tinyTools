import numpy as np
import open3d as o3d

input_path="/home/zhaoruifeng/improve3d/202401/evaluation/"
output_path="/home/zhaoruifeng/improve3d/202401/evaluation/"
dataname="5080_54435_5_final_cut_new_1_ground.xyzn"
point_cloud= np.loadtxt(input_path+dataname,skiprows=1)

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(point_cloud[:,:3])
# pcd.colors = o3d.utility.Vector3dVector(point_cloud[:,3:6]/255)
pcd.normals = o3d.utility.Vector3dVector(point_cloud[:,3:9])

o3d.visualization.draw_geometries([pcd])

distances = pcd.compute_nearest_neighbor_distance()
avg_dist = np.mean(distances)
radius = 5 * avg_dist
bpa_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(pcd,o3d.utility.DoubleVector([radius, radius * 2]))
dec_mesh = bpa_mesh.simplify_quadric_decimation(100000)
dec_mesh.remove_degenerate_triangles()
dec_mesh.remove_duplicated_triangles()
dec_mesh.remove_duplicated_vertices()
dec_mesh.remove_non_manifold_edges()

poisson_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=8, width=0, scale=1.1, linear_fit=False)[0]
bbox = pcd.get_axis_aligned_bounding_box() 
p_mesh_crop = poisson_mesh.crop(bbox)
# o3d.io.write_triangle_mesh(output_path+"bpa_mesh.ply", dec_mesh)
o3d.io.write_triangle_mesh(output_path+"p_mesh_c.ply", p_mesh_crop)
o3d.io.write_triangle_mesh(output_path+"bpa_mesh.ply", dec_mesh)
