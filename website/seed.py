from . import db
from .models import FishSpecies

def seed_fish_species():

    fish_data = [
        {
                'name': 'Atlantic Salmon',
                'scientific_name': 'Salmo salar',
                'habitat': 'Found in both marine and freshwater environments. Adults spawn in freshwater rivers and migrate to the sea.',
                'image_url': 'https://example.com/images/atlantic-salmon.jpg'
        },
        {
            'name': 'Rainbow Trout',
            'scientific_name': 'Oncorhynchus mykiss',
            'habitat': 'Cold, clear freshwater streams and lakes with gravel bottoms and moderate to fast currents.',
            'image_url': 'https://example.com/images/rainbow-trout.jpg'
        },
        {
            'name': 'Bluefin Tuna',
            'scientific_name': 'Thunnus thynnus',
            'habitat': 'Pelagic, found in temperate to tropical waters of the North Atlantic Ocean and Mediterranean Sea.',
            'image_url': 'https://example.com/images/bluefin-tuna.jpg'
        }
    ]
            

    try:
        # Add all fish species to the database
        for fish in fish_data:
            new_species = FishSpecies(**fish)
            db.session.add(new_species)
            
        db.session.commit()
        print("Database seeded successfully!")
            
    except Exception as e:
        db.session.rollback()
        print(f"Error seeding database: {str(e)}")
