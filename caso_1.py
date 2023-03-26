import gempy as gp
import numpy as np
import osgeo

# Crear una cuadrícula
extent = [-50, 50, -50, 50, -50, 0] # x_min, x_max, y_min, y_max, z_min, z_max
resolution = [50, 50, 50] # nx, ny, nz
grid = gp.Grid(extent=extent, resolution=resolution)

# Definir las unidades geológicas y sus propiedades
geo_model = gp.create_model('Ejemplo_con_topografia')
layer1 = geo_model.add_surface('Capa_superior')
layer2 = geo_model.add_surface('Capa_inferior')

gp.set_series(geo_model, {'Serie_1': layer1, 'Serie_2': layer2}, order_series=['Serie_1', 'Serie_2'])

geo_model.set_is_fault([0], [1])
gp.map_stack_to_surfaces(geo_model, {"Capa_superior": layer1, "Capa_inferior": layer2})

geo_model.add_surface_points(-25, -25, -25, layer=layer1)
geo_model.add_surface_points(25, 25, -45, layer=layer2)

gp.set_interpolator(geo_model)

# Definir la topografía
x_topo, y_topo = np.meshgrid(np.linspace(-50, 50, 100), np.linspace(-50, 50, 100))
z_topo = -5 * (np.sin(np.sqrt(x_topo ** 2 + y_topo ** 2)) + 1)

geo_model.set_topography(points=np.hstack((x_topo.reshape(-1, 1), y_topo.reshape(-1, 1), z_topo.reshape(-1, 1))))

# Generar el modelo
gp.compute_model(geo_model)

# Visualizar el modelo
gp.plot_3d(geo_model, plotter_type='background', show_data=False)
gp.plot_3d(geo_model, plotter_type='basic', show_data=False)
gp.plot_2d(geo_model, direction='z', show_data=False)
