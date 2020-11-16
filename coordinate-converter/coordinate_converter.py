# Python implementation of code found here: http://micronavigation.com/latlong-gridref.html
import math

def grid_ref_to_lat_long(eastings, northings):
    a = 6377563.396
    b = 6356256.910

    f0 = 0.9996012717

    lat0 = 49*math.pi/180
    lon0 = -2*math.pi/180

    n0 = -100000
    e0 = 400000

    e2 = 1 - (b * b) / (a * a)
    n = (a - b) / (a + b)

    lat = lat0
    m = 0
    while northings - n0 - m >= 0.00001:
        lat = (northings - n0 - m) / (a * f0) + lat

        Ma = (1 + n + (5 / 4) * math.pow(n, 2) + (5 / 4) * math.pow(n, 3)) * (lat - lat0)
        Mb = (3 * n + 3 * n * n + (21 / 8) * math.pow(n, 3)) * math.sin(lat - lat0) * math.cos(lat 
            + lat0)
        Mc = ((15 / 8) * math.pow(n, 2) + (15 / 8)*math.pow(n, 3)) * math.sin(2 * (lat - 
            lat0)) * math.cos(2 * (lat + lat0))
        Md = (35 / 24) * math.pow(n, 3) * math.sin(3 * (lat - lat0)) * math.cos(3*(lat+lat0))

        m = b * f0 * (Ma - Mb + Mc - Md)

    cosLat = math.cos(lat)
    sinLat = math.sin(lat)
    nu = a * f0 / math.sqrt(1 - e2 * sinLat * sinLat);              
    rho = a * f0 * (1 - e2) / math.pow(1 - e2 * sinLat * sinLat, 1.5)
    eta2 = nu / rho - 1

    tanLat = math.tan(lat)

    secLat = 1 / cosLat
    nu3 = nu * nu * nu
    nu5 = nu3 * nu * nu
    nu7 = nu5 * nu * nu

    VII = tanLat / (2 * rho * nu)
    VIII = tanLat / (24 * rho * nu3) * (5 + 3 * math.pow(tanLat, 2) + eta2 - 9 * math.pow(tanLat, 2) * eta2)
    IX = tanLat / (720 * rho * nu5) * (61 + 90 * math.pow(tanLat, 2) + 45 * math.pow(tanLat, 4))
    X = secLat / nu
    XI = secLat / (6 * nu3) * (nu / rho + 2 * math.pow(tanLat, 2))
    XII = secLat / (120 * nu5) * (5 + 28 * math.pow(tanLat, 2) + 24 * math.pow(tanLat, 4))
    XIIA = secLat / (5040  * nu7) * (61 + 662 * math.pow(tanLat, 2) + 1320 * math.pow(tanLat, 4) + 720 * math.pow(tanLat, 6))

    dE = (eastings - e0)
    lat = lat - VII * math.pow(dE, 2) + VIII * math.pow(dE, 4) - IX * math.pow(dE, 6)
    lon = lon0 + X * dE - XI * math.pow(dE, 3) + XII * math.pow(dE, 5) - XIIA * math.pow(dE, 7)

    return {"lat": math.degrees(lat), "lon": math.degrees(lon)}
