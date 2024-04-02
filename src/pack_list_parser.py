import re


class PackReader:
    PACK_HEADER_PATTERN = re.compile(r"^#(\d+)\.+(.*)\.\s*\((\d+).*\)\.+\s*(\d+)\s*DP\/pack$")
    PACK_FOOTER_PATTERN = re.compile(r"-+")
