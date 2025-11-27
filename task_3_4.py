def mechanical_energy(m, h, v, g=9.81):
    potential_energy = m * g * h
    kinetic_energy = (m * v ** 2) / 2
    total_energy = potential_energy + kinetic_energy
    return total_energy
