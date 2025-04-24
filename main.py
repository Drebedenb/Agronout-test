import re

class PhoneExtractor:
    def __init__(self) -> None:
        self.pattern = re.compile(
            r'(?:\7|8)(?:\D{0,3})?(\d{3})(?:\D{0,3})?(\d{3})(?:\D{0,3})?(\d{2})(?:\D{0,3})?(\d{2})'
        )
        self.numbers_list: list[str] = []
        self.seen: set[str] = set()

    def normalize(self, parts: tuple[str, str, str, str]) -> str:
        return f'+7({parts[0]}){parts[1]}-{parts[2]}-{parts[3]}'

    def extract_from_file(self, input_path: str, output_path: str) -> None:
        with open(input_path, 'r', encoding='utf-8') as infile:
            for line in infile:
                for match in self.pattern.finditer(line):
                    number = self.normalize(match.groups())
                    if number not in self.seen:
                        self.seen.add(number)
                        self.numbers_list.append(number)

        with open(output_path, 'w', encoding='utf-8') as outfile:
            for number in self.numbers_list:
                outfile.write(f"{number}\n")



if __name__ == "__main__":
    extractor = PhoneExtractor()
    extractor.extract_from_file("test.txt", "phones_output.txt")

