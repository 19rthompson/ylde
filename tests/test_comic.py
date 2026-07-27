from datetime import date, datetime

from comic import Comic


def test_comic_stores_expected_data():
    publication_date = date(2019, 10, 28)
    retrieved_date = datetime(2026, 7, 26, 10, 30)

    comic = Comic(
        num=2221,
        title="Emulation",
        safe_title="Emulation",
        publication_date=publication_date,
        transcript="",
        alt_text=(
            "I laugh at the software as if I'm 100% confident "
            "that it's 2019."
        ),
        image_url="https://imgs.xkcd.com/comics/emulation.png",
        link="",
        news="",
        explanation_text="An explanation of the comic.",
        source_url="https://www.explainxkcd.com/wiki/index.php/2221",
        retrieved_date=retrieved_date,
    )

    assert comic.num == 2221
    assert comic.title == "Emulation"
    assert comic.safe_title == "Emulation"
    assert comic.publication_date == publication_date
    assert comic.transcript == ""
    assert comic.alt_text.startswith("I laugh at the software")
    assert comic.image_url.endswith("emulation.png")
    assert comic.link == ""
    assert comic.news == ""
    assert comic.explanation_text == "An explanation of the comic."
    assert comic.source_url.endswith("/2221")
    assert comic.retrieved_date == retrieved_date



    def test_comic_automatically_records_retrieved_date():
        before_creation = datetime.now()

        comic = Comic(
            num=2221,
            title="Emulation",
            safe_title="Emulation",
            publication_date=date(2019, 10, 28),
            transcript="",
            alt_text="Example alt text.",
            image_url="https://imgs.xkcd.com/comics/emulation.png",
            link="",
            news="",
            explanation_text="Example explanation.",
            source_url="https://www.explainxkcd.com/wiki/index.php/2221",
    )

        after_creation = datetime.now()

        assert before_creation <= comic.retrieved_date <= after_creation