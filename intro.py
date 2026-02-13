from manim import *
import numpy as np

class SphereScene(ThreeDScene):
    def construct(self):
        # 1. Setup Axes
        axes = ThreeDAxes()
        
        # 2. Define the Sphere using the 2-variable lambda
        sphere = Surface(
            lambda u, v: np.array([
                2 * np.sin(u) * np.cos(v), # x
                2 * np.sin(u) * np.sin(v), # y
                2 * np.cos(u)              # z
            ]),
            u_range=[0, PI],      # phi (vertical)
            v_range=[0, 2*PI],    # theta (horizontal)
            checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(20, 40)   # Number of grid lines
        )

        # 3. Position Camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        # 4. Animate
        self.add(axes)
        self.play(Create(sphere), run_time=3)
        self.begin_ambient_camera_rotation(rate=0.2) # Rotate to see 3D
        self.wait(4)