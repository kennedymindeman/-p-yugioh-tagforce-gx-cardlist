from src.pack_list_parser import PackReader


def test_pack_list_parser_with_pack1():
    pack = PackReader("pack-list.txt").read_pack()
    assert pack
    assert pack.name == "First Monster"
    assert pack.number == 1
    assert pack.cost == 100
