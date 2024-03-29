import sys
from heapq import heapify, heappush


def algo(source, dest):
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
    high = 8
    low = 0
    if source in colours["Green"] and dest in colours["Green"]:
        graph = {
            "Anjanapura": {"Thalaghattapura": 8},
            "Thalaghattapura": {"Anjanapura": 8, "Vajrahalli": 8},
            "Vajrahalli": {"Thalaghattapura": 8, "Doddakallasandra": 8},
            "Doddakallasandra": {"Vajrahalli": 8, "Konankunte Cross": 8},
            "Konankunte Cross": {"Doddakallasandra": 8, "Yelachenhalli": 8},
            "Yelachenhalli": {"Konankunte Cross": 8, "Jayaprakash Nagar": 8},
            "Jayaprakash Nagar": {"Yelachenhalli": 8, "Banashankari": 8},
            "Banashankari": {"Jayaprakash Nagar": 8, "Rashtriya Vidhyalaya road": 8},
            "Rashtriya Vidhyalaya road": {"Banashankari": 8, "Jayanagar": 8},
            "Jayanagar": {"Rashtriya Vidhyalaya road": 8, "South End Circle": 8},
            "South End Circle": {"Jayanagar": 8, "Lalbagh": 8},
            "Lalbagh": {"South End Circle": 8, "National College": 8},
            "National College": {"Lalbagh": 8, "Krishna Rajendra Market": 8},
            "Krishna Rajendra Market": {"National College": 8, "Chickpete": 8},
            "Chickpete": {
                "Krishna Rajendra Market": 8,
                "Nadaprabhu Kempe Gowda Majestic": 8,
            },
            "Nadaprabhu Kempe Gowda Majestic": {
                "Mantri Square Sampige Road": high,
                "Chickpete": high,
            },
            "Mantri Square Sampige Road": {
                "Nadaprabhu Kempe Gowda Majestic": 8,
                "Srirampura": 8,
            },
            "Srirampura": {"Mantri Square Sampige Road": 8, "Kuvempu Road": 8},
            "Kuvempu Road": {"Srirampura": 8, "Rajajinagar": 8},
            "Rajajinagar": {"Kuvempu Road": 8, "Mahalaxmi": 8},
            "Mahalaxmi": {"Rajajinagar": 8, "Sandal Soap Factory": 8},
            "Sandal Soap Factory": {"Mahalaxmi": 8, "Yeshwantpur": 8},
            "Yeshwantpur": {"Sandal Soap Factory": 8, "Goraguntepalya": 8},
            "Goraguntepalya": {"Yeshwantpur": 8, "Peenya": 8},
            "Peenya": {"Goraguntepalya": 8, "Peenya Industry": 8},
            "Peenya Industry": {"Peenya": 8, "Jalahalli": 8},
            "Jalahalli": {"Peenya Industry": 8, "Dasarahalli": 8},
            "Dasarahalli": {"Jalahalli": 8, "Nagasandra": 1},
            "Nagasandra": {"Dasarahalli": 10},
        }
    if source in colours["Voilet"] and dest in colours["Voilet"]:
        graph = {
            "Challaghatta": {"Kengeri Bus Terminal": 1},
            "Kengeri Bus Terminal": {"Challaghatta": 10, "Mailasandra": 8},
            "Mailasandra": {"Pattanagere": 8, "Kengeri Bus Terminal": 8},
            "Pattanagere": {"Mailasandra": 8, "Jnanabharathi": 8},
            "Jnanabharathi": {"Pattanagere": 8, "Rajarajeshwari Nagar": 8},
            "Rajarajeshwari Nagar": {"Jnanabharathi": 8, "Nayandahalli": 8},
            "Nayandahalli": {"Rajarajeshwari Nagar": 8, "Mysuru Road": 8},
            "Mysuru Road": {"Nayandahalli": 8, "Deepanjali Nagar": 8},
            "Deepanjali Nagar": {"Mysuru Road": 8, "Attiguppe": 8},
            "Attiguppe": {"Deepanjali Nagar": 8, "Vijayanagar": 8},
            "Vijayanagar": {"Attiguppe": 8, "BGS Hosahalli": 8},
            "BGS Hosahalli": {"Vijayanagar": 8, "Magadi Road": 8},
            "Magadi Road": {"BGS Hosahalli": 8, "KSR City Railway Station": 8},
            "KSR City Railway Station": {
                "Magadi Road": 8,
                "Nadaprabhu Kempe Gowda Majestic": 8,
            },
            "Nadaprabhu Kempe Gowda Majestic": {
                "Sir M Visveswaraya Central College": high,
                "KSR City Railway Station": high,
            },
            "Sir M Visveswaraya Central College": {
                "Nadaprabhu Kempe Gowda Majestic": 8,
                "Dr. B R Ambedkar Vidhana Soudha": 8,
            },
            "Dr. B R Ambedkar Vidhana Soudha": {
                "Sir M Visveswaraya Central College": 8,
                "Cubbon Park": 8,
            },
            "Cubbon Park": {
                "Dr. B R Ambedkar Vidhana Soudha": 8,
                "Mahatma Gandhi Road": 8,
            },
            "Mahatma Gandhi Road": {"Cubbon Park": high, "Trinity": high},
            "Trinity": {"Mahatma Gandhi Road": 8, "Halasuru": 8},
            "Halasuru": {"Trinity": 8, "Indiranagar": 8},
            "Indiranagar": {"Halasuru": 8, "Swami Vivekananda Road": 8},
            "Swami Vivekananda Road": {"Indiranagar": 8, "Baiyyappanahalli": 8},
            "Baiyyappanahalli": {"Swami Vivekananda Road": 8, "Benniganahalli": 8},
            "Benniganahalli": {"Baiyyappanahalli": 8, "Krishnaraja Puram": 8},
            "Krishnaraja Puram": {"Benniganahalli": 8, "Mahadevapura": 8},
            "Mahadevapura": {"Krishnaraja Puram": 8, "Garudacharpalya": 8},
            "Garudacharpalya": {"Mahadevapura": 8, "Hoodi Junction": 8},
            "Hoodi Junction": {"Garudacharpalya": 8, "Sitarama Palya": 8},
            "Sitarama Palya": {"Hoodi Junction": 8, "Kundalahalli": 8},
            "Kundalahalli": {"Sitarama Palya": 8, "Nallurahalli": 8},
            "Nallurahalli": {"Kundalahalli": 8, "Sadaramangala": 8},
            "Sadaramangala": {"Nallurahalli": 8, "Pattanduru Agrahara": 8},
            "Pattanduru Agrahara": {"Sadaramangala": 8, "Kadugodi Industrial Area": 8},
            "Kadugodi Industrial Area": {"Pattanduru Agrahara": 8, "Channasandra": 8},
            "Channasandra": {"Kadugodi Industrial Area": 8, "Whitefield": 8},
            "Whitefield": {"Channasandra": 8},
        }
    if source in colours["Voilet"] and dest in colours["Green"]:
        if dest in [
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
        ]:
            graph = {
                "Challaghatta": {"Kengeri Bus Terminal": 1},
                "Kengeri Bus Terminal": {"Challaghatta": 10, "Mailasandra": 8},
                "Mailasandra": {"Pattanagere": 8, "Kengeri Bus Terminal": 8},
                "Pattanagere": {"Mailasandra": 8, "Jnanabharathi": 8},
                "Jnanabharathi": {"Pattanagere": 8, "Rajarajeshwari Nagar": 8},
                "Rajarajeshwari Nagar": {"Jnanabharathi": 8, "Nayandahalli": 8},
                "Nayandahalli": {"Rajarajeshwari Nagar": 8, "Mysuru Road": 8},
                "Mysuru Road": {"Nayandahalli": 8, "Deepanjali Nagar": 8},
                "Deepanjali Nagar": {"Mysuru Road": 8, "Attiguppe": 8},
                "Attiguppe": {"Deepanjali Nagar": 8, "Vijayanagar": 8},
                "Vijayanagar": {"Attiguppe": 8, "BGS Hosahalli": 8},
                "BGS Hosahalli": {"Vijayanagar": 8, "Magadi Road": 8},
                "Magadi Road": {"BGS Hosahalli": 8, "KSR City Railway Station": 8},
                "KSR City Railway Station": {
                    "Magadi Road": 8,
                    "Nadaprabhu Kempe Gowda Majestic": 8,
                },
                "Sir M Visveswaraya Central College": {
                    "Nadaprabhu Kempe Gowda Majestic": 8,
                    "Dr. B R Ambedkar Vidhana Soudha": 8,
                },
                "Dr. B R Ambedkar Vidhana Soudha": {
                    "Sir M Visveswaraya Central College": 8,
                    "Cubbon Park": 8,
                },
                "Cubbon Park": {
                    "Dr. B R Ambedkar Vidhana Soudha": 8,
                    "Mahatma Gandhi Road": 8,
                },
                "Mahatma Gandhi Road": {"Cubbon Park": high, "Trinity": high},
                "Trinity": {"Mahatma Gandhi Road": 8, "Halasuru": 8},
                "Halasuru": {"Trinity": 8, "Indiranagar": 8},
                "Indiranagar": {"Halasuru": 8, "Swami Vivekananda Road": 8},
                "Swami Vivekananda Road": {"Indiranagar": 8, "Baiyyappanahalli": 8},
                "Baiyyappanahalli": {"Swami Vivekananda Road": 8, "Benniganahalli": 8},
                "Benniganahalli": {"Baiyyappanahalli": 8, "Krishnaraja Puram": 8},
                "Krishnaraja Puram": {"Benniganahalli": 8, "Mahadevapura": 8},
                "Mahadevapura": {"Krishnaraja Puram": 8, "Garudacharpalya": 8},
                "Garudacharpalya": {"Mahadevapura": 8, "Hoodi Junction": 8},
                "Hoodi Junction": {"Garudacharpalya": 8, "Sitarama Palya": 8},
                "Sitarama Palya": {"Hoodi Junction": 8, "Kundalahalli": 8},
                "Kundalahalli": {"Sitarama Palya": 8, "Nallurahalli": 8},
                "Nallurahalli": {"Kundalahalli": 8, "Sadaramangala": 8},
                "Sadaramangala": {"Nallurahalli": 8, "Pattanduru Agrahara": 8},
                "Pattanduru Agrahara": {
                    "Sadaramangala": 8,
                    "Kadugodi Industrial Area": 8,
                },
                "Kadugodi Industrial Area": {
                    "Pattanduru Agrahara": 8,
                    "Channasandra": 8,
                },
                "Channasandra": {"Kadugodi Industrial Area": 8, "Whitefield": 8},
                "Whitefield": {"Channasandra": 8},
                "Nadaprabhu Kempe Gowda Majestic": {"Mantri Square Sampige Road": high},
                "Mantri Square Sampige Road": {
                    "Nadaprabhu Kempe Gowda Majestic": 8,
                    "Srirampura": 8,
                },
                "Srirampura": {"Mantri Square Sampige Road": 8, "Kuvempu Road": 8},
                "Kuvempu Road": {"Srirampura": 8, "Rajajinagar": 8},
                "Rajajinagar": {"Kuvempu Road": 8, "Mahalaxmi": 8},
                "Mahalaxmi": {"Rajajinagar": 8, "Sandal Soap Factory": 8},
                "Sandal Soap Factory": {"Mahalaxmi": 8, "Yeshwantpur": 8},
                "Yeshwantpur": {"Sandal Soap Factory": 8, "Goraguntepalya": 8},
                "Goraguntepalya": {"Yeshwantpur": 8, "Peenya": 8},
                "Peenya": {"Goraguntepalya": 8, "Peenya Industry": 8},
                "Peenya Industry": {"Peenya": 8, "Jalahalli": 8},
                "Jalahalli": {"Peenya Industry": 8, "Dasarahalli": 8},
                "Dasarahalli": {"Jalahalli": 8, "Nagasandra": 1},
                "Nagasandra": {"Dasarahalli": 10},
            }
        else:
            graph = {
                "Challaghatta": {"Kengeri Bus Terminal": 1},
                "Kengeri Bus Terminal": {"Challaghatta": 10, "Mailasandra": 8},
                "Mailasandra": {"Pattanagere": 8, "Kengeri Bus Terminal": 8},
                "Pattanagere": {"Mailasandra": 8, "Jnanabharathi": 8},
                "Jnanabharathi": {"Pattanagere": 8, "Rajarajeshwari Nagar": 8},
                "Rajarajeshwari Nagar": {"Jnanabharathi": 8, "Nayandahalli": 8},
                "Nayandahalli": {"Rajarajeshwari Nagar": 8, "Mysuru Road": 8},
                "Mysuru Road": {"Nayandahalli": 8, "Deepanjali Nagar": 8},
                "Deepanjali Nagar": {"Mysuru Road": 8, "Attiguppe": 8},
                "Attiguppe": {"Deepanjali Nagar": 8, "Vijayanagar": 8},
                "Vijayanagar": {"Attiguppe": 8, "BGS Hosahalli": 8},
                "BGS Hosahalli": {"Vijayanagar": 8, "Magadi Road": 8},
                "Magadi Road": {"BGS Hosahalli": 8, "KSR City Railway Station": 8},
                "KSR City Railway Station": {
                    "Magadi Road": 8,
                    "Nadaprabhu Kempe Gowda Majestic": 8,
                },
                "Sir M Visveswaraya Central College": {
                    "Nadaprabhu Kempe Gowda Majestic": 8,
                    "Dr. B R Ambedkar Vidhana Soudha": 8,
                },
                "Dr. B R Ambedkar Vidhana Soudha": {
                    "Sir M Visveswaraya Central College": 8,
                    "Cubbon Park": 8,
                },
                "Cubbon Park": {
                    "Dr. B R Ambedkar Vidhana Soudha": 8,
                    "Mahatma Gandhi Road": 8,
                },
                "Mahatma Gandhi Road": {"Cubbon Park": high, "Trinity": high},
                "Trinity": {"Mahatma Gandhi Road": 8, "Halasuru": 8},
                "Halasuru": {"Trinity": 8, "Indiranagar": 8},
                "Indiranagar": {"Halasuru": 8, "Swami Vivekananda Road": 8},
                "Swami Vivekananda Road": {"Indiranagar": 8, "Baiyyappanahalli": 8},
                "Baiyyappanahalli": {"Swami Vivekananda Road": 8, "Benniganahalli": 8},
                "Benniganahalli": {"Baiyyappanahalli": 8, "Krishnaraja Puram": 8},
                "Krishnaraja Puram": {"Benniganahalli": 8, "Mahadevapura": 8},
                "Mahadevapura": {"Krishnaraja Puram": 8, "Garudacharpalya": 8},
                "Garudacharpalya": {"Mahadevapura": 8, "Hoodi Junction": 8},
                "Hoodi Junction": {"Garudacharpalya": 8, "Sitarama Palya": 8},
                "Sitarama Palya": {"Hoodi Junction": 8, "Kundalahalli": 8},
                "Kundalahalli": {"Sitarama Palya": 8, "Nallurahalli": 8},
                "Nallurahalli": {"Kundalahalli": 8, "Sadaramangala": 8},
                "Sadaramangala": {"Nallurahalli": 8, "Pattanduru Agrahara": 8},
                "Pattanduru Agrahara": {
                    "Sadaramangala": 8,
                    "Kadugodi Industrial Area": 8,
                },
                "Kadugodi Industrial Area": {
                    "Pattanduru Agrahara": 8,
                    "Channasandra": 8,
                },
                "Channasandra": {"Kadugodi Industrial Area": 8, "Whitefield": 8},
                "Whitefield": {"Channasandra": 8},
                "Nadaprabhu Kempe Gowda Majestic": {"Chickpete": high},
                "Chickpete": {
                    "Krishna Rajendra Market": 8,
                    "Nadaprabhu Kempe Gowda Majestic": 8,
                },
                "Krishna Rajendra Market": {"National College": 8, "Chickpete": 8},
                "National College": {"Lalbagh": 8, "Krishna Rajendra Market": 8},
                "Lalbagh": {"South End Circle": 8, "National College": 8},
                "South End Circle": {"Jayanagar": 8, "Lalbagh": 8},
                "Jayanagar": {"Rashtriya Vidhyalaya road": 8, "South End Circle": 8},
                "Rashtriya Vidhyalaya road": {"Banashankari": 8, "Jayanagar": 8},
                "Banashankari": {
                    "Jayaprakash Nagar": 8,
                    "Rashtriya Vidhyalaya road": 8,
                },
                "Jayaprakash Nagar": {"Yelachenhalli": 8, "Banashankari": 8},
                "Yelachenhalli": {"Konankunte Cross": 8, "Jayaprakash Nagar": 8},
                "Konankunte Cross": {"Doddakallasandra": 8, "Yelachenhalli": 8},
                "Doddakallasandra": {"Vajrahalli": 8, "Konankunte Cross": 8},
                "Vajrahalli": {"Thalaghattapura": 8, "Doddakallasandra": 8},
                "Thalaghattapura": {"Anjanapura": 8, "Vajrahalli": 8},
                "Anjanapura": {"Thalaghattapura": 8},
            }
    if source in colours["Green"] and dest in colours["Voilet"]:
        if dest in [
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
        ]:
            graph = {
                "Anjanapura": {"Thalaghattapura": 8},
                "Thalaghattapura": {"Anjanapura": 8, "Vajrahalli": 8},
                "Vajrahalli": {"Thalaghattapura": 8, "Doddakallasandra": 8},
                "Doddakallasandra": {"Vajrahalli": 8, "Konankunte Cross": 8},
                "Konankunte Cross": {"Doddakallasandra": 8, "Yelachenhalli": 8},
                "Yelachenhalli": {"Konankunte Cross": 8, "Jayaprakash Nagar": 8},
                "Jayaprakash Nagar": {"Yelachenhalli": 8, "Banashankari": 8},
                "Banashankari": {
                    "Jayaprakash Nagar": 8,
                    "Rashtriya Vidhyalaya road": 8,
                },
                "Rashtriya Vidhyalaya road": {"Banashankari": 8, "Jayanagar": 8},
                "Jayanagar": {"Rashtriya Vidhyalaya road": 8, "South End Circle": 8},
                "South End Circle": {"Jayanagar": 8, "Lalbagh": 8},
                "Lalbagh": {"South End Circle": 8, "National College": 8},
                "National College": {"Lalbagh": 8, "Krishna Rajendra Market": 8},
                "Krishna Rajendra Market": {"National College": 8, "Chickpete": 8},
                "Chickpete": {
                    "Krishna Rajendra Market": 8,
                    "Nadaprabhu Kempe Gowda Majestic": 8,
                },
                "Mantri Square Sampige Road": {
                    "Nadaprabhu Kempe Gowda Majestic": 8,
                    "Srirampura": 8,
                },
                "Srirampura": {"Mantri Square Sampige Road": 8, "Kuvempu Road": 8},
                "Kuvempu Road": {"Srirampura": 8, "Rajajinagar": 8},
                "Rajajinagar": {"Kuvempu Road": 8, "Mahalaxmi": 8},
                "Mahalaxmi": {"Rajajinagar": 8, "Sandal Soap Factory": 8},
                "Sandal Soap Factory": {"Mahalaxmi": 8, "Yeshwantpur": 8},
                "Yeshwantpur": {"Sandal Soap Factory": 8, "Goraguntepalya": 8},
                "Goraguntepalya": {"Yeshwantpur": 8, "Peenya": 8},
                "Peenya": {"Goraguntepalya": 8, "Peenya Industry": 8},
                "Peenya Industry": {"Peenya": 8, "Jalahalli": 8},
                "Jalahalli": {"Peenya Industry": 8, "Dasarahalli": 8},
                "Dasarahalli": {"Jalahalli": 8, "Nagasandra": 1},
                "Nagasandra": {"Dasarahalli": 10},
                "Nadaprabhu Kempe Gowda Majestic": {"KSR City Railway Station": high},
                "Challaghatta": {"Kengeri Bus Terminal": 1},
                "Kengeri Bus Terminal": {"Challaghatta": 10, "Mailasandra": 8},
                "Mailasandra": {"Pattanagere": 8, "Kengeri Bus Terminal": 8},
                "Pattanagere": {"Mailasandra": 8, "Jnanabharathi": 8},
                "Jnanabharathi": {"Pattanagere": 8, "Rajarajeshwari Nagar": 8},
                "Rajarajeshwari Nagar": {"Jnanabharathi": 8, "Nayandahalli": 8},
                "Nayandahalli": {"Rajarajeshwari Nagar": 8, "Mysuru Road": 8},
                "Mysuru Road": {"Nayandahalli": 8, "Deepanjali Nagar": 8},
                "Deepanjali Nagar": {"Mysuru Road": 8, "Attiguppe": 8},
                "Attiguppe": {"Deepanjali Nagar": 8, "Vijayanagar": 8},
                "Vijayanagar": {"Attiguppe": 8, "BGS Hosahalli": 8},
                "BGS Hosahalli": {"Vijayanagar": 8, "Magadi Road": 8},
                "Magadi Road": {"BGS Hosahalli": 8, "KSR City Railway Station": 8},
                "KSR City Railway Station": {
                    "Magadi Road": 8,
                    "Nadaprabhu Kempe Gowda Majestic": 8,
                },
            }
        else:
            graph = {
                "Anjanapura": {"Thalaghattapura": 8},
                "Thalaghattapura": {"Anjanapura": 8, "Vajrahalli": 8},
                "Vajrahalli": {"Thalaghattapura": 8, "Doddakallasandra": 8},
                "Doddakallasandra": {"Vajrahalli": 8, "Konankunte Cross": 8},
                "Konankunte Cross": {"Doddakallasandra": 8, "Yelachenhalli": 8},
                "Yelachenhalli": {"Konankunte Cross": 8, "Jayaprakash Nagar": 8},
                "Jayaprakash Nagar": {"Yelachenhalli": 8, "Banashankari": 8},
                "Banashankari": {
                    "Jayaprakash Nagar": 8,
                    "Rashtriya Vidhyalaya road": 8,
                },
                "Rashtriya Vidhyalaya road": {"Banashankari": 8, "Jayanagar": 8},
                "Jayanagar": {"Rashtriya Vidhyalaya road": 8, "South End Circle": 8},
                "South End Circle": {"Jayanagar": 8, "Lalbagh": 8},
                "Lalbagh": {"South End Circle": 8, "National College": 8},
                "National College": {"Lalbagh": 8, "Krishna Rajendra Market": 8},
                "Krishna Rajendra Market": {"National College": 8, "Chickpete": 8},
                "Chickpete": {
                    "Krishna Rajendra Market": 8,
                    "Nadaprabhu Kempe Gowda Majestic": 8,
                },
                "Mantri Square Sampige Road": {
                    "Nadaprabhu Kempe Gowda Majestic": 8,
                    "Srirampura": 8,
                },
                "Srirampura": {"Mantri Square Sampige Road": 8, "Kuvempu Road": 8},
                "Kuvempu Road": {"Srirampura": 8, "Rajajinagar": 8},
                "Rajajinagar": {"Kuvempu Road": 8, "Mahalaxmi": 8},
                "Mahalaxmi": {"Rajajinagar": 8, "Sandal Soap Factory": 8},
                "Sandal Soap Factory": {"Mahalaxmi": 8, "Yeshwantpur": 8},
                "Yeshwantpur": {"Sandal Soap Factory": 8, "Goraguntepalya": 8},
                "Goraguntepalya": {"Yeshwantpur": 8, "Peenya": 8},
                "Peenya": {"Goraguntepalya": 8, "Peenya Industry": 8},
                "Peenya Industry": {"Peenya": 8, "Jalahalli": 8},
                "Jalahalli": {"Peenya Industry": 8, "Dasarahalli": 8},
                "Dasarahalli": {"Jalahalli": 8, "Nagasandra": 1},
                "Nagasandra": {"Dasarahalli": 10},
                "Nadaprabhu Kempe Gowda Majestic": {
                    "Sir M Visveswaraya Central College": high
                },
                "Sir M Visveswaraya Central College": {
                    "Nadaprabhu Kempe Gowda Majestic": 8,
                    "Dr. B R Ambedkar Vidhana Soudha": 8,
                },
                "Dr. B R Ambedkar Vidhana Soudha": {
                    "Sir M Visveswaraya Central College": 8,
                    "Cubbon Park": 8,
                },
                "Cubbon Park": {
                    "Dr. B R Ambedkar Vidhana Soudha": 8,
                    "Mahatma Gandhi Road": 8,
                },
                "Mahatma Gandhi Road": {"Cubbon Park": high, "Trinity": high},
                "Trinity": {"Mahatma Gandhi Road": 8, "Halasuru": 8},
                "Halasuru": {"Trinity": 8, "Indiranagar": 8},
                "Indiranagar": {"Halasuru": 8, "Swami Vivekananda Road": 8},
                "Swami Vivekananda Road": {"Indiranagar": 8, "Baiyyappanahalli": 8},
                "Baiyyappanahalli": {"Swami Vivekananda Road": 8, "Benniganahalli": 8},
                "Benniganahalli": {"Baiyyappanahalli": 8, "Krishnaraja Puram": 8},
                "Krishnaraja Puram": {"Benniganahalli": 8, "Mahadevapura": 8},
                "Mahadevapura": {"Krishnaraja Puram": 8, "Garudacharpalya": 8},
                "Garudacharpalya": {"Mahadevapura": 8, "Hoodi Junction": 8},
                "Hoodi Junction": {"Garudacharpalya": 8, "Sitarama Palya": 8},
                "Sitarama Palya": {"Hoodi Junction": 8, "Kundalahalli": 8},
                "Kundalahalli": {"Sitarama Palya": 8, "Nallurahalli": 8},
                "Nallurahalli": {"Kundalahalli": 8, "Sadaramangala": 8},
                "Sadaramangala": {"Nallurahalli": 8, "Pattanduru Agrahara": 8},
                "Pattanduru Agrahara": {
                    "Sadaramangala": 8,
                    "Kadugodi Industrial Area": 8,
                },
                "Kadugodi Industrial Area": {
                    "Pattanduru Agrahara": 8,
                    "Channasandra": 8,
                },
                "Channasandra": {"Kadugodi Industrial Area": 8, "Whitefield": 8},
                "Whitefield": {"Channasandra": 8},
            }

    inf = sys.maxsize
    node_data = {
        "Anjanapura": {"cost": inf, "pred": []},
        "Thalaghattapura": {"cost": inf, "pred": []},
        "Vajrahalli": {"cost": inf, "pred": []},
        "Doddakallasandra": {"cost": inf, "pred": []},
        "Konankunte Cross": {"cost": inf, "pred": []},
        "Yelachenhalli": {"cost": inf, "pred": []},
        "Jayaprakash Nagar": {"cost": inf, "pred": []},
        "Banashankari": {"cost": inf, "pred": []},
        "Rashtriya Vidhyalaya road": {"cost": inf, "pred": []},
        "Jayanagar": {"cost": inf, "pred": []},
        "Lalbagh": {"cost": inf, "pred": []},
        "South End Circle": {"cost": inf, "pred": []},
        "National College": {"cost": inf, "pred": []},
        "Krishna Rajendra Market": {"cost": inf, "pred": []},
        "Chickpete": {"cost": inf, "pred": []},
        "Nadaprabhu Kempe Gowda Majestic": {"cost": inf, "pred": []},
        "Mantri Square Sampige Road": {"cost": inf, "pred": []},
        "Srirampura": {"cost": inf, "pred": []},
        "Kuvempu Road": {"cost": inf, "pred": []},
        "Rajajinagar": {"cost": inf, "pred": []},
        "Mahalaxmi": {"cost": inf, "pred": []},
        "Sandal Soap Factory": {"cost": inf, "pred": []},
        "Yeshwantpur": {"cost": inf, "pred": []},
        "Goraguntepalya": {"cost": inf, "pred": []},
        "Peenya": {"cost": inf, "pred": []},
        "Peenya Industry": {"cost": inf, "pred": []},
        "Jalahalli": {"cost": inf, "pred": []},
        "Dasarahalli": {"cost": inf, "pred": []},
        "Nagasandra": {"cost": inf, "pred": []},
        "Manjunath NAgar": {"cost": inf, "pred": []},
        "Challaghatta": {"cost": inf, "pred": []},
        "Kengeri Bus Terminal": {"cost": inf, "pred": []},
        "Mailasandra": {"cost": inf, "pred": []},
        "Pattanagere": {"cost": inf, "pred": []},
        "Jnanabharathi": {"cost": inf, "pred": []},
        "Rajarajeshwari Nagar": {"cost": inf, "pred": []},
        "Nayandahalli": {"cost": inf, "pred": []},
        "Mysuru Road": {"cost": inf, "pred": []},
        "Deepanjali Nagar": {"cost": inf, "pred": []},
        "Attiguppe": {"cost": inf, "pred": []},
        "Vijayanagar": {"cost": inf, "pred": []},
        "BGS Hosahalli": {"cost": inf, "pred": []},
        "Magadi Road": {"cost": inf, "pred": []},
        "KSR City Railway Station": {"cost": inf, "pred": []},
        "Nadaprabhu Kempe Gowda Majestic": {"cost": inf, "pred": []},
        "Sir M Visveswaraya Central College": {"cost": inf, "pred": []},
        "Dr. B R Ambedkar Vidhana Soudha": {"cost": inf, "pred": []},
        "Cubbon Park": {"cost": inf, "pred": []},
        "Trinity": {"cost": inf, "pred": []},
        "Halasuru": {"cost": inf, "pred": []},
        "Indiranagar": {"cost": inf, "pred": []},
        "Swami Vivekananda Road": {"cost": inf, "pred": []},
        "Baiyyappanahalli": {"cost": inf, "pred": []},
        "Benniganahalli": {"cost": inf, "pred": []},
        "Mahadevapura": {"cost": inf, "pred": []},
        "Garudacharpalya": {"cost": inf, "pred": []},
        "Hoodi Junction": {"cost": inf, "pred": []},
        "Sitarama Palya": {"cost": inf, "pred": []},
        "Kundalahalli": {"cost": inf, "pred": []},
        "Nallurahalli": {"cost": inf, "pred": []},
        "Sadaramangala": {"cost": inf, "pred": []},
        "Pattanduru Agrahara": {"cost": inf, "pred": []},
        "Kadugodi Industrial Area": {"cost": inf, "pred": []},
        "Channasandra": {"cost": inf, "pred": []},
        "Whitefield": {"cost": inf, "pred": []},
        "Mahatma Gandhi Road": {"cost": inf, "pred": []},
        "Krishnaraja Puram": {"cost": inf, "pred": []},
    }

    try:
        node_data[source]["cost"] = 0
    except KeyError:
        return -1

    visited = []
    temp = source
    while temp != dest:
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for j in graph[temp]:
                if j not in visited:
                    cost = node_data[temp]["cost"] + graph[temp][j]
                    if cost < node_data[j]["cost"]:
                        node_data[j]["cost"] = cost
                        node_data[j]["pred"] = node_data[temp]["pred"] + list(temp)
                        print(temp, end=" -> ")
                    heappush(min_heap, (node_data[j]["cost"], j))
        heapify(min_heap)
        temp = min_heap[0][1]

    str_price = str(node_data[dest]["cost"])
    return str_price
