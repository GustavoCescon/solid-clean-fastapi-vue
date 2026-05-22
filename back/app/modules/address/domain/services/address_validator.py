class AddressValidator:

    def validate(self, street: str, number: str, neighborhood: str,
                 city: str, state: str, zip_code: str):
        if not street or len(street) < 3:
            raise ValueError("Street must be at least 3 characters")
        if not number:
            raise ValueError("Number is required")
        if not neighborhood or len(neighborhood) < 2:
            raise ValueError("Neighborhood must be at least 2 characters")
        if not city or len(city) < 2:
            raise ValueError("City must be at least 2 characters")
        if not state or len(state) != 2:
            raise ValueError("State must be a 2-letter code")
        cleaned = "".join(filter(str.isdigit, zip_code or ""))
        if len(cleaned) != 8:
            raise ValueError("Invalid zip code")
