import re

from src.pack import Pack


class PackReader:
    PACK_HEADER_PATTERN = re.compile(r"^#(\d+)\.+(.*)\.\s*\((\d+).*\)\.+\s*(\d+)\s*DP\/pack$")
    PACK_FOOTER_PATTERN = re.compile(r"-+")
    def __init__(self, file_path):
        self.file = open(file_path)

    def read_pack(self):
        for line in self.file:
            pattern_match = PackReader.PACK_HEADER_PATTERN.match(line)
            if not pattern_match:
                continue

            pack_number = int(pattern_match.group(1))
            pack_name = str(pattern_match.group(2))
            num_cards = int(pattern_match.group(3))
            cost = int(pattern_match.group(4))

            return Pack(pack_name, pack_number, cost)
