from flask import Flask, render_template
import folium

# Coordinates for 10 tourist attractions in Pittsburgh
locations = {
    "Pittsburgh Zoo & PPG Aquarium": (40.4876, -79.9183),
    "Carnegie Museum of Natural History": (40.4433, -79.9506),
    "Phipps Conservatory and Botanical Gardens": (40.4392, -79.9474),
    "Andy Warhol Museum": (40.4485, -80.0025),
    "Carnegie Science Center": (40.4457, -80.0185),
    "Duquesne Incline": (40.4398, -80.0182),
    "Point State Park": (40.4416, -80.0139),
    "Heinz Field": (40.4468, -80.0158),
    "Frick Art & Historical Center": (40.4484, -79.9039),
    "National Aviary": (40.4531, -80.0087)
}

app = Flask(__name__)

@app.route('/')
def mapview():
    # Create a map centered around Pittsburgh
    pittsburgh_map = folium.Map(location=[40.4406, -79.9959], zoom_start=14)

    # Add markers for each location
    for place, (lat, lon) in locations.items():
        folium.Marker([lat, lon], popup=place).add_to(pittsburgh_map)

    # Render map to HTML
    map_html = pittsburgh_map._repr_html_()

    return render_template('map.html', map_html=map_html)

if __name__ == '__main__':
    app.run(debug=True)


