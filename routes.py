from Silo.Routing import Route

routes = [
    Route().get('/', 'home_controller@index'),
    Route().get('/test', 'home_controller@details'),
    Route().get('/test/', 'home_controller@details'),
    Route().get('/test/{test_var}/edit', 'home_controller@test'),
    Route().resource('examples', 'example_controller'),
]
