import numpy as np

V = np.array([5, 8.5, 12, 15.5, 18.5])
V_unc = np.array([0.5, 0.5, 0.5, 0.5, 0.5])

m = np.array([0.0695, 0.0043, -0.0074, 0.0105, 0.0014])
m_unc = np.array([0.1221, 0.0088, 0.0084, 0.011, 0.0061])

V_max = np.add(V, V_unc)
m_max = np.add(m, m_unc)

V_min = np.subtract(V, V_unc)
m_min = np.subtract(m, m_unc)

print(np.poly1d(np.polyfit(V, m, 3)))
print(np.poly1d(np.polyfit(V_max, m_max, 3)))
print(np.poly1d(np.polyfit(V_min, m_min, 3)))