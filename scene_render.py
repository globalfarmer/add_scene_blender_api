import bpy, os, math

CAMERA_LOCATION = (0, 0, 1.5)
CAMERA_ROTATION = (math.pi/2, 0, 0)
BASE_PATH = "D:\\hdr"
FILENAME = "autumn_hockey_16k.hdr"

camera = bpy.data.objects["Camera"]
camera.location = CAMERA_LOCATION
camera.rotation_euler = CAMERA_ROTATION
# camera.data.type = "PANO"
# camera.data.cycles.panorama_type = 'EQUIRECTANGULAR'
print(os.path.join(BASE_PATH, FILENAME))
bpy.data.images.load(os.path.join(BASE_PATH, FILENAME), check_existing=True)
bpy.context.scene.world.node_tree.nodes["Environment Texture"].image = bpy.data.images[0]
