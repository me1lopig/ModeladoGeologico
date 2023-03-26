import gempy as gp
import numpy as np

# Crear una cuadrícula
extent = [0, 10, 0, 10, 0, 10] # x_min, x_max, y_min, y_max, z_min, z_max
resolution = [50, 50, 50] # nx, ny, nz
grid = gp.Grid(extent=extent, resolution=resolution)

# Definir las unidades geológicas y sus propiedades
geo_model = gp.create_model('Ejemplo_simple')
layer1 = geo_model.add_surface('Capa_arenisca')
layer2 = geo_model.add_surface('Capa_lutita')

geo_model.set_is_fault([0], [1])
gp.map_stack_to_surfaces(geo_model, {"Capa_arenisca": layer1, "Capa_lutita": layer2})

geo_model.add_surface_points(5, 5, 0, layer=layer1)
geo_model.add_surface_points(5, 5, 2, layer=layer2)

# Generar el modelo
gp.set_interpolator(geo_model)
gp.compute_model(geo_model)

# Visualizar el modelo
gp.plot_3d(geo_model, show_data=True)
