def get_sector(naics):
    """
    Cette fonction prend en entrée le naics et renvoie une chaîne de caractères correspondant au secteur de l'entreprise.
    
        :param naics: Le naics de l'entreprise
        :return : La catégorie correspondante ou NaN
    """

    sector = {
        "11": "Agriculture, forestry, fishing and hunting",
        "21": "Mining, quarrying, and oil and gas extraction",
        "22": "Utilities",
        "23": "Construction",
        "31": "Manufacturing",
        "32": "Manufacturing",
        "33": "Manufacturing",
        "42": "Wholesale trade",
        "44": "Retail trade",
        "45": "Retail trade",
        "48": "Transportation and warehousing",
        "49": "Transportation and warehousing",
        "51": "Information",
        "52": "Finance and insurance",
        "53": "Realestate and rental and leasing",
        "54": "Professional, scientific, and technical services",
        "55": "Management of companies and enterprises",
        "56": "Administrative and support and waste management and remediation services",
        "61": "Educational services",
        "62": "Health care and social assistance",
        "71": "Arts, entertainment, and recreation",
        "72": "Accommodation and food services",
        "81": "Other services (except public administration)",
        "92": "Public administration"
    }
    first_two_digits = str(naics)[:2]
    if first_two_digits in sector:
        return sector[first_two_digits]
    else:
        return "Sector not known"
def is_new(code):
    """
    Retourne si le buisness est nouveau ou non 
    """

    if code.lower() == "on":
        return "Existing"
    else:
        return "New"
