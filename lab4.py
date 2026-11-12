
class Park:
    def __init__(self, address="Невідомо", len_velo=0, bilet_price=0):
        self.__address = address
        self.__len_velo = len_velo
        self.__bilet_price = bilet_price

        self.name = "Міський парк"
        self.visitors = 0

    def get_address(self):
        return self.__address

    def get_len_velo(self):
        return self.__len_velo

    def get_bilet_price(self):
        return self.__bilet_price

    def __str__(self):
        return (f"Назва Парку: {self.name}\n"
                f"Адрес Парку: {self.__address}\n"
                f"Довжина велосипедних доріжок: {self.__len_velo} м\n"
                f"Ціна вхідного квитка: {self.__bilet_price} грн\n"
                f"Кількість відвідувачів: {self.visitors}")

    def __repr__(self):
        return (f"Park(address={self.__address!r}, "
                f"len_velo={self.__len_velo!r}, "
                f"bilet_price={self.__bilet_price!r})")

    def __del__(self):
        print(f"Об'єкт парку '{self.name}' видалено")


def main():
    park1 = Park()

    park2 = Park("м. Львів, вул. Стрийська, 202", 2500, 50)
    park2.name = "Стрийський парк"
    park2.visitors = 150

    park3 = Park("м. Львів, вул. Університетська, 1", 1800, 30)
    park3.name = "Парк Івана Франка"
    park3.visitors = 200

    for i, park in enumerate([park1, park2, park3], start=1):
        print(f"\n--- Парк №{i} ---")
        print(park)

        print("Адрес Парку:", park.get_address())
        print("Довжина доріжок:", park.get_len_velo())
        print("Ціна квитка:", park.get_bilet_price())
        print("repr:", repr(park))


if __name__ == "__main__":
    main()

test = Park('0GFGFGF',10,10)
print(test.name)
print(test.get_address())