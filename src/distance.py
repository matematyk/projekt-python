import math 

def distance_on_geoid(lat1, lon1, lat2, lon2):
 
	# Convert degrees to radians
	lat1 = lat1 * math.pi / 180.0
	lon1 = lon1 * math.pi / 180.0
 
	lat2 = lat2 * math.pi / 180.0
	lon2 = lon2 * math.pi / 180.0
 
	# radius of earth in metres
	r = 6378100
 
	# P
	rho1 = r * math.cos(lat1)
	z1 = r * math.sin(lat1)
	x1 = rho1 * math.cos(lon1)
	y1 = rho1 * math.sin(lon1)
 
	# Q
	rho2 = r * math.cos(lat2)
	z2 = r * math.sin(lat2)
	x2 = rho2 * math.cos(lon2)
	y2 = rho2 * math.sin(lon2)
 
	# Dot product
	dot = (x1 * x2 + y1 * y2 + z1 * z2)
	cos_theta = dot / (r * r)
 
	theta = math.acos(cos_theta)
 
	# Distance in Metres
	return r * theta

