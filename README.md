# Linear Maths 

For this question, we will deal with the geometry of the plane, and we will use tuples to denote points and vectors.

More precisely, if $v$ is a vector or point in the plane, we represent it by the tuple of coordinates $v = (x, y)$. A similar representation can, of course, be used for vectors in arbitrary dimensions.

We know that a straight line $L$ in the plane is uniquely determined by either of the following:

- Two different points $P$ and $Q$ that lie on the line.

- A point $P$ on the line together with a direction vector $v$.

And we will make use of both of these definitions.

$$\textbf{Code}$$

### Geometry in the Plane

The code incorporates both definitions of a straight line and allows for calculations and operations involving points, vectors, and lines in the plane.

By utilizing tuples to represent points and vectors, this code provides a convenient and intuitive way to perform geometric computations in $\mathbb{R}^{2}$. It offers functionalities such as finding lines given two points or a point and a direction vector, performing operations on vectors, and more.

This code serves as a valuable tool for solving geometric problems and conducting plane geometry-related computations in various applications.

### Perpendicular Vector Calculator

This program takes two points, $P$ and $Q$, in the plane as input and computes a vector that is perpendicular to the line passing through $P$ and $Q$.

The functionality of the program is as follows:
1. Accepts two points, $P$ and $Q$, as input.
2. Determines the direction vector of the line passing through $P$ and $Q$.
3. Calculates a vector perpendicular to the line using the properties of perpendicular vectors.
4. Returns the perpendicular vector.

To test the correctness of the program, a function `assert_orthogonal` is provided. This function can be used to verify whether two vectors are orthogonal to each other. By using `assert_orthogonal` on the computed perpendicular vector and the line vector connecting $P$ and $Q$, we can ensure the accuracy of the program's output.

This program is particularly useful in scenarios where determining a perpendicular vector to a given line is required. It provides a convenient and efficient solution for calculating perpendicular vectors, allowing for further analysis and computations in various applications involving plane geometry.

### Intersection of Two Lines

This program includes a function called `intersection_lines` that computes the point of intersection between two lines, $L_1$ and $L_2$, in the plane. Both lines are given in the format $(P, v)$, where $P$ is a point and $v$ is a vector. The input parameter is a tuple of length 2, with each element being a tuple of length 2.

The functionality of the `intersection_lines` function is as follows:
1. Accepts two lines, $L_1$ and $L_2$, as input in the format $(P, v)$.
2. Solves the system of linear equations to find the values of $s$ and $t$, which correspond to the intersection point of the lines.
3. Computes the intersection point as a tuple $(x, y)$, where $x$ and $y$ are floats.
4. Returns the intersection point.

To ensure that the lines are not parallel (meaning they intersect), the program utilizes an `assert` statement. If the lines are parallel, an `AssertionError` is raised. Alternatively, a `ValueError` can be raised to handle this condition.

In order to calculate the intersection point, the program uses the coefficients of the linear equations obtained from the lines' parameter format. By solving the system of equations, it determines the values of $s$ and $t$ in terms of the other coefficients.

It is recommended to work out the equations on paper first, understanding the conditions for parallel lines and finding the expressions for $s$ and $t$, before implementing the code.

This program is particularly useful in scenarios where determining the intersection point of two lines is required, facilitating further analysis and computations in various applications involving plane geometry.

Usage of this program enables users to compute the intersection point of lines and verify if they are parallel or not. It can be applied in fields such as computer graphics, physics, engineering, and mathematics.

$$\textbf{Conclusion}$$

In conclusion, this code implementation offers a concise and efficient solution for performing geometric computations in the plane. By representing points and vectors using tuples, it provides functionalities to calculate perpendicular vectors and find the intersection point between two lines. The code ensures accuracy and reliability by incorporating error handling mechanisms, such as assertions or value errors. With its intuitive functions and broad applications in various fields, including computer graphics and engineering, this code allows users to gain a deeper understanding of geometric relationships and solve practical problems. By integrating this code into your projects, you can explore the power of geometry and unleash its potential.
