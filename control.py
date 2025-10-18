def controller(ref, pos, Kp, Kd, e_prev, dt):
    e = ref-pos
    d = (e - e_prev)/dt # Euler's discrete time derivative
    u = Kp*e + Kd*d
    return u, e