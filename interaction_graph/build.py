from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable
import dotenv
import os
dotenv.load_dotenv()


class App:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

    def add_view_link(self, cv_id, offer_id):
        with self.driver.session(database='neo4j') as session:
            result = session.execute_write(
                self._add_view_link,
                cv_id,
                offer_id
            )

    def _add_view_link(tx, cv_id, offer_id):
        query = """
            MATCH (user: User{ cv_id: $cv_id })
            MATCH (offer: Offer{ offer_id: $offer_id })
            MERGE user - [:HAS_VIEWED] -> offer
        """
        result = tx.run(query, cv_id=cv_id,
                        offer_id=offer_id)


if __name__ == "__main__":
    # Aura queries use an encrypted connection using the "neo4j+s" URI scheme
    uri = os.getenv('NEO4J_URI')
    user = os.getenv('NEO4J_USERNAME')
    password = os.getenv('NEO4J_PASSWORD')
    app = App(uri, user, password)
