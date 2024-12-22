# PyGame Pyramid

Before I explain the code, I'll be explaining the math behind it.
So, first things first...

# How are you projecting a 3D shape onto a 2D screen?

It's actually quite simple.
First, we start by initiating each point of the 3D plane.
We do this by creating a list, which contains a _numpy_ array in the form of a vector. (i.e. [[1], [0], [0]] represents Vector3(1, 0, 0))
Next, we must smush the z axis, so that it becomes a flat 2D set of points.
We do this using a projection matrix.
The projection matrix is as follows:

$$\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 0
\end{bmatrix}
\cdot\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}
=\begin{bmatrix}
x\prime \\
y\prime \\
\end{bmatrix}$$

This equation is represented in the project function in the code too.

# How'd you make a pyramid?

The pyramid is defined in a list of points, these points being numpy arrays.
Each array holds the same form as from above.
For a visualization, refer to [this](https://technology.cpm.org/general/3dgraph/?graph3ddata=____bHwWawWawWaIxmuwWawWaJxmuxmuwWaKwWaxmuwWaKw7kw7kxmu).

# But how do you rotate it?
We use rotation matrices.
The rotation matrices are as follows:

$$R_{x}(\theta) = \begin{bmatrix}
1 & 0 & 0 \\
0 & \cos\theta & -\sin\theta \\
0 & \sin\theta & \cos\theta
\end{bmatrix}$$

$$R_{y}(\theta) = \begin{bmatrix}
\cos\theta & 0 & \sin\theta \\
0 & 1 & 0 \\
-\sin\theta & 0 & \cos\theta
\end{bmatrix}$$

$$R_{z}(\theta) = \begin{bmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{bmatrix}$$

These are the rotation matrices for the x, y, and z axes, respectively.
Each point must run through all three of these calculations sequentially.
For example, given point A, you must calculate $A\prime = (A\cdot R_{x}\cdot R_{y}\cdot R_{z})$.

That's pretty much all you need to know though.
