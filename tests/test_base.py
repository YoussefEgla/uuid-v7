from uuid_v7.base import uuid6, uuid7, UUID


def test_uuid7_returns_uuid_instance():
    assert isinstance(uuid7(), UUID)


def test_uuid7_returns_unique_values():
    for _ in range(1000):
        assert uuid7() != uuid7()


def test_uuid7_correct_length():
    assert len(str(uuid7())) == 36


def test_uuid7_returns_sortable_values():
    uuid7_1 = uuid7()
    for _ in range(100000):
        uuid7_2 = uuid7()
        assert uuid7_1 < uuid7_2
        uuid7_1 = uuid7_2


def test_uuid6_returns_uuid_instance():
    assert isinstance(uuid6(), UUID)


def test_uuid6_returns_unique_values():
    for _ in range(1000):
        assert uuid6() != uuid6()


def test_uuid6_correct_length():
    assert len(str(uuid6())) == 36


def test_uuid6_returns_sortable_values():
    uuid6_1 = uuid6()
    for _ in range(100000):
        uuid6_2 = uuid6()
        assert uuid6_1 < uuid6_2
        uuid6_1 = uuid6_2
