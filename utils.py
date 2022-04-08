import json
import sqlite3

DATA_BASE_PATH = "data_base/netflix.db"
DATA_BASE = 'netflix'


class DataBase:
    def __init__(self):
        self.path = DATA_BASE_PATH
        self.data_base = DATA_BASE

    def load_data_from_base(self, query):
        with sqlite3.connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result

    def search_by_name(self, search_title):
        query = f"""
        SELECT title, country, MAX(release_year), listed_in, description
        FROM {self.data_base}
        WHERE title like '%{search_title}%'
        """
        search_results = self.load_data_from_base(query)
        for value in search_results:
            value_dict = {"title": value[0],
                          "country": value[1],
                          "release_year": value[2],
                          "genre": value[3],
                          "description": value[4]
                          }
        return value_dict

    def search_by_range_of_years(self, year_1, year_2):
        query = f"""
                SELECT title, release_year
                FROM {self.data_base}
                WHERE release_year BETWEEN {year_1} AND {year_2}
                LIMIT 100
                """
        search_results = self.load_data_from_base(query)
        req_list = []

        for res in search_results:
            req_format = {"title": res[0],
                          "release_year": res[1]}
            req_list.append(req_format)
        return req_list

    def search_by_rating(self, rating):
        query = f"""
                SELECT title, rating, description
                FROM {self.data_base}
                WHERE rating = '{rating}'
                LIMIT 100
                """
        search_results = self.load_data_from_base(query)

        req_list = []

        for res in search_results:
            req_format = {"title": res[0],
                          "rating": res[1],
                          "description": res[2]
                          }
            req_list.append(req_format)
        return req_list

    def search_by_genre(self, genre):
        query = f"""
                SELECT title, description
                FROM {self.data_base}
                WHERE listed_in like '%{genre}%'
                ORDER BY release_year DESC
                LIMIT 10
                """
        search_results = self.load_data_from_base(query)

        req_list = []

        for req in search_results:
            req_dict = {"title": req[0],
                        "description": req[1]}
            req_list.append(req_dict)

        return req_list

    def search_by_two_actor(self, actor_1, actor_2):
        query = f"""
                SELECT "cast" 
                FROM {self.data_base}
                WHERE "cast" like '%{actor_1}%' And "cast" like '%{actor_2}%'
                """
        search_results = self.load_data_from_base(query)

        names = []
        result = []

        for film in search_results:
            actor_list = film[0].split(", ")
            for k in actor_list:
                names.append(k)

        s = [actor_1, actor_2]

        names = set(names) - set(s)

        for i in search_results:
            print(i)

        for name in names:
            count = 0
            for tuple_ in search_results:
                list_ = list(tuple_)
                one_list_actors = list_[0].split(', ')

                if name in one_list_actors:
                    count += 1

            if count > 2:
                result.append(name)

        return result

    def search_by_type_year_genre(self, type_, year, genre):
        query = f"""
                SELECT title, description
                FROM {self.data_base}
                WHERE "type" = '{type_}'
                AND release_year = '{year}'
                AND listed_in like '%{genre}%'
                """
        search_results = self.load_data_from_base(query)

        list_result = []

        for result in search_results:
            transform_result = {"title": result[0],
                                "description": result[1]}
            list_result.append(transform_result)


        return json.dumps(list_result)
