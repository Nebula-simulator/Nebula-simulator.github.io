import numpy as np

# Point exposure

# Parameters:
x = 0         # starting x
y = 0         # starting y
z = 5         # starting z
N = 1000000   # Number of electrons
energy = 1000 # Beam energy, in eV


# This is a numpy datatype that corresponds to pri files
electron_dtype = np.dtype([
    ('x',  '=f'), ('y',  '=f'), ('z',  '=f'), # Position
    ('dx', '=f'), ('dy', '=f'), ('dz', '=f'), # Direction
    ('E',  '=f'),                             # Energy
    ('px', '=i'), ('py', '=i')])              # Pixel index


# Open file
with open('reels.pri', 'wb') as file:
	# Allocate numpy buffer
	buffer = np.empty(N, dtype=electron_dtype)

	# Fill with data
	buffer['x'] = x
	buffer['y'] = y
	buffer['z'] = z
	buffer['dx'] = 0
	buffer['dy'] = 0
	buffer['dz'] = -1
	buffer['E'] = energy
	buffer['px'] = 0
	buffer['py'] = 0

	# Write buffer to file
	buffer.tofile(file)
