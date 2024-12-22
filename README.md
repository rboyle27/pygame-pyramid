# PyGame Pyramid

Before I explain the code, I'll be explaining the math behind it.
So, first things first...

# How are you projecting a 3D shape onto a 2D screen?

It's actually quite simple.
The process in which it works is as follows:
1. Initializing 3D points
   - Start by defining each point of the 3D shape using arrays.
   - For example, [[1], [0], [0]] represents Vector3(1, 0, 0).
2. Flatten the Z-axis
   - To display a 3D shape onto a 2D screen, you must flatten it by removing the z-axis.
   - This is done using a projection matrix.
3. Projection matrix
   - The projection matrix is as follows: $`\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{bmatrix} \cdot\begin{bmatrix} x \\ y \\ z \end{bmatrix} =\begin{bmatrix} x\prime \\ y\prime \\ \end{bmatrix}`$
   - When you multiply the projection matrix by a 3D point $`v=\begin{bmatrix} x \\ y \\ z \end{bmatrix}`$, the result is $`\begin{bmatrix} x\prime \\ y\prime \\ 0 \end{bmatrix}`$.
   - This means we're keeping the x and y coordinates and setting z to zero, which effectively flattens the point onto a 2D plane.

# How'd you make a pyramid?

Creating a pyramid involves defining its shape with points in 3D space.
1. Define pyramid points
   - The pyramid is made up of several points, each repesented as a numpy array.
   - Each point makes up the base to the top of the pyramid, that is applicable to any shape in 3D too.

For a visualization, refer to [this](https://technology.cpm.org/general/3dgraph/?graph3ddata=____bHwWawWawWaIxmuwWawWaJxmuxmuwWaKwWaxmuwWaKw7kw7kxmu).

# But how do you rotate it?
We use rotation matrices.

They are as follows...

### X-axis rotation
   
$`R_{x}(\theta) = \begin{bmatrix} 1 & 0 & 0 \\
0 & \cos\theta & -\sin\theta \\
0 & \sin\theta & \cos\theta \end{bmatrix}`$

### Y-axis rotation
     
$`R_{y}(\theta) = \begin{bmatrix} \cos\theta & 0 & \sin\theta \\
 0 & 1 & 0 \\
 -\sin\theta & 0 & \cos\theta \end{bmatrix}`$

### Z-axis rotation

$`R_{z}(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\
 \sin\theta & \cos\theta & 0 \\
 0 & 0 & 1 \end{bmatrix}`$

2. Applying rotation matrices
   - To rotate a point in a 3D space, you must apply these matrices to it.
Order matters here, the sequence in which you apply it affects its position.
Typically, you rotate on the x-axis, then y-axis, and finally z-axis.

For example, given a point $A$, the rotated point $A\prime$ is calculated as:
$`A\prime = A\cdot R_{x}(\theta_{x})\cdot R_{y}(\theta_{y})\cdot R_{z}(\theta_{z})`$

This means you first rotate $A$ around the x-axis by $`\theta_{x}`$, then around the y-axis by $`\theta_{y}`$, and finally around the z-axis by $`\theta{z}`$.
