from mysql_repository import MysqlRepository


def test_get_comic_by_num():
    repository = MysqlRepository()

    comic = repository.get_comic_by_num(2221)

    repository.close()

    assert comic is not None
    assert comic.num == 2221
    assert comic.title == "Emulation"
    assert comic.safe_title == "Emulation"
    assert comic.publication_date == "2019-10-28"