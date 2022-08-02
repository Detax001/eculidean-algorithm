# There are a couple ways to write it, so there are a couple functions of it in here
def euclideanAlgorithm1(a, b):
    """
    Finds the greatest common divisor and the two integers that can find it
    gcd(a, b) = r = uv + vb
    :param a:
    :param b:
    :return:
    """
    up, vp, rp = 1, 0, a
    uc, vc, rc = 0, 1, b
    while rc != 0:
        q = rp // rc
        rp, rc = rc, rp - q * rc
        up, uc = uc, up - q * uc
        vp, vc = vc, vp - q * vc
    g, u, v = rp, up, vp
    return g, u, v


def euclideanAlgorithm2(a, b):
    """
    Finds the greatest common divisor and the two integers that can find it, uses the first euclidean algorithm to solve
    gcd(a, b) = r = uv + vb
    :param a:
    :param b:
    :return:
    """
    if b == 0:
        return a, 1, 0
    g, ur, vr = euclideanAlgorithm1(b, a % b)
    q = a // b
    u, v = vr, ur - q * vr
    return g, u, v