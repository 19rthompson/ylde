import mysql.connector

from comic import Comic
from repository import Repository


class MysqlRepository(Repository):

    def __init__(
        self,
        host: str = "localhost",
        port: int = 32000,
        user: str = "root",
        password: str = "root",
        database: str = "xkcd",
    ):
        self.connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
        )

    def get_comic_by_num(self, comic_num: int) -> Comic | None:
        sql = """
        SELECT
            num,
            title,
            safe_title,
            publication_date,
            transcript,
            alt_text,
            image_url,
            link,
            news,
            explanation_text,
            source_url,
            retrieved_date
        FROM comics
        WHERE num = %s;
        """

        cursor = self.connection.cursor()
        cursor.execute(sql, (comic_num,))
        row = cursor.fetchone()
        cursor.close()

        if row is None:
            return None

        return Comic(
            num=row[0],
            title=row[1],
            safe_title=row[2],
            publication_date=row[3],
            transcript=row[4],
            alt_text=row[5],
            image_url=row[6],
            link=row[7],
            news=row[8],
            explanation_text=row[9],
            source_url=row[10],
            retrieved_date=row[11],
        )

    def close(self) -> None:
        self.connection.close()