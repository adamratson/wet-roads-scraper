from coordinate_converter import grid_ref_to_lat_long


class TestGridRefLatToLong:
    def test_grid_ref_to_lat_long(self):
        lat_lon = grid_ref_to_lat_long(287000, 765000)
        assert lat_lon['lat'] == 56.7630152583901
        assert lat_lon['lon'] == -3.848721342371393