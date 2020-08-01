import math, random
from vector import add, norm, normed, dotprod
from activation_function import heaviside


def get_annulus_segment_points(x=0.0, y=0.0, r0=0.0, r1=1.0, a0=0.0, a1=math.pi, n=250):
    P = []
    for _ in range(n):
        a, s = random.uniform(a0, a1), random.uniform(r0, r1)
        P.append((x + s * math.cos(a), y + s * math.sin(a)))
    return P


def get_annulus_test_data(x=0.4, y=-0.4, r0=1.1, r1=1.5, n=125):
    A0 = get_annulus_segment_points(r0=r0, r1=r1, n=n)
    A1 = get_annulus_segment_points(x=x, y=y, a0=math.pi, a1=2 * math.pi, r0=r0, r1=r1, n=n)
    T = [(u, 1) for u in A0] + [(u, 0) for u in A1]
    random.shuffle(T)
    return A0, A1, T


def verify_annulus_classification(A0, A1, w, b, classify=heaviside):
    assert all(classify(dotprod(w, x) + b) == 1 for x in A0) and all(
        classify(dotprod(w, x) + b) == 0 for x in A1
    )
