# Type of planner
from math import exp

POINT_PLANNER=0; TRAJECTORY_PLANNER=1



class planner:
    def __init__(self, type_):

        self.type=type_

    
    def plan(self, goalPoint=[-1.0, -1.0]):
        
        if self.type==POINT_PLANNER:
            return self.point_planner(goalPoint)
        
        elif self.type==TRAJECTORY_PLANNER:
            return self.trajectory_planner()


    def point_planner(self, goalPoint):
        x = goalPoint[0]
        y = goalPoint[1]
        return x, y

    # TODO Part 6: Implement the trajectories here
    def trajectory_planner(self):
        # Parabola: y = x^2 for x in [0.0, 1.5]
        parabola=[]
        x=0.0
        step=0.05
        while x <= 1.5 + 1e-9:
            parabola.append([x, x * x])
            x+=step

        # Sigmoid: 2/(1 + e^{-2x}) - 1 for x in [0.0, 2.5]
        sigmoid=[]
        x=0.0
        while x <= 2.5 + 1e-9:
            y=(2 / (1 + exp(-2 * x))) - 1
            sigmoid.append([x, y])
            x+=step

        # Offset sigmoid to start after parabola to keep a continuous path
        if parabola:
            x_offset=parabola[-1][0] + step
            y_offset=parabola[-1][1]
            sigmoid=[[pt[0] + x_offset, pt[1] + y_offset] for pt in sigmoid]

        # the return should be a list of trajectory points: [ [x1,y1], ..., [xn,yn]]
        return parabola + sigmoid

