# kalman.py
from filterpy.kalman import KalmanFilter
import numpy as np

class BallKalman:
    def __init__(self):
        self.kf = KalmanFilter(dim_x=4, dim_z=2)
        self.kf.F = np.array([[1,0,1,0],
                              [0,1,0,1],
                              [0,0,1,0],
                              [0,0,0,1]])
        self.kf.H = np.array([[1,0,0,0],
                              [0,1,0,0]])
        self.kf.P *= 1000
        self.kf.R *= 5
        self.kf.Q *= 0.01
        self.initialized = False

    def update(self, z):
        if not self.initialized:
            self.kf.x[:2] = z.reshape(2,1)
            self.initialized = True
        self.kf.predict()
        self.kf.update(z)
        return self.kf.x[:2].flatten()
