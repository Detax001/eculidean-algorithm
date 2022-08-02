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
