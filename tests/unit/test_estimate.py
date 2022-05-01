import app

# Unit test the estimate calculation

# From assignment sheet:
# Programmatically input 180 inch radius and 360 inch height into "/estimate"
# and test that the value of $141,300.00 is returned. (POST)


def test_TopArea_calculation():
    assert app.calculate_AreaTop(180) == 101736

def test_SideArea_calculation():
    assert app.calculate_AreaSide(180,360) == 406944