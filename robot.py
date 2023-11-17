import math


class ACMR():

    N_parts = 9
    joints = []
    Length = 0
    a = 3.8
    b = 6
    c = 0
    w = 8

    def __init__(self, sim, robot_id):
        self.sim = sim

        # joints handle
        path = f'/{robot_id}/vJoint'
        for part in range(self.N_parts-1):
            opt = {"index" : part}
            self.joints.insert(0,self.sim.getObject(path,opt))

        # robot dimensions
        robotHandle = self.sim.getObject(f'/{robot_id}')
        _,_,dimensions = self.sim.getShapeGeomInfo(robotHandle)
        print(dimensions)

        pos1 = self.sim.getObjectPosition(self.joints[0],self.joints[0])
        pos2 = self.sim.getObjectPosition(self.joints[1],self.joints[0])
        
        self.Length = (pos2[0]-pos1[0])*self.N_parts
        print(f"ACMR - n = {self.N_parts} - L = {self.Length}")


    def set_movement(self, a, b, c, w):
        self.a = a
        self.b = b
        self.c = c
        self.w = w

    def calculate_angles(self, time):
        angles = []
        a = self.a #* math.sin(time)
        b = self.b #* math.sin(time)
        c = self.c #* math.sin(time)
        w = self.w

        for i in range(self.N_parts-1):
            """
            sin1 = math.sin((i*b*self.Length/self.N_parts) + ((self.Length * b) / 2*(self.N_parts)))
            sin2 = math.sin((self.Length * b) / 2*(self.N_parts))
            res = (2*a*sin1*sin2) - (self.Length*c/self.N_parts)
            angles.append(res)
            """

            beta = (self.Length * b) / (self.N_parts)
            gamma = - (self.Length*c/self.N_parts)
            alpha = 2*a*math.sin(beta/2)
            angle = alpha * math.sin(w*time + (i - 1)*beta) + gamma
            angles.append(angle)
        
        return angles
    
    def set_joint(self, joint, value):
        self.sim.setJointTargetPosition(self.joints[joint], value)


