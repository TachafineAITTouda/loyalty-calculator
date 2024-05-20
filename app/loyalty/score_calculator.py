from django.db import connection

class ScoreCalculator:
    def __init__(self, customer):
        self.customer = customer

    def execute_sql(self, query, params):
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchone()[0]

    def calculate_loyalty_score(self):
        # Define maximum observed values for normalization
        max_purchases = 15
        max_reviews = 10
        max_login_count = 40
        max_distinct_login_days = 25

        num_purchases_query = "SELECT COUNT(*) FROM loyalty_purchase WHERE customer_id = %s"
        num_purchases = self.execute_sql(num_purchases_query, [self.customer.id])

        num_reviews_query = "SELECT COUNT(*) FROM loyalty_review WHERE customer_id = %s"
        num_reviews = self.execute_sql(num_reviews_query, [self.customer.id])

        login_count_query = "SELECT SUM(login_count) FROM loyalty_engagement WHERE customer_id = %s"
        login_count = self.execute_sql(login_count_query, [self.customer.id]) or 0

        distinct_login_days_query = "SELECT COUNT(DISTINCT DATE(date)) FROM loyalty_engagement WHERE customer_id = %s"
        distinct_login_days = self.execute_sql(distinct_login_days_query, [self.customer.id]) or 0

        # Calculate scores
        purchase_score = (num_purchases / max_purchases) * 50 if max_purchases else 0
        review_score = (num_reviews / max_reviews) * 30 if max_reviews else 0
        login_frequency_score = (login_count / max_login_count) * 10 if max_login_count else 0
        distinct_login_days_score = (distinct_login_days / max_distinct_login_days) * 10 if max_distinct_login_days else 0

        # Total engagement score
        engagement_score = login_frequency_score + distinct_login_days_score

        # Total loyalty score
        total_loyalty_score = purchase_score + review_score + engagement_score

        return total_loyalty_score
