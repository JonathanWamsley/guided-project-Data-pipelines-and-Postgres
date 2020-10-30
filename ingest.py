import requests
import psycopg2


def batch_process_console():
    """Batch process: company B has to wait for all the requests to be finished"""
    with requests.get("http://127.0.0.1:5000/very_large_request/100") as r:
        print(r.text)

def stream_process_console():
    """Stream process: company B receives data from the mock api when available"""
    with requests.get("http://127.0.0.1:5000/very_large_request/100", stream=True) as r:
        buffer = ""
        for chunk in r.iter_content(chunk_size=1):
            if chunk.endswith(b'\n'):
                t = eval(buffer)
                print(t)
                buffer = ""
            else:
                buffer += chunk.decode()

def stream_process_postgres():
    with requests.get("http://127.0.0.1:5000/very_large_request/10") as r:
        """Stream process: company B receives data from mock api that is then dumped into postgres"""
        conn = psycopg2.connect(database="stream_test", user="postgres", host="127.0.0.1", password="postgres")
        cur = conn.cursor()
        sql = "INSERT INTO transactions (txid, uid, amount) VALUES (%s, %s, %s)"

        buffer = ""
        # to prevent from loading all content into memory at once.
        for chunk in r.iter_content(chunk_size=1):
            if chunk.endswith(b'\n'):
                # eval: evaluates string or compiled code input (currently in the form of a tuple)
                t = eval(buffer)
                print(t)
                cur.execute(sql, (t[0], t[1], t[2]))
                conn.commit()
                buffer = ""
            else:
                # decode: converts bytes to string
                buffer += chunk.decode()

if __name__ == "__main__":
    #batch_process_console()
    #stream_process_console()
    stream_process_postgres()
