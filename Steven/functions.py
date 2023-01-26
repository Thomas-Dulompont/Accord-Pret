import numpy as np
import pandas as pd


def dol_to_float(elt):
    """
    Retire le dollar et transforme l'élément en Float 
    """
    elt = elt[1:].replace(",", "")
    return float(elt)

def month_l_to_n(date):
    """
    Retourne le mois en chiffre
    """
    month = date[2:6].replace("-", "")
    dict_month = {
        "jan" : "01",
        "feb" : "02",
        "mar" : "03",
        "apr" : "04",
        "may" : "05",
        "jun" : "06",
        "jul" : "07",
        "aug" : "08",
        "sep" : "09",
        "oct" : "10",
        "nov" : "11",
        "dec" : "12"
    }
    n_month = dict_month[month.lower()]
    date = date.replace(month, n_month)
    return date


def in_default(elt):
    """
    Retourne True / False si l'element est en default
    """
    if elt == "P I F":
        return 0
    elif elt == "CHGOFF":
        return 1
    else:
        return None

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

def urban_or_rural(code):
    """
    Retourne si le secteur est rural ou urbain
    """

    if code == 1:
        return "Urban"
    elif code == 2:
        return "Rural"
    elif code == 0:
        return "Undefined"

def is_new(code):
    """
    Retourne si le buisness est nouveau ou non 
    """

    if code == 1:
        return "Existing"
    elif code == 2:
        return "New"
    else:
        return None

def is_lowdoc(code):
    """
    Retourne si le pret est dans le programme lowdoc
    """
    if code == "N":
        return 0
    elif code == "Y":
        return 1
    else:
        return None

def is_renouvelable(code):
    """
    Retourne si c'est un credit renouvelable ou non
    """
    if code == "Y":
        return 1
    else:
        return 0
