
from coppelia import Coppelia
from robot import ACMR
import time


def main(args=None):
    coppelia = Coppelia()
    robot = ACMR(coppelia.sim, 'ACMR')
    coppelia.start_simulation()
    value = 1.0
    step = 0
    while (t := coppelia.sim.getSimulationTime()) < 10:
        print(f'Simulation time: {t:.3f} [s]')
        value = value * -1
        angles = robot.calculate_angles(step)

        for n in range(robot.N_parts-1):
            robot.set_joint(n,angles[n])

        '''
        for n in range(robot.N_parts-1):
            robot.set_joint(n,value)
            value = value * -1
            time.sleep(0.1)
        '''

        step = step + 0.1
        
    coppelia.stop_simulation()

if __name__ == '__main__':
    main()
