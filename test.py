
from coppelia import Coppelia
from robot import ACMR


def main(args=None):
    coppelia = Coppelia()
    robot = ACMR(coppelia.sim, 'ACMR')
    coppelia.start_simulation()

    params = [
            1.0863487702422514,
            -6.181889363444142,
            -0.04364371968101932,
            -12.406393661654905
    ] 

    for _ in range(1):
        robot.set_movement_params(params)
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
