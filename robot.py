import math
import time

class ACMR():

    N_parts = 9
    joints = []
    Length = 0
    a = 0
    b = 0
    c = 0
    w = 0
    startPosition = []
    startOrientation = []
    robotHandle = 0

    def __init__(self, sim, robot_id):
        self.sim = sim

        # joints handle
        path = f'/{robot_id}/vJoint'
        for part in range(self.N_parts-1):
            opt = {"index" : part}
            self.joints.insert(0,self.sim.getObject(path,opt))

        # robot positions
        self.robotHandle = self.sim.getObject(f'/{robot_id}')
        self.startPosition = self.sim.getObjectPosition(self.robotHandle)
        self.startOrientation = self.sim.getObjectOrientation(self.robotHandle)
        pos1 = self.sim.getObjectPosition(self.joints[0],self.joints[0])
        pos2 = self.sim.getObjectPosition(self.joints[1],self.joints[0])
        
        self.Length = (pos2[0]-pos1[0])*self.N_parts
        #print(f"ACMR - n={self.N_parts} - L={self.Length}")
        #print(f"Init position: x={self.startPosition[0]}, y={self.startPosition[1]}")

    def get_actual_position(self):
        return self.sim.getObjectPosition(self.robotHandle)
    
    def set_movement_params(self, params):
        self.a = params[0]
        self.b = params[1]
        self.c = params[2]
        self.w = params[3]
    
    def calculate_angles(self, time):
        angles = []
        a = self.a
        b = self.b
        c = self.c
        w = self.w

        for i in range(self.N_parts-1):
            beta = (self.Length * b) / (self.N_parts)
            gamma = - (self.Length*c/self.N_parts)
            alpha = 2*a*math.sin(beta/2)
            angle = alpha * math.sin(w*time + (i - 1)*beta) + gamma
            angles.append(angle)
        
        return angles
    
    def set_joint_angles(self, angles):
        for n in range(self.N_parts-1):
            self.set_joint(n,angles[n])
            self.sim.setJointTargetPosition(self.joints[n], angles[n])
    
    def set_joint(self, joint, value):
        self.sim.setJointTargetPosition(self.joints[joint], value)
    
    def reset_position(self):
        reset_angles = [0 for _ in range(self.N_parts-1)]
        self.set_joint_angles(reset_angles)
        time.sleep(1)
        self.sim.setObjectPosition(self.robotHandle, self.startPosition)
        self.sim.setObjectOrientation(self.robotHandle, self.startOrientation)
        self.sim.resetDynamicObject(self.robotHandle)
        time.sleep(0.1)


