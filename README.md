Project for monitoring outages in the local network at yggamore.

Runs in a couple of containers:
- monitor
    - constantly queries the things that it's supposed to 
- storage
    - records all of the outputs of the tests
- presentation
    - shows people the status of the tests
        - uptime
        - % up for the last 24, 72, 168h

Project plan:
    1. write a daemon (process) that polls various sites periodically, writes output to a log
    2. write a web interface that parses the log
    3. update daemon to write to a database
    4. update web interface to read from the database
    5. start separating things 