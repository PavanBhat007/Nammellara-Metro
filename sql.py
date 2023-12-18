import sqlite3


def insert_values(cursor, colours):
    i = 0
    for line, stations in colours.items():
        i = 0
        while i < len(stations):
            curr_stn = stations[i]
            try:
                next_stn = stations[i + 1]
            except IndexError:
                next_stn = curr_stn

            cursor.execute(
                """
                INSERT INTO stations (stn_name, next_stn, line)
                VALUES (?, ?, ?)
            """,
                (curr_stn, next_stn, line),
            )

            i += 1


def create_tables(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_auth (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            hash TEXT NOT NULL
        );
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL, 
            age INTEGER NOT NULL, 
            gender CHAR NOT NULL, 
            credits INTEGER DEFAULT 1000 NOT NULL, 
            FOREIGN KEY (user_id) REFERENCES user_auth (user_id));            
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS travels (
            travel_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER, 
            source TEXT NOT NULL, 
            dest NOT NULL, 
            amount INTEGER NOT NULL, 
            date DATE, 
            FOREIGN KEY (user_id) REFERENCES user_auth (user_id));
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stations (
            stn_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            stn_name TEXT, 
            next_stn TEXT, 
            line TEXT
        );
    """
    )
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_pass (
            user_id INTEGER PRIMARY KEY, 
            pass_type TEXT NOT NULL, 
            FOREIGN KEY (user_id) REFERENCES user_auth (user_id)
        );
    """)

def create_trigger(cursor):
    cursor.execute("""
        CREATE TRIGGER IF NOT EXISTS after_insert_travel
        AFTER INSERT ON travels
        BEGIN
            UPDATE users SET credits = credits - NEW.amount
            WHERE user_id = NEW.user_id;
        END;
    """)

def create_procedure(cursor):
    cursor.execute("""
        CREATE PROCEDURE IF NOT EXISTS DeductCredits(user_id_param INTEGER, amount_param INTEGER)
        BEGIN
            UPDATE users SET credits = credits - amount_param WHERE user_id = user_id_param;
        END;   
    """)


def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    colours = {
        "Blue": [
            "KIA Terminals",
            "Airport City",
            "Doddaljala",
            "Bettahalasur",
            "Bagalur Cross",
            "Yelahanka",
            "Jakkur Cross",
            "Kodigehalli",
            "Hebbal",
            "Kempapura",
            "Veeranna Palya",
            "HBR Layout",
            "Kalyan Nagar",
            "HRBR Layout",
            "Horamavu",
            "Kasturi Nagar",
            "Krishnaraja Puram",
            "Saraswathi Nagar",
            "DRDO Sports Complex",
            "Doddanekkundi",
            "ISRO",
            "Marathahalli",
            "Kaadubeesanahalli",
            "Devarabeesanahalli",
            "Bellandur",
            "Ibblur",
            "Agara Lake",
            "Venkatapura",
        ],
        "Purple": [
            "Kadugondanahalli ",
            "Venkateshpura",
            "Tannery Road",
            "Pottery Town",
            "Cantonment",
            "Shivajinagar",
            "Rashtriya Millitary School",
            "Langford Town",
            "Lakkasandra",
            "Dairy Circle",
            "Taverekere",
            "Jayadeva",
            "JP NAgar 4th phase",
            "IIMB",
            "Hulimavu",
            "Kalena Agrahara",
        ],
        "Yellow": [
            "Bommasandra",
            "Hebbagodi",
            "Huskur Road",
            "Infosys Foundation Konappana Agrahara",
            "Electronic City",
            "Beratena Agrahara",
            "Hosa Road",
            "Singasandra",
            "Kudlu Gate",
            "Hongasandra",
            "Bommanahalli",
            "Central Silk Board",
            "BTM Layout",
            "Ragigudda",
        ],
        "Green": [
            "Madavara",
            "Chikkabidirakallu",
            "Manjunath Nagar",
            "Nagasandra",
            "Dasarahalli",
            "Jalahalli",
            "Peenya Industry",
            "Peenya",
            "Goraguntepalya",
            "Yeshwantpur",
            "Sandal Soap Factory",
            "MAhalaxmi",
            "Rajajinagar",
            "Kuvempu Road",
            "Srirampura",
            "Mantri Square Sampige Road",
            "Chickpete",
            "Krishna Rajendra Market",
            "National College",
            "Lalbagh",
            "South End Circle",
            "Jayanagar",
            "Rashtriya Vidhyalaya Road",
            "Banashankari",
            "Jayaprakash NAgar",
            "Yelachenahalli",
            "Konanakunte Cross",
            "Doddakallasandra",
            "Vajrahalli",
            "Thalaghattapura",
            "Anjanapura",
        ],
        "Voilet": [
            "Challaghatta",
            "Kengeri Bus Terminal",
            "Mailasandra",
            "Pattanagere",
            "Jnanabharathi",
            "Rajarajeshwari Nagar",
            "Nayandahalli",
            "Mysuru Road",
            "Deepanjali Nagar",
            "Deepanjali Nagar",
            "Attiguppe",
            "Vijayanagar",
            "BGS Hosahalli",
            "Magadi Road",
            "KSR City Railway Station",
            "Nadaprabhu Kempe Gowda Majestic",
            "Sir M Visveswaraya Central College",
            "Dr. B R Ambedkar Vidhana Soudha",
            "Cubbon Park",
            "Mahatma Gandhi Road",
            "Trinity",
            "Halasuru",
            "Indiranagar",
            "Swami Vivekananda Road",
            "Baiyyappanahalli",
            "Benniganahalli",
            "Mahadevpura",
            "Garudacharpalya",
            "Hoodi Junction",
            "Sitarama Palya",
            "Kundalahalli",
            "Nallurahalli",
            "Sadaramangala",
            "Pattanduru Agrahara",
            "Kadugodi Industrial Area",
            "Channasandra",
            "Whitefield",
        ],
    }
    
    create_tables(cursor)
    # insert_values(cursor, colours)
    # create_procedure(cursor)
    create_trigger(cursor)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
