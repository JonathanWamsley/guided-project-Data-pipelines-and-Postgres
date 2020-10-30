# guided project: Data Pipelines and Postgres

This is a guided project that I followed from [Seanwasere youtube](https://www.youtube.com/watch?v=QF-qHWekhxw&ab_channel=seanwasereytbe), [git](https://github.com/Sean-Bradley/Stream-Data-From-Flask-To-Postgres)


- This project:
    - Company A creates data through a mock api
        - implemented using flask
        - generates fake user data with associated values
    - Company B ingest data
        - implements batch processing through the console
        - stream processing through the console
        - stream processing into postgres data base

note to get this project running on windows subsystem for linux I had to add `host="127.0.0.1` under argument when connecting to the posgres database
