def controller(ref, pos, Kp, Kd, time_step, e_prev=0, dt=1):

    # Compute error using the current reference at this time index
    e = ref[time_step] - pos
    # Discrete derivative
    d = (e - e_prev) / dt
    u = Kp * e + Kd * d
    return u, e