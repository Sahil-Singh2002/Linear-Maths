# Linear Maths 

These codes focuses on dealing with geometry of the plane and use tuples to denote points and vectors. More preciesly, if **v** is a vector or point in the plane we represent it by the tuple of coordinates **v** = (*x,y*). A similar representation can of course be used for vectors in arbitrary dimensions. A straight line *L* in the plane is uniquely determined by either of the following:

  - Two different points *P* and *Q* that lie on the line.
  - A point *P* on the line together with a direction vector **v**

and we make use of both of these definitions.

* The function scalar_product(v1,v2) helps compute the scalar product of two vectors of arbitrary but equal lenght. The function uses assert to ensure that the input values are tuples, that they are tuples of equal lenght and they contain only integers or floats. 
* The function vector_perpendicular(P,Q) in takes two points *P* and *Q* in the plane and returns a vector that is perpendicular to the line through *P* and *Q*.

In conclusion the coursework requires us to use for-loops and assert to compute scalar product of two vectors and findind a vector perpendicular to two points.
