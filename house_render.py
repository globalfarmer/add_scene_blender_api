import bpy, math

CAMERA_LOCATION = (0, 0, 1.5)
CAMERA_ROTATION = (math.pi/2, 0, 0)

camera = bpy.data.objects["Camera"]
camera.location = CAMERA_LOCATION
camera.rotation_euler = CAMERA_ROTATION
camera.data.type = "PANO"
camera.data.cycles.panorama_type = 'EQUIRECTANGULAR'

bpy.context.scene.cycles.film_transparent = True