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
        "Mahalaxmi",
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

BASE_PRICE = 10

def discount(amt, pass_type):
    if pass_type == "No pass":
        return amt
    elif pass_type == "general":
        return amt - amt * 0.1
    elif pass_type == "executive":
        return amt - amt * 0.3


def price(src, dst, pass_type):
    global BASE_PRICE, colours
    travel_fare = 0
    src_line = ""
    dst_line = ""

    for line, stns in colours.items():
        if src in stns and dst in stns:
            BASE_PRICE = 10
            travel_fare = abs(stns.index(src) - stns.index(dst)) * 8 + BASE_PRICE
            return discount(travel_fare, pass_type)
        
        else:
            BASE_PRICE = 30
            if src in stns:
                src_line = line
            elif dst in stns:
                dst_line = line

    print(colours[src_line].index(src), colours[dst_line].index(dst))
    travel_fare = (
        colours[src_line].index(src) + colours[dst_line].index(dst) * 8 + BASE_PRICE
    )

    return discount(travel_fare, pass_type)
