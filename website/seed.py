from . import db
from .models import FishSpecies

def seed_fish_species():

    fish_data = [
        {
            'name': 'Brook Trout',
            'scientific_name': 'Salvelinus fontinalis',
            'habitat': 'Cold, clean, well-oxygenated streams and rivers with rocky bottoms.',
            'image_url': 'https://example.com/images/brook-trout.jpg'
        },
        {
            'name': 'Rainbow Trout',
            'scientific_name': 'Oncorhynchus mykiss',
            'habitat': 'Cold, clear freshwater streams and lakes with gravel bottoms and moderate to fast currents.',
            'image_url': 'https://example.com/images/rainbow-trout.jpg'
        },
        {
            'name': 'Brown Trout',
            'scientific_name': 'Salmo trutta',
            'habitat': 'Cool streams, rivers, and lakes with adequate cover and moderate to fast currents.',
            'image_url': 'https://example.com/images/brown-trout.jpg'
        },
        {
            'name': 'Largemouth Bass',
            'scientific_name': 'Micropterus salmoides',
            'habitat': 'Warm, slow-moving rivers, lakes, and ponds with plenty of vegetation and cover.',
            'image_url': 'https://t3.ftcdn.net/jpg/05/99/39/78/240_F_599397886_Qn1NLcNffWm5OLpVtjVIsVorJrltdAyL.jpg'
        },
        {
            'name': 'Smallmouth Bass',
            'scientific_name': 'Micropterus dolomieu',
            'habitat': 'Cool, clear streams and rivers with rocky or gravelly bottoms, as well as lakes.',
            'image_url': 'https://example.com/images/smallmouth-bass.jpg'
        },
        {
            'name': 'Chain Pickerel',
            'scientific_name': 'Esox niger',
            'habitat': 'Slow-moving rivers, lakes, and ponds with abundant aquatic vegetation.',
            'image_url': 'https://example.com/images/chain-pickerel.jpg'
        },
        {
            'name': 'Bluegill',
            'scientific_name': 'Lepomis macrochirus',
            'habitat': 'Warm lakes, ponds, and slow-moving rivers with plenty of aquatic plants and structures.',
            'image_url': 'https://example.com/images/bluegill.jpg'
        },
        {
            'name': 'Pumpkinseed Sunfish',
            'scientific_name': 'Lepomis gibbosus',
            'habitat': 'Shallow, weedy areas of lakes, ponds, and slow-moving streams.',
            'image_url': 'https://example.com/images/pumpkinseed-sunfish.jpg'
        },
        {
            'name': 'Yellow Perch',
            'scientific_name': 'Perca flavescens',
            'habitat': 'Lakes, ponds, and slow-moving rivers with sandy or muddy bottoms.',
            'image_url': 'https://example.com/images/yellow-perch.jpg'
        },
        {
            'name': 'Black Crappie',
            'scientific_name': 'Pomoxis nigromaculatus',
            'habitat': 'Lakes, ponds, and slow-moving rivers with submerged structures for cover.',
            'image_url': 'https://example.com/images/black-crappie.jpg'
        },
        {
            'name': 'Walleye',
            'scientific_name': 'Sander vitreus',
            'habitat': 'Larger lakes and rivers with rocky or sandy bottoms and clear waters.',
            'image_url': 'https://example.com/images/walleye.jpg'
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
