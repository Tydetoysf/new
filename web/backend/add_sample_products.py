from database import db, Product, User
from config import app

def add_sample_products():
    with app.app_context():
        # Check if products already exist
        existing = Product.query.first()
        if existing:
            print("Products already exist. Skipping...")
            return
        
        # Create sample products
        products = [
            {
                'name': 'Fortnite External',
                'category': 'Game Enhancement',
                'price': 49,
                'description': '''Premium Fortnite external tool with advanced features.

Features:
• Undetected aimbot with smooth targeting
• ESP (Player, Loot, Vehicles)
• Radar overlay
• Wall penetration detection
• Customizable FOV and smoothing
• Tournament-safe mode
• Regular updates

Compatibility:
• Windows 10 & 11 (23H2)
• All graphics cards supported
• Works with all game modes

Includes:
• Lifetime updates
• 24/7 support
• Setup guide
• Configuration presets''',
                'seller_id': '1',
                'link_to_video': 'https://youtube.com/@tydeyousf',
                'image1': 'fortnite_external.png',
                'image2': '',
                'image3': '',
                'pin': True,
                'in_stock': 50
            },
            {
                'name': 'SOSA Temporary Spoofer',
                'category': 'Security Tool',
                'price': 29,
                'description': '''Temporary hardware ID spoofer designed for stealth, privacy, and speed.

Features:
• Fortnite Tournament Cleaner
• TPM Spoofing (Safe in FN Tournaments)
• Configurable Spoofing
• Mac Spoofing
• Built-in Cleaner
• Serial Checker
• Changes All Hardware Identifiers
• Changes All Components
• Universal Spoofing
• Activate Windows

Compatibility:
• Windows 10 & 11 (23H2)
• All Motherboards Supported
• Intel & AMD CPUs

Supported Games:
• Fortnite (Tournaments Supported)
• Apex Legends
• Dead by Daylight
• Rainbow Six Siege
• Arc Raiders

Note: Temporary spoofing - resets after restart''',
                'seller_id': '1',
                'link_to_video': 'https://youtube.com/@tydeyousf',
                'image1': 'temp_spoofer.png',
                'image2': '',
                'image3': '',
                'pin': True,
                'in_stock': 100
            },
            {
                'name': 'SOSA Permanent Spoofer',
                'category': 'Security Tool',
                'price': 79,
                'description': '''Permanent hardware ID spoofer with all features of the temporary version, but changes persist after restart.

Features:
• All Temporary Spoofer features
• Permanent hardware ID changes
• Fortnite Tournament Cleaner
• TPM Spoofing (Safe in FN Tournaments)
• Configurable Spoofing
• Mac Spoofing
• Built-in Cleaner
• Serial Checker
• Changes All Hardware Identifiers
• Changes All Components
• Universal Spoofing
• Activate Windows
• Backup & Restore functionality

Compatibility:
• Windows 10 & 11 (23H2)
• All Motherboards Supported
• Intel & AMD CPUs

Supported Games:
• Fortnite (Tournaments Supported)
• Apex Legends
• Dead by Daylight
• Rainbow Six Siege
• Arc Raiders

Note: Changes persist permanently until manually reverted''',
                'seller_id': '1',
                'link_to_video': 'https://youtube.com/@tydeyousf',
                'image1': 'perm_spoofer.png',
                'image2': '',
                'image3': '',
                'pin': True,
                'in_stock': 75
            }
        ]
        
        for product_data in products:
            product = Product(**product_data)
            db.session.add(product)
        
        db.session.commit()
        print(f"✅ Added {len(products)} sample products successfully!")
        
        # Display products
        all_products = Product.query.all()
        print("\nCurrent products in database:")
        for p in all_products:
            print(f"  - {p.name} (${p.price}) - Stock: {p.in_stock}")

if __name__ == '__main__':
    add_sample_products()
