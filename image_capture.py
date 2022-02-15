
import pyzed.sl as sl
import cv2
init_params = sl.InitParameters()
# runtime = sl.RuntimeParameters()
init_params.camera_resolution = sl.RESOLUTION.HD2K
# init_params.camera_fps = 30
zed = sl.Camera()
zed.open(init_params)
if not zed.is_opened():
  print("Opening ZED Camera...")
zed.grab(init_params)
image = sl.Mat()

zed.retrieve_image(image) # Retrieve the left image
cv2.imwrite("test.png", image.get_data())