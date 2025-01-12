from __future__ import annotations
import csv
from typing import List, Literal

class Person:
    def __init__(self, id: int, first_name: str, last_name: str, email: str, gender: str, ip_address: str):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__gender = gender
        self.__ip_address = ip_address

    def __str__(self) -> str:
        return (f"Person(id={self.__id}, first_name={self.__first_name}, "
                f"last_name={self.__last_name}, email={self.__email}, "
                f"gender={self.__gender}, ip_address={self.__ip_address})")
    
    @property
    def id(self) -> int:
        return self.__id

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def email(self) -> str:
        return self.__email

    @property
    def gender(self) -> str:
        return self.__gender

    @property
    def ip_address(self) -> str:
        return self.__ip_address


def load_person_data_from_file(dateiname:str)->list[Person]:
    list_of_people = []
    with open(file=dateiname,mode="r") as file:
        reader = csv.DictReader(file) #had to ask ChatGPT for this
        for row in reader:
            list_of_people.append(Person(row["id"],row["first_name"],row["last_name"],row["email"],row["gender"],row["ip_address"]))
    return list_of_people

def swap(x,y)->list[Person]:
    pass

def selection_sort_by(list_of_people:list[Person],unique_key: Literal["id","first_name","last_name","email","gender","ip_address"]):
    listed_by_key = []
    sorted_list_of_people = []
    last_person = "a"
    for idx,_ in enumerate(list_of_people):
        listed_by_key.append(getattr(list_of_people[idx],unique_key))
    for unique_key in listed_by_key:
        if (ord(unique_key[0].lower())) > (ord(last_person[0].lower())):
            sorted_list_of_people.append(unique_key)
            last_person = unique_key
    return sorted_list_of_people

if __name__ == "__main__":
    test = load_person_data_from_file("data.csv")
    print(selection_sort_by(test,"first_name"))