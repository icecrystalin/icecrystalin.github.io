import numpy as np
import math as math
def scale(s,a):
    mat = np.matrix([[s,0,0],[0,s,0],[0,0,s]])
    return np.matmul(a,mat)

def rotation_matrix(axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    axis = np.asarray(axis)
    axis = axis/math.sqrt(np.dot(axis, axis))
    a = math.cos(theta/2.0)
    b, c, d = -axis*math.sin(theta/2.0)
    aa, bb, cc, dd = a*a, b*b, c*c, d*d
    bc, ad, ac, ab, bd, cd = b*c, a*d, a*c, a*b, b*d, c*d
    return np.array([[aa+bb-cc-dd, 2*(bc+ad), 2*(bd-ac)],
                     [2*(bc-ad), aa+cc-bb-dd, 2*(cd+ab)],
                     [2*(bd+ac), 2*(cd-ab), aa+dd-bb-cc]])
def rotation(axis, theta, b):
    m = rotation_matrix(axis, theta)
    #b = np.delete(a,3,axis=1)
    b = b.transpose()
    b =  np.dot(m,b)
    return b.transpose()

def translate(x,y,z, a):
    z1 = np.full((len(a),1),1)
    b = np.append(a,z1, axis =1)
    b = b.transpose()
    mat = np.matrix([[1,0,0, x ],[0,1,0,y],[0,0,1,z],[0,0,0,1]])
    return np.matmul(mat,b).transpose()


a = np.matrix([[-0.5447,    1.3323,   -0.0013],[ 0.6985,   -0.6359,    0.0058],[-0.4701,    0.1063,    0.0070],[ 2.0143,   -0.0386,   -0.0057],[-1.6980,   -0.7641,   -0.0059],[ 0.6423,   -1.6500,   -0.0141],[ 2.6279,   -0.5471,    0.7418],[ 1.9657,    1.0301,    0.2163],[ 2.4489,   -0.1908,   -0.9966],[-2.5800,   -0.1596,    0.2234],[-1.8162,   -1.2127,   -0.9959],[-1.6122,   -1.5549,    0.7449]])
a = scale(4,a)
a = rotation([1,0,0],-math.pi/4, a)
a = rotation([0,0,1],-math.pi/4, a)
a = rotation([0,1,0],math.pi/6, a)
print(translate(16,16,16,a))