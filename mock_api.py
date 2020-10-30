from flask import Flask, Response, stream_with_context
import time
import uuid
import random

# this script contains a mock api for company
APP = Flask(__name__)

@APP.route("/very_large_request/<int:rowcount>", methods=["GET"])
def get_large_request(rowcount):
    """returns N rows of data"""
    def f():
        """The generator of mock data"""
        for _i in range(rowcount):
            time.sleep(.1)
            txid = uuid.uuid4()
            uid = uuid.uuid4()
            amount = round(random.uniform(-1000, 1000), 2)
            print(txid)
            yield f"('{txid}', '{uid}', '{amount}')\n"
    return Response(stream_with_context(f()))

if __name__ == "__main__":
    APP.run(debug=True)