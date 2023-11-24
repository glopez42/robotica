
from coppelia import Coppelia
from robot import ACMR


def main(args=None):
    coppelia = Coppelia()
    robot = ACMR(coppelia.sim, 'ACMR')
    coppelia.start_simulation()
    while (t := coppelia.sim.getSimulationTime()) < 20:
        print(f'Simulation time: {t:.3f} [s]')
        angles = robot.calculate_angles(t)
        for n in range(robot.N_parts-1):
            robot.set_joint(n,angles[n])

    coppelia.stop_simulation()

if __name__ == '__main__':
    main()
