
# Home page loads correctly when the user visits "/"
def test_route_index(app,client):
    print("\r") # Create space and show what test is running
    print(" '/' GET Test ")
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200
        assert b"Verticle Tank Maintenance" in res.data
        assert b"Welcome to VTM!" in res.data

# About page loads correctly when the user visits "/about"
def test_route_about(app,client):
    print("\r") # Create space and show what test is running
    print(" '/about' Get Test ")
    with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200
        assert b"Verticle Tank Maintenance" in res.data
        assert b"About Verticle Tank Maintenance" in res.data

# Estimate page loads correctly when a user visits "/estimate" (GET)
def test_route_estimate(app,client):
    print("\r") # Create space and show what test is running
    print(" '/estimate' GET Test")
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 200
        assert b"Verticle Tank Maintenance" in res.data
        assert "Create an Estimate" in res.data

# Test estimator (POST)
def test_price_estimator(app,client):
    print('\r') # Create space and show what test is running
    print(" '/estimate' POST Test")
    with app.test_client as test_client:
        estimate_Calculation = {"radius":"180", "height":"360", "estimate":"x"}
        res = test_client.post('/estimate', data = estimate_Calculation)
        assert res.status_code == 200
        assert b"$141,300.00" in res.data

