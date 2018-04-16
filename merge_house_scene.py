import bpy, os

BASE_PATH = "C:\\Users\\H3D_anhdv\\Desktop\\H3D-1326"
HOUSE = "house0001.png"
SCENE = "scene0001.png"
print("Load " + HOUSE);
bpy.data.images.load(os.path.join(BASE_PATH, HOUSE), check_existing=True)
print("Load " + SCENE)
bpy.data.images.load(os.path.join(BASE_PATH, SCENE), check_existing=True)
bpy.context.scene.node_tree.nodes[2].image = bpy.data.images[SCENE]
bpy.context.scene.node_tree.nodes[3].image = bpy.data.images[HOUSE]