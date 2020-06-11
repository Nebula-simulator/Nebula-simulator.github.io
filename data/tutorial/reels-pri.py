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
	array = np.empty(N, dtype=electron_dtype)

	# Fill with data
	array['x'] = x
	array['y'] = y
	array['z'] = z
	array['dx'] = 0
	array['dy'] = 0
	array['dz'] = -1
	array['E'] = energy
	array['px'] = 0
	array['py'] = 0

	# Write buffer to file
	array.tofile(file)
