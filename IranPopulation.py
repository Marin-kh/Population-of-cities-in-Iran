import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
m = Basemap(llcrnrlon=40., llcrnrlat=20.,urcrnrlon=70.,urcrnrlat=45.,
            rsphere=(6378137.00, 6356752.3142),
            resolution='l', projection='merc',
            lat_0=40., lon_0=-20., lat_ts=20.)

m.drawcoastlines()
m.fillcontinents()

data = pd.read_csv("cities.csv")
x, y = m(data['Longitude'], data['Latitude'])
plt.scatter(x, y, s=data['Population']/12000, alpha=0.6)

m.drawparallels(np.arange(20, 50, 10), labels=[1, 1, 0, 1])
m.drawmeridians(np.arange(40, 80, 10), labels=[1, 1, 0, 1])

ax.set_title('Population of some cities in Iran')

plt.show()