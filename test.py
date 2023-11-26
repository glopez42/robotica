
from coppelia import Coppelia
from robot import ACMR


def main(args=None):
    coppelia = Coppelia()
    robot = ACMR(coppelia.sim, 'ACMR')
    coppelia.start_simulation()

    for _ in range(3):
        robot.set_movement_params([-1,2,0,4])
        start = coppelia.sim.getSimulationTime()
        t = 0
        while (t) < 20:
            print(f'Simulation time: {t} [s]')
            angles = robot.calculate_angles(t)
            for n in range(robot.N_parts-1):
                robot.set_joint(n,angles[n])

            t = coppelia.sim.getSimulationTime() - start

        robot.reset_position()
        
    coppelia.stop_simulation()

if __name__ == '__main__':
    main()
