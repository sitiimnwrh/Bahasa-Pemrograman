class InsuranceData:
    def __init__(self):
        self.data = {
            "what": [],
            "who": {
                "insurance_companies": [],
                "policyholders": [],
                "agents_brokers": [],
                "regulators": [],
                "actuaries": []
            },
            "when": [],
            "where": [],
            "why": [],
            "how": []
        }

    def add_what(self, description):
        self.data["what"].append(description)

    def add_who(self, category, description):
        if category in self.data["who"]:
            self.data["who"][category].append(description)
        else:
            raise ValueError("Invalid category for 'who'")

    def add_when(self, timestamp):
        self.data["when"].append(timestamp)

    def add_where(self, location):
        self.data["where"].append(location)

    def add_why(self, reason):
        self.data["why"].append(reason)

    def add_how(self, method):
        self.data["how"].append(method)

    def get_data(self):
        return self.data

def get_input(prompt):
    return input(prompt)

def main():
    insurance_data = InsuranceData()

    # Input data manually
    print("Masukkan data asuransi berdasarkan analisis 5W 1H")

    # What
    what = get_input("Apa data yang dikumpulkan? ")
    insurance_data.add_what(what)

    # Who
    print("Siapa yang terlibat? (Masukkan data untuk masing-masing kategori)")
    insurance_companies = get_input("Perusahaan asuransi: ")
    insurance_data.add_who("insurance_companies", insurance_companies)
    policyholders = get_input("Pemegang polis: ")
    insurance_data.add_who("policyholders", policyholders)
    agents_brokers = get_input("Agen dan broker asuransi: ")
    insurance_data.add_who("agents_brokers", agents_brokers)
    regulators = get_input("Regulator: ")
    insurance_data.add_who("regulators", regulators)
    actuaries = get_input("Aktuaris: ")
    insurance_data.add_who("actuaries", actuaries)

    # When
    when = get_input("Kapan data dikumpulkan? ")
    insurance_data.add_when(when)

    # Where
    where = get_input("Di mana data dikumpulkan? ")
    insurance_data.add_where(where)

    # Why
    why = get_input("Mengapa data dikumpulkan? ")
    insurance_data.add_why(why)

    # How
    how = get_input("Bagaimana data dikumpulkan? ")
    insurance_data.add_how(how)

    # Mendapatkan dan mencetak data yang telah dimasukkan
    data = insurance_data.get_data()
    print("\nData yang telah dimasukkan:")
    print(data)

if __name__ == "__main__":
    main()
