

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Gggg
from django.db import connection
import json
@login_required(login_url='signin')
def gis_x(request):

    with connection.cursor() as cursor:
        cursor.execute("SELECT id_0, f_id, farm_id,tlu,area, ST_AsGeoJSON(geom) AS geometry FROM gggg")
        result = cursor.fetchall()

        # Создание GeoJSON-объекта
        geojson = {
            "type": "FeatureCollection",
            "features": []
        }

        for row in result:
            id_0 = row[0]
            f_id = row[1]
            farm_id = row[2]
            tlu = row[3]
            area = row[4]
            geometry = json.loads(row[5])
            feature = {
                "type": "Feature",
                "geometry": geometry,
                "properties": {
                    "id_0": id_0,
                    "f_id": f_id,
                    "farm_id": farm_id,
                    "tlu": tlu,
                    "area": area
                }
            }
            geojson["features"].append(feature)

            cursor.execute("UPDATE gggg SET geojson = %s WHERE id_0 = %s", (json.dumps(feature), id_0))





        # Запись в файл GeoJSON
        with open("result.geojson", "w") as outfile:
            json.dump(geojson, outfile)
        result_data = Gggg.objects.all()
    return render(request,'gis_x/gis_x.html', {'result_data':result_data})


