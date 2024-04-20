from queue import Queue
import threading
import time

import airsim


class AirsimWrapper:
	def __init__(self, rpc_queue:Queue):
		# connect to the AirSim simulator
		self.client = airsim.MultirotorClient()
		self.client.confirmConnection()
		self.client.enableApiControl(True)
		self.home = {}
		self.lock = threading.Lock()
		self.rpc_queue = rpc_queue

		def set_global_camera():
			global_camera = "GlobalCamera"
			self.client.enableApiControl(True, global_camera)
			self.client.takeoffAsync(vehicle_name=global_camera).join()
			self.client.moveToPositionAsync(0, 0, -20, 10, vehicle_name=global_camera).join()
			self.client.hoverAsync(global_camera).join()

		set_global_camera()
		message = (
			"1. Push / to switch to chase with spring arm mode.\n"
			"2. Wait for the drone to fly to an altitude of 300 meters.\n"
			"3. Push M to switch to manual camera control.\n"
			"4. Push S to move the view downwards, regard the drone as a global camera.\n"
			"5. Press any key to continue after the global camera is ready."
		)
		airsim.wait_key(message=message)

	def set_home(self, agents_list: list):
		group = len(self.home)
		for i in range(len(agents_list)):
			pose = airsim.Pose(airsim.Vector3r(group, i * 2, 0), airsim.to_quaternion(0, 0, 0))
			self.client.simAddVehicle(agents_list[i], "simpleflight", pose)
			self.home[agents_list[i]] = pose
			self.client.enableApiControl(True, agents_list[i])
		# self.client.armDisarm(True, agents_list[i])
		time.sleep(2)

	def takeOff_API(self, *rpc_args, vehicle_name):
		def rpc_call():
			res = self.client.takeoffAsync(vehicle_name=vehicle_name)
			self.lock.acquire()
			res.join()
			self.lock.release()
		self.rpc_queue.put(rpc_call)

	def flyToHeight_API(self, *rpc_args, vehicle_name):
		h = rpc_args[0]
		def rpc_call():
			pose = self.client.simGetVehiclePose(vehicle_name=vehicle_name)
			res = self.client.moveToPositionAsync(pose.position.x_val, pose.position.y_val, -h, 10, vehicle_name=vehicle_name)
			self.lock.acquire()
			res.join()
			self.lock.release()
		self.rpc_queue.put(rpc_call)

