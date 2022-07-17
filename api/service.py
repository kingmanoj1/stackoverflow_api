import requests


API_PREFIX = 'https://api.stackexchange.com/2.3/'


class GetStackOverflow:
    def get_all_questions(self, page, order="desc", sort="activity"):
        param = {
            "order": order,
            "sort": sort,
            "site": "stackoverflow"
        }
        try:
            # https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow
            question_url = f"{API_PREFIX}questions"
            response = requests.get(question_url, params=param)
            json_response = response.json()
            return json_response
        except Exception as err:
            print(f'Error occurred, Error: {err}')

    def search(self, page, tagged, order="desc", sort="activity"):
        param = {
            "tagged": tagged,
            "page": page,
            "order": order,
            "sort": sort,
            "site": "stackoverflow"
        }
        try:
            search_url = f"{API_PREFIX}search"
            response = requests.get(search_url, params=param)
            json_response = response.json()
            return json_response
        except Exception as err:
            print(f'Error occurred, Error: {err}')

    def answer_search(self, question_id, order="desc", sort="activity"):
        param={
            "order": order,
            "sort": sort,
            "site": "stackoverflow"
        }
        try:
            # "https://api.stackexchange.com/2.2/answers/68984450?order=desc&sort=activity&site=stackoverflow"
            answer_url = f"{API_PREFIX}answer/{question_id}"
            response = requests.get(answer_url, params=param)
            json_response = response.json()
            return json_response
        except Exception as err:
            print(f'Error occurred, Error: {err}')

    def get_all_articles(self, page, order="desc", sort="activity"):
        param = {
            "order": order,
            "sort": sort,
            "site": "stackoverflow"
        }
        try:
            # https://api.stackexchange.com/2.3/articles?order=desc&sort=activity&site=stackoverflow
            article_url = f"{API_PREFIX}articles"
            response = requests.get(article_url, params=param)
            json_response = response.json()
            return json_response
        except Exception as err:
            print(f'Error occurred, Error: {err}')

    def article_search(self, article_id, order="desc", sort="activity"):
        param={
            "order": order,
            "sort": sort,
            "site": "stackoverflow"
        }
        try:
            # "https://api.stackexchange.com/2.3/articles/{ids}?order=desc&sort=activity&site=stackoverflow"
            article_url = f"{API_PREFIX}articles/{article_id}"
            response = requests.get(article_url, params=param)
            json_response = response.json()
            return json_response
        except Exception as err:
            print(f'Error occurred, Error: {err}')